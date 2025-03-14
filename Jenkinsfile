pipeline {
    agent any

    triggers {
        // Simple periodic polling as a fallback
        pollSCM('H/5 * * * *')
        
        // GitHub PR trigger with correct syntax
        githubPullRequests {
            spec('H/5 * * * *')
            branchRestriction {
                targetBranch('Development', 'main')
            }
        }
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
                pip install pytest pytest-html selenium pytest-markers
                
                # Create test results directory
                mkdir -p test-results
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    def branch = env.BRANCH_NAME ?: env.GIT_BRANCH ?: 'unknown'
                    def testSelector = ""
                    
                    echo "Detected branch: ${branch}"
                    
                    if (branch.contains('/')) {
                        branch = branch.split('/')[1]  // Handle origin/branch format
                    }
                    
                    if (branch == 'main') {
                        echo "Running ALL tests for main branch"
                        testSelector = ""  // Run all tests
                    } 
                    else if (branch == 'Development') {
                        echo "Running selected tests for dev branch"
                        testSelector = "not new-feature"  // Run everything except new-feature tests
                    }
                    else if (branch.startsWith('feature_') || branch.startsWith('feature/')) {
                        echo "Running only new-feature tests for feature branch"
                        testSelector = "new-feature"  // Only run new-feature tests
                    }
                    else {
                        echo "Branch pattern not recognized, running all tests"
                        testSelector = ""  // Default: run all tests
                    }
                    
                    sh """
                    # Activate the virtual environment
                    . venv/bin/activate
                    
                    # Export environment variable for headless mode
                    export SELENIUM_HEADLESS=true
                    
                    # Run tests with Python module path and appropriate filter
                    python -m pytest src/tests/ -v ${testSelector ? "-k '" + testSelector + "'" : ""} --junitxml=test-results/junit-report.xml --html=test-results/report.html
                    """
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