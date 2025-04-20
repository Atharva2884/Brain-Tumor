pipeline {
    agent any

    environment {
        // Environment variables, such as your Python version or project directories
        PYTHON_VERSION = '3.12'
        VENV_DIR = 'venv'
        PROJECT_DIR = 'brain-tumor-predictor-pipeline'
        REQUIREMENTS_FILE = 'requirements.txt'
    }

    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                script {
                    echo "🚚 Checking out source code..."
                    checkout scm
                }
            }
        }

        stage('Build Environment') {
            steps {
                script {
                    echo "🏗️ Building Python environment..."
                    // Create a virtual environment
                    bat "python -m venv ${env.VENV_DIR}"
                    // Activate the virtual environment
                    bat ".\\${env.VENV_DIR}\\Scripts\\activate"
                    // Install dependencies from requirements.txt
                    bat "pip install --upgrade pip"
                    bat "pip install -r ${env.REQUIREMENTS_FILE}"
                }
            }
        }

        stage('Build Verification') {
            steps {
                script {
                    echo "🔍 Verifying the build..."
                    // You can add any build verification steps, like running tests here
                    bat "python -m unittest discover"
                }
            }
        }

        stage('Deploy to Staging') {
            steps {
                script {
                    echo "🚀 Deploying to Staging..."
                    // Example: Deploying the application to staging
                    // You could use tools like Docker or SCP here for deployment
                    // bat "docker-compose up -d"
                }
            }
        }

        stage('Production Deployment') {
            steps {
                script {
                    echo "🌍 Deploying to Production..."
                    // Example: Deploying the application to production
                    // Add any necessary steps to deploy your application
                    // bat "docker-compose -f docker-compose.prod.yml up -d"
                }
            }
        }
    }

    post {
        always {
            echo "🧹 Cleaning up resources..."
            // Clean up resources like virtual environments or temporary files
            bat "rmdir /s /q ${env.VENV_DIR}"
        }

        success {
            echo "✅ Pipeline completed successfully!"
        }

        failure {
            echo "❌ Pipeline failed!"
        }
    }
}
