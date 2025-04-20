pipeline {
    agent any

    environment {
        APP_NAME = 'brain_tumor_app'
        PORT = '5000'
        VENV_DIR = 'venv'
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
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Code Linting') {
            steps {
                echo '🧹 Running code linting...'
                bat """
                    call %VENV_DIR%\\Scripts\\activate
                    pip install flake8
                    flake8 app.py --ignore=E501
                """
            }
        }

        stage('Run Flask App') {
            steps {
                echo "🚀 Launching Flask app on port %PORT%..."
                bat """
                    call %VENV_DIR%\\Scripts\\activate
                    set FLASK_APP=app.py
                    set FLASK_ENV=development
                    start /B flask run --host=0.0.0.0 --port=%PORT%
                """
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up background processes...'
            bat """
                taskkill /F /IM python.exe /T || exit 0
            """
        }
    }
}
