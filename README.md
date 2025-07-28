# GamePy

### Projeto 1- Game (Curso Programação em Python do básico ao avançado) - Geek University (com algumas modificações)

### Não é necessário nenhum módulo extra do Python para execução deste Game.

O game consiste em algumas etapas:

##### 1 - Selecionar a dificuldade do jogo. É possível selecionar valores entre 1 e 4.
##### 2 - É exibida uma operação matemática, gerada randomicamente. As possíveis operações são três operações matemáticas fundamentais: soma, subtração, e multiplicação. São utilizados dois valores numéricos na operação. O número de algarismos significativos nestas operações correspondem ao valor da dificuldade selecionada.
##### 3 - O usuário digita a possívell resposta. 
##### 4 - O programa imprime "Resposta correta" caso a resposta esteja correta. Caso contrário, o programa imprime "Resposta incorreta".
##### 5 - O programa solicita ao usuário se deseja continuar com o jogo. Caso a resposta seja 1, o programa retorna para etapa 1. Caso seja 0, o programa encerra, e caso não corresponda a nenhuma desses valores, o programa inicia essa etapa (etapa 5).
##### 6 - Quando o programa encerra, imprime a quantidade de pontos acumulados.


### Sugestões futuras

##### 1 - Operações de multiplicação serão mais relevantes.
##### 2 - Utilização do método time.sleep() na biblioteca time, para imprimir tempo restante, de acordo com a relevância da operação e do nível de dificuldade.

```

Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: 2
Informe o resultado para a seguinte operação: 
71 - 81 = ?
-10
Resposta correta!
71 - 81 = -10
Você possui 1 ponto
Deseja continuar no jogo? [1 - sim, 0 - não]: 1
Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: 2
Informe o resultado para a seguinte operação: 
6 - 51 = ?
-45
Resposta correta!
6 - 51 = -45
Você possui 2 pontos
Deseja continuar no jogo? [1 - sim, 0 - não]: 1
Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: 1
Informe o resultado para a seguinte operação: 
6 - 7 = ?
-1
Resposta correta!
6 - 7 = -1
Você possui 3 pontos
Deseja continuar no jogo? [1 - sim, 0 - não]: 1
Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: 4
Informe o resultado para a seguinte operação: 
3687 + 4515 = ?
8202
Resposta correta!
3687 + 4515 = 8202
Você possui 4 pontos
Deseja continuar no jogo? [1 - sim, 0 - não]: 1
Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: 3
Informe o resultado para a seguinte operação: 
867 * 900 = ?
780300
Resposta correta!
867 * 900 = 780300
Você possui 5 pontos
Deseja continuar no jogo? [1 - sim, 0 - não]: 0
Você finalizou com 5 pontos
Até a próxima!


```
