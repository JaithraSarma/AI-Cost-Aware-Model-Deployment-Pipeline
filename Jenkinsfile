pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/<your-username>/ai-cost-aware-pipeline.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python ml/train_model.py'
            }
        }

        stage('Build & Push Docker Image') {
            steps {
                sh 'docker build -t ai-cost-optimizer:latest .'
            }
        }

        stage('Deploy Model') {
            steps {
                sh 'docker run -d -p 5000:5000 ai-cost-optimizer:latest'
            }
        }

        stage('Run FinOps Automation') {
            steps {
                sh 'python scripts/finops_monitor.py'
            }
        }
    }

    post {
        success {
            echo 'MLOps + FinOps pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}
