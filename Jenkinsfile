pipeline {
  agent any

  parameters {
    choice(name: 'CLOUD_PROVIDER', choices: ['simulate','azure','aws'], description: 'Run mode')
  }

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/<your-username>/ai-cost-aware-pipeline.git'
      }
    }

    stage('Install Deps') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Train Model') {
      steps {
        sh 'python ml/train_model.py'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t ai-cost-optimizer:latest .'
      }
    }

    stage('Run Selected Mode') {
      steps {
        script {
          if (params.CLOUD_PROVIDER == 'simulate') {
            sh 'python scripts/finops_monitor.py'
          } else if (params.CLOUD_PROVIDER == 'azure') {
            sh 'python scripts/deploy_azure.py'
          } else {
            sh 'python scripts/deploy_aws.py'
          }
        }
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'reports/*.json', allowEmptyArchive: true
    }
    success { echo "Pipeline executed successfully" }
    failure { echo "Pipeline failed" }
  }
}
