pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ELAKIYA-C7/To-Do.git'
            }
        }

        stage('Build') {
            steps {
                echo "Build step: nothing to compile for static site"
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: '**/*.html, **/*.js, **/*.css', allowEmptyArchive: true
            }
        }

        stage('Test Add Button') {
            steps {
                echo 'Running Selenium test for Add button'
                bat 'python test_todo.py' // Use this on Windows
                // sh 'python3 test_todo.py' // Use this on Linux/Mac
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}