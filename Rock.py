import random


Choices = ["rock","scessir","paper"]


tries=6
com_score=0
player_score=0


def score_counter():
    print (f"you choose: {player_choise} and the computer choose: {com_choise} \n points are:\n {com_score} for computer \n {player_score} for you ...")


var=True
while var==True:

    com_choise=random.choices(Choices)

    print(com_choise)
    player_choise_input=input("what is your choise? \nrock => press 1 \nscessir => press 2 \npaper => press 3 \n ....")
    player_choise =[]
    if player_choise_input == "1":
            player_choise= ["rock"]
    elif player_choise_input == "2":
            player_choise= ["scessir"]
    elif player_choise_input == "3":
            player_choise= ["paper"]
    else:
            print ("Not valied input:(" )
    
    print ( f"you choose :{player_choise}")
    
    if player_choise == com_choise:
        score_counter()
    elif player_choise == ["rock"]  :
        if com_choise ==["paper"]:
            com_score +=1
            score_counter()
        elif com_choise ==["scessir"]:
            player_score+=1
            score_counter()
    
    elif player_choise == ["paper"] :
        if com_choise ==["scessir"]:
            com_score +=1
            score_counter()
        elif com_choise ==["rock"]:
            player_score+=1
            score_counter()
    
    elif player_choise == ["scessir"]:
        if com_choise ==["rock"]:
            com_score +=1
            score_counter()
        elif com_choise ==["paper"]:
            player_score+=1
            score_counter()
            
    
    tries-=1
    if tries ==0 :
        var=False

if com_score>player_score:
    print (f"You lose😕 \n total score is:\n {com_score} for computer \n {player_score} for you:(")      

else:
    print (f"You Won😍 \n total score is:\n {com_score} for computer \n {player_score} for you:)") 
