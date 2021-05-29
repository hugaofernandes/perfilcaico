
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

def idades(data, coluna): # histograma das idades absoluta e relativa
    fig, axs = plt.subplots(1, 2, tight_layout=True)
    N, bins, patches = axs[0].hist(data[coluna], bins=len(data[coluna]))
    fracs = N / N.max()
    norm = colors.Normalize(fracs.min(), fracs.max())
    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)
    axs[1].hist(data[coluna], bins=len(data[coluna]), density=True)
    axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))
    axs[0].set_title('Idades Absolutas')
    axs[1].set_title('Idades Relativas')
    plt.show()

def comunicacao(data, labels): # proporção por redes sociais
    fig, ax = plt.subplots()
    sizes = []
    for i in labels:
        sizes.append(len(data[data[i] == 1]))
    explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
    pie = ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    #ax.legend(labels, loc='lower right')
    ax.legend(pie[0],labels, bbox_to_anchor=(0,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
    ax.set_title('Uso de Meios de Comunicação')
    plt.show()








