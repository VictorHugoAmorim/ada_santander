from Geometria.Bola import *
from Geometria.Retangulo import *

# Criando uma instância da classe Bola
bola_1 = Bola('Azul', 6)

area_bola = bola_1.calcular_area()
print(f'Área da bola: {area_bola:.2f}')

bola_1.imprimir_cor()

volume_bola = bola_1.calcular_volume()
print(f'Volume da bola: {volume_bola:.2f}')

# Criando uma instância da classe Retangulo
retangulo_1 = Retangulo(4, 5)

area_retangulo = retangulo_1.calcular_area()
print(f'A área do retângulo é {area_retangulo:.2f}')
