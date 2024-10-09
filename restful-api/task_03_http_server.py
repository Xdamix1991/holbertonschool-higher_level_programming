#!/usr/bin/python3
"""
web server
"""
import http.server
import socketserver
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    this class a simple server
    """
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))

        elif self.path == '/info':
            data_info = {"version": "1.0",
                         "description": "A simple API built with http.server"}
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(data_info).encode('utf-8'))

        elif self.path == '/data':
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(dataset).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("404 Not Found".encode('utf-8'))


if __name__ == "__main__":
    PORT = 8000
    server_adress = ('', PORT)
    server = http.server.HTTPServer
    httpd = server(server_adress, SimpleAPIHandler)
    httpd.serve_forever()
