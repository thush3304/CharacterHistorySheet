pipeline{
    agent any

    environment{
        DOCKERHUB = credentials('DOCKERHUB')
        DATABASE_URI = credentials('DATABASE_URI')
        MYSQL_ROOT_PASSWORD = credentials('MYSQL_ROOT_PASSWORD')
    }

    stages{
        stage('Install Dependencies'){
            steps{
                sh "bash scripts/setup.sh"
            }
        }

        stage('Run Unit Tests'){
            steps{
                sh "bash scripts/test.sh"
            }
        }

        stage('Build And Push Docker Images'){
            steps{
                sh "bash scripts/build.sh"
            }
        }

        stage('Configure Hosts For Deployment'){
            steps{
                sh "bash scripts/config.sh"
            }
        }

        stage('Deploy Stack Manager'){
            steps{
                sh "bash scripts/deploy.sh"
            }
        }
    }
}