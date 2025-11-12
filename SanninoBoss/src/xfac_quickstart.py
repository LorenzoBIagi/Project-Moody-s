import xfacpy as xfac

# 1) ispeziona cosa espone il modulo
public = [n for n in dir(xfac) if not n.startswith("_")]
print("xfacpy symbols:", public[:25], "...")

# 2) se c'è una funzione con docstring, stampane l'help (cambia 'qualcosa' con un nome visto sopra)
# help(xfac.nome_funzione)

# Nota: xfac è una libreria C++ con binding; spesso espone routine per:
#  - approssimare funzioni multi-dimensionali in formato Tensor Train (TT)
#  - costruire TT da campionamenti f(x1,...,xN)
#  - fare 'cross interpolation'
# Usa help(...) e dir(...) per vedere i nomi esatti nel tuo build.
print("xfacpy caricato:", hasattr(xfac, "__doc__"))