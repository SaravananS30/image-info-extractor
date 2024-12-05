pipeline {
    agent none
    stages {
        stage("build & SonarQube Analysis"){
            agent any
            steps {
                withSonarQubeEnv('Sonar'){
                    sh 'mvn clean package sonar:sonar'
                }
            }
        }
    }
}
