class OperacoesMatematicas:
    def __init__(self, numero1, numero2, numero3, numero4):
        """
        Inicializa o TAD com dois números.
        :param numero1: Primeiro número.
        :param numero2: Segundo número.
        """
        self.numero1 = numero1
        self.numero2 = numero2
        self.numero3 = numero3
        self.numero4 = numero4
        
    def somar(self):
        """Retorna a soma dos dois números."""
        return self.numero3 + self.numero4

    def subtrair(self):
        """Retorna a subtração do primeiro número pelo segundo."""
        return self.numero1 - self.numero2

    def multiplicar(self):
        """Retorna a multiplicação dos dois números."""
        return self.numero1 * self.numero2

    def dividir(self):
        """
        Retorna a divisão do primeiro número pelo segundo, 
        garantindo que a divisão por zero não ocorra.
        """
        if self.numero2 == 0:
            return "Erro: Divisão por zero não é permitida."
        return self.numero1 / self.numero2

# Exemplo de uso do TAD
num1 = 25
num2 = 5
num3 = 2
num4 = 10
calc = OperacoesMatematicas(num1, num2, num3, num4)

print("Soma:", calc.somar())
print("Subtração:", calc.subtrair())
print("Multiplicação:", calc.multiplicar())
print("Divisão:", calc.dividir())