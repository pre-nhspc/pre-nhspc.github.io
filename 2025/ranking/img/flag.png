<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <!--<script async src="https://www.googletagmanager.com/gtag/js?id=UA-127507120-4"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-127507120-4');
    </script>-->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta property="og:url" content="ranking.nhspc.cc">
    <meta property="og:title" content="114 學年度 全國資訊學科能力競賽模擬賽－記分板">
    <meta property="og:type" content="website">
    <title>114 學年度 全國資訊學科能力競賽模擬賽－記分板</title>
    <meta name="description" content="114 學年度 全國資訊學科能力競賽模擬賽－記分板">
    <link rel="icon" type="image/png" sizes="32x32" href="./imgs/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="./imgs/favicon-16x16.png">
<style>
/* page related */
*,
*::before,
*::after {
    -webkit-box-sizing: border-box;
       -moz-box-sizing: border-box;
            box-sizing: border-box;
}
body, html{
    height: 100%;
    margin: 0;
    padding: 0;
}
body {
    font-family: "Ubuntu", "Helvetica", "微軟雅黑", "Microsoft YaHei", "Segoe UI Semibold", "Segoe UI", 
    "Lucida Grande", Verdana, Arial, Helvetica, sans-serif;
}
html {
    overflow-y: scroll;
}
main {
    display: flex;
    align-items: center;
    flex-direction: column;
    min-width: 100%;
    min-height: calc(100% - 10px);
    padding-top: 25px;
    opacity: 0;
}
main.fadein {
    transition: all 1.5s ease;
    -moz-transition: all 1.5s ease;
    -o-transition: all 1.5s ease;
    -webkit-transition: all 1.5s ease;
    opacity: 1;
}
#bg-div {
    position: fixed;
    left: 0px; 
    top: 0px; 
    width: 100%;
    height: 100%;
    z-index: -9999;
    display: block;
    background: url(./imgs/background.jpg) no-repeat center center fixed;
    /* Image credit: by Sagar Patil on Unsplash */
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
    opacity: 0.15;
}

/* title related */
#title-div {
    margin-top: 25vh;
    position: relative;
    text-align: left;
}
@media screen and (max-height: 550px){
    #title-div{margin-top: 14vh;}
}
@media screen and (max-height: 400px){
    #title-div{margin-top: 4vh;}
}
#title-row1{
    font-size: 25px;
}
#title-row2{
    font-weight: bold;
    font-size: 60px;
}
#title-row3{
    font-size: 22px;
}
#calendar-icon {
    height: 17px;
}

/* text related */
#text-div {
    margin-top: 30px;
    text-align: center;
    padding: 0 50px;
}
#text-span {
    color: red;
    font-size: 25px;
    font-weight: bold;
}

@media screen and (max-width: 910px){
    #title-row1{font-size: 20px;}
    #title-row2{font-size: 50px;}
    #title-row3{font-size: 18px;}
    #calendar-icon {height: 15px;}
}
@media screen and (max-width: 720px){
    #title-row2{font-size: 40px;}
    #text-span {font-size: 18px;}
}
@media screen and (max-width: 580px), screen and (max-height: 500px){
    #title-row1{font-size: 20px;}
    #title-row2{font-size: 35px;}
    #title-row3{font-size: 18px;}
    #calendar-icon {height: 15px;}
    #text-span {font-size: 20px;}
}
@media screen and (max-width: 500px){
    #title-row1{font-size: 15px;}
    #title-row2{font-size: 25px;}
    #title-row3{font-size: 13px;}
    #calendar-icon {height: 10px;}
    #text-span {font-size: 15px;}
}

/* button related */
#btn-div {
    width: 100%;
    display: flex;
    justify-content: center;
    max-width: 330px;
    margin: 35px 0;
}
#ranking-btn {
    font-size: 30px;
    letter-spacing: 0.2em;
    width: 200px;
    padding: 8px 0;
    text-align: center;
    color: #070;
    border: 1px solid #070;
    text-decoration: none;
    outline: none;
    background-color: transparent;
    transition: all 0.5s ease;
    -moz-transition: all 0.5s ease;
    -o-transition: all 0.5s ease;
    -webkit-transition: all 0.5s ease;
}
#ranking-btn:hover,#ranking-btn:active {
    background-color: #070;
    color: white;
}
#ranking-btn:active {
    transform: scale(0.9);
    background-color: #070;
    color: white;
}
/* helper class */
.no-break {
    display: inline-block;
}
</style>
    <noscript>
<style>
main {
    opacity: 1;
}
</style>
    </noscript>
</head>
<body>
    <div id="bg-div"></div>
    <main>
        <div id="title-div" class="">
            <span class="no-break" id="title-row1">114 學年度普通型高級中等學校</span><br>
            <span class="no-break" id="title-row2">資訊學科能力競賽決賽 模擬賽</span><br>
            <span class="no-break" id="title-row3"><img id="calendar-icon" src="./imgs/calendar-from-flaticon.svg"> 12/7（日）上午 9:00 至 下午 2:00</span>
        </div>
        <div id="text-div">
            <span id="text-span">
                <span class="no-break">根據全國資訊學科能力競賽規定，</span>
                <span class="no-break">參賽選手「不得」在賽中觀看記分板。</span>
            </span>
        </div>
        <div id="btn-div">
            <a href="#" onclick="go()" id="ranking-btn">記分板</a>
        </div>
    </main>
    <script>
        "use strict";
        window.onload = function(){
            setTimeout(() => {
                document.getElementsByTagName("main")[0].classList.add("fadein");
            }, 200);
        };
		function setCookie(name,value,days) {
			var expires = "";
			if (days) {
				var date = new Date();
				date.setTime(date.getTime() + (days*24*60*60*1000));
				expires = "; expires=" + date.toUTCString();
			}
			document.cookie = name + "=" + (value || "")  + expires + "; path=/";
		}
        function go(){
            if(confirm("根據全國資訊學科能力競賽規定，參賽選手「不得」在賽中觀看記分板。請問你是否要前往記分板？")){
                setCookie("allow_ranking", "Y", 1);
                window.location.reload(true);
            }
        }
    </script>
</body>
</html>
