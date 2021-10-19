
import matplotlib.pyplot as plt

############################ GRAFICO PIZZA = RENDA ############################

def renda(data):
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
    ax.set_title('Distribuição por Faixa de Renda')
    plt.show()

