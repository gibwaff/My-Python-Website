from http.server import HTTPServer, CGIHTTPRequestHandler

def server():
    server_data = ("localhost", 8000)
    server = HTTPServer(server_data, CGIHTTPRequestHandler)
    print("Server started")
    server.serve_forever()

if __name__ == "__main__":
    server()

