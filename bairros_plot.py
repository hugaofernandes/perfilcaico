
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

################################### HISTOGRAMA 2x1 = BAIRROS ##########################################

def bairros(data):
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


