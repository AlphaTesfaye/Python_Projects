name = input("Type your name: ")
print("Welcome", name, "to this adventure!!")

# Introduction
print("You find yourself standing at a crossroads in the middle of a dense forest.")
print("The path to the left leads into a dark and ominous cave, while the path to the right winds through a mysterious forest.")
print("Which path do you choose?")

# First choice: Left or Right
answer = input("Type 'left' to enter the cave or 'right' to explore the forest: ").lower()

if answer == "left":
    # Exploring the cave
    print("You cautiously enter the cave, feeling a chill run down your spine.")
    print("After what seems like hours of winding passages, you stumble upon a hidden chamber.")
    print("In the dim light, you see a gleaming treasure chest.")
    print("Do you open the chest or leave the cave?")
    
    # Second choice: Open the chest or Leave the cave
    answer2 = input("Type 'open' to open the chest or 'leave' to exit the cave: ").lower()
    
    if answer2 == "open":
        print("You open the chest and discover a priceless artifact! Congratulations, you win!")
    elif answer2 == "leave":
        print("You decide to leave the cave empty-handed. As you emerge into the sunlight, you hear a distant roar.")
        print("Perhaps it's best not to linger here for too long.")
        print("You continue on your journey.")
    else:
        print("Invalid choice. You stumble in the darkness and lose your way. Game over!")
        
elif answer == "right":
    # Exploring the forest
    print("You venture into the dense forest, the sound of rustling leaves and distant animal calls surrounding you.")
    print("As you walk deeper into the forest, you stumble upon a fork in the path.")
    print("Do you take the path leading uphill or downhill?")
    
    # Second choice: Uphill or Downhill
    answer3 = input("Type 'uphill' to take the path leading uphill or 'downhill' to take the path leading downhill: ").lower()
    
    if answer3 == "uphill":
        print("You climb the steep path, your muscles burning with exertion.")
        print("At the top, you're rewarded with a breathtaking view of the forest canopy stretching out before you.")
        print("You feel a sense of peace and tranquility wash over you. You continue your journey.")
    elif answer3 == "downhill":
        print("You descend into the shadowy depths of the forest, the air growing colder with each step.")
        print("Suddenly, you stumble upon a hidden glade, where a mystical creature awaits.")
        print("The creature offers you a choice: a magical boon or a dangerous curse.")
        
        # Third choice: Magical boon or Dangerous curse
        answer4 = input("Type 'boon' to accept the magical boon or 'curse' to accept the dangerous curse: ").lower()
        
        if answer4 == "boon":
            print("You accept the magical boon and feel a surge of power coursing through your veins.")
            print("With your newfound abilities, you journey forth, ready to face whatever challenges lie ahead.")
            print("Congratulations, you win!")
        elif answer4 == "curse":
            print("You accept the dangerous curse and feel its malevolent influence seeping into your soul.")
            print("As you stumble away from the glade, you realize too late the terrible mistake you've made.")
            print("The curse consumes you, and your journey comes to a tragic end. Game over!")
        else:
            print("Invalid choice. The creature grows impatient and vanishes into the shadows. You're left alone in the forest. Game over!")
    else:
        print("Invalid choice. You become hopelessly lost in the forest. Game over!")
        
else:
    print("Invalid choice. You hesitate at the crossroads, unable to make a decision.")
    print("As you stand there pondering your options, the sun sets and darkness falls.")
    print("You spend the night alone in the forest, shivering with fear.")
    print("When morning comes, you realize that you've wasted precious time.")
    print("You continue your journey, but the delay proves costly.")
    print("Your adventure ends in failure. Game over!")

print("Thank you for playing,", name)
