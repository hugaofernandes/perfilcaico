



'''################################### HISTOGRAMA 2x2 = BAIRROS ##########################################
fig, axs = plt.subplots(2, 1, tight_layout=True)
axs[0].hist(data['bairro'], bins=len(data['bairro']))
axs[0].set_title('Distribuição por Bairros Absolutas')
#plt.xticks(rotation=50, wrap=True)
plt.setp(axs[0].xaxis.get_majorticklabels(), rotation=60, wrap=True)
axs[1].hist(data['bairro'], bins=len(data['bairro']), density=True)
axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))
axs[1].set_title('Distribuição por Bairros Relativas')
#plt.xticks(rotation=50, wrap=True)
plt.setp(axs[1].xaxis.get_majorticklabels(), rotation=60, wrap=True)
plt.show()
'''


'''###############################  HISTOGRAMA 2x2 = EFEITO DA PANDEMIA ###################################
fig, axs = plt.subplots(2, 1, tight_layout=True)
axs[0].hist(data['pandemia'], bins=len(data['pandemia']))
axs[0].set_title('Efeitos da Pandemia nas Doações (Distribuição Absoluta)')
plt.setp(axs[0].xaxis.get_majorticklabels(), wrap=True)
axs[1].hist(data['pandemia'], bins=len(data['pandemia']), density=True)
axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))
axs[1].set_title('Efeitos da Pandemia nas Doações (Distribuição Relativa)')
plt.setp(axs[1].xaxis.get_majorticklabels(), wrap=True)
plt.show()
'''

'''############################# GRAFICO PIZZA 4x4 = IDADE, ESPIRITUALIDADE, ESTADO CIVIL e FILHOS ############################
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2) 

# proporção por idade
#fig, ax1 = plt.subplots()
labels = data.idade.unique().tolist()
sizes = []
for i in labels:
    sizes.append(len(data[data.idade == i]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
pie = ax1.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
#ax1.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.legend(pie[0],labels, bbox_to_anchor=(0,0.5), loc="lower left", bbox_transform=plt.gcf().transFigure)
#ax1.legend(labels, loc='lower left')
ax1.set_title('Distribuição por Idade')
#plt.show()

# proporção de espiritualidade
#fig, ax2 = plt.subplots()
labels = data.fe.unique().tolist()
sizes = []
for i in labels:
    sizes.append(len(data[data.fe == i]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
#ax2.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
pie = ax2.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax2.legend(pie[0],labels, bbox_to_anchor=(1,0.5), loc="lower right", bbox_transform=plt.gcf().transFigure)
#ax2.legend(labels, loc='center right')
ax2.set_title('Nível de Espiritualidade')
#plt.show()

# proporção por estado civil
#fig, ax3 = plt.subplots()
labels = data.estadoCivil.unique().tolist()
sizes = []
for i in labels:
    sizes.append(len(data[data.estadoCivil == i]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
pie = ax3.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax3.legend(pie[0],labels, bbox_to_anchor=(0,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
ax3.set_title('Distribuição por Estado Civil')
#plt.show()

# proporção de filhos
#fig, ax4 = plt.subplots()
labels = data.filhos.unique().tolist()
sizes = []
for i in labels:
    sizes.append(len(data[data.filhos == i]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
pie = ax4.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax4.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
ax4.set_title('Distribuição por Filhos')
plt.show()
'''







'''############################# GRAFICO PIZZA 4x4 = ESCOLARIDADE, RENDA, OCUPAÇÃO e GÊNERO #########################
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2) 

# proporção por ESCOLARIDADE
#fig, ax1 = plt.subplots()
labels = data.escolaridade.unique().tolist()
sizes = []
for i in labels:
    sizes.append(len(data[data.escolaridade == i]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
pie = ax1.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
#ax1.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.legend(pie[0],labels, bbox_to_anchor=(0,0.5), loc="lower left", bbox_transform=plt.gcf().transFigure)
#ax1.legend(labels, loc='lower left')
ax1.set_title('Distribuição por Escolaridade')
#plt.show()

# proporção de Renda
#fig, ax2 = plt.subplots()
labels = data.renda.unique().tolist()
sizes = []
for i in labels:
    sizes.append(len(data[data.renda == i]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
#ax2.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
pie = ax2.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax2.legend(pie[0],labels, bbox_to_anchor=(1,0.5), loc="lower right", bbox_transform=plt.gcf().transFigure)
#ax2.legend(labels, loc='center right')
ax2.set_title('Distribuição por Renda')
#plt.show()

# proporção por ocupação
#fig, ax3 = plt.subplots()
labels = data.ocupacao.unique().tolist()
sizes = []
for i in labels:
    sizes.append(len(data[data.ocupacao == i]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
pie = ax3.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax3.legend(pie[0],labels, bbox_to_anchor=(0,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
ax3.set_title('Distribuição por Ocupação')
#plt.show()

# proporção de genero
#fig, ax4 = plt.subplots()
labels = data.sexo.unique().tolist()
sizes = []
for i in labels:
    sizes.append(len(data[data.sexo == i]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
pie = ax4.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax4.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
ax4.set_title('Distribuição por Gênero')
plt.show()
'''

'''############################# GRAFICO PIZZA 2x2 = AJUDA MAIS e AJUDA MENOS ################################
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
ax1.set_title('Quem ajuda mais o Terceiro Setor?')
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
ax2.set_title('Quem ajuda menos o Terceiro Setor?')
plt.show()
'''






















'''############################# GRAFICO PIZZA 2x2 - MIDIAS + MESES + PREFERENCIAS + AVALIAÇÃO ################################
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

#fig, ax1 = plt.subplots()
labels = ['Rádio', 'Blogs e Sites', 'Televisão', 'Jornais e Revistas', 'Carros de Som', 'Igreja', 'Facebook', 'Instagram', 'Whatsapp']
sizes = []
for i in labels:
    sizes.append(len(data[data[i] == 1]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
pie = ax1.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
#ax1.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.legend(pie[0],labels, bbox_to_anchor=(0,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
#ax1.legend(labels, loc='lower left')
ax1.set_title('Meios de Comunicação mais utilizados')
#plt.show()

#fig, ax2 = plt.subplots()
labels = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
sizes = []
for i in labels:
    sizes.append(len(data[data[i] == 1]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
#ax2.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
pie = ax2.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax2.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
#ax2.legend(labels, loc='center right')
ax2.set_title('Meses Preferidos para Colaborações')
plt.show()

#fig, ax2 = plt.subplots()
labels = ['Recolher em casa', 'Transferência ou Depósito', 'Correspondência', 'Pix', 'Troco Solidário', 'Rifas e Sorteios', 'Dízimo']
sizes = []
for i in labels:
    sizes.append(len(data[data[i] == 1]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
#ax2.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
pie = ax3.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax3.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
#ax2.legend(labels, loc='center right')
ax3.set_title('Meios de Colaboração Preferidos')
plt.show()

#fig, ax2 = plt.subplots()
labels = ['Muito Importante', 'Importante', 'Mediana', 'Às vezes é Importante', 'Não é Importante']
sizes = []
for i in labels:
    for j in ['apae', 'acapam', 'aldeiasSOS', 'abrigo', 'caritas', 'fazendaEsperanca', 'cvv', 'risoterapia', 'hemocentro']:
        sizes.append(len(data[data[j] == i]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
#ax2.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
pie = ax4.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax4.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
#ax2.legend(labels, loc='center right')
ax4.set_title('Avaliação Geral das Entidades da Região')
plt.show()

'''








