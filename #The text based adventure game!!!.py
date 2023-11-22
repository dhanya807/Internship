#The text based adventure game!!!


def The_mysterious_jungle():
    print("Your choice has brought you to the heart of the mysterious jungle."
          "Here's a crucial piece of advice: the jungle harbors dangerous creatures, and navigating through it `"
          "recklessly may lead to dire consequences. Choose your path wisely to ensure your survival.")
    print("Before you stands a massive banyan tree."
          "As you ascend, you discover two diverging paths:"
          "one smooth and promising, devoid of obstacles, while the other poses challenges but reveals traces of previous travelers."
          "Choose your route wisely.")
    a = input("Enter 1 to choose the smooth road and 2 to choose the challenging road:")
    
    if a == "1":
        print("You find yourself on a smooth road, but ahead lies a lake:"
              "However, a troop of elephants is currently quenching their thirst."
              "Exercise caution as they may pose a threat. Be careful!")
        print("You have two choices ahead of you: the first is to conceal yourself behind the large tree until the elephants depart,"
              " and the second is to quietly traverse alongside the lake.")
        b = input("Enter your choice, 1 or 2:")
        
        if b == "1":
            print("Wow, you made a right choice!! The elephants have left now. You can travel alongside the lake.")
            print("You seem hungry! Two choices awaits you: first one is to eat the fruit from the tree on your left, "
                  "second is to continue your journey, hesitating due to the suspicion that the fruit might be poisonous.")
            c = input("Enter your choice 1 or 2:")
            
            if c == "1":
                print("You decide to satisfy your hunger by plucking and eating the fruit from the tree on your left.")
                print("Invalid choice!! The fruit was poisonous!! You are dead......")
                exit()
            elif c == "2":
                print("You opt to continue your journey, choosing not to risk consuming the potentially poisonous fruit.")
                print("As you travel further, you encounter a mysterious figure offering a map that could lead to hidden treasures.")
                d = input("Do you accept the map? (Enter 1 for Yes, 2 for No): ")
                
                if d == "1":
                    print("You accept the map and gain valuable insights into the jungle's secrets. Your adventure continues.")
                    print("Following the map, you reach a mystical clearing with ancient ruins.")
                    print("You discover a hidden chamber that presents two passages: one leading to a forgotten treasure, and the other to an unknown danger.")
                    e = input("Enter 1 to explore the treasure, or 2 to face the unknown danger: ")

                    if e == "1":
                        print("You choose the path to the forgotten treasure and uncover riches beyond imagination.")
                        print("However, your presence triggers a guardian, and you must solve a riddle to escape unharmed.")
                        print("The riddle is:I'am orange,I wear a green hat and sound like a parrot.What am I?")
                        f = input("Enter your answer to the riddle: ")
            
                        if f.lower() == "carrot":
                            print("Congratulations! Your wisdom impresses the guardian, and you escape with the treasure.")
                            print("Your journey continues as a legendary adventurer in the mysterious jungle.")
                            exit()

                        else:
                            print("The guardian is displeased with your answer. You narrowly escape, leaving the treasure behind.")
                            print("Your adventure continues with lessons learned.")
                            exit()

                    elif e == "2":
                        print("You choose the path to the unknown danger, discovering a hidden civilization with unique customs.")
                        print("To proceed, you must participate in a ceremonial ritual. Choose your actions carefully.")
                        g = input("Enter 1 to observe quietly or 2 to actively participate: ")

                        if g == "1":
                            print("Your observant nature earns the respect of the civilization. They offer you guidance for your journey.")
                            print("Armed with newfound knowledge, you venture deeper into the jungle.")
                            exit()

                        elif g == "2":
                            print("Your active participation in the ritual impresses the civilization. They grant you a mystical artifact.")
                            print("The artifact provides protection as you face upcoming challenges in the mysterious jungle.")
                            exit()


                        else:
                            print("Invalid choice. The civilization is wary of your indecision. You must leave the area without further assistance.")
                            print("Your adventure continues with caution.")
                            exit()

                elif d == "2":
                    print("You decline the map, deciding to rely on your instincts alone. The journey becomes more challenging.")
                    print("As you navigate the jungle without the map, you encounter a dense fog. The atmosphere becomes unsettling.")
                    print("You must decide whether to press on through the fog or find an alternative route.")
                    h = input("Enter 1 to continue through the fog or 2 to search for an alternative route: ")

                    if h == "1":
                        print("You bravely press on through the fog, revealing a hidden portal to a mystical realm.")
                        print("This realm offers a shortcut, but it comes with unknown consequences. Enter at your own risk.")
                        i = input("Enter 1 to enter the portal or 2 to avoid it: ")

                        if i == "1":
                            print("You enter the mystical realm, experiencing a surreal journey that defies the laws of nature.")
                            print("Upon exiting, you find yourself closer to the heart of the mysterious jungle, but altered in unforeseen ways.")
                            print("Your adventure takes a surreal turn as you adapt to the mystical changes.")
                            exit()

                    elif h == "2":
                        print("You choose to avoid the portal, opting for a longer but safer route.")
                        print("The journey continues through the dense jungle, revealing more secrets and challenges along the way.")
                        exit()

            else:
                print("Invalid choice. Your indecision leaves you stuck in the fog. The jungle becomes denser, and your progress is hindered.")
                print("Your adventure continues with increased difficulty.")
                exit()

        elif b == "2":
            print("You decide to search for an alternative route, leading you to an ancient stone bridge.")
            print("The bridge appears fragile, and you must decide whether to cross it or find another way around.")
            j = input("Enter 1 to cross the bridge or 2 to find another way around: ")

            if j == "1":
                print("You cautiously cross the ancient stone bridge, successfully navigating its delicate structure.")
                print("On the other side, you uncover a hidden oasis with replenishing resources.")
                print("Your journey continues with newfound supplies and confidence.")
                exit()

            elif j == "2":
                print("You opt to find another way around the ancient stone bridge, discovering a perilous but rewarding path.")
                print("This detour leads you to a magnificent waterfall with healing properties.")
                print("Refreshed and invigorated, you forge ahead with renewed determination.")
                exit()

            else:
                print("Invalid choice. Your indecision leaves you stuck near the ancient stone bridge, unsure of the best course of action.")
                print("Your adventure continues with increased uncertainty.")
                exit()

        else:
            print("Invalid choice. The jungle becomes denser, and your progress is hindered.")
            print("Your adventure continues with increased difficulty.")
            exit()


    elif a == "2":
        print("You have chosen the challenging road!!")
        print("You encountered a nearby villager who has entered the forest for wood.")
        print("If you help him, he will provide you the map to travel out of the jungle. Otherwise, you have to follow your own road.")
        
        help_villager = input("Enter 1 to help the villager or 2 to follow your own road: ")
        
        if help_villager == "1":
            print("You decide to help the villager. In gratitude, he gives you a detailed map of the jungle.")
            print("With the map in hand, you navigate through the challenging terrain more efficiently.")
            print("Your journey becomes slightly easier as you follow the marked path on the map.")
        elif help_villager == "2":
            print("You choose to follow your own road, bravely facing the challenges that come your way.")
            print("Without a map, the journey becomes tougher, but you press on with determination.")
            print("Your adventure continues with self-reliance and courage.")
            exit()
        else:
            print("Invalid choice. The villager waits for your decision.")
            print("Your adventure continues with uncertainty.")
            exit()

    else:
        print("Invalid choice. The jungle becomes denser, and your progress is hindered.")
        print("Your adventure continues with increased difficulty.")
        exit()


name=input("Please enter your name:")
print(f"Hey {name}, Welcome to text based adventure game!!!")
print(name,"You awaken in a dense mist, disoriented and alone."
      "As the fog lifts you find yourself standing at a road which leads you to the forest"
"Choose your nextsteps wisely in the forest, as the journey ahead is shaped by your decisions.")

while True:
    choice=input("Enter 1 to continue: ")
    if choice == "1":
        The_mysterious_jungle()
    
    
    else:
        print("Your choice is invalid....")
        exit()


       
    