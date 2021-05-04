pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        build(quietPeriod: 1, job: 'test')
      }
    }

  }
}