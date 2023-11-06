import json
import requests
import boto3
import pandas as pd
import os
from datetime import datetime
import io
def lambda_handler(event, context):
    # Chave API declarada nas variáveis de ambiente do Lambda
    api_key = os.environ.get("chaveAPI")
    
    # Função possui permissão ao S3
    s3 = boto3.client('s3')

    bucketNome = 'bucketlab-will'
    s3KeyMovies = 'Raw/Local/CSV/movies/2023/10/23/movies.csv'
    # s3KeySeries = 'Raw/Local/CSV/series/2023/10/23/series.csv' caso fosse necessário usar séries

    response = s3.get_object(Bucket=bucketNome, Key=s3KeyMovies)
    df = pd.read_csv(response['Body'], sep='|')
    # Vetor para armazenar resultado
    rentaveis = []
    # Filtro para pegar apenas filmes de terror
    filmesTerror = df.loc[(df['genero'] == 'Horror')]
    filmesTerror = filmesTerror.drop_duplicates(subset='id')

    for movie_id in filmesTerror['id']:
        # Busca por informações do filme (id)
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR"
        response = requests.get(url)
        filmeInfo = response.json()

        # Guardar informações necessárias
        languageOriginal = filmeInfo.get('original_language', '')
        titleOriginal = filmeInfo.get('original_title', '')
        popularity = filmeInfo.get('popularity', 0)
        production_countries = [country['name'] for country in filmeInfo.get('production_countries', [])]
        releaseDate = filmeInfo.get('release_date', '')
        duracaoMinutos = filmeInfo.get('runtime', 0)
        spoken_languages = [lang['name'] for lang in filmeInfo.get('spoken_languages', [])]
        vote_average = filmeInfo.get('vote_average', 0)
        vote_count = filmeInfo.get('vote_count', 0)
        revenue = filmeInfo.get('revenue', 0)
        budget = filmeInfo.get('budget', 0)

        # Busca por informações da equipe
        url_credits = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}"
        response_credits = requests.get(url_credits)
        credits_info = response_credits.json()
        director = ""
        production_companies = []
        for membro in credits_info.get('crew', []):
            if membro.get('job') == 'Director':
                director = membro.get('original_name')
                break
        for company in filmeInfo.get('production_companies', []):
            production_companies.append(company.get('name'))
            if director:
                # Guardar informações na variável
                rentaveis.append({
                    'id_filme': movie_id,
                    'budget': budget,
                    'original_language': languageOriginal,
                    'original_title': titleOriginal,
                    'popularity': popularity,
                    'production_countries': production_countries,
                    'release_date': releaseDate,
                    'revenue': revenue,
                    'runtime': duracaoMinutos,
                    'spoken_languages': spoken_languages,
                    'vote_average': vote_average,
                    'vote_count': vote_count,
                    'production_companies': production_companies,
                    'original_name': director
                })
    # Divide df usando list comprehension
    splitRentaveis = [rentaveis[i:i+100] for i in range(0, len(rentaveis), 100)]

    # Retorno da data atual
    dataEnvio = datetime.now()
    ano = dataEnvio.strftime("%Y")
    mes = dataEnvio.strftime("%m")
    dia = dataEnvio.strftime("%d")
    # Estrutura para armazenar resultado em arquivos json (100 em 100)
    for i, part in enumerate(splitRentaveis):
        arquivo = f"rentaveis_{i + 1}.json"
        pathArquivo = f'Raw/TMDB/JSON/{ano}/{mes}/{dia}/{arquivo}'
        arqObj = io.BytesIO(json.dumps(part, ensure_ascii=False, indent=4).encode('utf-8'))
        s3.upload_fileobj(
            Fileobj=arqObj,
            Bucket=bucketNome,
            Key=pathArquivo
        )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
