"""Esse módulo tem a função de fazer o Bot rodar no Telegram. Para isso, ele faz a conexão do bot com o Telegram por meio de uma chave que é gerada pelo BotFather. O envio e recebimeto de mensagens é feito por funções que estão atribuidas a um Decorators, para cada função existe um Decorators. O objeito deles são configurar quando a função de envio ou recebimento de mensagens é aciada, quando o paramentro da Ddecorator é atendido, o bot executa a função da linha abaixo."""

# Importa biblioteca que possuí as funções de bot no Telegram
import telebot


#Importa os módulos necessários e as mensagem que serão usadas no chat
import mem_cal
import cons_pot
import taxas
import hsp_taxa
import locs
from SalveDados import *
from mensagens import *


# Chave api do bot na plataforma do Telegram
chave_api = "1780980031:AAErPKs5y8zhqQdBhgD7msF0JSTpFEEfT2w"


# Chamar a função bot e conectar com a api
bot = telebot.TeleBot(chave_api)


@bot.message_handler(commands=["ok"])
def resultado(mensagem):

    """Função envia as informações com os cálculos quando o usuário apertar /ok. As informações serão calculadas usando a função do módulo 'mem_cal' e substituindo os resultado nas variavéis do módulo 'cons_pot' que armazena os dados temporariamente."""

    cons_pot.ptotal, cons_pot.pmax, cons_pot.pmin = mem_cal.calcula(cons_pot.con, taxas.hsp)

    cons_pot.mes_tres,cons_pot.mes_seis,cons_pot.ano_um,cons_pot.ano_dois,cons_pot.ano_cinco = mem_cal.cal_economia(cons_pot.con,taxas.tarifa)

    cadastra_resultados(cons_pot.cpf, cons_pot.con, cons_pot.ptotal, cons_pot.pmax, cons_pot.pmin, cons_pot.mes_tres, cons_pot.mes_seis, cons_pot.ano_um, cons_pot.ano_dois, cons_pot.ano_cinco)


    bot.reply_to(mensagem, mensagem_sis.format(cons_pot.nome,cons_pot.ptotal, cons_pot.pmax, cons_pot.pmin))



def concat(lista):
    """Função que faz uma interação pra remover os possiveis espaços existentes no meio da palavra e deixar em letras minisculas"""

    local = ""
    for i in lista:
        local += i

    local = local.lower()

    return local


@bot.message_handler(commands=["local"])
def local(mensagem):
    """Função que recebe o nome do estado do usuário por meio do seu comando /local, e faz o tratamentos de erros caso o usuário digite apenas o comando sem o nome do local, ou caso o usuário digite o nome errado ou de um estado inexistente. Para todos os casos de erros será enviada uma mensagem pedindo que o usuário digite novamente. Caso não terra erros, será enviada a mensagem do próximo passo e o nome do Estado será enviado para a variavél 'estado' no módulo 'locs'. Quando é um nome composto, existe uma função que tira os espaços para fazer um validação do nome"""

    local_texto = mensagem.text
    local_texto = local_texto.split(" ")

    if len(local_texto) <= 1:
        bot.reply_to(mensagem, mensagem_vazia)
    else:
        local_texto.pop(0)
        locs.estado = concat(local_texto)

        if hsp_taxa.valida_loc(locs.estado):
            hsp_taxa.set_taxas(locs.estado)
            bot.reply_to(mensagem, mensagem_loc)
        else:
            bot.reply_to(mensagem, mensagem_ort)



@bot.message_handler(commands=["con"])
def consumo(mensagem):
    """Função que recebe o consumo do usuário por meio do seu comando /con, e faz o tratamento de erros caso o usuário digite apenas o comando sem o consumo energético, ou caso o usuário insira letras no valor, ou em ultimo caso, se o usuário digitar um valor menor ou igual a 0. Para todos os casos de erros será enviada uma mensagem pedindo que o usuário digite novamente. Caso não terra erros, será enviada a mensagem do próximo passo e o valor do consumo será enviado para a variavél 'con' no módulo 'cons_pot'."""


    con = mensagem.text
    con = con.split(" ")

    if len(con) <= 1:
        bot.reply_to(mensagem, mensagem_vazcon)

    else:
        con = con[1]

        try:
            con = float(con)
        except:
            bot.reply_to(mensagem, mensagem_conerro)

        if type(con) == float or type(con) == int:
            if con <= 0:
                bot.reply_to(mensagem, mensagem_erroneg)

            else:
                bot.reply_to(mensagem, mensagem_con.format(con))
                cons_pot.con = con


@bot.message_handler(commands=["passo1"])
def passo1(mensagem):
    """Função que manda a mensagem solicitando que seja informando o valor mensal do consumo de energia, quando o usuário apertar ou digitar /passo1.
    """

    bot.reply_to(mensagem, mensagem_passo1)


@bot.message_handler(commands=["passo2"])
def localinstalacao(mensagem):
    """Função que manda a mensagem, solicitando que seja informado o estado de instalação do sistema solar, quando o usuário apertar ou digitar /passo2.
    """

    bot.reply_to(mensagem, mensagem_passo2)


@bot.message_handler(commands=["nome"])
def nome(mensagem):
    """
    Função que recebe o nome do usuário por meio do seu comando /nome, e faz o tratamentos de erro caso o usuário digite o comando sem estar acompanhado do seu nome, mandando uma mensagem de erro ao usuário. Caso não terra erro, será enviada a mensagem do próximo passo e o nome do usuário será enviado para a variavél 'nome' no módulo 'cons_pot', para que seja usado posteriormente na mensagem final."""

    nome = mensagem.text
    nome = nome.split(" ")

    if len(nome) <= 1:
        bot.reply_to(mensagem, mensagem_nomerro)
    else:
        nome = str(nome[1]).lower().capitalize()
        cons_pot.nome = nome

        bot.reply_to(mensagem, mensagem_inicial)


@bot.message_handler(commands=["cpf"])
def cpf(mensagem):
    """
    Função que recebe o cpf do usuário por meio do seu comando /cpf, e faz o tratamentos de erros caso o usuário digite apenas o comando sem o número do cpf, ou caso o usuário digite letras no meio do valor do cpf, e em último caso, caso o usuário insira o cpf sem os 11 digitos padrões, em todos os erros será emitida uma mensagem de erro. Caso não terra erros, será enviada a mensagem do próximo passo e o valor do cpf do usuário será enviado para a variavél 'cpf' no módulo 'cons_pot', para que se tenha um controle de cadastro. 
    """

    cpf2 = mensagem.text
    cpf2 = cpf2.split(" ")

    if len(cpf2) <= 1:
        bot.reply_to(mensagem, mensagem_cpferro)

    else:
        cpf2 = cpf2[1]

        try:
            int(cpf2)
        except:
            bot.reply_to(mensagem, mensagem_cpferro)

        cpf2 = str(cpf2)
        tamanho_cpf = len(cpf2)

        if tamanho_cpf != 11:
            bot.reply_to(mensagem, mensagem_cpferro)

        else:
            bot.reply_to(mensagem, mensagem_nome)
            cons_pot.cpf = cpf2
    

def verificar(mensagem):
    """Função que verifica se o usuário mandou uma mensagem no chat com o Bot, se houver mensagem ele retorna True
    """

    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    """Função que verifica a mensagem que o usuário enviou, pelo Return True. Quando ele indentificar que existe uma mensagem que não se encaixa nos outros comando de handler, será enviada a primeira mensagem pedindo o cpf da pessoa.
    """

    bot.reply_to(mensagem, mensagem_cpf)


bot.polling()
"""
Essa linha de código faz um loop da conexão do bot com o telegram, pra ficar verificando a chegada de mensagem no chat
"""
