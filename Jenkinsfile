pipeline {
    agent any

    environment {
        // Application Configuration
        APP_NAME = 'brain-tumor-detection'
        PORT = '5000'
        
        // Environment Paths (Windows)
        VENV_DIR = "${env.WORKSPACE}\\venv"
        PYTHON = "${VENV_DIR}\\Scripts\\python.exe"
        PIP = "${VENV_DIR}\\Scripts\\pip.exe"
        
        // Deployment Flags
        DEPLOY_ENV = 'staging'  // Change to 'production' for live deployment
    }

    stages {
        stage('Checkout') {
            steps {
                echo '🚚 Checking out source code...'
                checkout scm
            }
        }

        stage('Build Environment') {
            steps {
                echo '🏗️ Building Python environment...'
                bat """
                    python -m venv "${VENV_DIR}"
                    call "${VENV_DIR}\\Scripts\\activate"
                    ${PYTHON} -m pip install --upgrade pip setuptools wheel
                    ${PIP} install --prefer-binary -r requirements.txt
                """
            }
        }

        stage('Build Verification') {
            steps {
                echo '🔍 Verifying build...'
                bat """
                    call "${VENV_DIR}\\Scripts\\activate"
                    ${PYTHON} -c "import torch; print('PyTorch OK')"
                    ${PYTHON} -c "import flask; print('Flask OK')"
                """
            }
        }

        stage('Deploy to Staging') {
            when {
                equals expected: 'staging', actual: env.DEPLOY_ENV
            }
            steps {
                echo '🚀 Deploying to staging...'
                bat """
                    call "${VENV_DIR}\\Scripts\\activate"
                    set FLASK_APP=app.py
                    start "BrainTumorApp" /B ${PYTHON} -m flask run --host=0.0.0.0 --port=${PORT}
                    timeout /t 15 /nobreak > nul
                """
                echo "✅ Application running at: http://${env.JENKINS_URL}:${PORT}"
            }
        }

        stage('Production Deployment') {
            when {
                equals expected: 'production', actual: env.DEPLOY_ENV
            }
            steps {
                echo '🚀 PRODUCTION DEPLOYMENT INITIATED...'
                // Add your production deployment steps here
                // Example: Docker build/push, cloud deployment, etc.
                echo '⚠️ Production deployment logic goes here'
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up resources...'
            bat """
                taskkill /FI "WINDOWTITLE eq BrainTumorApp" /F /T > nul 2>&1 || echo "No app process found"
                rmdir /s /q "${VENV_DIR}" > nul 2>&1 || echo "Could not remove venv"
            """
        }
        success {
            echo '✅ Pipeline completed successfully!'
            // Add notification here (Slack, Email, etc.)
        }
        failure {
            echo '❌ Pipeline failed!'
            // Add failure notification here
        }
    }
}
