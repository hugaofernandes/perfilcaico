
import matplotlib.pyplot as plt

############################ GRAFICO PIZZA = PREFERENCIAS ############################

def preferencias(data):
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
    ax.set_title('Meios de Colaboração Preferidos')
    plt.show()

