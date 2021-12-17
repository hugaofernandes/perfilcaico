# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        if total == 0:
            val = 0
        else:
            val = int(round(pct*total/100.0))
        if pct <= 3:
            return ''
        if pct < 10:
            return '{v:d}\n({p:.0f}%)'.format(p=pct,v=val)
        if pct < 15:
            return '{v:d}\n({p:.1f}%)'.format(p=pct,v=val)
            #return '{p:.1f}%\n({v:d})'.format(p=pct,v=val)
        return '{v:d} ({p:.1f}%)'.format(p=pct,v=val)
        #return '{p:.1f}% ({v:d})'.format(p=pct,v=val)
    return my_autopct

def make_autopct2(values, value):
    total = sum(values)
    if total == 0:
        return '{v:d}\n({p:.1f}%)'.format(p=total,v=value)
    else:
        return '{v:d}\n({p:.1f}%)'.format(p=(value/total*100.0),v=value)

def make_autopct3(value1, value2):
    total = value1 + value2
    pct = (value1/total*100.0)
    if pct <= 3:
        return ''
    if pct < 10:
        return '{v:d} ({p:.1f}%)'.format(p=pct,v=value1)
    return '{v:d}\n({p:.1f}%)'.format(p=pct,v=value1)

def testeMax(values):
    if len(values) == 0:
        return 0
    return max(values)

def testeData(data, atributo):
    labels, explore, values = [], [0.1], []
    #print (type(data[atributo]))
    labels = data[atributo].unique().tolist()
    for label in labels:
        try:
            values.append(len(data[data[atributo] == label]))
        except:
            values.append(0)
    return labels, explore*len(labels), values

def testeValues(data, labels):
    values = []
    for label in labels:
        try:
            values.append(len(data[data[label] == 1]))
        except:
            values.append(0)
    return values

def testeNome(nome):
    if type(nome) != str:
        labels = []
        for label in nome:
            labels.append(testeNome(label))
        return labels
    if nome == 'apae':
        return 'APAE CAICÓ'
    if nome == 'aldeiasSOS':
        return 'ALDEIAS INFANTIS SOS CAICÓ'
    if nome == 'abrigo':
        return 'ABRIGO PEDRO GURGEL'
    if nome == 'caritas':
        return 'CÁRITAS DIOCESANA'
    if nome == 'fazendaEsperanca':
        return 'FAZENDA DA ESPERANÇA'
    if nome == 'cvv':
        return 'CVV CAICÓ'
    if nome == 'hemocentro':
        return 'HEMOCENTRO CAICÓ'
    if nome == 'voluntario':
        return 'TRABALHO VOLUNTÁRIO'
    if nome == 'roupas':
        return 'ROUPAS E AGASALHOS'
    if nome == 'higiene':
        return 'PRODUTOS DE LIMPEZA E HIGIENE'
    if nome == 'racao':
        return 'RAÇÃO ANIMAL'
    if nome == 'sangue':
        return 'DOAÇÃO DE SANGUE'
    return nome.upper()


def pizza(data, atributo, titulo, pasta):
    fig, ax = plt.subplots(figsize=(8, 6))
    labels, explode, values = testeData(data, atributo)
    pie = ax.pie(values, explode=explode, autopct=make_autopct(values), shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
    ax.set_title(titulo)
    plt.savefig(pasta+titulo, format='png')
    #plt.show()


def pizza2D_ajuda(data, atributo1, atributo2, titulo1, titulo2, pasta):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    labels, explode, values = testeData(data, atributo1)
    pie = ax1.pie(values, explode=explode, autopct=make_autopct(values), shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.legend(pie[0],labels, bbox_to_anchor=(0,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
    ax1.set_title(titulo1)

    labels, explode, values = testeData(data, atributo2)
    pie = ax2.pie(values, explode=explode, autopct=make_autopct(values), shadow=True, startangle=90)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
    ax2.set_title(titulo2)
    plt.savefig(pasta+titulo1, format='png')
    #plt.show()


def pizza4D_ajuda(data1, data2, atributo1, atributo2, titulo1, titulo2, titulo3, titulo4):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    labels, explode, values = testeData(data1, atributo1)
    pie = ax1.pie(values, explode=explode, autopct=make_autopct(values), shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.legend(pie[0],labels, bbox_to_anchor=(0,0.5), loc="lower left", bbox_transform=plt.gcf().transFigure)
    ax1.set_title(titulo1)

    labels, explode, values = testeData(data1, atributo2)
    pie = ax2.pie(values, explode=explode, autopct=make_autopct(values), shadow=True, startangle=90)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.legend(pie[0],labels, bbox_to_anchor=(1,0.5), loc="lower right", bbox_transform=plt.gcf().transFigure)
    ax2.set_title(titulo2)

    labels, explode, values = testeData(data2, atributo1)
    pie = ax3.pie(values, explode=explode, autopct=make_autopct(values), shadow=True, startangle=90)
    ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax3.legend(pie[0],labels, bbox_to_anchor=(0,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
    ax3.set_title(titulo3)

    labels, explode, values = testeData(data2, atributo2)
    pie = ax4.pie(values, explode=explode, autopct=make_autopct(values), shadow=True, startangle=90)
    ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax4.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
    ax4.set_title(titulo4)
    plt.show()


def pizza2D(data1, data2, atributo, titulo1, titulo2, pasta):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    labels, explode, values = testeData(data1, atributo)
    pie = ax1.pie(values, explode=explode, autopct=make_autopct(values), shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.legend(pie[0],labels, bbox_to_anchor=(0,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
    ax1.set_title(titulo1)

    labels, explode, values = testeData(data2, atributo)
    pie = ax2.pie(values, explode=explode, autopct=make_autopct(values), shadow=True, startangle=90)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
    ax2.set_title(titulo2)
    plt.savefig(pasta+titulo1, format='png')
    #plt.show()


def barras(data, labels, titulo, pasta):
    fig, ax = plt.subplots(figsize=(12, 6))
    width = 0.35
    aux = 0
    x = np.arange(len(labels))
    values = testeValues(data, labels)
    p1 = ax.bar(x, values, width)
    ax.axhline(0, color='grey', linewidth=0.8)
    ax.set_title(titulo)
    ax.set_xticks(x)
    ax.set_ylim(0, testeMax(values)+10)
    wrapped_labels = [label.replace(' ', '\n') for label in labels]
    ax.set_xticklabels(wrapped_labels)
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, wrap=True, fontsize=9)
    for value in values:
        plt.annotate(make_autopct2(values, value), xy = (aux, value), xytext = (0,0.2), textcoords = "offset points", ha = 'center', va = 'bottom')
        aux += 1
    plt.savefig(pasta+titulo, format='png')
    #plt.show()


def barras_bairros(data, atributo, titulo, pasta):
    fig, ax = plt.subplots(figsize=(24, 8))
    width = 0.35
    aux = 0
    labels, explode, values = testeData(data, atributo)
    x = np.arange(len(labels))
    p1 = ax.bar(x, values, width)
    ax.axhline(0, color='grey', linewidth=0.8)
    ax.set_title(titulo)
    ax.set_xticks(x)
    ax.set_ylim(0, testeMax(values)+10)
    wrapped_labels = [label.replace(' ', '\n') for label in labels]
    ax.set_xticklabels(wrapped_labels)
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, wrap=True, fontsize=7)
    #plt.annotate(make_autopct(values), xy = (np.arange(len(values)), values), xytext = (0,0.2), textcoords = "offset points", ha = 'center', va = 'bottom')
    #total = sum(values)
    for value in values:
        #plt.annotate('{v:d}\n({p:.1f}%)'.format(p=(value/total*100.0),v=value), xy = (aux, value), xytext = (0,0.2), textcoords = "offset points", ha = 'center', va = 'bottom')
        plt.annotate(make_autopct2(values, value), xy = (aux, value), xytext = (0,0.2), textcoords = "offset points", ha = 'center', va = 'bottom')
        aux += 1
    plt.savefig(pasta+titulo, format='png')
    #plt.show()


def barras2D_bairros(data1, data2, atributo, titulo1, titulo2, pasta):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(24, 8))
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
    width = 0.35
    aux = 0
    labels, explode, values = testeData(data1, atributo)
    x = np.arange(len(labels))
    p1 = ax1.bar(x, values, width)
    ax1.axhline(0, color='grey', linewidth=0.8)
    ax1.set_title(titulo1)
    ax1.set_xticks(x)
    ax1.set_ylim(0, testeMax(values)+10)
    wrapped_labels = [label.replace(' ', '\n') for label in labels]
    ax1.set_xticklabels(wrapped_labels)
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=0, wrap=True, fontsize=7)
    for value in values:
        ax1.annotate(make_autopct2(values, value), xy = (aux, value), xytext = (0,0.2), textcoords = "offset points", ha = 'center', va = 'bottom')
        aux += 1

    aux = 0
    labels, explode, values = testeData(data2, atributo)
    x = np.arange(len(labels))
    p1 = ax2.bar(x, values, width)
    ax2.axhline(0, color='grey', linewidth=0.8)
    ax2.set_title(titulo2)
    ax2.set_xticks(x)
    ax2.set_ylim(0, testeMax(values)+10)
    wrapped_labels = [label.replace(' ', '\n') for label in labels]
    ax2.set_xticklabels(wrapped_labels)
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=0, wrap=True, fontsize=7)
    for value in values:
        ax2.annotate(make_autopct2(values, value), xy = (aux, value), xytext = (0,0.2), textcoords = "offset points", ha = 'center', va = 'bottom')
        aux += 1
    plt.savefig(pasta+titulo1, format='png')
    #plt.show()


def barras2D(data1, data2, labels, titulo1, titulo2, pasta):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
    width = 0.35
    aux = 0
    values = testeValues(data1, labels)
    x = np.arange(len(labels))
    p1 = ax1.bar(x, values, width)
    ax1.axhline(0, color='grey', linewidth=0.8)
    ax1.set_title(titulo1)
    ax1.set_xticks(x)
    ax1.set_ylim(0, testeMax(values)+10)
    wrapped_labels = [label.replace(' ', '\n') for label in labels]
    ax1.set_xticklabels(wrapped_labels)
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=0, wrap=True, fontsize=9)
    for value in values:
        ax1.annotate(make_autopct2(values, value), xy = (aux, value), xytext = (0,0.2), textcoords = "offset points", ha = 'center', va = 'bottom')
        aux += 1

    values = testeValues(data2, labels)
    aux = 0
    p1 = ax2.bar(x, values, width)
    ax2.axhline(0, color='grey', linewidth=0.8)
    ax2.set_title(titulo2)
    ax2.set_xticks(x)
    ax2.set_ylim(0, testeMax(values)+10)
    wrapped_labels = [label.replace(' ', '\n') for label in labels]
    ax2.set_xticklabels(wrapped_labels)
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=0, wrap=True, fontsize=9)
    for value in values:
        ax2.annotate(make_autopct2(values, value), xy = (aux, value), xytext = (0,0.2), textcoords = "offset points", ha = 'center', va = 'bottom')
        aux += 1
    plt.savefig(pasta+titulo1, format='png')
    #plt.show()


def testeNotas(data, entidades, nota):
    valuesAvaliacao, valuesAbstencao, valuesPopularidade = [], [], []
    for entidade in entidades:
        avaliacao = len(data[data[entidade] == nota])
        popularidade = len(data[data[entidade] != 'Abstenção'])
        abstencao = len(data[data[entidade] == 'Abstenção'])
        valuesAvaliacao.append(avaliacao)
        valuesPopularidade.append(popularidade)
        valuesAbstencao.append(abstencao)
    return valuesAvaliacao, valuesPopularidade, valuesAbstencao

def barras_avaliacao(data, labels, notas, titulo, pasta):
    fig, ax = plt.subplots(figsize=(12, 6))
    bases = [0]*len(labels)
    for nota in notas:
        avaliacoes, popularidades, abstencoes = testeNotas(data, labels, nota)
        ax.bar(labels, avaliacoes, width=0.35, bottom=bases, label=nota)
        bases=np.add(avaliacoes, bases)
        #print (nota, avaliacoes)
        aux = 0
        for avaliacao, popularidade, base in zip(avaliacoes, popularidades, bases):
            plt.annotate(make_autopct3(avaliacao, popularidade-avaliacao), xy = (aux, base-avaliacao/2-2), xytext = (0,0), textcoords = "offset points", ha = 'center', va = 'bottom', fontsize=7)
            aux += 1
    ax.set_title(titulo)
    #ax.set_xticks(labels)
    #ax.set_ylim(0, 160)
    ax.legend()
    labels = testeNome(labels)
    wrapped_labels = [label.replace(' ', '\n') for label in labels]
    ax.set_xticklabels(wrapped_labels)
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, wrap=True, fontsize=9)
    plt.savefig(pasta+titulo, format='png')
    #plt.show()


def barras_popularidade(data, labels, titulo, pasta):
    fig, ax = plt.subplots(figsize=(12, 6))
    width = 0.35
    x = np.arange(len(labels))
    aux = 0
    avaliacoes, popularidades, abstencoes = testeNotas(data, labels, '')
    ax.bar(x-width/2, popularidades, width, label='Conhece')
    ax.bar(x+width/2, abstencoes, width, label='Não conhece')
    for popularidade, abstencao in zip(popularidades, abstencoes):
        plt.annotate(make_autopct3(popularidade, abstencao), xy = (aux-width/2, popularidade), xytext = (0,0.2), textcoords = "offset points", ha = 'center', va = 'bottom', fontsize=8)
        plt.annotate(make_autopct3(abstencao, popularidade), xy = (aux+width/2, abstencao), xytext = (0,0.2), textcoords = "offset points", ha = 'center', va = 'bottom', fontsize=8)
        aux += 1
    #ax.axhline(0, color='grey', linewidth=0.8)
    ax.set_title(titulo)
    ax.set_xticks(x)
    #ax.set_ylim(0, 150)
    ax.legend()
    labels = testeNome(labels)
    wrapped_labels = [label.replace(' ', '\n') for label in labels]
    ax.set_xticklabels(wrapped_labels)
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, wrap=True, fontsize=9)
    plt.savefig(pasta+titulo, format='png')
    #plt.show()

def testeZero(data, label):
    labels = data[label].unique().tolist()
    for l in labels:
        if 'Zero' in l:
            return l

def barras_doacoes(data, labels, titulo, pasta):
    fig, ax = plt.subplots(figsize=(12, 8))
    width = 0.35
    x = np.arange(len(labels))
    aux = 0
    naoAjuda, ajudaComAlgo = [], []
    for label in labels:
        zero = testeZero(data, label)
        #print (label, zero)
        ajudaComAlgo.append(len(data[data[label] != zero]))
        naoAjuda.append(len(data[data[label] == zero]))
    ax.bar(x-width/2, ajudaComAlgo, width, label='Ajudam com algo')
    ax.bar(x+width/2, naoAjuda, width, label='Não ajudam')
    for ajuda, nao in zip(ajudaComAlgo, naoAjuda):
        plt.annotate(make_autopct3(ajuda, nao), xy = (aux-width/2, ajuda), xytext = (0,0.2), textcoords = "offset points", ha = 'center', va = 'bottom', fontsize=8)
        plt.annotate(make_autopct3(nao, ajuda), xy = (aux+width/2, nao), xytext = (0,0.2), textcoords = "offset points", ha = 'center', va = 'bottom', fontsize=8)
        aux += 1
    #ax.axhline(0, color='grey', linewidth=0.8)
    ax.set_title(titulo)
    ax.set_xticks(x)
    #ax.set_ylim(0, 150)
    ax.legend()
    labels = testeNome(labels)
    wrapped_labels = [label.replace(' ', '\n') for label in labels]
    ax.set_xticklabels(wrapped_labels)
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, wrap=True, fontsize=9)
    plt.savefig(pasta+titulo, format='png')
    #plt.show()


def clustering3D(data):
    X = data.loc[:, data.columns != 'target']
    target = data['target']
    fig = plt.figure(1, figsize=(12, 6))
    ax = Axes3D(fig, elev=-150, azim=110)
    X_reduced = PCA(n_components=3).fit_transform(X)
    #print (X_reduced)
    scatter = ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=target, cmap=plt.cm.Set1, edgecolor="k", s=40)
    legend1 = ax.legend(*scatter.legend_elements(), title="Grupos")
    ax.add_artist(legend1.get_title())
    #ax.legend()
    title = 'ANÁLISE DE AGRUPAMENTOS COM '+str(len(np.unique(target)))+' GRUPOS'
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.w_xaxis.set_ticklabels([])
    ax.set_ylabel("Y")
    ax.w_yaxis.set_ticklabels([])
    ax.set_zlabel("Z")
    ax.w_zaxis.set_ticklabels([])
    #plt.savefig(pasta+title, format='png')
    plt.show()



