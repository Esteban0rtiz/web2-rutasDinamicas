node {
    stage('Checkout') {
        checkout scm
    }

    stage('Instalar Dependencias') {
         'npm install'
    }

    stage('Construir') {
         'npm run build'
    }

    stage('Enviar Correo Electrónico') {
        script {
            // Agrega el comando para ejecutar tu script de Python aquí
           'python script.py'
        }
    }
}
