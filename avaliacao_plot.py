
import matplotlib.pyplot as plt

############################ GRAFICO PIZZA = AVALIACAO ############################

def avaliacao(data):
    fig, ax = plt.subplots()
    labels = ['Muito Importante', 'Importante', 'Mediana', 'Às vezes é Importante', 'Não é Importante']
    #labels = data['apae', 'acapam', 'aldeiasSOS', 'abrigo', 'caritas', 'fazendaEsperanca', 'cvv', 'risoterapia', 'hemocentro'].unique().tolist()
    sizes = []
    aux = 0
    for i in labels:
        for j in ['apae', 'acapam', 'aldeiasSOS', 'abrigo', 'caritas', 'fazendaEsperanca', 'cvv', 'risoterapia', 'hemocentro']:
            aux += len(data[data[j] == i])
        sizes.append(aux)
        aux = 0
    explode = [0.1]*len(labels)
    #ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    pie = ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(pie[0],labels, bbox_to_anchor=(0,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
    #ax.legend(labels, loc='center right')
    ax.set_title('Avaliação Geral das Entidades da Região')
    plt.show()

