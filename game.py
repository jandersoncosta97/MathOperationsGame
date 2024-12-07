from models.calcular import Calcular

def main() -> None:
    pontos: int = 0

def jogar(pontos: int) -> None:
    dificuldade: int = input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: ')

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())
    
    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você possui {pontos} pontos')

    continuar: int = int(input('Deseja continua no jogo? [1 - sim, 0 - não] '))
    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} pontos')
        print('Até a próxima!')
    
if __name__ == '__main__':
    main()
    
