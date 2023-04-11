pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                 git branch: 'main', url: 'https://github.com/Aishwarya-123-afk/Python_Demo.git' 
            }
        }
        stage('Test') { 
            steps {
                bat 'python sample.py' 
            }
        }
        stage('Deploy') { 
            steps {
                git add .
                git commit -m "updated checklists"
                git push
            }
        }
    }
}
