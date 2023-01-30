import random

def main():
    print("Welcome to the fight game!")
    player_health = 100
    player_attack = random.randint(20, 30)
    player_defense = random.randint(10, 20)
    player_healing = 30
    player_special_attack = 50
    player_magic = 100

    enemy_health = 100
    enemy_attack = random.randint(10, 20)
    enemy_defense = random.randint(5, 10)
    enemy_special_attack = 70
    enemy_magic = 80

    while player_health > 0 and enemy_health > 0:
        player_choice = input("Do you want to attack, defend, heal, or use special attack? ")
        if player_choice.lower() == "attack":
            enemy_health -= player_attack
            print(f"You attacked and dealt {player_attack} damage. Enemy health is now {enemy_health}")
        elif player_choice.lower() == "defend":
            player_defense += 5
            print(f"You defend and increase defense by 5. Defense is now {player_defense}")
        elif player_choice.lower() == "heal":
            player_health += player_healing
            print(f"You heal and increase health by {player_healing}. Health is now {player_health}")
        elif player_choice.lower() == "use special attack":
            if player_magic >= 20:
                player_magic -= 20
                enemy_health -= player_special_attack
                print(f"You used special attack and dealt {player_special_attack} damage. Enemy health is now {enemy_health}")
                print(f"Your magic value is now {player_magic}")
            else:
                print("You don't have enough magic value to use the special attack.")
        
        enemy_choice = random.choice(["attack", "defend", "use special attack"])
        if enemy_choice == "attack":
            player_health -= enemy_attack
            print(f"Enemy attacked and dealt {enemy_attack} damage. Your health is now {player_health}")
        elif enemy_choice == "defend":
            enemy_defense += 5
            print(f"Enemy defends and increase defense by 5. Defense is now {enemy_defense}")
        else:
            if enemy_magic >= 20:
                enemy_magic -= 20
                player_health -= enemy_special_attack
                print(f"Enemy used special attack and dealt {enemy_special_attack} damage. Your health is now {player_health}")
                print(f"Enemy's magic value is now {enemy_magic}")
            else:
                print("Enemy doesn't have enough magic value to use the special attack.")
    
    if player_health <= 0:
        print("You lost the fight")
    else:
        print("You won the fight")

if __name__ == "__main__":
    main()