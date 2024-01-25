node {
    stage('Checkout') {
        checkout scm
    }

    stage('Instalar Dependencias') {
        sh 'npm install'
    }

    stage('Construir') {
        bat 'npm run build'
    }

    
}
