sudo apt-get update
sudo apt-get install -y python3-venv

sudo apt-get install -y git
git clone https://github.com/LiorAronov/Flask-Crypto-App.git
cd Flask-Crypto-App/Production-Env/app

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sudo apt-get install nginx

  GNU nano 6.2                                                                             /etc/systemd/system/app.service                                                                                      
[Unit]
Description=Gunicorn instance for a simple hello world app
After=network.target
[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/Flask-Crypto-App/Production-Env/app
ExecStart=/home/ubuntu/Flask-Crypto-App/Production-Env/app/venv/bin/gunicorn -b localhost:8000 app:app
Restart=always
[Install]
WantedBy=multi-user.target

















