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
        sh '''pip install --upgrade pip && \\
   apk add --update alpine-sdk && \\
   apk add --update --no-cache postgresql-client && \\
   apk add --update --no-cache --virtual .tmp-build-deps \\
      build-base gcc python3-dev postgresql-dev musl-dev libffi-dev openssl-dev cargo  && \\
   /py/bin/pip install -r /tmp/requirements.txt && \\
'''
        sh 'apk add --update libstdc++'
        sh 'pip install -r requirements.txt'
        sh 'python ./netconf \\menu/main.py &'
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