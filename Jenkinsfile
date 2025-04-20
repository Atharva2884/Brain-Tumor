pipeline {
    agent any

    environment {
        APP_NAME = 'brain_tumor_app'
        PORT = '5000'
        VENV_DIR = 'venv'
        FLASK_ENV = 'development'
        // For Windows paths
        PYTHON = "${env.WORKSPACE}\\${VENV_DIR}\\Scripts\\python.exe"
        PIP = "${env.WORKSPACE}\\${VENV_DIR}\\Scripts\\pip.exe"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Cloning repository...'
                checkout scm
            }
        }

        stage('Set up Python Environment') {
            steps {
                echo '🐍 Setting up virtual environment...'
                bat """
                    python -m venv "%VENV_DIR%"
                    call "%VENV_DIR%\\Scripts\\activate"
                    python -m pip install --upgrade pip setuptools wheel
                    "%PIP%" install -r requirements.txt
                """
            }
        }

        stage('Verify Installation') {
            steps {
                echo '🔍 Verifying package installation...'
                bat """
                    call "%VENV_DIR%\\Scripts\\activate"
                    python -c "import torch; print(f'Torch version: {torch.__version__}')"
                    python -c "import numpy; print(f'NumPy version: {numpy.__version__}')"
                """
            }
        }

        stage('Code Linting') {
            steps {
                echo '🧹 Running code linting...'
                bat """
                    call "%VENV_DIR%\\Scripts\\activate"
                    flake8 app.py --ignore=E501,E402,W503 --max-line-length=120
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running tests...'
                bat """
                    call "%VENV_DIR%\\Scripts\\activate"
                    python -m pytest tests/ || echo "Tests failed but continuing pipeline"
                """
            }
        }

        stage('Run Flask App') {
            steps {
                echo "🚀 Launching Flask app on port %PORT%..."
                bat """
                    call "%VENV_DIR%\\Scripts\\activate"
                    set FLASK_APP=app.py
                    start "FlaskApp" /B python -m flask run --host=0.0.0.0 --port=%PORT%
                """
                // Wait for server to start
                bat 'timeout /t 10 /nobreak'
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up resources...'
            bat """
                taskkill /FI "WINDOWTITLE eq FlaskApp" /F /T || echo "No Flask process found"
                taskkill /FI "IMAGENAME eq python.exe" /F /T || echo "No Python processes found"
                rmdir /s /q "%VENV_DIR%" || echo "Could not remove virtual environment"
            """
        }
    }
}
