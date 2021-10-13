"""Esse módulo tem a função de armazenar as mensagens que serão enviadas para o usuário, por meio da exportação para o módulo 'Main'
"""


#Mensagem que será enviada inicialmente para o usuário pedindo seu cpf 
mensagem_cpf = """
    Olá, seja bem-vindo(a). Meu nome é Clara e estou aqui para te auxiliar no Dimensionamento do seu projeto Fotovoltaico. 
\U0001F31E \U0001F609

    Preciso que me informe seu cpf para fazer o armazenamento dos seus cálculos! Não se preocupe, ele será guardado de uma forma segura!

    Digite /cpf e logo em seguida digite seu cpf, não é necessário ponto ou hífen!

    Ex.: /cpf 12345678910

    """


#Mensagem que será enviada caso o usuário digite o cpf errado ou apenas digite o comando /cpf
mensagem_cpferro = """Por favor, ocorreu um erro com a digitação do seu cpf. Digite novamente!

Ex.: /cpf 12345678910"""


#Mensagem que será enviada pedindo o nome do usuário
mensagem_nome = """Obrigada por me ajudar nessa, agora gostaria se saber seu nome! 

Para isso digite /nome e logo em seguida digite seu nome

Ex.: /nome Clara"""


#Mesagem que será enviada caso a mensagem de /nome apresente algum erro
mensagem_nomerro = """
Ocorreu um erro ao inserir o seu nome. Peço para que digite novamente com o comando /nome

Ex.: /nome Clara"""


#Mensagem que será enviada para o inicio da coleta de dados 
mensagem_inicial="""
Muito obrigada! \U0001F601
Para começarmos o dimensionamento, irei precisar que você me fale algumas informações importantes, são elas: Consumo energético e o local da instalação do sistema!
    
Estou animada para te ajudar! Vamos nessa?!
Siga a sequência de passos e faça o que se pede!

Clique no passo1 para começar! 

    /passo1: Olá, preciso saber o seu consumo mensal de energia!

    """


#Mensagem que será enviada quando o usuário selecionar para começar o passo 1
mensagem_passo1 = """
    Por favor, me informe o seu gasto de energia mensal!

Para isso, digite o comando /con e logo em seguida digite seu consumo em kWh!

Exemplo para um consumo de 600 kWh:
/con 600 
"""


#Mensagem que será enviada, caso o usuário não indique o valor do consumo
mensagem_vazcon = """
Por favor, informe qual o seu consumo mensal de energia elétrica, para que todos os cálculos sejam feitos! \U0001F604

"""

#Mensagem de erro que será enviada caso o usuário digite um valor negativo para o consumo
mensagem_erroneg = """
Por favor, insira um valor válido! Digite novamente.
"""


#Mensagem que será enviada caso o usuário digite o consumo de forma incorreta, incluindo letras no valor 
mensagem_conerro = """
Ocorreu algum erro na digitação do consumo!

Por favor, insira novamente! \U0001F604
"""


#Mensagem que será enviada quando o usuário enviar o seu consumo de energia corretamente
mensagem_con = """
    O seu consumo mensal é de: {} kWh

Agora, vamos para o próximo passo! Estamos quase lá!

Clique no passo2 para avançar!

    /passo2: Informe o local que irá acontecer a instalação do Sistema
  
 """


#Mensagem que será enviada quando o usuário selecionar para começar o passo 2
mensagem_passo2 = """
    O primeiro passo foi concluído com sucesso!
Para continuar, preciso saber o estado que você deseja instalar o sistema!

Para isso, digite o comando /local e logo em seguida digite o nome do seu estado!

Exemplo: /local paraiba
"""


#Mensagem que será enviada caso o usuário não informe o nome do estado, sendo lido como uma mensagem vazia
mensagem_vazia = """
Por favor, preciso que digite o nome do estado que irá acontecer a instalação do sistema. Digite novamente! \U0001F609

"""


#Mensagem que será enviada caso o usuário escreva o nome do estado de forma incorreta, ou informe o nome de um estado que não existe
mensagem_ort = """
Opss! Ocorreu um erro de digitação! \U0001F625

Por favor, é necessário que insira o nome do estado corretamente. Digite novamente! 
"""


#Mensagem que será enviada quando o usuário enviar o nome do Estado de instalação
mensagem_loc = """
    Obrigada por me ajudar na coleta de informações! \U0001F60A
    
Agora irei fazer os cálculos para seu projeto! Peço que aguarde alguns segundos!

Para continuar, aperte /ok ;)
"""


#Mensagem que será enviada com as informações do Sistema
mensagem_sis = """
Olá, {}!
Aqui estão as informações do seu Sistema Solar!

Potência Total: {:.2f} Kwp
Potência Maxima do Inversor: {:.2f} Kw
Potência Mínima do Inversor: {:.2f} Kw
"""




#Mensagem que será enviada informando quanto o usuário poderá economizar períodos de tempos definidos
mensagem_eco = """
3 meses: R$ {:.2f}
6 meses: R$ {:.2f}
1 ano: R$ {:.2f}
2 anos: R$ {:.2f}
5 anos: R$ {:.2f}
"""
