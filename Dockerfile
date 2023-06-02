From python:3.6

Run pip install flask

copy . /ops/

Expose 8080

WORKDIR /opt

ENTRYPOINT [ "python", "app.py"]ubuntu@