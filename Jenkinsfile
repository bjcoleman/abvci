node
{
    stage('Fetch')
    {
        checkout scm
    }
    stage('Unit Testing')
    {
        sh 'tox'
    }
}