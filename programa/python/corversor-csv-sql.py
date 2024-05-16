import csv
import re
from pathlib import Path

def extrair_dados()
# Obter o diretório atual
    diretorio_atual = Path(__file__).parent

# Gerar o caminho completo do arquivo CSV
    arquivo_csv = str(diretorio_atual)[:-6] + "dados/dadosSensores_grafico.csv"
    dados = [] 

    with open(arquivo_csv, 'r+') as csvfile:
    # Cria um objeto `reader` para ler as linhas existentes
        reader = csv.reader(csvfile)

    # Lê todas as linhas existentes e armazena em uma lista
        dados_existentes = [linha for linha in reader]
        if dados_existentes[0]!=['DIA DA SEMANA', 'DATA', 'HORA', 'UMIDADE DO SOLO','UMIDADE DO AMBIENTE','TEMPERATURA','VOLUME DE ÁGUA EM L']:
        # Reposiciona o cursor no início do arquivo
            csvfile.seek(0)

    # Cria um objeto `writer` para escrever o cabeçalho
            writer = csv.writer(csvfile)

   # Escreve o cabeçalho (lista de nomes de colunas)
          writer.writerow(['DIA DA SEMANA', 'DATA', 'HORA', 'UMIDADE DO SOLO','UMIDADE DO AMBIENTE','TEMPERATURA','VOLUME DE ÁGUA EM L'])

    # Escreve as linhas existentes de volta para o arquivo
            writer.writerows(dados_existentes)

    

    with open(arquivo_csv, 'r') as csvfile:  #transforma tudo em uma só biblioteca
        reader = csv.DictReader(csvfile) 
        for linha in reader: 
            dados.append(linha)
    valores = str(dados_existentes[1:]).replace('{',"(").replace("}",")").replace("[","(").replace("]",")").replace("TerÃ§a","Terça").replace("SÃ¡bado","Sábado")
#removedor de , para . do float
return dados

x = 0
y = 0
while x < 10:
    valores = valores.replace(f'{x},{y}',f'{x}.{y}')
    y = y+1
    if y == 10:
     y = 0
     x = x+1
print(dados)





