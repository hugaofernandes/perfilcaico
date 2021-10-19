

import matplotlib.pyplot as plt

############################# GRAFICO PIZZA 2x1 = AJUDA MAIS e AJUDA MENOS ################################

def ajuda(data):
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

