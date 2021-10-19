
import matplotlib.pyplot as plt

############################ GRAFICO PIZZA = MIDIAS ############################

def midias(data):
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
    ax.set_title('Meios de Comunicação mais Utilizados')
    plt.show()

