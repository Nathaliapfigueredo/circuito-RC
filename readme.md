# Projeto: Análise do Circuito RC com Arduino

## Objetivo
Investigar o comportamento de carga e descarga de um capacitor em um circuito RC (Resistor–Capacitor), utilizando o Arduino Uno para medir a variação de tensão e o Python para gerar gráficos comparativos entre as tensões no resistor e no capacitor ao longo do tempo. Neste experimento, o circuito RC foi montado e monitorado por meio do Arduino Uno, permitindo observar o comportamento da tensão no resistor (VR) e no capacitor (VC) durante os processos de carga e descarga.

## Entendimento da Teoria 

Com o objetivo de entender como esses fenômenos funcinando trago um pouco da teoria por trás como um adicional ao trabalho. Os circuitos Resistor–Capacitor são amplamente utilizados em sistemas eletrônicos por sua capacidade de armazenar e liberar energia de forma controlada. Eles aparecem em filtros, temporizadores, sensores e sistemas de controle analógico. 

A análise desses fenômenos baseia-se nas leis exponenciais de variação de tensão e na constante de tempo (τ), que determina a velocidade com que o capacitor se carrega ou descarrega. As equações matemáticas a seguir descrevem o comportamento dinâmico do circuito, permitindo comparar os valores experimentais medidos com os resultados teóricos esperados.

### Carga do Capacitor

A tensão no capacitor durante o processo de carga é dada por:

$$
\[
V_C(t) = V_f \cdot \left(1 - e^{-\frac{t}{R \cdot C}}\right)
\]
$$ 

onde:  


- $$\( V_C(t) \)$$: tensão no capacitor no instante \( t \)  
- $$\( V_f \)$$: tensão final (tensão de alimentação)  
- $$\( R \)$$: resistência (Ω)  
- $$\( C \)$$: capacitância (F)  
- $$\( t \)$$: tempo (s)


### Descarga do Capacitor

Durante a descarga, a tensão no capacitor decresce exponencialmente:

$$
\[
V_C(t) = V_0 \cdot e^{-\frac{t}{R \cdot C}}
\]
$$

onde:  
- $$\( V_0 \)$$: tensão inicial do capacitor no início da descarga  





### Constante de Tempo (τ)

A constante de tempo de um circuito RC é definida como:

$$
\[
\tau = R \cdot C
\]
$$

Ela representa o tempo necessário para que:  
- o capacitor carregue até 63% da tensão máxima $$(\( 0.63 \cdot V_f \))$$, ou  
- descarregue até 37% da tensão inicial $$(\( 0.37 \cdot V_0 \))$$.



## Materiais Utilizados

| Componente | Quantidade | Função |
|-------------|-------------|--------|
| Arduino Uno | 1 | Microcontrolador para leitura e envio de dados |
| Protoboard | 1 | Montagem do circuito |
| Capacitor eletrolítico (100 µF) | 1 | Armazenar carga elétrica |
| Resistores (10 kΩ) | 2 | Controlar a corrente e tempo de carga/descarga |
| LED | 1 | Indicação visual do circuito |
| Jumpers (fios) | vários | Conexões elétricas |


## Montagem do Circuito

O circuito RC foi montado conforme a figura abaixo:
<img width="722" height="272" alt="Screenshot 2025-10-23 144502" src="https://github.com/user-attachments/assets/ddef5ff3-620a-4f3b-ba4e-eb2eaf6bc34e" />


- O capacitor foi conectado entre o ponto de medição e o GND.  
- Os dois resistores formam o caminho de carga e descarga, limitando a corrente.  
- O fio laranja (A0) mede a tensão do capacitor (Vc).  
- O Arduino alimenta o circuito com 5V e coleta dados analógicos.  



## Código Utilizado (Arduino)

```cpp
int pinoNoRC=0; 
int valorLido = 0;
float tensaoCapacitor = 0, tensaoResistor;
unsigned long time; 
void setup(){ 
Serial.begin(9600); 
} 
void loop() { 
	time=millis(); 
	valorLido=analogRead(pinoNoRC); 
	tensaoResistor=(valorLido*5.0/1023); // 5.0V / 1023 degraus = 0.0048876 
	tensaoCapacitor = abs(5.0-tensaoResistor);
 	Serial.print(time); //imprime o conteúdo de time no MONITOR SERIAL
    Serial.print(" "); 
  	Serial.print(tensaoResistor);
  	Serial.print(" ");
  	Serial.println(tensaoCapacitor); 
	delay(400); 
}

```

## Coleta de Dados

Os valores foram coletados pelo Monitor Serial do Arduino.
Cada linha contém:

Tempo (ms)   Tensão no Resistor (V)   Tensão no Capacitor (V)

<img width="155" height="257" alt="image" src="https://github.com/user-attachments/assets/e663717d-5b7b-4060-8b21-467c1f6bf80d" />

## Plotagem dos Gráficos (Python)

Os dados foram copiados do Monitor Serial e utilizados no Python para gerar os gráficos de carga e descarga:

```cpp
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
```

Gráfico gerado:
<img width="1920" height="1080" alt="Untitled design (4)" src="https://github.com/user-attachments/assets/55c0f810-fe6d-464e-8f23-951959556a8d" />


## Análise dos Resultados

Observa-se que a tensão no resistor (VR) decresce exponencialmente durante a carga do capacitor. Simultaneamente, a tensão no capacitor (VC) aumenta exponencialmente, tendendo a 5 V.


