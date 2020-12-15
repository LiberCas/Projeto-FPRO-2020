# Projeto-FPRO-2020
## FPRO/MIEIC, 2020/21
## Igor Liberato de Castro (up202000161)
## 1MIEIC01

### Objetivo

1. Criar um jogo computadorizado do jogo de cartas "Blackjack" em Pygame.

### Repositório de código

1) Link para o repositório do GitHub: https://github.com/LiberCas/Projeto-FPRO-2020

### Descrição

*---É um jogo, originalmente em cartas físicas, de jogadores independentes contra o dealer.---*

#### Início da Ronda

*---No começo da ronda, todos os jogadores fazem suas apostas. Cada jogador começa com duas cartas de um bolo embaralhado de 4 baralhos standard de 52 cartas viradas para cima. O dealer começa com uma carta virada para baixo, a qual ninguém poderá ver(carta de furo) até que o dealer jogue, e uma carta virada para cima(carta ascendente).---*

#### Objectivo

*---O objectivo dos jogadores é conseguir que o somatório dos pontos das suas cartas seja o mais próximo possível, mas nunca maior que, 21. O dealer possui o mesmo objectivo que os jogadores. No caso do jogo virtual, a máquina faz o papel do dealer.---*

#### Gameplay

*---Cada jogador na mesa poderá, em sua vez, escolher bater(pedir uma nova carta do baralho para si) ou parar(passar sua vez). Caso a soma das cartas de qualquer jogador passe de 21, ele perde automaticamente para o dealer(bust). Quando nenhum dos jogadores da mesa quiser mais bater, o dealer jogará. O modo de jogo do dealer é predeterminado, podendo ser facilmente imitado por uma máquina. Começa por revelar para todos sua carta de furo e depois procede a bater. O dealer parará de bater quando a soma dos valor de suas cartas atingir ou passar de 17. Caso a soma do valor de suas cartas passar de 21 ele perderá para trodos os jogadores que não já perderam pelo mesmo motivo.---*

#### Fim da ronda

*---Ao fim da ronda, o dealer receberá para si todas as apostas dos jogadores cuja soma dos valores das suas cartas for maior que a sua, bem como daqueles que perderam por bust. O dealer tambem dará aos jogadores vencedores, da sua reserva, um valor em fichas equivalente às apostas que fizeram. Após esse passo as cartas de cada jogador são eliminadas do jogo e começa-se uma nova ronda.---*

### Pacotes

- Pygame

### Tarefas

1. fazer a interface do menu e regras
2. identificar se o jogador clicou em "jogar"
3. atribuir ao jogador um valor em fichas
4. captar a aposta do jogador
5. dar as cartas iniciais ao jogador e ao dealer
6. captar o input do jogador e dar-lhe novas cartas com base nisso
7. criar função para o comportamento do dealer
8. identificar condições de vitória/perda
9. dar/retirar dos jogadores as fichas relativas à sua vitória/perda
10. identificar se o jogador que jogar novamente ou sair
11. Identificar fim do deck de cartas

- Atualizado a última vez em 15/12/2020
