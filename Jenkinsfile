node {
    stage('Checkout') {
        checkout scm
    }

    stage('Instalar Dependencias') {
        bat 'npm install'
    }

    stage('Construir') {
        bat 'npm run build'
    }

    stage('Enviar Correo Electrónico') {
        script {
            // Ejecutar el script de Python 
            bat 'python script.py'
        }
    }
}
