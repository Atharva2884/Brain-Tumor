pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'  // Specify your virtual environment folder name
        PYTHON = 'python'  // You may use 'python3' if needed
        GIT_REPO_URL = 'https://github.com/yourusername/Brain-Tumor.git'  // Replace with your GitHub repo
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "Cloning the GitHub repository..."
                git url: "${GIT_REPO_URL}", branch: 'main'  // Clone your repository, adjust branch if necessary
            }
        }

        stage('Set up Virtual Environment') {
            steps {
                echo "Setting up Python virtual environment..."
                script {
                    // Check if the virtual environment exists, if not, create one
                    if (!fileExists("${VIRTUAL_ENV}")) {
                        sh "${PYTHON} -m venv ${VIRTUAL_ENV}"
                    }
                    // Activate the virtual environment and install dependencies
                    sh """
                        source ${VIRTUAL_ENV}/bin/activate  # For Linux/macOS
                        # On Windows, use: .\\${VIRTUAL_ENV}\\Scripts\\activate
                        pip install -r requirements.txt
                    """
                }
            }
        }

        stage('Train Model') {
            steps {
                echo "Training the model..."
                script {
                    // Activate the environment and train your model
                    sh """
                        source ${VIRTUAL_ENV}/bin/activate
                        # Train your model (ensure your train.py script is present in the repo)
                        python train.py
                    """
                }
            }
        }

        stage('Run Flask App') {
            steps {
                echo "Starting the Flask app..."
                script {
                    // Start the Flask app or a Gunicorn server (modify for local or deployment purposes)
                    sh """
                        source ${VIRTUAL_ENV}/bin/activate
                        # Run Flask app directly or use Gunicorn on Unix systems
                        # On Windows, use python app.py instead of gunicorn
                        gunicorn app:app --bind 0.0.0.0:5000  # For Linux/macOS (replace with python app.py for Windows)
                    """
                }
            }
        }

        stage('Deploy to Server') {
            steps {
                echo "Deploying the application to the server..."
                script {
                    // You can set up deployment steps here using SSH, Docker, or Kubernetes
                    // Example for Docker deployment:
                    sh """
                        docker build -t brain-tumor-app .
                        docker run -d -p 5000:5000 brain-tumor-app
                    """
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up..."
            // Clean up virtual environment or any temp files if necessary
            sh "rm -rf ${VIRTUAL_ENV}"
        }
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed. Please check the logs."
        }
    }
}
