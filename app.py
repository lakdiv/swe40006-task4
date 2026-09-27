from flask import Flask
import socket
import platform

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <html>
    <head>
      <title>SWE40006 Task 4.2</title>
      <style>
        body {{ font-family: Arial, sans-serif; max-width: 700px; margin: 60px auto; line-height: 1.6; }}
        td {{ padding: 4px 20px 4px 0; }}
      </style>
    </head>
    <body>
      <h1>Gayanuka's Dockerised Flask App</h1>
      <p>SWE40006 Software Deployment and Evolution – Task 4.2</p>
      <p>This is a simple Python Flask web application packaged as a Docker image,
         pushed to Docker Hub and deployed on multiple Docker hosts.</p>
      <table>
        <tr><td><b>Container ID</b></td><td>{socket.gethostname()}</td></tr>
        <tr><td><b>Host OS</b></td><td>{platform.system()} {platform.release()}</td></tr>
      </table>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)