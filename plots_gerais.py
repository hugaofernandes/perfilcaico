
######################### PLOS GERAIS ##############################

import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np

################################### BAIRROS ##########################################

'''def bairros(data):
    fig, axs = plt.subplots(2, 1, tight_layout=True)
    axs[0].hist(data['bairro'], bins=len(data['bairro']))
    axs[0].set_title('Distribuição por Bairros Absolutas')
    #plt.xticks(rotation=50, wrap=True)
    plt.setp(axs[0].xaxis.get_majorticklabels(), rotation=20, wrap=True, fontsize=9)
    axs[1].hist(data['bairro'], bins=len(data['bairro']), density=True)
    axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))
    axs[1].set_title('Distribuição por Bairros Relativas')
    #plt.xticks(rotation=50, wrap=True)
    plt.setp(axs[1].xaxis.get_majorticklabels(), rotation=20, wrap=True, fontsize=9)
    plt.show()'''

def bairros(data, titulo):
    fig, axs = plt.subplots()
    cm = plt.cm.get_cmap('RdYlBu_r')
    n, bins, patches = axs.hist(data['bairro'], bins=len(data['bairro']), density=True)
    col = (n-n.min())/(n.max()-n.min())
    for c, p in zip(col, patches):
        plt.setp(p, 'facecolor', cm(c))
    
    bin_centers = np.diff(bins)*0.5 + bins[:-1]
    aux = 0
    for fr, x, patch in zip(n, bin_centers, patches):
        height = n[aux]
        if height != 0:
            plt.annotate("{:.0%}".format(height), xy = (x, height), xytext = (0,0.2), textcoords = "offset points", ha = 'center', va = 'bottom')
        aux = aux+1

    axs.yaxis.set_major_formatter(PercentFormatter(xmax=1))
    axs.set_title(titulo)
    plt.setp(axs.xaxis.get_majorticklabels(), rotation=20, wrap=True, fontsize=9)
    plt.show()


############################### EFEITO DA PANDEMIA ###################################

'''def pandemia(data):
    fig, axs = plt.subplots(2, 1, tight_layout=True)
    axs[0].hist(data['pandemia'], bins=len(data['pandemia']))
    axs[0].set_title('Efeitos da Pandemia nas Doações (Distribuição Absoluta)')
    plt.setp(axs[0].xaxis.get_majorticklabels(), wrap=True)
    axs[1].hist(data['pandemia'], bins=len(data['pandemia']), density=True)
    axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))
    axs[1].set_title('Efeitos da Pandemia nas Doações (Distribuição Relativa)')
    plt.setp(axs[1].xaxis.get_majorticklabels(), wrap=True)
    plt.show()'''

def pandemia(data):
    fig, ax = plt.subplots()
    labels = data.pandemia.unique().tolist()
    sizes = []
    for i in labels:
        sizes.append(len(data[data.pandemia == i]))
    explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    pie = ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
    #ax.legend(labels, loc='center right')
    ax.set_title('Efeitos da Pandemia nas Doações')
    plt.show()

############################ IDADE ############################

def idades(data, titulo):
    fig, ax = plt.subplots()
    labels = data.idade.unique().tolist()
    sizes = []
    for i in labels:
        sizes.append(len(data[data.idade == i]))
    explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
    pie = ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    #ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
    #ax.legend(labels, loc='lower left')
    ax.set_title(titulo)
    plt.show()

############################ ESPIRITUALIDADE ############################

def fe(data, titulo):
    fig, ax = plt.subplots()
    labels = data.fe.unique().tolist()
    sizes = []
    for i in labels:
        sizes.append(len(data[data.fe == i]))
    explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    pie = ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
    #ax.legend(labels, loc='center right')
    ax.set_title(titulo)
    plt.show()


############################ ESTADO CIVIL ############################

def estadoCivil(data, titulo):
    fig, ax = plt.subplots()
    labels = data.estadoCivil.unique().tolist()
    sizes = []
    for i in labels:
        sizes.append(len(data[data.estadoCivil == i]))
    explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    pie = ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
    #ax.legend(labels, loc='center right')
    ax.set_title(titulo)
    plt.show()

############################ FILHOS ############################

def filhos(data, titulo):
    fig, ax = plt.subplots()
    labels = data.filhos.unique().tolist()
    sizes = []
    for i in labels:
        sizes.append(len(data[data.filhos == i]))
    explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    pie = ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
    #ax.legend(labels, loc='center right')
    ax.set_title(titulo)
    plt.show()

############################ ESCOLARIDADE ############################

def escolaridade(data, titulo):
    fig, ax = plt.subplots()
    labels = data.escolaridade.unique().tolist()
    sizes = []
    for i in labels:
        sizes.append(len(data[data.escolaridade == i]))
    explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    pie = ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
    #ax.legend(labels, loc='center right')
    ax.set_title(titulo)
    plt.show()

############################ RENDA DOMICILIAR ############################

def renda(data, titulo):
    fig, ax = plt.subplots()
    labels = data.renda.unique().tolist()
    sizes = []
    for i in labels:
        sizes.append(len(data[data.renda == i]))
    explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    pie = ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
    #ax.legend(labels, loc='center right')
    ax.set_title(titulo)
    plt.show()

############################ OCUPACAO ############################

def ocupacao(data, titulo):
    fig, ax = plt.subplots()
    labels = data['ocupacao'].unique().tolist()
    sizes = []
    for i in labels:
        sizes.append(len(data[data['ocupacao'] == i]))
    explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    pie = ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(pie[0],labels, bbox_to_anchor=(0,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
    #ax.legend(labels, loc='center right')
    ax.set_title(titulo)
    plt.show()

############################ GENERO ############################

def genero(data, titulo):
    fig, ax = plt.subplots()
    labels = data['sexo'].unique().tolist()
    sizes = []
    for i in labels:
        sizes.append(len(data[data['sexo'] == i]))
    explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    pie = ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(pie[0],labels, bbox_to_anchor=(0,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
    #ax.legend(labels, loc='center right')
    ax.set_title(titulo)
    plt.show()


############################# AJUDA MAIS e AJUDA MENOS ################################

def ajuda(data, titulo1, titulo2):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    #fig, ax1 = plt.subplots()
    labels = data.ajudaMais.unique().tolist()
    sizes = []
    for i in labels:
        sizes.append(len(data[data.ajudaMais == i]))
    explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
    pie = ax1.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    #ax1.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.legend(pie[0],labels, bbox_to_anchor=(0,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
    #ax1.legend(labels, loc='lower left')
    ax1.set_title(titulo1)
    #plt.show()

    #fig, ax2 = plt.subplots()
    #labels = data.ajudaMenos.unique().tolist()
    sizes = []
    for i in labels:
        sizes.append(len(data[data.ajudaMenos == i]))
    #explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #ax2.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    pie = ax2.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
    #ax2.legend(labels, loc='center right')
    ax2.set_title(titulo2)
    plt.show()

############################ MIDIAS ############################

def midias(data, titulo):
    fig, ax = plt.subplots()
    labels = ['Rádio', 'Blogs e Sites', 'Televisão', 'Jornais e Revistas', 'Carros de Som', 'Igreja', 'Facebook', 'Instagram', 'Whatsapp']
    sizes = []
    for i in labels:
        sizes.append(len(data[data[i] == 1]))
    explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    pie = ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(pie[0],labels, bbox_to_anchor=(0,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
    #ax.legend(labels, loc='center right')
    ax.set_title(titulo)
    plt.show()

def midias2(data, titulo):
    fig, axs = plt.subplots()
    labels = ['Rádio', 'Blogs e Sites', 'Televisão', 'Jornais e Revistas', 'Carros de Som', 'Igreja', 'Facebook', 'Instagram', 'Whatsapp']
    sizes = []
    for i in labels:
        #print (i + str(len(data[i])))
        #print (i + str(len(data[data[i] == 1])))
        for j in range(len(data[data[i] == 1])):
            sizes.append(i)
    #print (sizes)
    cm = plt.cm.get_cmap('RdYlBu_r')
    n, bins, patches = axs.hist(sizes, bins=len(data), density=True)
    col = (n-n.min())/(n.max()-n.min())
    for c, p in zip(col, patches):
        plt.setp(p, 'facecolor', cm(c))
    
    bin_centers = np.diff(bins)*0.5 + bins[:-1]
    aux = 0
    for fr, x, patch in zip(n, bin_centers, patches):
        height = n[aux]
        if height != 0:
            plt.annotate("{:.0%}".format(height), xy = (x, height), xytext = (0,0.2), textcoords = "offset points", ha = 'center', va = 'bottom')
        aux = aux+1

    axs.yaxis.set_major_formatter(PercentFormatter(xmax=1))
    axs.set_title(titulo)
    plt.setp(axs.xaxis.get_majorticklabels(), rotation=20, wrap=True, fontsize=9)
    plt.show()

############################ MESES ############################

def meses(data, titulo):
    fig, ax = plt.subplots()
    labels = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    sizes = []
    for i in labels:
        sizes.append(len(data[data[i] == 1]))
    explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    pie = ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(pie[0],labels, bbox_to_anchor=(0,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
    #ax.legend(labels, loc='center right')
    ax.set_title(titulo)
    plt.show()

############################ PREFERENCIAS ############################

def preferencias(data, titulo):
    fig, ax = plt.subplots()
    labels = ['Recolher em casa', 'Transferência ou Depósito', 'Correspondência', 'Pix', 'Troco Solidário', 'Rifas e Sorteios', 'Dízimo']
    sizes = []
    for i in labels:
        try:
            sizes.append(len(data[data[i] == 1]))
        except:
            sizes.append(0)
    explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    pie = ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(pie[0],labels, bbox_to_anchor=(0,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
    #ax.legend(labels, loc='center right')
    ax.set_title(titulo)
    plt.show()


############################ USUARIO ############################

def usuario(data, titulo):
    fig, ax = plt.subplots()
    labels = ['APAE Caicó', 'Acapam', 'Aldeias Infantis SOS', 'Abrigo Pedro Gurgel', 'Cáritas Diocesana', 'Fazenda da Esperança', 'Centro de Valorização da Vida - CVV', 'Risoterapia', 'Hemocentro Caicó']
    sizes = []
    for i in labels:
        try:
            sizes.append(len(data[data[i] == 1]))
        except:
            sizes.append(0)
    explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    pie = ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(pie[0],labels, bbox_to_anchor=(0,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
    #ax.legend(labels, loc='center right')
    ax.set_title(titulo)
    plt.show()



############################ AVALIACAO ############################

def notas(data, entidades, nota):
    aux = 0
    sizes = []
    for e in entidades:
        aux += len(data[data[e] == nota])
        sizes.append(aux)
        aux = 0
    return sizes

def avaliacao(data):
    entidades = ['apae', 'acapam', 'aldeiasSOS', 'abrigo', 'caritas', 'fazendaEsperanca', 'cvv', 'risoterapia', 'hemocentro']
    muitoImportante = notas(data, entidades, 'Muito Importante')
    importante = notas(data, entidades, 'Importante')
    mediana = notas(data, entidades, 'Mediana')
    vezes = notas(data, entidades, 'Às vezes é Importante')
    naoImportante = notas(data, entidades, 'Não é Importante')

    ind = np.arange(len(entidades))
    width = 0.35

    fig, ax = plt.subplots()
    p1 = ax.bar(ind, muitoImportante, width, label='Muito Importante')
    p2 = ax.bar(ind, importante, width, label='Importante')
    p3 = ax.bar(ind, mediana, width, label='Mediana')
    p4 = ax.bar(ind, vezes, width, label='Às vezes é Importante')
    p5 = ax.bar(ind, naoImportante, width, label='Não é Importante')

    ax.axhline(0, color='grey', linewidth=0.8)
    ax.set_ylabel('Avaliações')
    ax.set_title('Avaliação Geral de algumas Entidades da Região')
    ax.set_xticks(ind)
    ax.set_xticklabels(('Apae\n Caicó', 'Acapam', 'Aldeias Infantis\n SOS', 'Abrigo\n Pedro Gurgel', 'Caritas\n Diocesana', 'Fazenda da\n Esperanca', 'CVV', 'Risoterapia', 'Hemocentro\n Caicó'))
    ax.legend()
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, wrap=True, fontsize=9)

    plt.show()


############################ POPULARIDADE ############################

def abstencao(data, entidades, a):
    aux = 0
    sizes = []
    for e in entidades:
        aux += len(data[data[e] == a])
        sizes.append(aux)
        aux = 0
    return sizes

def conhece(data, entidades, a):
    aux = 0
    sizes = []
    for e in entidades:
        aux += len(data[data[e] != a])
        sizes.append(aux)
        aux = 0
    return sizes

def popularidade(data):
    entidades = ['apae', 'acapam', 'aldeiasSOS', 'abrigo', 'caritas', 'fazendaEsperanca', 'cvv', 'risoterapia', 'hemocentro']
    conhec = conhece(data, entidades, 'Abstenção')
    #print (conhec)
    abstenc = abstencao(data, entidades, 'Abstenção')
    #print (abstenc)

    x = np.arange(len(entidades))
    width = 0.35

    fig, ax = plt.subplots()
    p1 = ax.bar(x - width/2, conhec, width, label='Conhece')
    p2 = ax.bar(x + width/2, abstenc, width, label='Não Conhece')

    ax.axhline(0, color='grey', linewidth=0.8)
    ax.set_ylabel('Popularidade Absoluta')
    ax.set_title('Popularidade de algumas Entidades da Região')
    ax.set_xticks(x)
    ax.set_xticklabels(('Apae\n Caicó', 'Acapam', 'Aldeias Infantis\n SOS', 'Abrigo\n Pedro Gurgel', 'Caritas\n Diocesana', 'Fazenda da\n Esperanca', 'CVV', 'Risoterapia', 'Hemocentro\n Caicó'))
    ax.legend()
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, wrap=True, fontsize=9)

    #ax.text(0.01, 0.99, 'Margem de Erro = 6%', horizontalalignment='left', verticalalignment='top', transform=ax.transAxes)
    #plt.legend(loc = "upper left")

    #ax.bar_label(p1, padding=3)
    #ax.bar_label(p2)

    plt.show()



