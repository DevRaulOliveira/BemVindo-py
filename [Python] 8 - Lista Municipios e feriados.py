import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL do site com a lista de municípios e feriados
url = 'https://www.calendario.com.br/'

# Fazer a requisição ao site
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extrair os nomes dos municípios
municipios = [option.get_text() for option in soup.find_all('option')]

# Extrair os feriados
feriados = [option.get_text() for option in soup.find_all('option', attrs={'data-type': 'municipal'})]

# Criar um DataFrame com os dados
df = pd.DataFrame({'Município': municipios, 'Feriado': feriados})

# Exibir a tabela
print(df)
