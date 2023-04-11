pipeline {
    agent any
    stages {
        stage('build') {
            steps {
               git branch: 'main', url: 'https://github.com/Aishwarya-123-afk/Python_Demo.git'
            }
          stage('run python script')
            {
                bat 'python sample.py'
            }
        }
    }
}
