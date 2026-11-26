import os, socket
from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    version = os.getenv("APP_VERSION", "dev")[:7]
    return f"<h1>NGDS CI/CD</h1><p>version: {version}</p><p>pod: {socket.gethostname()}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)