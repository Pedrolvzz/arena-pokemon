# 🎮 Arena Pokémon em Python

Jogo de batalhas por turnos no terminal, desenvolvido para praticar lógica de programação em Python. Escolha seu Pokémon inicial e enfrente três adversários para conquistar o título de Campeão da Arena.

**Python 3 · Terminal · Sem dependências externas**

## Funcionalidades

- Escolher entre Bulbasaur, Charmander e Squirtle.
- Enfrentar Rattata, Arbok e Charizard, nessa ordem.
- Atacar com dano aleatório.
- Usar poções para recuperar vida.
- Consultar a vida dos Pokémon e as poções restantes durante as batalhas.
- Fugir para encerrar a participação na arena.
- Exibir mensagens de vitória e derrota.

## Como executar

É necessário ter **Python 3** instalado. O projeto utiliza apenas o módulo `random`, incluído no Python.

1. Baixe o código e salve como `main.py`.
2. Abra o terminal na pasta do arquivo.
3. Execute:

```bash
python main.py
```

## Como jogar

Escolha seu Pokémon pelo número ou pelo nome:

| Pokémon | Vida máxima | Dano por ataque |
|---|---:|---:|
| 🌱 Bulbasaur | 120 | 12 a 20 |
| 🔥 Charmander | 85 | 18 a 28 |
| 💧 Squirtle | 100 | 15 a 24 |

Digite `S` para começar. Durante cada turno, escolha uma ação:

```text
[1] Atacar
[2] Curar
[3] Fugir
```

Também é possível digitar `atacar`, `curar` ou `fugir`.

### Regras da arena

- Seu Pokémon ataca primeiro.
- O adversário contra-ataca se sobreviver.
- Você começa com **3 poções**, compartilhadas entre os combates.
- Cada poção recupera até **35 pontos de vida**, sem ultrapassar o limite do Pokémon.
- Uma cura válida consome o turno e permite o contra-ataque.
- Ações inválidas e tentativas de cura sem poções ou com vida cheia não consomem o turno.
- Após vencer Rattata e Arbok, seu Pokémon recupera até **20 pontos de vida**.
- Derrote Charizard para conquistar o título de campeão.

### Adversários

| Pokémon | Vida | Dano por ataque |
|---|---:|---:|
| 🐀 Rattata | 40 | 5 a 10 |
| 🐍 Arbok | 65 | 8 a 14 |
| 🔥 Charizard | 100 | 12 a 20 |

## Conceitos praticados

- Estruturas de repetição com `while`.
- Condições com `if`, `elif` e `else`.
- Operadores lógicos `and` e `or`.
- Controle do fluxo com `break` e `continue`.
- Entrada de dados com `input()`.
- Manipulação de textos com `.strip()`, `.lower()` e `.upper()`.
- Geração de números aleatórios com `random.randint()`.
- Controle de vida, dano, turnos e quantidade de itens.
- Formatação de mensagens com f-strings.

## Limitações

O progresso é mantido apenas durante a execução. O jogo não possui salvamento, evolução, captura ou vantagens de tipo. Os atributos dos Pokémon foram adaptados para esta arena e não seguem os valores oficiais.

## Possíveis melhorias

- Adicionar ataques especiais.
- Implementar vantagens e desvantagens de tipo.
- Organizar os combates em funções para reduzir a repetição de código.
- Permitir jogar novamente sem reiniciar o programa.
- Mostrar um resumo final com turnos e poções utilizadas.
