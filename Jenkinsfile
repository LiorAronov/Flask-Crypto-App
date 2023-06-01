pipeline {

    parameters {
        booleanParam(name: 'autoApprove', defaultValue: false, description: 'Automatically run apply after generating plan?')
    } 
    environment {
        AWS_ACCESS_KEY_ID     = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
    }

   agent  any

    stages {
        stage('checkout') {
            steps {
                script{
                        {
                            git "https://github.com/LiorAronov/Flask-Crypto-App.git"
                            }
                }
            }
        }

        stage('terraform init') {
            steps { 
                dir('infrastructure/dev') {
                sh 'terraform init'
                }
            }
        }

        stage('Plan') {
            steps {
                dir('infrastructure/dev') {
                sh 'terraform plan'
                }
            }
        }

        stage('Apply') {
            steps {
                echo "Terraform action is ${action}"
                dir('infrastructure/dev') {
                sh 'terraform apply'
                    }
                }
            }
    }
}