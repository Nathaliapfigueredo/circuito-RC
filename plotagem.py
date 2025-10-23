import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Dados do Monitor Serial 
dados = """
401 4.80 0.20
803 4.61 0.39
1205 4.43 0.57
1607 4.26 0.74
2010 4.09 0.91
2412 3.93 1.07
2813 3.77 1.23
3216 3.63 1.37
3618 3.48 1.52
4021 3.34 1.66
4423 3.21 1.79
4825 3.08 1.92
5227 2.97 2.03
5629 2.85 2.15
6032 2.74 2.26
6434 2.63 2.37
6836 2.52 2.48
7238 2.42 2.58
7641 2.33 2.67
8043 2.24 2.76
8445 2.15 2.85
8847 2.06 2.94
9249 1.98 3.02
9652 1.91 3.09
10054 1.83 3.17
10457 1.76 3.24
10859 1.69 3.31
11260 1.62 3.38
11663 1.56 3.44
12065 1.50 3.50
12468 1.44 3.56
12870 1.38 3.62
13273 1.32 3.68
13675 1.28 3.72
14077 1.22 3.78
14480 1.17 3.83
14882 1.13 3.87
15285 1.09 3.91
15686 1.04 3.96
16089 1.00 4.00
16491 0.96 4.04
16893 0.92 4.08
17296 0.88 4.12
17698 0.85 4.15
18101 0.82 4.18
18503 0.79 4.21
18906 0.75 4.25
19308 0.72 4.28
19709 0.70 4.30
20112 0.67 4.33
20514 0.64 4.36
0 5.00 0.00
"""

df = pd.read_csv(StringIO(dados), sep=" ", names=["tempo_ms", "tensao_resistor", "tensao_capacitor"])

# Converte o tempo para segundos
df["tempo_s"] = df["tempo_ms"] / 1000

# Plota o gráfico 1:  Tensão no Capacitor (Carga)
plt.figure(figsize=(8,5))
plt.plot(df["tempo_s"], df["tensao_capacitor"], 'o-', color='blue', label='Tensão no Capacitor (VC)')
plt.title("Curva de Carga do Capacitor (VC)")
plt.xlabel("Tempo (s)")
plt.ylabel("Tensão (V)")
plt.grid(True)
plt.legend()
plt.show()

# Plota o gráfico 2: Tensão no Resistor (Descarga)
plt.figure(figsize=(8,5))
plt.plot(df["tempo_s"], df["tensao_resistor"], 'o-', color='red', label='Tensão no Resistor (VR)')
plt.title("Curva de Descarga no Resistor (VR)")
plt.xlabel("Tempo (s)")
plt.ylabel("Tensão (V)")
plt.grid(True)
plt.legend()
plt.show()

# Plota o gráfico 3: Comparação
plt.figure(figsize=(8,5))
plt.plot(df["tempo_s"], df["tensao_resistor"], 'r-', label='VR (Descarga)')
plt.plot(df["tempo_s"], df["tensao_capacitor"], 'b-', label='VC (Carga)')
plt.title("Comparação: Carga e Descarga (VR x VC)")
plt.xlabel("Tempo (s)")
plt.ylabel("Tensão (V)")
plt.grid(True)
plt.legend()
plt.show()
