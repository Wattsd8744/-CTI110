#DariusWatts
#05/13/2026
#finalexamproject
#MyRhythmgame
#withthehelpofAICHATGPT

import random
import time

def main():
 while True:
    print("Welcome to my rhythm game, totally not a budget cut rhythm heaven without music!")
    print("\n==========================================")
    print("       ~ T E X T  H E A V E N ~")
    print("==========================================")
    print("  Watch: 1 ... 2 ... 3 ... then HIT!")
    print("  3 Misses and it's Game Over!")

    player = {
       "score": 0,
       "combo": 0,
       "misses": 0
       }
    time.sleep(1)
    print("1")

    time.sleep(1)

    print("2")

    time.sleep(1)

    print("3")
    
    letters = ["A", "B", "C"]

    while player ["misses"] < 3:

     time.sleep(random.uniform(0.5, 2.0)) 
     start_time = time.time()
     note = random.choice(letters) 
     print("!>>>HIT:", note,"<<<<!")

     player_input = input("Your key: ").upper()
     end_time = time.time()

     reaction = end_time - start_time
     time_limit = 2.5 - (player["misses"] - 0.1)
       
     if player_input == note:
      
      if reaction > time_limit:
        print("Miss!")
        player["misses"] += 1
        player["combo"] = 0

      elif reaction <= 0.5:
        print("Perfect!")
        player["score"] +=300
        player["combo"] += 1

      elif reaction <= 1.0:
        print("Cool!")
        player["score"] += 200
        player["combo"] += 1

      elif reaction <= time_limit:
        print("Good!")
        player["score"] += 100
        player["combo"] += 1

      else:
        print("Late...")
        player["score"] += 50
        player["combo"] += 1
    

     else:
       print("miss!")
       player["misses"] += 1
       player["combo"] = 0 
         
       print("Score:", player["score"], 
      "| Combo:", player["combo"], 
      "| Misses:", player["misses"])
       
    if player["score"] >= 2000 and player["misses"] == 0:
        rank = "S"
    elif player["score"] >= 1500:
        rank = "A"
    elif player["score"] >= 1000:
        rank = "B"
    else:
        rank = "C"

    choice = input("\nPlay again? (Y/N): ").upper()
    if choice != "Y":
     print("Thanks for playing!")
     break
    print("Game Over! You missed 3 times.")
    print("Final Score:", player["score"])
main()
