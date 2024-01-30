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
                bat 'npm install'
            }
        }

        stage('Construir') {
            steps {
                bat 'npm run build'
            }
        }

        stage('Enviar Correo Electrónico') {
            steps {
                script {
                    def scriptPath = "send_email.py"
                    def cmd = "python ${scriptPath}"

                    // Ejecutar el script Python
                    bat returnStatus: true, script: cmd
                }
            }
        }
    }
}
