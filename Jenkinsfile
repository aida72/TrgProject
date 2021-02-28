node {    
      def app     
      stage('Clone repository') {               
             
            git branch: "main", url: 'https://github.com/aida72/TrgProject.git'   
      }
          {
      }
      stage('Build image') {         
       
            app = docker.build("123456odi/trgproject")    
       }
        stage('Test image') {           
            app.inside {            
             
             sh 'python /code/test_hello_world.py'       
            }    
        }
        stage('Push image') {
            docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {            
            app.push("${env.BUILD_NUMBER}")            
            app.push("latest")        
            }    
        }
        stage('add ansible') {
           
             ansiblePlaybook( 
             playbook: 'ansible/playbook.yml'
             )
        }
    }