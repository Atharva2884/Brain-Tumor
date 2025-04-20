pipeline {
    agent any

    environment {
        APP_NAME = 'brain_tumor_app'
        PORT = '5000'
        VENV_DIR = 'venv'
        FLASK_ENV = 'development'  // Moved to environment for consistency
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Cloning repository...'
                checkout scm
            }
        }

        stage('Set up Python & Virtual Environment') {
    steps {
        echo '🐍 Setting up virtual environment...'
        bat """
            python -m venv "%VENV_DIR%"
            call "%VENV_DIR%\\Scripts\\activate"
            python -m pip install --upgrade pip setuptools wheel
            pip install -r requirements.txt
        """
    }
}

        stage('Code Linting') {
            steps {
                echo '🧹 Running code linting...'
                bat """
                    call "%VENV_DIR%\\Scripts\\activate"
                    pip install flake8
                    flake8 app.py --ignore=E501,E402,W503
                """
            }
        }

        stage('Run Tests') {  // Added test stage
            steps {
                echo '🧪 Running tests...'
                bat """
                    call "%VENV_DIR%\\Scripts\\activate"
                    python -m pytest tests/  // Assuming you have tests
                """
            }
        }

        stage('Run Flask App') {
            steps {
                echo "🚀 Launching Flask app on port %PORT%..."
                bat """
                    call "%VENV_DIR%\\Scripts\\activate"
                    set FLASK_APP=app.py
                    start "FlaskApp" /B flask run --host=0.0.0.0 --port=%PORT%
                """
                // Added title to start command for better process identification
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up background processes...'
            bat """
                taskkill /FI "WINDOWTITLE eq FlaskApp" /F /T || exit 0
                taskkill /FI "IMAGENAME eq python.exe" /F /T || exit 0
            """
        }
    }
}
