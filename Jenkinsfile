pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "kalyanpd/ticket-booking-app"   // Your DockerHub repo
	DOCKER_USER = 'kalyan3599'
	DOCKER_CREDENTIALS = "1234"                   // Jenkins credentials ID
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/kalyanpd/ticket-booking-app.git'
                sh 'ls -l'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                    docker rmi -f ${DOCKER_IMAGE}:latest || true
                    docker build -t ${DOCKER_IMAGE}:latest .
                """
            }
        }
	stage('Push to DockerHub') {
	    steps {
       		 withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS}",
                                          usernameVariable: 'DOCKER_USER',
                                          passwordVariable: 'DOCKER_PASS')]) {
            	sh """
                echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                docker push ${DOCKER_IMAGE}:latest
                docker logout
            """
        }
    }
}

        stage('Run Container') {
            steps {
                sh """
                    docker rm -f ticket-booking-app || true
                    docker run -d --name ticket-booking-app -p 8080:80 ${DOCKER_IMAGE}:latest
                """
            }
        }
    }
}

