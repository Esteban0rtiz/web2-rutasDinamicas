pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Instalar Dependencias') {
            steps {
                 'npm install'
            }
        }

        stage('Construir') {
            steps {
                 'npm run build'
            }
        }

        stage('Enviar Correo Electrónico') {
            steps {
                script {
                    def scriptPath = "send_email.py"
                    def cmd = "python ${scriptPath}"

                    // Ejecutar el script Python
                     returnStatus: true, script: cmd
                }
            }
        }
    }
}
