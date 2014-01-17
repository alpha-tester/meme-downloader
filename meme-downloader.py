import urllib
import re
import os
from os.path import basename

def scrap(url):
    print"[+] Opening %s" % url
    page = urllib.urlopen(url).read()
    img_pattern = re.compile('.+img\ssrc\=\"(.+\.jpeg).+\/\>\<\/a\>')
    # Universal Regular Expression pattern for img tag
    # I don't copy it, I just created it
    # NOT universal, if you need to use it in other script
    # Remove '\<\/a\>'
    img_link = img_pattern.findall(page)
    # parse the links
    img_names = [basename(i) for i in img_link]
    # Scrap the img names off the link
    print img_link, img_names
    return img_link, img_names

def main():
    gallery = 'http://memedroid.com/gallery/p/'
    homepage = 'http://memedroid.com/'
    
    try:
        clear()
        print"MEMEDROID Downloader"
        print"How many pages would you like to download?\n Press Enter for just homepage page"
        no_pages = raw_input("=> ")
        if not no_pages:
            no_pages = 1
            download(scrap(homepage))
            # Homepage will return img_link, img_names
            # download requires two parameters
            # link and names
        elif no_pages:
            urls = [gallery+str(i) for i in range(1,int(no_pages)+1)]
            # Generate the gallery urls with page number
            for i in urls:
                download(scrap(i))
                # Download the link after scraped it
        print"[+] Downloaded Everything in 'MEME' folder"
            
        
    except KeyboardInterrupt:
        exit()
        
def clear():
    # Just clear the screen
    # command is not the same in different os
    if os.name == 'posix': os.system('clear')
    elif os.name == 'nt': os.system('cls')
    else: print "[!] Not for MAC\n[!]Get Lost"
    # Not for MAC idiots
    
def download(link,names):
    if not os.exists('meme'):
    # If meme folder didn't exist
    # Create it
        os.mkdir('meme')
        
    if 'meme' not in os.path.abspath('.'):
    # If not inside meme folder
    # cd into it
        os.chdir('meme')    
    for i in link:
        clear()
        urllib.urlretrieve(i,names[link.index(i)])
        print "[+] Downloaded %s" % names[link.index(i)]
        print "[+] {0} Left to Download".format(len(link)-link.index(i)+1)
        
main()
