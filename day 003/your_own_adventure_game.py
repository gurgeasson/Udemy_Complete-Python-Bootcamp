yes_answer = ["Yes", "yes", "Y", "y", "igen"]
no_answer = ["No", "no", "N", "n", "nem"]

print(r'''
    __      ____ _ ___ _ __  
    \ \ /\ / / _` / __| '_ \ 
     \ V  V / (_| \__ \ |_) |
      \_/\_/ \__,_|___/ .__/ 
                      | |    
                      |_|   

         " ,  ,
            ", ,
               ""     _---.    ..;%%%;, .
                 "" .",  ,  .==% %%%%%%% ' .
                   "", %%%   =%% %%%%%%;  ; ;-_
                   %; %%%%%  .;%;%%%"%p ---; _  '-_
                   %; %%%%% __;%%;p/; O        --_ "-,_
                    q; %%% /v \;%p ;%%%%%;--__    "'-__'-._
                    //\\" // \  % ;%%%%%%%;',/%\_  __  "'-_'\_
                    \  / //   \/   ;%% %; %;/\%%%%;;;;\    "- _\
                       ,"             %;  %%;  %%;;'  ';%       -\-_
                  -=\="             __%    %%;_ |;;    %%%\          \
                                  _/ _=      \==_;;,_ %%%; % -_      /
                                 / /-          =%- ;%%%%; %%;  "--__/
                                //=             ==%-%%;  %; %
                                /             _=_-  d  ;%; ;%;  :F_P:
                                \            =,-"    d%%; ;%%;
                                            //        %  ;%%;
                                           //          d%%%"
                                            \           %%
                                                        V
      ''')
# https://ascii.co.uk/art/wasp
print("Welcome to the wasp garden, try to escape the wasps\n")
while True:
    if input("You are poking a wasps nest in the picturesque wasp garden." \
    " Do you want to hang around to see what happens? Yes/No: ") in no_answer:
        print("Good Choice.")
    else:
        print("You're in the hospital being treated for 1K+ wasp stings.")
        success = False
        break
    if input("You're making a hasty exist, but on your way out you " \
    "notice a £50 note in the grass. Pick it up? Yes/No: ") in no_answer:
        print("I agree, better not stop.")
    else:
        print("Oh no, it's monopoly money and the wasps got you.")
        success = False
        break
    final_choice = input("Now at the gate of the Wasp Graden, you can make your " \
    "final escape... but you just remembered, that you left your towel at the far " \
    "corner of the garden. Do you go back? Yes/No/Maybe/Sit down and think: ")
    if  final_choice in no_answer:
        print("You're out of the garden, safe now. Enjoy this cake.")
        success = True
    elif final_choice in yes_answer:
        print("You're crazy man.")
        success = False
    elif final_choice == "Maybe":
        print("Maybe the wasps got you.")
        success = False
    else:
        print("Too slow, you're dead.")
        success = False
    break
if success == False:
    print(r'''
                                               .""--.._
                                               []      `'--.._
                                               ||__           `'-,
                                             `)||_ ```'--..       \
                         _                    /|//}        ``--._  |
                      .'` `'.                /////}              `\/
                     /  .""".\              //{///
                    /  /_  _`\\            // `||
                    | |(_)(_)||          _//   ||
                    | |  /\  )|        _///\   ||
                    | |L====J |       / |/ |   ||
                   /  /'-..-' /    .'`  \  |   ||
                  /   |  :: | |_.-`      |  \  ||
                 /|   `\-::.| |          \   | ||
               /` `|   /    | |          |   / ||
             |`    \   |    / /          \  |  ||
            |       `\_|    |/      ,.__. \ |  ||
            /                     /`    `\ ||  ||
          ''')
else:
    print('''
           ,
        ___|___
       |: : : :|
     __|_______|__
          ''')
print("Game Over")
