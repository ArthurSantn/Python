class calculando:
    def __init__(self, numero1, numero2):
        
        self.numero1 = numero1
        self.numero2 = numero2
        
    def soma(self):
        return self.numero1 + self.numero2
    
    def subtrair(self):
        return self.numero1 - self.numero2
    
    def multiplicar(self):
        return self.numero1 * self.numero2
    
    def divisao(self):
        if self.numero2 == 0:
            return "Não é possível dividir por zero seu lunático do caralho"
        else:
            return self.numero1 / self.numero2
        
num1 = 20
num2 = 10
calculo = calculando(num1, num2)

print("Receba seus resultados")

print("Soma:", calculo.soma())
print("Subtração:", calculo.subtrair())
print("multiplicação:", calculo.multiplicar())
print("Divisão:", calculo.divisao())