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
                
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Github_pass', url: 'https://github.com/Aishwarya-123-afk/Python_Demo.git']])
                sh 'git add .'
                sh 'git commit -m "updated checklist"'
                sh 'git push'
            }
        }
    }
}
