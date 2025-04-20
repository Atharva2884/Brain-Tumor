pipeline {
    agent any

    environment {
        APP_NAME = 'brain-tumor-predictor'
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                echo 'Creating virtual environment and installing dependencies...'
                bat '''
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat '''
                    docker build -t %APP_NAME%:latest .
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running the Flask app in a Docker container...'
                bat '''
                    docker run -d -p 5000:5000 --name %APP_NAME%_container %APP_NAME%:latest
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
            // Clean workspace to avoid issues in future builds
            cleanWs()
        }
    }
}
