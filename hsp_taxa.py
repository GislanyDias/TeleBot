"""Esse módulo tem como função fazer a validação do estado e fazer a iteração com as chaves do dicionário para atualizar seu hsp e tarifa de acordo com o estado dado. Para isso, ele faz a importação das variaveis que estão no módulo taxas para autaliza-las. Para fazer a iteração e pegar as variaveis, foi criado um dicionário, onde a chave é o nome do estado que possui uma lista de valores, no index 0 está o hsp do estado, e no index 1 está a tarifa de energia do local"""


#Importa o módulo taxas
import taxas


#Dicionário com o nome dos estados e seus valores de hsp e tarifa energétia 
hsp_tari = {
    "acre": [4.57,0.582],
    "alagoas": [5.35,0.626],
    "amazonas": [4.42,0.693],
    "amapa": [4.94,0.505],
    "bahia": [5.36,0.620],
    "ceara": [5.69,0.589],
    "distritofederal": [5.28,0.515], 
    "espiritosanto": [4.76,0.611],
    "goias": [5.26,0.600],
    "maranhao": [5.21,0.642],
    "matogrosso": [5.05,0.684],
    "matogrossodosul": [4.99,0.694],
    "minasgerais": [5.42,0.618],
    "para": [4.60,0.766],
    "paraiba": [5.25,0.597],
    "parana": [4.67,0.588],
    "pernambuco": [5.25,0.619],
    "piaui": [5.66,0.582],
    "riodejaneiro": [4.73,1.025],
    "riograndedonorte": [5.70,0.559],
    "rondonia": [4.55,0.514],
    "riograndedosul": [4.43,0.588],
    "roraima": [4.48,0.575],
    "santacatarina": [4.03,0.610],
    "sergipe": [5.50,0.761],
    "saopaulo": [4.45,0.664],
    "tocantins":[5.17,0.669]
}



def valida_loc (local):

    """Função que irá verificar se o estado informado, está nos estados listados no dicionário, caso esteja, será retornado True"""

    if local in hsp_tari:
        return True
        

def set_taxas(est):

    """Função que irá fazer um iteração com as chaves do dicionário, definidas pelos nomes dos estado. Quando o nome do estado informado for igual a alguma chave com o mesmo nome, a variaveis hsp e tarifa assumirão os valores dos indices 0 e 1, respetivamente, da lista que cada estado tem com esses valores"""
    
    for estado,hsp_e_tari in hsp_tari.items():
        if est == estado:
            taxas.hsp = hsp_tari[estado][0]    
            taxas.tarifa = hsp_tari[estado][1]

        
