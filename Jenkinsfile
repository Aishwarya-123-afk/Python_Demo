pipeline {
    agent any
    stages {
      stage('Run Python Script') {
            steps {
                sh 'python sample.py'
            }
        }
       
        stage('push code') {
            steps {
               sh 'git add .'
               sh 'git commit -m "update done"'
               sh 'git push'
            }
        }
    }
}
