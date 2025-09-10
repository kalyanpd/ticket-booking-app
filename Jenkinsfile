pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "kalyanpd/ticket-booking-app"   // Replace with your DockerHub username/repo
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/kalyanpd/ticket-booking-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE:latest .'
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: '1234', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh '''
                            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                            docker push $DOCKER_IMAGE:latest
                            docker logout
                        '''
                    }
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Stop old container if running
                    sh 'docker rm -f ticket-booking || true'

                    // Run new container from DockerHub image
                    sh 'docker run -d -p 5005:5000 --name ticket-booking $DOCKER_IMAGE:latest'
                }
            }
        }
    }
}

