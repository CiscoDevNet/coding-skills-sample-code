# !/usr/bin/env python

import http.server
import random

server_ip = "127.0.0.1"
server_port = 8000


class CustomRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):

        route_path = self.path.rstrip("/")

        # print(route_path)
        if route_path == '/object':
            self.send_response(200)
            self.write_object()
        elif route_path == '/array':
            self.send_response(200)
            self.write_array()
        elif route_path == '/random':
            self.send_response(200)
            self.write_random()
        elif route_path == '/random/array':
            self.send_response(200)
            self.write_random_array()
        elif route_path == '/complex':
            self.send_response(200)
            self.write_complex()
        elif route_path == '/complex/array':
            self.send_response(200)
            self.write_complex_array()
        else:
            # Otherwise send a default response
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(open("./data/index.html", "rb").read())

        return

    def write_object(self):
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{ "first_name": "Mike", "last_name": "Maas" }')

    def write_array(self):
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b'[{ "first_name": "Mike", "last_name": "Maas" }, { "first_name": "Matt", "last_name": "Denapoli" }]')

    def write_complex(self):
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(open("./data/complex.json", "rb").read())

    def write_complex_array(self):
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(open("./data/complex-array.json", "rb").read())

    def write_random(self):
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        result = '{"value":' + str(random.randrange(0, 100, 1)) + '}'
        self.wfile.write(bytes(result, "utf-8"))

    def write_random_array(self):
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Construct a JSON array with random entries
        values = []
        value_count = random.randint(0, 15)
        for element in range(0, value_count):
            value = '{{ "{}" : {}, "value" : {} }}'.format("id", element, str(random.randrange(0, 100, 1)))
            values.append(value)

        result = '[' + ', '.join(values) + ']'
        self.wfile.write(bytes(result, "utf-8"))


def run():
    # Set the server settings
    server_address = (server_ip, server_port)
    httpd = http.server.HTTPServer(server_address, CustomRequestHandler)
    print("Serving content at http://" + server_ip + ":" + str(server_port))
    httpd.serve_forever()


if __name__ == '__main__':
    run()
