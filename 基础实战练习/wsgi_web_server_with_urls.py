#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

from wsgiref.simple_server import make_server

# 1.路由的分发器，负责把URL 匹配到对应的函数
# 2.开发好对应 的业务 函数
# 3.一个请求来了之后，先走路由分发器，如果找到对应的function，就执行，如果没有找到，就返回404错误

def run_server(environ, start_response):

    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h1>这美女是哪里的啊!!', encoding='utf-8'), ]


if __name__ == '__main__':
    httpd = make_server('localhost', 8888, run_server)
    httpd.serve_forever()