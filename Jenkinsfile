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
                 {
                sh 'pwd; cd tf_test/infrastructure/dev; terraform init'
                sh 'pwd; cd tf_test/infrastructure/dev; terraform plan -out=tfplan'
                sh 'pwd; cd tf_test/infrastructure/dev; terraform show -json tfplan > tfstate.json'
                }
            }
        }

        stage('Approval') {
            steps {
                script {
                    if (!params.autoApprove) {
                        def state = readFile 'tf_test/infrastructure/dev/tfstate.json'
                        input message: 'Do you want to apply the plan?', parameters: [
                            text(name: 'State', description: 'Please review the state', defaultValue: state)
                        ]
                    }
                }
            }
        }
            

        stage('Apply') {
            steps {
                sh 'pwd; cd tf_test/infrastructure/dev; terraform apply tfplan'

            }
        }
    }
}
    
