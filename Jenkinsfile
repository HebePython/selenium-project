pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Verify Environment') {
            steps {
                sh '''
                echo "Python version:"
                python3 --version
                
                echo "Chrome version:"
                google-chrome --version
                
                echo "ChromeDriver version:"
                chromedriver --version
                '''
            }
        }
        
        stage('Prepare Test Environment') {
            steps {
                sh '''
                # Use Python if available, install packages in user space
                python3 -m pip install --user pytest pytest-html selenium || python -m pip install --user pytest pytest-html selenium
                
                # Create test results directory
                mkdir -p test-results
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                # Add pip user bin directory to PATH
                export PATH=$PATH:~/.local/bin
                
                # Export environment variable for headless mode
                export SELENIUM_HEADLESS=true
                
                # Run tests with Python module path
                python3 -m pytest src/tests/ -v --junitxml=test-results/junit-report.xml --html=test-results/report.html || \
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