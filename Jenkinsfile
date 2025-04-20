pipeline {
    agent any
    environment {
        GIT_REPO = 'https://github.com/Atharva2884/Brain-Tumor.git'
        BRANCH = 'main'
        VENV_DIR = 'venv'
    }
    stages {
        stage('Checkout SCM') {
            steps {
                script {
                    checkout scm
                }
            }
        }
        stage('Set up Virtual Environment') {
            steps {
                script {
                    // Assuming you're using Python and venv
                    bat 'python -m venv venv'
                    bat 'venv\\Scripts\\activate'
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        stage('Train Model') {
            steps {
                script {
                    // Add your training command here
                    bat 'python train_model.py'
                }
            }
        }
        stage('Run Flask App') {
            steps {
                script {
                    // Run the Flask application
                    bat 'flask run'
                }
            }
        }
        stage('Deploy to Server') {
            steps {
                script {
                    // Add deployment steps
                }
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            // Perform cleanup actions
        }
    }
}
