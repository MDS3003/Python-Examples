import http.server
# added to see change
class HTTPFrontend(object) :
    def __init__(self, port) :
        self.server = http.server(('', port), self.RequestHandler)
        print("Web interface listening on http://localhost:" + str(port))

    def start(self) :
        self.server.serve_forever()

    def stop(self) :
        self.server.socket.close()

    class RequestHandler(http.server.SimpleHTTPRequestHandler) :
        def do_GET(self) :
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            templateFile = open("home.html")
            template = templateFile.read()
            templateFile.close()

            message = "this is how simple templating works"

            self.wfile.write(template % {'message': message})

        def do_POST(self) :
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write("this is a POST")

if __name__ == "__main__":
    server = HTTPFrontend(8080)
    server.start()
