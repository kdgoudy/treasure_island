print('''
    ___ __ 
   (_  ( . ) )__                  '.    \   :   /    .'
     '(___(_____)      __           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|/_/__      -----____   _  _____-----
_______________''.--o/___  \_______________(_)___________
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     ___|_||_____     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..:: ......
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~
   ~                  ~    ~ ~                 ~''')
print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')
choice1 = input('You are at a crossroads, where do you want to go? Type "left" or "right" ').lower()

if choice1 == "left":
    choice2 = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ').lower()
        if choice3 == "red":
            print("The room is full of fire. Game over.")
        elif choice3 == "yellow":
            print("You found the treasure! You win.")
        elif choice3 == "blue":
            print("You enter a room full of beasts. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        print('You got attacked by angry fish. Game over')
else:
    print("You fell into a hole. Game over.")