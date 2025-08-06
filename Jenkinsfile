pipeline {
    agent any

    environment {
        IMAGE_NAME = 'my-app'
        IMAGE_TAG = 'v1.0.0'
        VENV_PATH = 'venv'
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
                    python3 -m venv $VENV_PATH
                    source $VENV_PATH/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    source $VENV_PATH/bin/activate
                    pytest -v test_app.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    source $VENV_PATH/bin/activate
                    python docker_build.py
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
                    source $VENV_PATH/bin/activate
                    python docker_push.py
                '''
            }
        }

        stage('Deploy') {
            when {
                branch 'master'
            }
            steps {
                sh '''
                    source $VENV_PATH/bin/activate
                    python deploy.py
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline succeeded!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
        always {
            cleanWs()
        }
    }
}
