pipeline {
    agent any

    environment {
        IMAGE_NAME = 'your-dockerhub-username/my-app'  // <-- Replace this
        IMAGE_TAG = 'v1.0.0'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest -v test_app.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    . venv/bin/activate
                    IMAGE_NAME=$IMAGE_NAME IMAGE_TAG=$IMAGE_TAG python docker_build.py
                '''
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                    . venv/bin/activate
                    IMAGE_NAME=$IMAGE_NAME IMAGE_TAG=$IMAGE_TAG python docker_push.py
                '''
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh '''
                    . venv/bin/activate
                    python deploy.py
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline succeeded!"
        }
        failure {
            echo "❌ Pipeline failed!"
        }
        always {
            cleanWs()
        }
    }
}
