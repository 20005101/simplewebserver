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