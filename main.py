import matplotlib.pyplot as plt
from matplotlib_venn import venn2
# Creamos los conjuntos a partir de los datos proporcionados
set_pollo = set(range(1, 80))
set_vacuna = set(range(1, 68)).union(set(range(35, 80)))
set_pescado = set(range(1, 58)).union(set(range(22, 80)))

# Creamos el diagrama de Venn
venn2(subsets=[set_pollo-set_vacuna-set_pescado, set_vacuna|set_pescado-set_pollo, set_pollo&set_vacuna&set_pescado],
      set_labels=('Pollo', 'Vacuna / Pescado'))

# Mostramos el diagrama
plt.show()
