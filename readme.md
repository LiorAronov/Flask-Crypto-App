# --IN PROGRESS--
#
# Crypto Currency Data Flask Application 

## Introduction
This Flask application is designed to provide users with real-time cryptocurrency information by connecting to the CoinMarketCap and CoinGecko API. \
Leveraging the power of AWS EC2 instances and managed the infrastructure by using Terraform, the application offers a seamless and scalable infrastructure for data retrieval and storage. \
The application have range of features including:
- Market general information.
- Currency up-to-date Prices.
- Currency price history.
- Last 24h trending coins, NFT.
- Public companies holdings data.
- Conversion calculator.
- More features will be uploaded soon.

Additionally, user searches are stored in a MongoDB database, allowing for efficient tracking and monitoring of user activity.

## Infrastructure
The project's infrastructure is built on AWS EC2 Linux instances, which provide a reliable and secure environment for hosting the Flask application. \
By utilizing AWS, we ensure high availability and scalability to handle varying levels of user traffic. \
The infrastructure configuration is automated using Terraform, a widely adopted Infrastructure-as-Code tool, which enables efficient provisioning, configuration, and management of the AWS resources required for the application.\
The infrastructure Terraform configuration includes:
- EC2 Linux instances that hosts the flask application.
- All the necessary settings of the instances (Security Group, Roles, Elastic Ip, key_pair and more).
- S3 bucket & DynamoDB that serves as Terraform remote and locking state.
- Route 53 records that routing EC2 Elastic Ip to domain address.

## Data Retrieval:
Our Flask application integrates with the CoinMarketCap and CoinGecko API, which serves as a trusted and comprehensive source for cryptocurrency data. \
Through a series of well-defined functions, the application extracts relevant information, ensuring accurate and up-to-date data retrieval.\
This data includes market prices, currency details, and other pertinent information required to provide a holistic view of the cryptocurrency market.

## Technologies Used
- Terraform
- AWS
- Linux 
- Python
- Flask
- MongoDB
- HTML
- CSS
- Git
- CoinMarketCap API
- CoinGecko API

## Project Structure
~~~
├── app
│    ├── static
│    │     ├── css
│    │     │     ├── coin_data.css
│    │     │     ├── main_tamplate.css
│    │     │     ├── market_data.css
│    │     │     └── page_style.css
│    │     └── web-image
│    │          ├── background
│    │          │     └── main-background.jpg
│    │          └── icon
│    │                ├── exchange-128.png
│    │                ├── github-64px.png
│    │                └── linkedin-64px.png
│    ├── templates
│    │     ├── coin_data.html
│    │     ├── exchanges.html
│    │     ├── home.html
│    │     ├── main_tamplate.html
│    │     └── market_data.html
│    ├── app.py 
│    ├── CoinGecko.py 
│    ├── CoinMarketCap.py
│    ├── function_action.py
│    ├── Keys.py
│    └── URL_API_Request.py
│    
│    
├── terraform
│    ├── dev
│    │     ├── backend.tf
│    │     ├── main.tf
│    │     ├── terraform.tfvars
│    │     └── variable.tf    │
│    └── modules
│          ├── ec2
│          │     ├── key_pair
│          │     │     ├── main.tf
│          │     │     └── variable.tf
│          │     ├── main.tf
│          │     ├── output.tf
│          │     ├── security_group.tf
│          │     └── variable.tf
│          ├── route53
│          │     ├── data_source.tf
│          │     ├── main.tf
│          │     └── variable.tf
│          ├── tf-state
│          │     ├── main.tf
│          │     └── variable.tf
├── .gitignore
└── README.md

~~~