import pymongo
from faker import Faker
import json

// cria e popula uma collection com 10kb de dados 


# Conecta ao MongoDB (certifique-se de que o MongoDB esteja em execução)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Seleciona o banco de dados (substitua 'seu_banco_de_dados' pelo nome desejado)
db = client['seu_banco_de_dados']

# Nome da coleção
collection_name = 'tecnologias_disruptivas'

# Define a coleção
collection = db[collection_name]

# Gera dados fictícios usando a biblioteca Faker
fake = Faker()

# Função para criar documentos com dois níveis de identação
def create_document():
    technology = {
        'name': fake.word(),
        'description': fake.sentence(),
        'popularity': fake.random_int(min=1, max=10),
        'features': {
            'feature1': fake.word(),
            'feature2': fake.word(),
            'feature3': fake.word(),
        }
    }
    return technology

# Popula a coleção com pelo menos 10 KB de dados
while True:
    document = create_document()
    document_json = json.dumps(document)
    document_size_kb = len(document_json.encode('utf-8')) / 1024
    if document_size_kb >= 10:
        break
    collection.insert_one(document)

print(f"A coleção '{collection_name}' foi populada com pelo menos 10 KB de dados.")
