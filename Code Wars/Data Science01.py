import pandas as pd

uri = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv'
filmes = pd.read_csv(uri)  # dataframe
filmes.head()
filmes.columns = ["filmesid", 'titulo', 'gêneros']

uri = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv'

notas = pd.read_csv(uri)  # serie
notas.head()
notas.columns = ['usuarioid', 'filmesid', 'nota', 'momento']

notas.describe()

notas['nota'].head()
notas['nota'].unique()

print(uri)
