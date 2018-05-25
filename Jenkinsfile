pipeline {
  agent any
  stages {
    stage('run') {
      steps {
        sh '''echo "test"
pip install -r requirements.txt

python run.py'''
      }
    }
  }
}