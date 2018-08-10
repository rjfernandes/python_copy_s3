import boto3
import configparser
import os, os.path
from os import walk

class UploadFile:
    success = False
    error = None
    url = None
    isDebug = True
    keyPath = ''

    def __init__(self):
        self.loadConfig()

        if self.error != None:
            return

        s3 = self.session.resource('s3')
        self.bucket = s3.Bucket(self.bucketName)

    def loadConfig(self):
        if not os.path.isfile('config.ini'):
            self.error = 'Erro. Falta arquivo de configuração'
            print(self.error)
        else:
            config = configparser.ConfigParser()
            config.read('config.ini')
            self.session = boto3.session.Session(config['aws']['access_key'], config['aws']['secret_access_key'])
            self.bucketName = config['aws']['bucket']

    def upload(self, file):
        if self.error != None:
            return

        extraKeys = {
            'ACL': 'public-read',
            'ContentType': 'application/pdf'
        }

        filename = file.split('/')[-1]

        keyFile = '{}/{}'.format(self.keyPath, filename)

        print("")
        print("Realizando o upload de {} para {}...".format(filename, keyFile))
        try:
            self.bucket.upload_file(file, keyFile, extraKeys)    
        except:
            print("Erro no upload de {}.".format(filename))
            self.error = 'Erro no upload da imagem'