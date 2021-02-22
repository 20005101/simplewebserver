# Developing a Simple Webserver
## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation
### Step 2:
Design of webserver workflow
### Step 3:
Implementation using Python code
### Step 4:
Serving the HTML pages.
### Step 5:
Testing the webserver

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler

content="""
<html>
<h1>Multiplication Table</h1>
<p>2x1=2</p>
<p>2x2=4</p>
<p>2x3=6</p>
<p>2x4=8</p>
<p>2x5=10</p>
<p>2x6=12</p>
<p>2x7=14</p>
<p>2x8=16</p>
<p>2x9=18</p>
<p>2x10=20</p>
</html>
"""

class myHandler(BaseHTTPRequestHandler):
    def do_Get(self):
        print("req received")
        self.send_response(200)
        self.send_header('content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address=('',80)

httpd=HTTPServer(server_address,myHandler)
print("server is running")
httpd.serve_forever()
```

## OUTPUT:
```
Server is Running
```
## RESULT:
Thus the simplewebserver.py is created and it is available in Github 