pipeline {
    agent any

    environment {
        IMAGE_NAME = 'my-app'
        IMAGE_TAG = 'v1.0.0'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                echo "Running tests"
                sh 'pytest -v test_app.py'
            }
        }

        stage('Build') {
            steps {
                echo "Building Docker image"
                sh 'python docker_build.py'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push') {
            steps {
                echo "Pushing Docker image"
                sh 'python docker_push.py'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo "Deploying"
                sh 'python deploy.py'
            }
        }
    }

    post {
        success {
            echo "Pipeline succeeded!"
        }
        failure {
            echo "Pipeline failed!"
        }
        always {
            cleanWs()
        }
    }
}
