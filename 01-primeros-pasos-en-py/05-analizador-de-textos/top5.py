from cantidad_de import separar_y_contar
from collections import Counter
def top5(ruta):
    top_5 = separar_y_contar(ruta)
    print(top_5.most_common(5))