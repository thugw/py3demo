pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''
            echo "build start ..."
            return
        '''
      }
    }
    stage('Deploy') {
      steps {
        sh '''
            echo "deploy start ..."
            python3 d1/arr.py
        '''
      }
    }
  }

  post {
    always{
        echo "always ..."
    }
    changed {
        echo "changed ..."
    }
    failure {
        echo "failure ..."
    }
    success {
        echo "success ..."
    }
    unstable {
        echo "ustable ..."
    }
    aborted {
        echo "aborted..."
    }
  }

}