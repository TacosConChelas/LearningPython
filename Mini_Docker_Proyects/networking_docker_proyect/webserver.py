# webserver.py
from http.server import HTTPServer, BaseHTTPRequestHandler
PORT = 8000

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Cuando alguien entra al navegador, respondemos esto:
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # El mensaje HTML
        mensaje = """
        <html>
            <body>
                <h1> Hola desde Docker! </h1>
                <p> Si ves esto, funciona. </p>
            </body>
        </html>
        """
        self.wfile.write(mensaje.encode("utf-8"))

def run():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"--- Servidor Python corriendo en el puerto {PORT} ---")
    httpd.serve_forever()

if __name__ == "__main__":
    run()