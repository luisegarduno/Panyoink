import re
import sys
import time
import os.path

import wget
from wget import download
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

# Current working directory
cwd = os.path.dirname(os.path.realpath(__file__))

title = '''
            ██████╗  █████╗ ███╗   ██╗██╗   ██╗ ██████╗ ██╗███╗   ██╗██╗  ██╗
            ██╔══██╗██╔══██╗████╗  ██║╚██╗ ██╔╝██╔═══██╗██║████╗  ██║██║ ██╔╝
            ██████╔╝███████║██╔██╗ ██║ ╚████╔╝ ██║   ██║██║██╔██╗ ██║█████╔╝
            ██╔═══╝ ██╔══██║██║╚██╗██║  ╚██╔╝  ██║   ██║██║██║╚██╗██║██╔═██╗
            ██║     ██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║██║ ╚████║██║  ██╗
            ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
                          ~ Website : https://gardunos.tech
'''

print(title + "\n")


os.system('cls' if os.name == 'nt' else 'clear')
print(title + "\n")
print("\n            -----------------------------------------------------------------\n\n")

og = input("Enter Panopto URL: ")
auth = input("Enter '.ASPXAUTH' Cookie: ")

r = Request(og, headers = {'Cookie': ".ASPXAUTH="+auth})
responseCheck = urlopen(r).read()
titles = BeautifulSoup(responseCheck, "lxml").findAll("title")
name = re.split(">|<", str(titles[0]))[2]

panopto = og.split('Viewer.aspx?id=')
baseURL = panopto[0]
id = panopto[1]

# create a downloader class.
class downloader:
    #  Create a custom prgress bar method
    def progressBar(self, current, total, whats):
        print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))

    # Create a downloadfile method
    # Accepting the url and the file storage location
    # Set the location to an empty string by default.
    def downloadFile(self, url, location=""):
        # Download file and with a custom progress bar
        download(url, out=location, bar=self.progressBar)
    
    def download_file(self, url):
    	s = str(name).strip().replace(' ', '')
    	s = str(s).strip().replace('/', '-')
    	print(f"{name}")
    	download(url,f"{s}.mp4")


# ############ Option 1 : Podcast Player #############
podcast = baseURL[:baseURL.index("/Pages") + 1] + f'Podcast/Syndication/{id}.mp4'
try:
    flag = False
    responseCode = urlopen(podcast).getcode()
    if responseCode != 403:
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(title + "\n")
        print("\n            -----------------------------------------------------------------\n\n")

        panyoink = downloader()
        panyoink.download_file(podcast)
        print("\n\nAll Done!")

        flag = True
        sys.exit(0)

except:
    if flag:
        raise
    if not flag:
        print("Manual URL needed...\n")

time.sleep(1.5)
os.system('cls' if os.name == 'nt' else 'clear')
print(title + "\n")
print("\n            -----------------------------------------------------------------\n\n")

# ############ Option 2 : Embeded Player #############

embed = baseURL + f'Embed.aspx?id={id}&v=1&ignoreflash=true'
responseEm = urlopen(embed).read()
soupEm = BeautifulSoup(responseEm, "lxml")

vidPlayer = soupEm.findAll("script", {"type": "text/javascript"})

if str(vidPlayer).find("VideoUrl"):
    idxVid = str(vidPlayer).find("VideoUrl")
    # print(str(vidPlayer)[idxVid : idxVid + 100 ])

    if str(vidPlayer).find(".mp4"):
        mp4 = str(vidPlayer).find(".mp4")
        # print(str(player)[idxVid: mp4 + 3])

print("1.) Go here: \nview-source:" + embed)
print("\n2.) Ctrl+F : 'VideoUrl'")
vidLink = input("\n3.) Paste the URL here: ")
newLink = vidLink.replace("\\", "")

time.sleep(1.5)
os.system('cls' if os.name == 'nt' else 'clear')
print(title + "\n")
print("\n            -----------------------------------------------------------------\n\n")

print("Download has started:")
panyoinks = downloader()
panyoinks.downloadFile(newLink)

print("All Done!")
