def  app = ''
pipeline {
    agent any
    stages {
            stage('Clone repository') {               
                steps {
                    script {
                        git branch: "main", url: 'https://github.com/aida72/TrgProject.git' 
                    }
                }  
            }
            stage('Build image') {         
                steps {
                        script {
                            app = docker.build("123456odi/trgproject")   
                        }
                    }   
            }
            stage('Test image') { 
                steps {
                        script {          
                        app.inside {                 
                            sh 'python /code/test_hello_world.py'       
                        }    
                        }
                }
            }
            stage('Push image') {
                steps {
                    script {
                        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {            
                            app.push("${env.BUILD_NUMBER}")            
                            app.push("latest") 
                        } 
                    }
                }  
            }
            stage('add ansible') {
                steps {
                    script {
                        ansiblePlaybook( 
                            playbook: 'ansible/playbook.yml'
                        )
                    }
                }
            }
        }
}