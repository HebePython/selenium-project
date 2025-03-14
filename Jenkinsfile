pipeline {
    agent any

    triggers {
        // Simple periodic polling - this will work on all Jenkins installations
        pollSCM('H/5 * * * *')
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
                        testSelector = "not new_feature"  // Run everything except new-feature tests
                    }
                    else if (branch.startsWith('feature_') || branch.startsWith('feature/')) {
                        echo "Running only new-feature tests for feature branch"
                        testSelector = "new_feature"  // Only run new-feature tests
                    }
                    else if (branch.startsWith('smoke')) {
                        echo "Running smoke tests only"
                        testSelector = "smoke"
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

                    # List test directory contents
                    echo "=== DIRECTORY STRUCTURE ==="
                    find src -type f -name "*.py" | sort

                    # Check if pytest.ini is found
                    echo "=== PYTEST.INI CONTENT ==="
                    cat pytest.ini || echo "pytest.ini not found!"

                    # Show which tests are collected
                    echo "=== COLLECTED TESTS ==="
                    python -m pytest src/tests/ --collect-only

                    # Try collecting just smoke_tests.py
                    echo "=== SMOKE TESTS COLLECTION ==="
                    python -m pytest src/tests/smoke_tests.py --collect-only || echo "Failed to collect smoke tests"

                    # Check for import errors
                    echo "=== CHECKING FOR IMPORT ERRORS ==="
                    python -c "import sys; sys.path.append('src'); import pages; import driver_setup" || echo "Import error detected"

                    # Run tests with Python module path and appropriate filter
                    python -m pytest src/tests/ -v ${testSelector ? "-m '" + testSelector + "'" : ""} --junitxml=test-results/junit-report.xml --html=test-results/report.html || true

                    # Run smoke tests
                    python -m pytest src/tests/ -v -m smoke
                    """
                }
            }
            post {
                always {
                    catchError(buildResult: 'SUCCESS', stageResult: 'SUCCESS') {
                        junit allowEmptyResults: true, testResults: 'test-results/junit-report.xml'
                    }
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