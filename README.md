# Scrappy
[Support me on Ko-fi!](https://ko-fi.com/g4bibi)

Scrappy is a GUI URL Scrapper to HTML and Markdown made by Gabby (aka gabibi, g4b1b1) in Python 3

The file "scrappy.py" can be used standalone without the TrueType-Font files (.ttf)
    or the other TTF-to-Base64 converter (ttfToB64.py).

The other files are present because im offering this FOSS's (Free, Open-Source Software) entire source code
    (basically what has been used to make this piece of software.)

Hopefully you enjoy using it.
## Scrappy has been tested on:
### Windows 11 25H2
### Debian 13 (Trixie)
### macOS 10.15 (Catalina

Dependencies (pip packages):
* winotify
* bs4
* markdownify
* requests

This has been stress tested against the following websites:
* Random BBC Sport F1 article - works nicely
* example.com - works nicely ofc
* Github DOOM 3 repository - works nicely
* Google search on 'how to pet cats' - works partially, because google fetches results from its servers, and the results are not stored in HTML or MD
* MDN doc on HTML - works nicely
* Oracle Java Help Center - works nicely
* Reddit MGS2 post - worked also partially, because like Google, it tries to fetch the post from its servers
* Wikipedia Walrus article - did not work (403)
* Stack Overflow "what is if \_\_name\_\_ == "\_\_main\_\_" mean?" - did not work (403)
* W3Schools Python tutorial - did not work (403)
