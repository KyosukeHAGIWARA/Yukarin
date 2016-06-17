#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from bs4 import BeautifulSoup
import urllib.request
import json


def gen_image_url_list(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml").select(".article-body-more")
    a_list = soup[0].find_all("a")

    ans = []
    url_dict = {}
    for a in a_list:
        for c in a.children:
            if str(type(c)) == "<class 'bs4.element.Tag'>":
                c["class"] = "thumbnail"
                big = a.get("href")
                small = c.get("src")
                url_dict.update({small: big})
                ans.append(c)

    return ans, url_dict

if __name__ == '__main__':
   url = sys.argv[1].replace("\\", "")
   urls = json.loads(url)
   ans = []
   url_dict = {}
   for u in urls:
       one_ans, one_url_dict = gen_image_url_list(u)
       ans += one_ans
       url_dict.update(one_url_dict)

   html_top = '''
    <!DOCTYPE html>
    <html>
            <head>
                <title>Yukarin</title>
                <link rel="stylesheet" href="./style.css" />
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
            </head>
        <body>
            <div id="main">
                <ul class="image_list">


   '''
   content_root= ""

   for a in ans:
       content = '''
        <li>
            <div class="image_box">
        '''
       content += str(a)
       content += '''
                <input class="disabled_checkbox" type="checkbox" checked="true" />
            </div>
        </li>

        '''

       content_root += content

   html_bottom = '''
                </ul>

                <input type="button" value="generate!" onclick="generate()">
                <div id="output" size="40">
                <script type="text/javascript">
                    url_dict =
    '''



   html_foot = '''
                ;</script>
                <script src="./base.js"></script>
            </div>
        </body>
    </html>
   '''

   print(html_top + content_root + html_bottom + str(url_dict) + html_foot)
