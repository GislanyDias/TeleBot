"""Esse módulo tem a função de fazer a função que irá cadastrar e atualizar os valores que serão passados pelo o arquivo gerado, com a extensão .ini. Foram usadas as bibliotecas ConfigParser para fazer o cadastro dos valores e a Copy para fazer um deep copy do template da configuração do arquivo ini. Para isso, foi criada uma Def que recebe como parametros, as variaveis que serão cadastradas"""

#Importa as bibliotecas necessárias
import configparser
import copy

#Chama a biblioteca ConfigParser
config = configparser.ConfigParser()


def cadastra_resultados(cpf,consumo, ptotal,pmax,pmin,mes_tres,mes_seis,ano_um,ano_dois,ano_cinco):
    """Função que recebe os paramentros que serão cadastrados no arquivo .ini, gerando um template de configuração. Após isso, a chave 'usuário' receberá um DeepCopy desse template que será escrito no arquivo criado, chamado 'DadosClientes.ini' """

    template_dados = {"cpf":cpf,
    "consumo":consumo, 
    "ptotal": '{:.2f}'.format(ptotal), 
    "pmax":'{:.2f}'.format(pmax),
    "pmin":'{:.2f}'.format(pmin),
    "mes_tres":'{:.2f}'.format(mes_tres),
    "mes_seis":'{:.2f}'.format(mes_seis),
    "ano_um":'{:.2f}'.format(ano_um),
    "ano_dois":'{:.2f}'.format(ano_dois),
    "ano_cinco":'{:.2f}'.format(ano_cinco)}

    config['usuario'] = copy.deepcopy(template_dados)

    with open("DadosClientes.ini", "w") as guarda_dados:
        config.write(guarda_dados)

