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
