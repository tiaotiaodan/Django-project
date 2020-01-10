#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import  socket

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('127.0.0.1',8888))
    sock.listen(5)

    while True:
        # 等待浏览器访问
        conn, addr = sock.accept()

        #接收浏览器发送来的请求内容
        data = conn.recv(1024)
        print(data)

        #给浏览器返回内容
        conn.send(b"HTTP/1.1 200 OK\r\nContent-Type:text/html; charset=utf-8\r\n\r\n")
        conn.send("美女长的真好看！".encode("utf-8"))

        conn.close()

if __name__ == "__main__":
    main()