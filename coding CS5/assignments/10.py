#i recomment playing on fullscreen terminal where you can see ascii art properly

import random as r
import re

hangman = [
"""                  
    |___                 
    """,

"""
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,
    
"""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,
    
"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,

"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    """,

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    """,


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    """,


"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    """,



"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    """,


"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    """]

with open("slovnik.txt", "r", encoding="utf-8") as f:
    words = f.read().split("\n")

play = "yes"

while play == "yes":
    word = r.choice(words)

    while len(word.split(" ")) > 1:
        word = r.choice(words)

    guess = ["_"]*len(word)

    wrong = 0
    while "_" in guess:
        letter = input("What is your guessed letter? ")
        if len(re.findall(letter, word)) == 0:
            msg = hangman[wrong] + f"\nYour guess was bad, letter: {letter}"
            wrong += 1
            if wrong > len(hangman):
                print("You are done my friend, that was your last try")
                exit
        else:
            for i in re.finditer(letter, word):
                guess[i.start()] = letter
            msg = f"Your guess was good, letter: {letter}, guess: {''.join(guess)}"
        print(msg)

    print("!!! You've won !!!")
    print("""
                                        .
                . .                     -:-             .  .  .
                .'.:,'.        .  .  .     ' .           . \ | / .
                .'.;.`.       ._. ! ._.       \          .__\:/__.
                `,:.'         ._\!/_.                     .';`.      . ' .
                ,'             . ! .        ,.,      ..======..       .:.
                ,                 .         ._!_.     ||::: : | .        ',
        .====.,                  .           ;  .~.===: : : :|   ..===.
        |.::'||      .=====.,    ..=======.~,   |"|: :|::::::|   ||:::|=====|
    ___| :::|!__.,  |:::::|!_,   |: :: ::|"|l_l|"|:: |:;;:::|___!| ::|: : :|
    |: :|::: |:: |!__|; :: |: |===::: :: :|"||_||"| : |: :: :|: : |:: |:::::|
    |:::| _::|: :|:::|:===:|::|:::|:===F=:|"!/|\!"|::F|:====:|::_:|: :|::__:|
    !_[]![_]_!_[]![]_!_[__]![]![_]![_][I_]!//_:_\\![]I![_][_]!_[_]![]_!_[__]!
    -----------------------------------"---''''```---"-----------------------
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |= _ _:_ _ =| _ _ _ _ _ _ _ _ _ _ _ _
                                        |=    :    =|                Valkyrie
    _____________________________________L___________J________________________
    --------------------------------------------------------------------------    
    """)
    
    play = input("Do you want to play again (yes/no): ")
