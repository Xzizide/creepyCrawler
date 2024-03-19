import urllib.request, json
urllist = {
    "https://sv.wikipedia.org/":1
    ,}
urlstocheck = ["https://sv.wikipedia.org/"]
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
stopint = 100

while urlstocheck != []:
    stopint-=1
    
    try:
        req = urllib.request.Request(urlstocheck[0], headers=hdr)
        with urllib.request.urlopen(req) as file:
            urltext = str(file.read())
            newurl = ""
            start = urltext.find("https")
            while start >= 0:
                iterator = 0
                for letter in urltext[start:]:
                    iterator += 1
                    if letter == '"' or letter == "'" or letter == " ":
                        break
                    else:
                        newurl += letter
                urltext = urltext[start+iterator:]
                iterator = 0
                start = urltext.find("https")
                if newurl in urllist.keys():
                    urllist[newurl] += 1
                else:
                    urllist[newurl] = 1
                    urlstocheck.append(newurl)
                newurl = ""
        urlstocheck.pop(0)
    except:
        urlstocheck.pop(0)
    if stopint < 0:
        break

with open("result.json", "w") as f:
    f.write(json.dumps(urllist, indent=4))
    print("done")