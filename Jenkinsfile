pipeline {
   agent  any

    environment {
        AWS_ACCESS_KEY_ID     = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
    }


    stages {
        stage('Checkout') {
            steps {
                script{
                    git "https://github.com/LiorAronov/Flask-Crypto-App.git"
                }
            }
        }

        stage('Terraform Init') {
            steps { 
                dir('infrastructure/dev') {
                sh 'terraform init'
                }
            }
        }

        stage('Terraform Plan') {
            steps {
                dir('infrastructure/dev') {
                sh 'terraform plan'
                }
            }
        }

        stage('Terraform Apply') {
            steps {
                dir('infrastructure/dev') {
                sh 'terraform apply -auto-approve'
                }
            }
        }
    }
}