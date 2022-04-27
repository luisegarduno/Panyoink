    ██████╗  █████╗ ███╗   ██╗██╗   ██╗ ██████╗ ██╗███╗   ██╗██╗  ██╗
    ██╔══██╗██╔══██╗████╗  ██║╚██╗ ██╔╝██╔═══██╗██║████╗  ██║██║ ██╔╝
    ██████╔╝███████║██╔██╗ ██║ ╚████╔╝ ██║   ██║██║██╔██╗ ██║█████╔╝
    ██╔═══╝ ██╔══██║██║╚██╗██║  ╚██╔╝  ██║   ██║██║██║╚██╗██║██╔═██╗
    ██║     ██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║██║ ╚████║██║  ██╗
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
                 ~ Website : https://gardunos.tech 

# Panyoink

Panyoink is a python script that is able to download videos that are available to a user on Panopto such as recorded lectures, meetings, etc. The great
thing about panyoink is that the user does not have to be the owner of the video.

## Prerequisites:
- Have the following python3 modules installed: lxml, wget, urllib3, beautifulsoup4   
  - `$ pip install -r requirements.txt`

## Instructions:
**1.** Obtain a Panopto URL for a recording that is available to you.
  - Example: 'https://xxxx.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'   

**2.** When prompted: (1st) Enter the URL, (2nd) Then enter the value of your Panopto Authentication Cookie ('.ASPXAUTH').

**3.** That's it! Panyoink will do the rest** for you!
  - ** In some cases, users have to retrieve the URL manually and paste it into panyoink to begin the download.
