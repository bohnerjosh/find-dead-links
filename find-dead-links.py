from sys import argv
from pathlib import Path
import requests
from bs4 import BeautifulSoup

progname = Path(argv[0]).stem

def search_url(url, num_levels=0):
    # Iterativate stuff here
    try:
        resp = requests.get(url)
        links_to_traverse = [] 
        soup = BeautifulSoup(resp.text, features='html.parser')
        results = soup.find_all('a')
        if not num_levels < 0:
            for result in results:
                thing = str(result)
                #print(thing)
                if not "href=\"#\"" in thing and not "href=\".\"" in thing:
                    first = thing.find('"')
                    search = thing[first+1:]
                    second = search.find('"')
                    final = search[:second]
                    if final.startswith("http"):
                        links_to_traverse.append(final)
                    else:
                        if url[-1] == "/":
                            appendurl = url + final[1:]
                        else:
                            appendurl = url + final

                        links_to_traverse.append(appendurl)
        if resp.status_code not in [200, 302]:
            print("Link: %s : Bad link" % url)
        else:
            print("Link: %s : Good link!" % url)
            for link in links_to_traverse:
                
                if num_levels >= 0:
                    pass_levels = num_levels-1
                    #print("Searching link %s" % link)
                    search_url(link, pass_levels)
                    
                    #print("Searching link %s" % link)
                else:
                    continue
                    #print("Searching link %s" % link)
            return
    except:
        #print("Bad link!")
        print("Link: %s : Bad link" % url)
        return

if len(argv) > 3 or len(argv) < 2:
    print("Usage: %s -<link_depth> <url>" % progname)
    print("Usage: %s <url>" % progname)
    exit(1)

if argv[1].startswith("-"):
    url = argv[2]
    levels = argv[1]
    levels = int(levels[1:])
    search_url(url, levels)
else:
    url = argv[1]
    search_url(url)

