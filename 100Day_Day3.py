has_key = False
has_machete =  False

print('''
   ..=*#*=:......                                 
   .-=**=-:-=-=+**=:.....                         
  ..=++++++++===+------+##+-:......               
  .:##+=---::=+=:=-=======:-:::-*##*=::...        
      .#@@@@@%+#++*+=+=-=-==+-==+-:-:::-----...   
        ..*@@@@@@@@@%*=-:-.:-==+==+:-===++=*=-.   
       ...-#@@@@@@%%%%%@@@@%*=----:::=++#**##==:  
   ..:=%%%@@@@@@@@%%###%##%%%%@@@@%*++=++*#*#%+=..
.:*%@%%%%%%@@@@%@%#%%%%%%%%%%%%%%%%%%%*==+##*##+=.
.:=-=*#@%%%%%%%%%%#%#%%%%%%%%%%%%%%%#%%%%*=+***+=.
.:+**+=-:-=*#%@@@%#%%%%%##%%%%%%%%%%%%%%%%%+==**..
.:+*++++**+==:-=+##%%%%%%%%%%%%%%%%%%%%%*=+###*-  
..=+*####++*+***+=-::-+*#%%%%%%%%%%%%*==*%####=.  
..=***####********+++*+=--:-=#%@@%#=-+##*###*+-   
 .=***++****+::++****+++*****==-:-+*#*###**+++:   
..-+++****+++.-+==##**##**++***:-=***#**++****:   
..:==+++++**#*=++=+***#+****##*-==#*+++++****+.   
 ..:---++======+*%***++********:====++***#**+=.   
     ...::-=++====++*###**++**+:==++*####*+=-..   
        ....:-:-======+=*#*#**+:-=*#****+=:..     
              ...::-====+++++++:-+****+-:.        
                 ....:::-=++*=+--+**+-:..         
                       ...:---=--=--...           
                         .....-::-..
Welcome to Treasure Island!
You must find the treasure and leave before nightfall, else the curse will never let you leave!
''')
while True:
    startDirection = input('''
Which way do you travel?
Forward is a thick jungle 
Left will take you along the beach 
Right will take you along the beach in the other direction 
Forward, Left, or Right?\n''')

    if startDirection == 'Forward':
        pathSplitDirection = input('''You venture into the dense forest and the path splits.
        Which direct will you take? Forward or Left?\n''')
        if pathSplitDirection == 'Forward' and has_machete == True:
            path2Direction = input("You found some ruins, search or go back?\n")
            if path2Direction == 'search' and has_key == True:
                print('''You find a chest and unlock it, finding more gold than you could ever spend.
                Congrats, you are rich.''')
                break
            elif path2Direction == 'search' and has_key == False:
                print('''You find a chest, but its locked. There must be a key somewhere.
                You waste too much time looking around the ruins, night falls. 
                You curse the developer for being too lazy to allow you to path back as you lose''')
                break
        elif pathSplitDirection == 'Forward' and has_machete == False:
            print("You get lost and night falls, you lose.")
            break
        elif pathSplitDirection == 'Left':
            print("You fall into a quicksand pit and cant make it out, you lose")
            break

    elif startDirection == 'Left':
        print("You find a key buried in the sand")
        has_key = True

    elif startDirection == 'Right':
        print("You find a machete buried in the sand")
        has_machete = True

    else:
        print('''That probably wasnt an option, or the dev was too lazy to allow lowercase input.
        Try again''')