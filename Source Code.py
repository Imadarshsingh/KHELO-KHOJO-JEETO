positive=['yes','y','Y',"YES","Yes"]
negative=['no','n','N','No','NO']
def start():
        print("Let's Start!!")
        print("Would you like to try JUNGLE SAFARI?")
        ans=str(input(">>>"))
        def restart():
            print("\nWould you like to TRY Again??")
            ans=str(input(">>>"))
            if ans in positive:
                start()
            else:
                print("Thank You!!")
                print("See you Soon..🫡")
                print("We'll be waiting for you!!")
        if ans in positive:
            print("Welcome To JUNGLE SAFARI")
            print("You entered the jungle and after walking a mile, you found a small river passing by.")
            print("\nyou have to cross that river either by swimming or making temporary boat.")
            print("\nWould you like to Swim??")
            ans=str(input(">>>"))
            if ans in positive:
                print("Game Over!! You DIED as river was full of CROCODILES..")
                restart()
            else:
                print("Smart Choice..")
                print("You made the boat and crossed the river.")
                print("\nNow you're too close to your destination..After crossing the river,you walked another 2 miles of distance.")
                print("\nSuddenly you saw an old box lying in the bushes entitled with")  
                print("\nDANGER!! DO NOT OPEN❌❌..")
                print("\nWould you like to open it?")
                ans=str(input(">>>"))
                if ans in positive:
                    print("\nYou Won..🏆🏆")
                else: 
                    print("You ignored the stone and kept walking towards Jungle")
                    print("\nGAME OVER...YOU LOSE")
                    restart()
        else:
            print("Would you like to try DESERT SAFARI?")
            ans=str(input(">>>"))
            if ans in positive:
                print("Welcome To DESERT SAFARI")
                print("\nYou've entered the desert...Keep Walking until you find the stone..")
                print("\nYou've been walking since 2 hours...you saw two things..A village around 10 minutes away and a pond with some trees around.")
                print("\nWould you like to go towards village??")
                ans=str(input(">>>"))
                if ans in positive:
                    print("Smart Choice..You went to people of that village.They provided you food and water.")
                    print("\nYou again started the Journey,after walking a mile of distance")
                    print("\nYou found a palm tree")
                    print("\nWould you like to take rest?")
                    ans=str(input(">>>"))
                    if ans in positive:
                        print("\nCongratulation,You found the Stone in the box buried under the palm tree..")
                        print("\nYou Won..🏆🏆")
                        print()
                    else:
                        print("\nYou missed the Stone in the box buried under the palm tree.")
                        print("\nGAME OVER...YOU LOSE")
                        restart()
                else:
                    print("\nYou've been fooled..It was just a Mirage...Now You don't have enough energy to go to the Village")
                    print("\nGAME OVER!! You died due to lack of water in your body..")
                    restart()
            else:
                print("Sorry!! Currently only these TWO options are available.")
                restart()
print("Welcome TO KHELO KHOJO AUR JEETO")
instruct="""\nInstructions:
1. All you have to enter is yes/no. No other entries will be valid.
2. Only way to win game is finding that stone."""
print(instruct)
print("\nShall we Start?")
ans=str(input(">>>"))
if ans in positive:
    start()
elif ans in negative:
    print("You just missed a Thriller experience..☹️")
else:
    print("Invalid Input..❌❌")