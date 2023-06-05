FROM ubuntu

RUN apt update
RUN apt install python3-pip -y
RUN apt install python3-venv -y
RUN apt install -y git
RUN pip install -r requirements.txt

WORKDIR /app-d

COPY . .

CMD [ "python", "app.py" ]

