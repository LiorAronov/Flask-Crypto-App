sudo apt-get update
sudo apt-get install -y python3-venv

sudo apt-get install -y git
git clone https://github.com/LiorAronov/Flask-Crypto-App.git
cd Flask Crypto App/Production-Env/app

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
