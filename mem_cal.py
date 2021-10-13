""" Esse módulo tem a função de receber os dados de consumo, que está armazenado no módulo 'main', e os valores de hsp e tarifa energética que estão armazenados no módulo 'taxas'. 
Após o recebimento de dados, ele irá fazer os cálculos de Potencia Total, Potencia Máxima e Minima que e o Inversor pode ter, e valores que o usuário poderá economizar em determinados períodos de tempo.
"""


def calcula (consumo,hsp):

    """Função que recebe os argumentos de consumo e hsp. Logo após irá calcular o consumo de energia em dias, a potencia total do sistema de acordo com o consumo diário, o hsp e o rendimento de 75%. Irá calcular tambem a potencia máxima e minima que o inversor pode assumir para esse sistema, e retornar essas informações. """


    #Calcula o consumo de energia do cliente em dias
    DIAS = 30 
    ConsumoDia = consumo/DIAS 

    #Calcula potencia total que o projeto deverá ter por dia
    RENDIMENTO = 0.75
    PontenciaTotal = ConsumoDia / (hsp * RENDIMENTO)

    #Calcula a potencia maxima e minina que os inversores podem ter, 20% para mais e 20% para minima 
    Mais20 = 1.2
    Menos20 = 0.80
    PotMaxInv = PontenciaTotal * Mais20
    PotMinInv= PontenciaTotal * Menos20

    return PontenciaTotal,PotMaxInv,PotMinInv



def cal_economia(consumo,tarifa):

    """Função que irá receber a potencia encontrada para o sistema e a tarifa de energia do estado, e calcular quanto ele economizará em 3 meses, 6 meses, 1 ano, 2 anos e 5 anos, e retornar para o usuário"""


    #Constantes que armazenar a quantidade de dias por cada período de tempo 
    TRES_MESES = 3
    SEIS_MESES = 6
    UM_ANO = 12
    DOIS_ANOS = 24
    CINCO_ANOS = 60


    #Calculo que é feito para cada período de tempo, com sabe na potencia total, kilowatts, dias e a tarifa energética
    mes_tres = consumo * TRES_MESES * tarifa
    mes_seis = consumo * SEIS_MESES * tarifa
    ano_um = consumo * UM_ANO * tarifa
    ano_dois = consumo * DOIS_ANOS * tarifa
    ano_cinco = consumo * CINCO_ANOS * tarifa

    return mes_tres, mes_seis, ano_um, ano_dois, ano_cinco

