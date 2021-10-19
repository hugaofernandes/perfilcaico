
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

###############################  HISTOGRAMA 2x1 = EFEITO DA PANDEMIA ###################################

def pandemia(data):
    fig, axs = plt.subplots(2, 1, tight_layout=True)
    axs[0].hist(data['pandemia'], bins=len(data['pandemia']))
    axs[0].set_title('Efeitos da Pandemia nas Doações (Distribuição Absoluta)')
    plt.setp(axs[0].xaxis.get_majorticklabels(), wrap=True)
    axs[1].hist(data['pandemia'], bins=len(data['pandemia']), density=True)
    axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))
    axs[1].set_title('Efeitos da Pandemia nas Doações (Distribuição Relativa)')
    plt.setp(axs[1].xaxis.get_majorticklabels(), wrap=True)
    plt.show()


