#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

# Crea el dataset con << tus datos obtenidos en barplot_data.txt >>
array_from_file = np.loadtxt("barplot_data.txt", dtype=str)
array_from_file = array_from_file.T

labels = array_from_file[0]
labels = [ '\n'.join(wrap(l, 11)) for l in labels]

data = np.array(array_from_file[1], dtype='i4')

y_pos = np.arange(len(labels))

# Gráfico de barras
plt.bar(y_pos, data)

# Nombres en el eje-x
plt.xticks(y_pos, labels, rotation=45)

plt.savefig('graph.png')
plt.tight_layout()
# Mostrar la gráfica
plt.show()

