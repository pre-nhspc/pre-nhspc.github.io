import json
import time
import os
import sys
import requests

if len(sys.argv) < 2:
    print("CMS Ranking dumper v0.1")
    print("\tUsage: python3 dumper.py <url> [-c]")
    exit(0)

SINGLE_FILES = ["Chart.js", "Config.js", "DataStore.js", "HistoryStore.js", "Overview.js", "Ranking.css", "Ranking.html", "Ranking.js", "Scoreboard.js", "TeamSearch.js", "TimeView.js", "UserDetail.js", "history", "logo", "scores"]
LIBS = ["eventsource.js", "explorercanvas.js", "jquery.js", "raphael.js"]
IMGS = ["close.png", "face.png", "favicon.ico", "flag.png", "logo.png", "tick_black.png", "tick_white.png"]
HTACCESS = "DirectoryIndex index.json"

# Parse URL
url = sys.argv[1]
if url[-1] != '/':
    url = url + '/'

# cURL helper function
def curl(location, saveas = None):
    if saveas is None:
        saveas = location
    result = requests.get(url + location, stream=True)
    if result.status_code != 200:
        print("Error", result.status_code, "downloading", url + location)
    with open(saveas, "wb") as f:
        for chunk in result.raw:
            f.write(chunk)

def write_htaccess(directory):
    with open(directory + "/.htaccess", "w+") as f:
        f.write(HTACCESS)

details = {}
processed = {}
scores = {}

def dump_indexed(output=True):
    os.makedirs("subchanges", exist_ok=True)
    curl("subchanges", "subchanges/index.json")
    os.makedirs("submissions", exist_ok=True)
    curl("submissions", "submissions/index.json")
    with open("subchanges/index.json") as subc:
        with open("submissions/index.json") as subm:
            change      = json.load(subc)
            submissions = json.load(subm)
            for sub in change:
                if change[sub]['submission'] not in details:
                    details.update({change[sub]['submission'] : change[sub]['extra']})
            for sub in submissions:
                if sub not in processed:
                    if sub not in details:
                        continue
                    processed.update({sub: True})
                    user = submissions[sub]['user']
                    task = submissions[sub]['task']
                    extra = details[sub]
                    if user not in scores:
                        scores.update({user: {}})
                    if task not in scores[user]:
                        scores[user].update({task: [0] * len(extra)})
                    previous = sum(scores[user][task])
                    for i in range(len(extra)):
                        scores[user][task][i] = max(scores[user][task][i], int(extra[i]))
                    current = sum(scores[user][task])
                    total = sum([sum([j for j in i]) for i in scores[user].values()])
                    if output:
                        color = f"\033[{2 if previous == current else 0}m"
                        if task == "distance":
                            task = "\033[0m\033[0;31m" + task
                        print(f"{color}{'=' if previous == current else '+'} {user} submitted {task}{color}, changes from {previous} -> {current}\t", end='')
                        if total <= 100:
                            print(f"\033[2m(total score {total})\033[0m")
                        elif total <= 150:
                            print(f"\033[0m(total score {total})\033[0m")
                        elif total <= 200:
                            print(f"\033[0;31m(total score {total})\033[0m")
                        elif total <= 250:
                            print(f"\033[0;33m(total score {total})\033[0m")
                        else:
                            print(f"\033[0;32m(total score {total})\033[0m")

def dump_two(main, sub):
    print(f"Dumping {main} and {sub}...")
    os.makedirs(main, exist_ok=True)
    os.makedirs(sub, exist_ok=True)  
    write_htaccess(main)
    curl(main, main + "/index.json")
    with open(main + "/index.json") as index:
        list = json.load(index)
        for elem in list:
            curl(main + "/" + elem)  
            curl(sub + "/" + elem)  

def dump_user(users, sublist, faces):
    print(f"Dumping {users}, {sublist} and {faces}...")
    os.makedirs(users, exist_ok=True)
    os.makedirs(sublist, exist_ok=True)  
    os.makedirs(faces, exist_ok=True)
    write_htaccess(users)
    curl(users, users + "/index.json")
    with open(users + "/index.json") as index:
        list = json.load(index)
        for elem in list:
            if ("team" not in elem) or (elem["team"] == "null"):
                print(elem, "has no team!")
            curl(users + "/" + elem)  
            curl(sublist + "/" + elem)  
            if faces != None:
                curl(faces + "/" + elem)

# Get single files
print("Dumping submissions...")

# Get contests
dump_indexed(False)
while True:
    dump_indexed()
    time.sleep(0.5)
print("Finished!")