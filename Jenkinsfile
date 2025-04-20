pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                script {
                    // Clone your repository
                    git 'https://github.com/Atharva2884/Brain-Tumor.git'
                }
            }
        }
        
        stage('Build') {
            steps {
                script {
                    // Example build step
                    echo 'Building the project'
                    // Add your build commands here
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    // Example test step
                    echo 'Running tests'
                    // Add your test commands here
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    // Example deployment step
                    echo 'Deploying the project'
                    // Add your deployment commands here
                }
            }
        }
    }
}
