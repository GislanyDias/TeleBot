"""
Esse módulo tem a função atualizar as variaveis que estão sendo passadas no arquivo HTML. Ele faz isso importando uma biblioteca web do python, chamada Flask, que tem como recurso usar templates de html, a partir disso, pode-se fazer modificações nesse template por meio de uma função chamada 'render_template'. Esse módulo faz essa atualização, por meio da importação da biblioteca ConfigParser, lendo o arquivo que foi passado por ela. Depois da leitura, ele irá atribuir a variaveis, os valores que estão no objeto 'usuário' do arquivo .ini e substituir nos parametros do html. 

"""

#Importa as bibliotecas necessárias
from flask import Flask,render_template
import configparser


app = Flask('appteste')


#Chama o ConfigParser e lê o arquivo .ini
config = configparser.ConfigParser()
config.read('DadosClientes.ini')


#Atribuí as variavéis, os valores que estão no objeto 'usuário'
get_consumo = config['usuario']['consumo']
get_ptotal = config['usuario']['ptotal']
get_pmax = config['usuario']['pmax']
get_pmin = config['usuario']['pmin']
get_mes_tres = config['usuario']['mes_tres']
get_mes_seis = config['usuario']['mes_seis']
get_ano_um = config['usuario']['ano_um']
get_ano_dois = config['usuario']['ano_dois']
get_ano_cinco = config['usuario']['ano_cinco']


#Define a rota em que o site será executado e chama a função de renderização do arquivo
@app.route('/')
def index ():

    #Retorna a função, com a renderização do arquivo 'index.html' e subtituí as variavéis html pelos valores chamados anteriormente
    return render_template('index.html', consumo=get_consumo, ptotal = get_ptotal, pmax=get_pmax, pmin=get_pmin, mes_tres = get_mes_tres, mes_seis = get_mes_seis, ano_um = get_ano_um, ano_dois = get_ano_dois, ano_cinco = get_ano_cinco )


#Condição que faz com que o site rode por meio do seu nome, sem resquícios de erros
if __name__ == '__main__':
    app.run()