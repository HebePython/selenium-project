pipeline {
    agent any  // Use the Jenkins agent directly
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                # Install Python3 if not available
                apt-get update || true
                apt-get install -y python3 python3-pip python3-venv || true
                
                # Display Python version
                python3 --version
                '''
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                sh '''
                # Create virtual environment with python3
                python3 -m venv venv || python -m venv venv
                . venv/bin/activate
                
                # Upgrade pip
                pip install --upgrade pip
                
                # Install requirements
                pip install -r requirements.txt
                pip install pytest pytest-html
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    sh '''
                    . venv/bin/activate
                    mkdir -p test-results
                    python -m pytest src/tests/ -v --junitxml=test-results/junit-report.xml --html=test-results/report.html
                    '''
                }
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