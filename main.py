#This code was a collaborative work between two students.

import random
#yay!!! ap comp sci 

#List of questions and answers for game
questionsListHard = [["Hangman","What game is this?"],
["Whale",	"Whats the biggest animal on earth?"],
["Red",	"Whats my favorite color?"],
["Fifty",	"Whats 25 plus 25?"],
["Jupiter",	"Which planet has the most gravity?"],
["Oysters",	"What animals are pearls found in?"],
["The skin", "What is the body's largest organ?"],
["Alaska", "Whats the largest American state (by area)?"],
["September",	"What month is labor day in?"],
["June or July", "People with the zodiac sign Cancer are born in..."],
["Five", "How many eyes does a bee have?"],
["Olympus", "What is the name of the home of the Greek Gods?"],
["Elephant",	"What is the largest land animal?"],
["Cats",	"What's better, cats or dogs?"],
["Eight",	"How many legs does a spider have?"],
["Michelangelo",	"Caravaggio shared a first name with what other famous artist?"],
["Stonefish",	"What is the world's most poisonous fish?"],
["John Adams",	"Who was the 2nd president of the USA?"],
["Pumice",	"What type of rock is lightweight and can float on water?"],
["Homo Erectus",	"Which human species survived for the longest in total?"]]
questionsListEasy = [["five", "What is 3 plus 2?"], ["Blue", "What color is the sky?"], ["Orange", "What color are oranges?"], ["Dog", "What kind of animal barks?"], ["No", "Does 10 plus 3 equal 12?"]]

def introduction():                  
  print(''' \\\                               =o)    
 (o>                              /\\\   
_(()_Dracula Guessing Game Challenge_\_V_ 
 //                                \\\  
                                    \\\ ''')
  print("Welcome to Dracula Guessing Game Challenge! To play, enter letters one at a time to answer the questions. Each time you get a letter wrong, Dracula gets closer... Don't let him get you! Have fun!")

def hangbot(i):
  if i == 0:
    print('''
                   ,-----,,,,  ,,,--------,__ 
                _-/|\\\/|\\\/|\\\\|\//\\\\//|/|//|\\\_  
               /|\/\//\\\\\\\\\\\\\\\\\\\\//////////////\\\\\\\  
             //|//           \\\\///            |\\\|\  
            ///|\/             \/               \|\|\  
           |/|//                                 |\\\\|\     
          |/|/                                    \|\|\    
          ///;    ,,=====,,,  ~~-~~  ,,,=====,,    ;|\|\ 
         |/|/   '"          `'     '"          "'   ;|\| 
         ||/`;   _--~~~~--__         __--~~~~--_   ;/|\| 
         /|||;  :  /       \~~-___-~~/       \  :  ;|\|   
         /\|;    -_\  (o)  / ,'; ;', \  (o)  /_-    ;|| 
         |\|;      ~-____--~'  ; ;  '~--____-~      ;\| 
          ||;            ,`   ;   ;   ',            ;|| 
        __|\ ;        ,'`    (  _  )    `',        ;/|__ 
    _,-~###\|/;    ,'`        ~~ ~~        `',    ;|\###~-,_ 
  ,'#########||;  '                           '  ;\|/#######`, 
 .############; ,         _--~~-~~--_           ;#############'.
,-' `;-,########;        ,; |_| | |_| ;,       ;;########,-;' `-,
      ;@`,######;       ;_| :%`~'~'%: |_;       ;######,'@;
       ;@@`,#####;     :%%`\/%%%%%%%\/'%%:     ;#####,'@@;
        ;@@@`,####;     :%%%%%%%%%%%%%%%;     ;####,'@@@;
         ;@@@@`,###;     ;./\_%%%%%_/\.;     ;####,@@@@;
      _-'@@@@@@@@;-~;     ~~--|~|~|--~~     ;~--;@@@@@@@'-_
  _,-'@@@@@@@@@@@@;  ;        ~~~~~        ;   ;@@@@@@@@@@@`-,_
,~@@@@@@@@@@@@@@@@@;  \`~--__         __--~/  ;@@@@@@@@@@@@@@@@~,
@@@@@@@@@@@@@@@@@@@@;   \   ~~-----~~    /   ;@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@~-_  \  /  |  \   /  _-~@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@~~-\/   |   \/ -~~@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@(=)=;==========;=(=)@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@;    |     ;@@@@@@@@@@@@@@@@@@@@@@@@@@''')
    #credits to spb, found at https://www.asciiart.eu/mythology/monsters
  if i == 1:
    print('''










         ||/`;   _--~~~~--__         __--~~~~--_   ;/|\| 
         /|||;  :  /       \~~-___-~~/       \  :  ;|\|   
         /\|;    -_\  (o)  / ,'; ;', \  (o)  /_-    ;|| 
         |\|;      ~-____--~'  ; ;  '~--____-~      ;\| 
          ||;            ,`   ;   ;   ',            ;|| 
        __|\ ;        ,'`    (  _  )    `',        ;/|__ 
    _,-~###\|/;    ,'`        ~~ ~~        `',    ;|\###~-,_ 
  ,'#########||;  '                           '  ;\|/#######`, 
 .############; ,         _--~~-~~--_           ;#############'.
,-' `;-,########;        ,; |_| | |_| ;,       ;;########,-;' `-,
      ;@`,######;       ;_| :%`~'~'%: |_;       ;######,'@;
       ;@@`,#####;     :%%`\/%%%%%%%\/'%%:     ;#####,'@@;
        ;@@@`,####;     :%%%%%%%%%%%%%%%;     ;####,'@@@;
         ;@@@@`,###;     ;./\_%%%%%_/\.;     ;####,@@@@;
      _-'@@@@@@@@;-~;     ~~--|~|~|--~~     ;~--;@@@@@@@'-_
  _,-'@@@@@@@@@@@@;  ;        ~~~~~        ;   ;@@@@@@@@@@@`-,_
,~@@@@@@@@@@@@@@@@@;  \`~--__         __--~/  ;@@@@@@@@@@@@@@@@~,
@@@@@@@@@@@@@@@@@@@@;   \   ~~-----~~    /   ;@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@~-_  \  /  |  \   /  _-~@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@~~-\/   |   \/ -~~@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@(=)=;==========;=(=)@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@;    |     ;@@@@@@@@@@@@@@@@@@@@@@@@@@
''')
  if i == 2:
    print('''














           ||;            ,`   ;   ;   ',            ;|| 
        __|\ ;        ,'`    (  _  )    `',        ;/|__ 
    _,-~###\|/;    ,'`        ~~ ~~        `',    ;|\###~-,_ 
  ,'#########||;  '                           '  ;\|/#######`, 
 .############; ,         _--~~-~~--_           ;#############'.
,-' `;-,########;        ,; |_| | |_| ;,       ;;########,-;' `-,
      ;@`,######;       ;_| :%`~'~'%: |_;       ;######,'@;
       ;@@`,#####;     :%%`\/%%%%%%%\/'%%:     ;#####,'@@;
        ;@@@`,####;     :%%%%%%%%%%%%%%%;     ;####,'@@@;
         ;@@@@`,###;     ;./\_%%%%%_/\.;     ;####,@@@@;
      _-'@@@@@@@@;-~;     ~~--|~|~|--~~     ;~--;@@@@@@@'-_
  _,-'@@@@@@@@@@@@;  ;        ~~~~~        ;   ;@@@@@@@@@@@`-,_
,~@@@@@@@@@@@@@@@@@;  \`~--__         __--~/  ;@@@@@@@@@@@@@@@@~,
@@@@@@@@@@@@@@@@@@@@;   \   ~~-----~~    /   ;@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@~-_  \  /  |  \   /  _-~@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@~~-\/   |   \/ -~~@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@(=)=;==========;=(=)@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@;    |     ;@@@@@@@@@@@@@@@@@@@@@@@@@@
''')
  if i == 3:
    print('''
,-' `;-,########;        ,; |_| | |_| ;,       ;;########,-;' `-,
      ;@`,######;       ;_| :%`~'~'%: |_;       ;######,'@;
       ;@@`,#####;     :%%`\/%%%%%%%\/'%%:     ;#####,'@@;
        ;@@@`,####;     :%%%%%%%%%%%%%%%;     ;####,'@@@;
         ;@@@@`,###;     ;./\_%%%%%_/\.;     ;####,@@@@;
      _-'@@@@@@@@;-~;     ~~--|~|~|--~~     ;~--;@@@@@@@'-_
  _,-'@@@@@@@@@@@@;  ;        ~~~~~        ;   ;@@@@@@@@@@@`-,_
,~@@@@@@@@@@@@@@@@@;  \`~--__         __--~/  ;@@@@@@@@@@@@@@@@~,
@@@@@@@@@@@@@@@@@@@@;   \   ~~-----~~    /   ;@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@~-_  \  /  |  \   /  _-~@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@~~-\/   |   \/ -~~@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@(=)=;==========;=(=)@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@;    |     ;@@@@@@@@@@@@@@@@@@@@@@@@@@
''')
  if i == 4:
    print('''

,~@@@@@@@@@@@@@@@@@;  \`~--__         __--~/  ;@@@@@@@@@@@@@@@@~,
@@@@@@@@@@@@@@@@@@@@;   \   ~~-----~~    /   ;@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@~-_  \  /  |  \   /  _-~@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@~~-\/   |   \/ -~~@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@(=)=;==========;=(=)@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@;    |     ;@@@@@@@@@@@@@@@@@@@@@@@@@@
''')
def menu():
  while True:
    print('{1.Start Game}{2.Quit}')
    user_choice = input("Enter 1 or 2: ")

    if user_choice == '1':
      #asks for difficulty level
      difficultyLevel = int(input("Choose a difficulty level [type 1 for easy mode, 2 for hard mode.]: "))
      #begins game
      if difficultyLevel == 1:
        game(questionsListEasy)
      elif difficultyLevel == 2:
        game(questionsListHard)
      else:
        print("Invalid choice. Try again.")

    elif user_choice == '2':
      #Quits the program
      print('''  
      |.---------.|
      ||         ||
      ||   Bye   ||
      ||         ||
      |'---------'|
       `)__ ____('
       [=== -- o ]--.
     __'---------'__ \ 
    [::::::::::: :::] )
     `""'"""""'""""`/T\ 
                    \_/ 
                    ''')
      #Art by Joan Stark found at https://www.asciiart.eu/computers/computers
      break      
    else:
      print("Please choose a valid option.")
#Check if user won
def win_check(line, word,score): 
  length = len(word)
  adding = 0
  #Go through all the guessed letters and see which ones match up with letters in the answer. Count up how many match. 
  for z in range(length):
    if line[z] == word[z]: 
      adding += 1
  #If all letters in the answer have been guessed, you win!
  if adding == length:
    print("You won!")
    print("your score is "+(str(score)))
    return True
#Check if user lost
def lose_check(wrong_guesses_left):
  if wrong_guesses_left == 0:
    print('better luck next time. Loser.')
    return True
#print out question
def question (words):
  print('\n*********************') 
  print('GUESTION: ' + (words[1]))
  print('*********************\n')
#This function runs the entirety of the game. Takes in list that questions and answers are being drawn from.
def game(words):
  i = random.randint(0,len(words)-1)  
  words = words[i] 
  words[0] = words[0].replace(" ", "") #remove every spaces in words
  question(words)
  words[0] = words[0].lower() #lower every letters to lowercase so that case doesn't matter

  wordAnswer = (list(words[0])) #list with real letters in each list

  emptyLineList = (list(words[0])) 
  for i in range(len(words[0])): 
    emptyLineList[i] = "__"  #This list contain lists with empty lines. Where the user's (correct) guesses will later go
  print(emptyLineList)
  
  wrong_guesses_left = 5 
  right_guesses = 0
  wrong = []

  
  while True:
    enter = input('[Wrong guesses left: '+ str(wrong_guesses_left)+'] '+'[Point: '+ str(right_guesses)+']'+' [Wrong guesses:'+(' '.join(word[0] for word in wrong))+ '] '+'\nGuess a letter: ')
    enter = enter.lower()
    right = 0 #place holder, will change if user inputted a right answer
    #Go through all the letters in the answer to check if the user guessed right
    for i in range(len(wordAnswer)):
      if wordAnswer[i] == enter: 
        right_guesses += 1 #add point
        right = right + 1 #plus 1 so the other if won't execute

        emptyLineList[i] = enter #replace the empty line at i with right letter
        print('\n') 
        print(emptyLineList) 
      elif i + 1 == len(wordAnswer) and right == 0: #at the end of list and no match
        wrong.append(enter) #add user's wrong guess in a list
        wrong_guesses_left -= 1 #reduce user's wrong tries left
        hangbot(wrong_guesses_left) #show animation
        print(emptyLineList) 

    #Check if user has won or lost yet
    if win_check(emptyLineList,wordAnswer,right_guesses) == True:
      break
    elif lose_check(wrong_guesses_left) == True:
      break

#Down here is where the program is actually run by calling these two functions!
introduction()
menu()