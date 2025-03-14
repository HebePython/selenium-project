pipeline {
    agent any

    triggers {
        // Add GitHub pull request trigger
        githubPullRequest(
            cron: 'H/5 * * * *',
            triggerPhrase: '.*test\\s+this\\s+please.*',
            onlyTriggerPhrase: false,
            useGitHubHooks: true,
            permitAll: false,
            autoCloseFailedPullRequests: false,
            displayBuildErrorsOnDownstreamBuilds: true,
            whiteListTargetBranches: ['development', 'main']
        )
    }
    
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
                # Create a Python virtual environment
                python3 -m venv venv
                
                # Activate the virtual environment
                . venv/bin/activate
                
                # Install packages within virtual environment
                pip install pytest pytest-html selenium
                
                # Create test results directory
                mkdir -p test-results
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                # Activate the virtual environment
                . venv/bin/activate
                
                # Export environment variable for headless mode
                export SELENIUM_HEADLESS=true
                
                # Run tests with Python module path
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