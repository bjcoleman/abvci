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
    stage('Static Analysis')
    {
        sh 'pylint src/abvci/*.py tests/*.py'
    }
}