import random
import time


global money

money = 100
past_numbers = []


while True:

    cost = int(input(f"Du har {money} mynt. Hur mycket vill du satsa? "))
    if cost <= 0 or cost > money:
        print("Ogiltigt vad.")
        continue
    money -= cost
    prize = cost * 10
    while True:
     play = input(f"input (X/x) om du vill kasta din tärning. (A/a) för att avsluta: ")
     if play.lower() == "x":
      for spinner in range(10):
        a = random.randint(1, 6)
        print(f" tärning\r{a}", end="", flush=True)
        time.sleep(0.15)

      print()
      past_numbers.append(a)
      total_numbers = sum(past_numbers)
      print(f"Du har totalt: {total_numbers}")
      
      if (total_numbers == 21):
       money += prize
       print(f"You won! Du fick {prize} och har nu {money} mynt")
       past_numbers = []
       break

      elif (total_numbers > 21):
       print("You lost")
       past_numbers = []
       break

     elif play.lower() == "a":
        try:
            print(f"Fegis du fick bara {total_numbers}.")
            back = int(cost / total_numbers)
            money += back
            print(f"Du får tillbaka {back} mynt")
            past_numbers = []
            break
        except NameError:
          back = int(cost)
          money += back
          print(f"Du får tillbaka {back} mynt")
          break
     
     else:
       continue