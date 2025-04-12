def fun():
    x=guess.get()
    final_score.set(score.get())
    if score.get()>0:
 
        if x > 20 or x<0:
            hint.set("You just lost 1 Chance")
            score.set(score.get()-1)
            final_score.set(score.get())
   
        elif num==x:
            hint.set("Congratulation YOU WON!!!")
            score.set(score.get()-1)
            final_score.set(score.get())
     
        elif num > x:
            hint.set("Your guess was too low: Guess a number higher ")
            score.set(score.get()-1)
            final_score.set(score.get())
        elif num < x:
            hint.set("Your guess was too High: Guess a number Lower ")
            score.set(score.get()-1)
            final_score.set(score.get())
    else:
         hint.set("Game Over You Lost")