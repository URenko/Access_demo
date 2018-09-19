#!/usr/bin/env python3
# This is just a demo
import socket, ssl
import http.client

def access_demo(ip, host, url):
    context = ssl.create_default_context()
    context.check_hostname = False
    conn = http.client.HTTPSConnection(ip, context=context)
    conn.request('GET', url, headers={'Host': host})
    res = conn.getresponse()
    print(res.status, res.reason)
    print(res.read().decode('utf-8'))

if __name__ == '__main__':
    access_demo('210.129.120.55', 'www.pixiv.net', '/')