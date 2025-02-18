from random import choice
from game_data import figures

pessoas_escolhidas = []
score = 0
pessoa_a = {}
pessoa_b = {}

def inicioJogo():
    pessoa_a = escolhePessoa()
    pessoa_b = escolhePessoa()
    score = 0
    andamentoJogo(pessoa_a, pessoa_b, score)


def escolhePessoa():
    pessoa = choice(figures)
    nome_pessoa = pessoa.get('name')
    # Verifica se a pessoa já foi selecionada
    if nome_pessoa in pessoas_escolhidas:
        escolhePessoa()

    pessoas_escolhidas.append(nome_pessoa)
    return pessoa

def fimJogo(score, vitoria):
    if vitoria:
        print('Parabéns! Você finalizou o jogo!')
    else:
        print(f'Você errou! Sua pontuação final foi {score}')

    novo_jogo = ''
    while novo_jogo not in ['S', 'N']:
        print('Deseja iniciar um novo jogo? S / N')
        novo_jogo = input().upper()

    if novo_jogo == 'S':
        inicioJogo()
    else:
        print('Certo! Nos vemos na próxima!')


def andamentoJogo(pessoa_a, pessoa_b, score):
    if len(pessoas_escolhidas) == len(figures):
        fimJogo(score, True)

    names = [pessoa_a.get('name'), pessoa_b.get('name')]
    followers = [pessoa_a.get('followers'), pessoa_b.get('followers')]
    descriptions = [pessoa_a.get('description'), pessoa_b.get('description')]
    ganhador = 'A' if followers[0] >= followers[1] else 'B'
    print(f'Quem tem mais seguidores? [A] - {names[0]}, {descriptions[0]} ou [B] - {names[1]}, {descriptions[1]}')

    if input().upper() == ganhador:
        score+=1
        print(f'Correto!\nSeu score é {score}.\nPróximo nível:\n')
        andamentoJogo(pessoa_b, escolhePessoa(), score)
    else:
        fimJogo(score, False)

inicioJogo()
