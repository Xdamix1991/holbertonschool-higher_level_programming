#!/usr/bin/python3


"""
web server
"""
import http.server
import json


class Run(http.server.BaseHTTPRequestHandler):
    """
    this class a simple server
    """

    def do_GET(self):
        """
        function to handle the server and the requsts
        """

        if self.path == '/':
            self.send_response(200)
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())

        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            self.send_response(200)
            self.end_headers()
            self.wfile.write("OK".encode())

        elif self.path == '/info':
            data_info = {"version": "1.0",
                         "description": "A simple API built with http.server"}
            self.send_header('Content-type', 'application/json')
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(data_info).encode())

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write("Endpoint not found".encode())


if __name__ == "__main__":
    PORT = 8000
    server_adress = ('', PORT)
    server = http.server.HTTPServer
    httpd = server(server_adress, Run)
    httpd.serve_forever()
