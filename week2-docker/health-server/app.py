from http.server import HTTPServer,BaseHTTPRequestHandler

import json
import os
import datetime
import logging

logging.basicConfig(
    level=logging.INFO,format='%(asctime)s[%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

class HealthHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            self.handle_health()
        elif self.path == "/info":
            self.handle_info()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"NOT FOUND")
    
    def handle_health(self):
        health = {
            "status": "healthy",
            "timestamp": datetime.datetime.now().isoformat(),
            "version": os.environ.get("APP_VERSION","1.0.0")
        }
        self._send_json(200,health)
        logger.info(f"Health check: OK")

    def handle_info(self):
        info = {
            "app_name": os.environ.get("APP_NAME","Devops Health app"),
            "environment": os.environ.get("APP_ENV","development"),
            "port": os.environ.get("PORT","8000"),
            "build_by": "Maverick"
        }
        self._send_json(200,info)
        logger.info("INFO CHECKED : OK")

    def _send_json(self,status_code,data):
        body = json.dumps(data,indent=2).encode()
        self.send_response(status_code)
        self.send_header("Content-Type","application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self,format,*args):
        logger.info(f"Request: {self.path}")
    
def validate_env():
    required = ["APP_NAME","APP_ENV"]
    missing = [v for v in required if not os.environ.get(v)]
    if missing:
        logger.error(f"Missing required enviroment variables : {missing}")
        raise ValueError(f"Missing : {missing}")
    logger.info("Environment validation passed")

def main():
    validate_env()

    port = int(os.environ.get("PORT",8000))

    server = HTTPServer(("0.0.0.0",port),HealthHandler)

    logger.info(f"Starting {os.environ.get('APP_NAME')} on port{port}")
    logger.info(f"Environment: {os.environ.get('APP_ENV')}")
    logger.info("Endpoints : /health /info")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info("Server shutting down...")
        server.shutdown()

if __name__ == "__main__":
    main()
    