pipeline {
  agent {
    docker {
      image 'python:alpine3.7'
      args '-p 5000:5000'
    }

  }
  stages {
    stage('Build') {
      steps {
        echo 'Building..'
        sh 'apk add py3-pip'
        sh 'apk add --update alpine-sdk'
        sh 'apk add --update libstdc++'
        sh '''apk add --update --no-cache postgresql-client
 '''
        sh 'pip install -r requirements.txt'
        sh 'python ./netconf \\menu/main.py &'
        sh '''apk add --update --no-cache --virtual .tmp-build-deps build-base gcc python3-dev postgresql-dev musl-dev libffi-dev openssl-dev cargo
'''
      }
    }

    stage('Test') {
      steps {
        echo 'Testing..'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying....'
      }
    }

  }
  environment {
    registry = 'antonpast/netconf'
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
}