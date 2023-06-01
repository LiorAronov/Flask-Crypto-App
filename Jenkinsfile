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
                dir("tf_test/infrastructure/dev") {
                    sh 'terraform init'
                    sh 'terraform plan -out=tfplan'
                }
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
                def plan = sh(returnStdout: true, script: "terraform show -json tfplan")
                input message: 'Do you want to apply the plan?', parameters: [text(name: 'Plan', description: 'Please review the plan', defaultValue: plan)]
            }
        }

        stage('Apply') {
            steps {
                dir("tf_test/infrastructure/dev") {
                sh "terraform apply"
                }
            }
        }
    }
}