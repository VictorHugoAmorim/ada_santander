class Bola:
    def __init__(self, cor : 'str', raio : 'float') -> None:
        self.cor = cor
        self.raio = raio
    
    def calcular_area(self) -> float:
        area = 4 * 3.14 * self.raio ** 2
        return area
        
    def imprimir_cor(self):
        print(f'A cor da bola é {self.cor}')
    
    def calcular_volume(self) -> float:
        volume = (4/3) * 3.14 * self.raio ** 3
        return volume
    
bola_1 = Bola('Azul', 6)

area_bola = bola_1.calcular_area()
print(f'Área da bola: {area_bola}')

bola_1.imprimir_cor()

volume_bola = bola_1.calcular_volume()
print(f'Volume da bola: {volume_bola}')
