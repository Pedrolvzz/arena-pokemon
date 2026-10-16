import random

hp_rattata = 40
atq_rattata = 10
hp_arbok = 65
atq_arbok = 14
hp_charizard = 100
atq_charizard = 20

pocoes = 3
turno = 1
inimigo = 1

print("=== ARENA POKÉMON ===")
print("Escolha seu Pokémon:")
print("\n1 - 🌱 Bulbasaur: mais vida, menos ataque")
print("2 - 🔥 Charmander: menos vida, mais ataque")
print("3 - 💧 Squirtle: vida e ataque equilibrados")

pokemon = input("Escolha: ").strip().lower()

while pokemon not in (
    "1", "bulbasaur", "2", "charmander", "3", "squirtle"
):
    print("Pokémon inválido! Escreva o nome ou o número dele.")
    pokemon = input("Escolha: ").strip().lower()

if pokemon == "1" or pokemon == "bulbasaur":
    pokemon = "🌱 Bulbasaur"
    hp_maximo = 120
    atq_minimo = 12
    atq = 20

elif pokemon == "2" or pokemon == "charmander":
    pokemon = "🔥 Charmander"
    hp_maximo = 85
    atq_minimo = 18
    atq = 28

elif pokemon == "3" or pokemon == "squirtle":
    pokemon = "💧 Squirtle"
    hp_maximo = 100
    atq_minimo = 15
    atq = 24

hp = hp_maximo

print(f"Pokémon escolhido: {pokemon}")
print(f"❤️ HP: {hp}/{hp_maximo}")
print(f"⚔️ Ataque: {atq_minimo} a {atq}")
print(f"🧪 Poções: {pocoes}")

print("Você enfrentará Rattata, Arbok e Charizard!")
print("Você tem 3 poções para curar seu Pokémon no total.")
comecar = input("Começar batalha? [S/N] ").upper().strip()

if comecar == "S":
    print(f"\nInimigo {inimigo}: 🐀 Rattata")
    print(f"❤️ HP: {hp_rattata}")
    print(f"⚔️ Ataque: 5 a {atq_rattata}")

    while hp > 0 and hp_rattata > 0:
        print(f"\nTURNO: {turno}")
        print(f"{pokemon} | ❤️ Vida: {hp}/{hp_maximo}")
        print(f"🐀 Rattata | ❤️ Vida: {hp_rattata}")
        print(f"🧪 Poções: {pocoes}")
        print("[1] Atacar\n[2] Curar\n[3] Fugir")
        acao = input("Ação: ").strip().lower()

        if acao == "1" or acao == "atacar":
            dano = random.randint(atq_minimo, atq)
            hp_rattata -= dano
            print(f"{pokemon} causou {dano} de dano!")

        elif acao == "2" or acao == "curar":
            if hp >= hp_maximo:
                print("Seu Pokémon já está com vida máxima!")
                continue
            elif pocoes == 0:
                print("Você está sem poções!")
                continue
            else:
                hp += 35
                pocoes -= 1

                if hp > hp_maximo:
                    hp = hp_maximo

                print(f"Você se curou! Vida atual: {hp}")

        elif acao == "3" or acao == "fugir":
            print("🏃 Você fugiu da batalha...")
            break

        else:
            print("Ação inválida! Escolha entre Atacar, Curar ou Fugir!")
            continue

        if hp_rattata > 0:
            dano_inimigo = random.randint(5, atq_rattata)
            hp -= dano_inimigo
            print(f"Rattata causou {dano_inimigo} de dano!")

        turno += 1

    if hp <= 0:
        print(f"☠️ {pokemon} desmaiou! Você perdeu a batalha.")

    elif hp_rattata <= 0:
        hp += 20

        if hp > hp_maximo:
            hp = hp_maximo

        inimigo = 2
        print("\nRattata foi derrotado!")
        print(f"{pokemon} recuperou vida: {hp}/{hp_maximo}")
        print(f"Inimigo {inimigo}: 🐍 Arbok")
        print(f"❤️ HP: {hp_arbok}")
        print(f"⚔️ Ataque: 8 a {atq_arbok}")

        while hp > 0 and hp_arbok > 0:
            print(f"\nTURNO: {turno}")
            print(f"{pokemon} | ❤️ Vida: {hp}/{hp_maximo}")
            print(f"🐍 Arbok | ❤️ Vida: {hp_arbok}")
            print(f"🧪 Poções: {pocoes}")
            print("[1] Atacar\n[2] Curar\n[3] Fugir")
            acao = input("Ação: ").strip().lower()

            if acao == "1" or acao == "atacar":
                dano = random.randint(atq_minimo, atq)
                hp_arbok -= dano
                print(f"{pokemon} causou {dano} de dano!")

            elif acao == "2" or acao == "curar":
                if hp >= hp_maximo:
                    print("Seu Pokémon já está com vida máxima!")
                    continue
                elif pocoes == 0:
                    print("Você está sem poções!")
                    continue
                else:
                    hp += 35
                    pocoes -= 1

                    if hp > hp_maximo:
                        hp = hp_maximo

                    print(f"Você se curou! Vida atual: {hp}")

            elif acao == "3" or acao == "fugir":
                print("🏃 Você fugiu da batalha...")
                break

            else:
                print("Ação inválida! Escolha entre Atacar, Curar ou Fugir!")
                continue

            if hp_arbok > 0:
                dano_inimigo = random.randint(8, atq_arbok)
                hp -= dano_inimigo
                print(f"Arbok causou {dano_inimigo} de dano!")

            turno += 1

        if hp <= 0:
            print(f"☠️ {pokemon} desmaiou! Você perdeu a batalha.")

        elif hp_arbok <= 0:
            hp += 20

            if hp > hp_maximo:
                hp = hp_maximo

            inimigo = 3
            print("\nArbok foi derrotado!")
            print(f"{pokemon} recuperou vida: {hp}/{hp_maximo}")
            print(f"Inimigo {inimigo}: 🔥 Charizard")
            print(f"❤️ HP: {hp_charizard}")
            print(f"⚔️ Ataque: 12 a {atq_charizard}")

            while hp > 0 and hp_charizard > 0:
                print(f"\nTURNO: {turno}")
                print(f"{pokemon} | ❤️ Vida: {hp}/{hp_maximo}")
                print(f"🔥 Charizard | ❤️ Vida: {hp_charizard}")
                print(f"🧪 Poções: {pocoes}")
                print("[1] Atacar\n[2] Curar\n[3] Fugir")
                acao = input("Ação: ").strip().lower()

                if acao == "1" or acao == "atacar":
                    dano = random.randint(atq_minimo, atq)
                    hp_charizard -= dano
                    print(f"{pokemon} causou {dano} de dano!")

                elif acao == "2" or acao == "curar":
                    if hp >= hp_maximo:
                        print("Seu Pokémon já está com vida máxima!")
                        continue
                    elif pocoes == 0:
                        print("Você está sem poções!")
                        continue
                    else:
                        hp += 35
                        pocoes -= 1

                        if hp > hp_maximo:
                            hp = hp_maximo

                        print(f"Você se curou! Vida atual: {hp}")

                elif acao == "3" or acao == "fugir":
                    print("🏃 Você fugiu da batalha...")
                    break

                else:
                    print("Ação inválida! Escolha entre Atacar, Curar ou Fugir!")
                    continue

                if hp_charizard > 0:
                    dano_inimigo = random.randint(12, atq_charizard)
                    hp -= dano_inimigo
                    print(f"Charizard causou {dano_inimigo} de dano!")

                turno += 1

            if hp <= 0:
                print(f"☠️ {pokemon} desmaiou! Você perdeu a batalha.")

            elif hp_charizard <= 0:
                print(f"\n🏆 VITÓRIA! {pokemon} venceu todos os adversários!")
                print("🎉 Você conquistou o título de Campeão da Arena Pokémon!")
                print("❤️ A parceria entre vocês foi a chave dessa conquista!")