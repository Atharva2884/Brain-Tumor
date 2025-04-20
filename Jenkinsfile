pipeline {
    agent any

    environment {
        IMAGE_NAME = "brain-tumor-app"
        CONTAINER_NAME = "brain-tumor-container"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/your-username/your-brain-tumor-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Stop Old Container') {
            steps {
                sh """
                docker rm -f ${CONTAINER_NAME} || true
                """
            }
        }

        stage('Run New Container') {
            steps {
                sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}"
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful!'
        }
        failure {
            echo '❌ Deployment failed.'
        }
    }
}
