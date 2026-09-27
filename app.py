from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>Hello from Gayanuka's Dockerised Flask App!</h1>
    <p>SWE40006 - Task 4.2</p>
    <p>Running inside container: {socket.gethostname()}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)