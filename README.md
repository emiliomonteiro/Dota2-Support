# Dota 2 Support Timer

Este é um aplicativo simples de suporte para o jogo Dota 2, desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica.

## Funcionalidades

- Inicia um timer que pode ser usado para marcar tempos importantes durante uma partida de Dota 2.
- Permite ao usuário escolher entre "Safelane" e "Offlane" antes de iniciar o timer.
- Exibe mensagens "Stack" a cada minuto inteiro menor que 15 no segundo 50.
- Exibe mensagens "Bounty" nos tempos 00:00, 03:00, 06:00, etc., seguindo esse padrão.

## Como Usar

1. **Escolha da Lane:**
   - Ao iniciar o aplicativo, selecione se você está na "Safelane" ou "Offlane" clicando no botão correspondente.

2. **Iniciar o Timer:**
   - Após selecionar a lane, o timer começará após uma pausa de 20 segundos.
   - O timer mostrará os minutos e segundos decorridos desde o início.

3. **Mensagens Stack e Bounty:**
   - **Stack:** A cada minuto inteiro menor que 15 no segundo 50, uma mensagem "Stack" será exibida.
   - **Bounty:** Nos tempos 00:00, 03:00, 06:00, etc., uma mensagem "Bounty" será exibida.

4. **Histórico:**
   - O aplicativo mantém um histórico das últimas 5 mensagens exibidas, junto com seus timestamps.

5. **Fechar e Reiniciar:**
   - Use o botão "Fechar" para encerrar a aplicação.
   - Use o botão "GG" para reiniciar a aplicação ao estado inicial, permitindo a seleção da lane novamente.

## Pré-requisitos

- Python 3 instalado
- Biblioteca Tkinter (geralmente incluída na instalação padrão do Python)

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/dota2-support-timer.git
   cd dota2-support-timer


2. Execute o aplicativo:
   ```bash
   python main.py
