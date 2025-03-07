pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            args '--network="host" -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    triggers {
        githubPush()
    }

    parameters {
        string(name: 'BRANCH_NAME', defaultValue: 'main', description: 'Branch to build')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup') {
            steps {
                sh '''
                apt-get update
                apt-get install -y wget gnupg2
                wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
                echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
                apt-get update
                apt-get install -y google-chrome-stable
                pip install -r requirements.txt
                pip install pytest-xdist pytest-html
                '''
            }
        }
        
        stage('Test') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'main') {
                        // Run full test suite for main branch
                        sh 'python -m pytest src/tests/ -v --junitxml=test-results/junit-report.xml --html=test-results/report.html'
                    } else if (env.BRANCH_NAME == 'Development') {
                        // Maybe run a subset of tests for dev branch or with different flags
                        sh 'python -m pytest src/tests/ -v --junitxml=test-results/junit-report.xml --html=test-results/report.html'
                    } else if (env.BRANCH_NAME.startsWith('feature/')) {
                        // For feature branches, maybe run only specific tests
                        sh 'python -m pytest src/tests/ -v --junitxml=test-results/junit-report.xml --html=test-results/report.html'
                    }
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