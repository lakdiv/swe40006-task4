# swe40006-task4
Simple Python Flask web app containerised with Docker for SWE40006 Task 4 (Credit level).
# SWE40006 – Task 4: Container Deployment with Docker

Simple Python Flask web app containerised with Docker (Task 4.2 – Credit).

## Files
- `app.py` – Flask app listening on port 5000
- `Dockerfile` – builds the image from python:3.12-slim
- `requirements.txt` – Python dependencies

## Build and run locally
docker build -t flask-app .
docker run -d -p 8080:5000 --name myflask flask-app
# open http://localhost:8080

## Docker Hub
docker pull lakdiwwithana/flask-app:v1

## Live deployment
Running on an Azure VM (Ubuntu 24.04): http://20.53.249.202
