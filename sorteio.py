import random
from jinja2 import Template, Environment, FileSystemLoader

#CLASSE E SEUS ATRIBUTOS
class Sorteio():
    array_total_jogos = []

    def __init__(self, quantidade_dezenas, total_jogos):
        try:
            type(quantidade_dezenas) == int
        except:
            raise ValueError ("O valor escolhido precisa ser um número inteiro e estar entre 6 e 10.")
        try:
            if 6 <= quantidade_dezenas <= 10 and type(quantidade_dezenas) == int:
                self.__quantidade_dezenas = quantidade_dezenas
            else:
                raise AttributeError("O valor escolhido precisa ser um número inteiro e estar entre 6 e 10.")
        except:
            raise ValueError ("O valor escolhido como parâmetro precisa estar entre 6 e 10 e ser um inteiro.")
        self.__resultado = []
        self.__total_jogos = total_jogos
        self.__jogos = []

    #GETTERS
    @property
    def quantidade_dezenas(self):
        return self.__quantidade_dezenas

    @property
    def resultado(self):
        return self.__resultado

    @property
    def total_jogos(self):
        return self.__total_jogos

    @property
    def jogos(self):
        return self.__jogos

    #SETTERS
    @quantidade_dezenas.setter
    def quantidade_dezenas(self, valor):
        if 6 <= valor <= 10:
            self.__quantidade_dezenas = valor
        else:
            raise ValueError ("O valor escolhido precisa estar entre 6 e 10.")

    @resultado.setter
    def resultado(self, lista):
        self.__resultado.clear()
        try:
            if len(lista) != 6:
                raise Exception("A lista precisa conter 6 números inteiros.")
        except:
            raise TypeError("Os valores informados precisam ser uma lista com 6 números inteiros.")
        try:
            for i in lista:
                if type(i) == int:
                    self.__resultado.append(i)
                else:
                    raise ValueError("Os valores informados devem ser uma lista com 6 números inteiros.")
        except:
            raise ValueError("Os valores informados devem ser uma lista com 6 números inteiros.")

    @total_jogos.setter
    def total_jogos(self, val):
        if type(val) == int and val >= 1:
            self.__total_jogos = val
        else:
            raise ValueError("O valor precisa ser um inteiro maior do que 0.")

    @jogos.setter
    def jogos(self, valor):
        if type(valor) == list and 6 <= len(valor) <= 10:
            for i in valor:
                if type (i) != int or  i <= 0 or i > 60: 
                    raise ValueError("O valor precisa ser uma lista com números inteiros entre 1 e 60 e conter entre 6 e 10 números.")
            self.__jogos.append(valor)

        else:
            raise ValueError("O valor precisa ser uma lista com números inteiros entre 1 e 60 e conter entre 6 e 10 números.")

    #MÉTODOS

    def _retorna_dezena(self): #Retorna uma dezena randômica com números em ordem crescente e sem repetição. Números entre 1 e 60.
        try:
            if 6 <= self.quantidade_dezenas <= 10:
                numeros = list(range(1, 61))
                random.shuffle(numeros)
                numeros = numeros[:self.quantidade_dezenas]
                numeros = sorted(numeros)
                print(numeros)
                return(numeros)
            else:
                raise ValueError ("O valor desejado tem que ser entre 6 e 10 e ser um inteiro.")
        except:
            raise TypeError ("O campo informado precisa ser um número inteiro de 6 a 10.")

    def retorna_jogos(self): #Retorna todos os jogos criados que estão no atributo self.total__jogos.  
        if type(self.total_jogos) == int and self.total_jogos >= 1: 
            for i in range(self.total_jogos):
                jogo_x = self._retorna_dezena()
                sorteio.jogos = jogo_x
            return self.jogos
        else:
            raise ValueError("A quantidade de jogos precisa ser um inteiro e ser maior do que 0.")

    def sorteia_seis(self): #Sorteia um resultado com 6 números que não se repetem e salva no atributo resultado.
        numeros_resultado = list(range(1, 61))
        random.shuffle(numeros_resultado)
        numeros_resultado = numeros_resultado[:6]
        numeros_resultado = sorted(numeros_resultado)
        for i in numeros_resultado:
            sorteio.resultado.append(i)
        return(numeros_resultado)

    def confere(self): #Checa quantos números de cada jogo feito foram os mesmos do resultado. Retorna como uma lista renderizada em html.
        result = []
        for i in self.jogos:
            cont = 0
            for j in i:
                if j in self.resultado:
                    cont += 1
            result.append((' '.join(("{:02d}".format(numero) for numero in i)), cont))
        print(result)
        with open('template.html') as arquivo:
            template = Template(arquivo.read())
            renderiza_template = template.render(result=result)
        print(renderiza_template)

#PROGRAMA PRINCIPAL
sorteio = Sorteio(6, 10)
sorteio._retorna_dezena()
sorteio.sorteia_seis()
sorteio.retorna_jogos()
sorteio.confere()



