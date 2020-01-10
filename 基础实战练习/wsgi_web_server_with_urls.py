#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

from wsgiref.simple_server import make_server

# 1.路由的分发器，负责把URL 匹配到对应的函数
# 2.开发好对应 的业务 函数
# 3.一个请求来了之后，先走路由分发器，如果找到对应的function，就执行，如果没有找到，就返回404错误


def book(environ, start_response):
    print("book page")
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h1>book page</h1>', encoding='utf-8'), ]

def cloth(environ, start_response):
    print("cloth page")
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h1>cloth page</h1>', encoding='utf-8'), ]

#以上定义的函数相当于，html页面

def url_dispacher():
    urls = {
        '/book': book,
        '/cloth': cloth,
    }
    return urls

def run_server(environ, start_response):

    url_list = url_dispacher()   #拿到所有的url
    request_url = environ.get("PATH_INFO")
    print('request url', request_url)

    if request_url in url_list:
        func = url_list[request_url](environ, start_response)
        return  func
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h1>首页</h1>', encoding='utf-8'), ]

if __name__ == '__main__':
    httpd = make_server('localhost', 8888, run_server)
    httpd.serve_forever()