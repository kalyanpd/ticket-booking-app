pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/kalyanpd/ticket-booking-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ticket-booking-app:latest .'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Stop old container if running
                    sh 'docker rm -f ticket-booking || true'
                    
                    // Run new container
                    sh 'docker run -d -p 5000:5000 --name ticket-booking ticket-booking-app:latest'
                }
            }
        }
    }
}

