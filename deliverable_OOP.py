class Campeonato():
    def __init__(self, nome, pontuacao, qnt_jogos, posicao, vitorias, derrotas):
        '''
            A classe tem como objetivo definir nome, pontuação e outros 4 atributos para a tabela de
            um campeonato, cada elemento dessa classe tem esses atributos e ela permite operação entre
            os elementos.
        '''
        if type(nome) == str:
            self.nome = nome
            self.pontuacao = int(pontuacao)
            self.qnt_jogos = int(qnt_jogos)
            self.posicao = int(posicao)
            self.vitorias = int(vitorias)
            self.derrotas = int(derrotas)

    def __eq__(time1, time2):
        if time1.pontuacao == time2.pontuacao:
            return True
    
    def __ne__(time1, time2):
        if time1.pontuacao != time2.pontuacao:
            return True

    def __gt__(time1, time2):
        if time1.pontuacao > time2.pontuacao:
            return True
    
    def __lt__(time1, time2):
        if time1.pontuacao < time2.pontuacao:
            return True

    def __ge__(time1, time2):
        if time1.pontuacao >= time2.pontuacao:
            return True
    
    def __le__(time1, time2):
        if time1.pontuacao <= time2.pontuacao:
            return True

    def __add__(time1, time2):
        return time1.pontuacao + time2.pontuacao

    def __str__(self):
        return (f'O {self.nome} está com {self.pontuacao} pontos na {self.posicao} º colocação com {self.vitorias} vitorias e {self.derrotas} derrotas')