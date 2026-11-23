import time
import random
from http.server import HTTPServer, BaseHTTPRequestHandler
from prometheus_client import start_http_server, Counter, Gauge

REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests received')
CPU_TEMP_SIM = Gauge('simulated_server_temp_celsius', 'Simulated server temperature')

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Ignore browser icon requests so 1 refresh = 1 count
        if self.path == '/favicon.ico':
            self.send_response(204)
            self.end_headers()
            return

        REQUEST_COUNT.inc()
        CPU_TEMP_SIM.set(random.uniform(40.0, 75.0))

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello! Prometheus is tracking this page.")

if __name__ == '__main__':
    start_http_server(8000)
    server = HTTPServer(('0.0.0.0', 5000), SimpleHandler)
    print("App running on port 5000, metrics on port 8000...")
    server.serve_forever()