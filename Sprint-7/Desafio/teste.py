import boto3
import os
import csv
from datetime import datetime

# Acesso AWS

chaveAWS = 'key-aws'
chaveSecretaAWS = 'secret-key'

# Bucket S3

bucketNome = 'bucketlab-will'
CSV_DIR = '/app'



def uploadS3(local_path, s3_path):
    s3 = boto3.client('s3', aws_access_key_id=chaveAWS, aws_secret_access_key=chaveSecretaAWS)
    s3.upload_file(local_path, bucketNome, s3_path)


def main():
    dataAtual = datetime.now().strftime("%Y/%m/%d")
    for filename in ['movies.csv', 'series.csv']:
        csv_path = os.path.join(CSV_DIR, filename)
        s3_path = f'Raw/Local/CSV/{filename.split(".")[0]}/{dataAtual}/{filename}'

        uploadS3(csv_path, s3_path)
        
        print(f"UPLOAD {csv_path} S3://{bucketNome}/{s3_path} SUCESSO")


if __name__ == "__main__":
    main()

