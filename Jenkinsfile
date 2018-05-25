pipeline {
  agent any
  stages {
    stage('run') {
      steps {
        sh '''echo "test"
pip -r requirements.txt

python run.py'''
      }
    }
  }
}