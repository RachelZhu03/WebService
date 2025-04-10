pipeline {
    agent any
    environment {
        
        PATH = "/Users/rachelqu/anaconda3/bin:$PATH"
    }
    stages {
        stage('Clone Repo') {
            steps {
               git branch: 'main', url: 'https://github.com/RachelZhu03/WebService.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 test_main.py > test_results.txt'
            }
        }
        stage('Create PDF Report') {
            steps {
                sh 'python3 generate_pdf.py'
            }
        }
        stage('Zip Everything') {
            steps {
                sh '''
            /usr/local/bin/mongodump --db=inventory_db --out=dump
            zip -r database-$(date +%Y-%m-%d-%H%M).zip dump
            zip -r complete-$(date +%Y-%m-%d-%H%M).zip . test_results.pdf
        '''
            }
        }
    }
}