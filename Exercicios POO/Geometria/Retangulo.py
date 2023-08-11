class Retangulo:
    def __init__(self, lado_a, lado_b) -> None:
        self.lado_a = lado_a
        self.lado_b = lado_b
    
    def calcular_area(self) -> float:
        area = self.lado_a * self.lado_b
        return area

retangulo_1 = Retangulo(4,5)

area_retangulo = retangulo_1.calcular_area()
print(f'A área é do retângulo é {area_retangulo}')