#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import subprocess
import time
import os


def download_image(web_url, dirpath, out_name):
    path = dirpath + "/" + out_name
    print(path)
    if subprocess.call(["python", "-m", "wget", "-o", path, web_url]) != 0:
        print("download_error " + path)

if __name__ == '__main__':

    url_list = []
    outdir = ""

    if len(sys.argv) == 1:
        print("tell me url_list")
        str_list = input().replace("\\", "")
        url_list = json.loads(str_list)
        print("tell me output dirpath")
        outdir = input()

    elif len(sys.argv) == 3:
        url_list = json.loads(sys.argv[1])
        outdir = sys.argv[2]

    else:
        print("usage: python3 Karina.py [url_list] \"output dirpath\"")
        exit()

    os.makedirs(outdir)

    for url in url_list:
        outname = url.split("/")[-1]
        download_image(url, outdir, outname)
        time.sleep(0.3)