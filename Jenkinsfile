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
                        dir("tf_test")
                        {
                            git "https://github.com/LiorAronov/Flask-Crypto-App.git"

                        }
                    }
                }
            }

        stage('Plan') {
            steps {
                sh 'pwd;cd tf_test/infrastructure/dev ; terraform init'
                sh "pwd;cd tf_test/infrastructure/dev ; terraform plan "
                sh 'pwd;cd tf_test/infrastructure/dev ; terraform show '
            }
        }
        stage('Approval') {
           when {
               not {
                   equals expected: true, actual: params.autoApprove
               }
           }

           steps {
               script {
                    def plan = readFile 'terraform/tfplan.txt'
                    input message: "Do you want to apply the plan?",
                    parameters: [text(name: 'Plan', description: 'Please review the plan', defaultValue: plan)]
               }
           }
       }

        stage('Apply') {
            steps {
                sh "pwd;cd tf_test/infrastructure/dev  ; terraform apply"
            }
        }
    }

  }