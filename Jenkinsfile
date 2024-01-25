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

    
}
