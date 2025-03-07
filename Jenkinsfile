pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Run Tests') {
            agent {
                docker {
                    image 'python:3.9'
                    args '-v ${WORKSPACE}:/workspace'
                    reuseNode true
                }
            }
            steps {
                sh '''
                cd /workspace
                pip install -r requirements.txt
                pip install pytest pytest-html
                
                # Install Chrome
                wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
                echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
                apt-get update
                apt-get install -y google-chrome-stable
                
                mkdir -p test-results
                python -m pytest src/tests/ -v --junitxml=test-results/junit-report.xml --html=test-results/report.html
                '''
            }
            post {
                always {
                    junit 'test-results/junit-report.xml'
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'test-results',
                        reportFiles: 'report.html',
                        reportName: 'Test Report'
                    ])
                }
            }
        }
    }
    
    post {
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed, please check the report for details.'
        }
    }
}