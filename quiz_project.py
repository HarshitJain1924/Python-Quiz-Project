#Quiz Project
question={"About 36 and 42 islands make up New York City":"True",
          "Only one capital exists in South Africa.":"False",
          "The largest ocean in the world is the Atlantic Ocean.":"False",
          "The tallest mountain in the world is Mount Everest.":"True",
          "California is home to the “Desert of Death.”":"False",
          "Queen Elizabeth II has 3 children":"No",
          "13,171 miles is how far the Great Wall of China stretches in total.":"False",
          "The Mississippi and the Nile are the two longest rivers in the world.":"False",
          "The 31.5-mile-long Chunnel connects England and France.":"True",
          "The world largest island is Greenland.":"True"}

import random
quizqueslist=[]
while(len(quizqueslist)!=5):
    i=random.choice(list(question.keys()))
    if(i not in quizqueslist):
        quizqueslist.append(i)
score=0
print(""" 


        QUIZ GAME BEGIN!!! 
        
                            """)

for i in quizqueslist:
    print("\n"+i)
    a=input("\nEnter True or False: ")
    if(a==question[i]):
        print("\nRight answer! +10 points")
        score+=10
    else:
        print("\nWrong answer!")
print("\nTotal Score is :",score)