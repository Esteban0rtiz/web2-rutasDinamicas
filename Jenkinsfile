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
        // Ruta al script Python
        def scriptPath = "send_email.py"

        // Ejecutar el script Python
         "python ${scriptPath}"
    }
}
}
