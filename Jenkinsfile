pipeline{
    agent any
    triggers {
    githubPush()
    }
    stages{
        stage("Code Clone"){
            steps{
                echo "Code Clone Stage"
                git url: "https://github.com/manish-g0u74m/Simple-k8s-python-task.git", branch: "main"
            }
        }
        stage("Code Build & Test"){
            steps{
                echo "Code Build Stage"
                sh "docker build -t kainskep-app ."
            }
        }
        stage("Push To DockerHub"){
            steps{
                withCredentials([usernamePassword(
                    credentialsId:"dockerHubCreds",
                    usernameVariable:"dockerHubUser", 
                    passwordVariable:"dockerHubPass")]){
                sh 'echo $dockerHubPass | docker login -u $dockerHubUser --password-stdin'
                sh "docker image tag kainskep-app:latest ${env.dockerHubUser}/kainskep-app:latest"
                sh "docker push ${env.dockerHubUser}/kainskep-app:latest"
                }
            }
        }
        stage("Deploy"){
            steps{
                sh "kubectl apply -f k8s-pod.yml"
                sh "kubectl apply -f k8s-service.yml"
            }
        }
    }
}
