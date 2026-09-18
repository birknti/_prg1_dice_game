import random
import time


global Money

money = 100


while True:

 play = input(f"input (X/x) om du vill kasta din första tärning: ")
 if play.lower() == "x":
    cost = int(input(f"Du har {money} mynt. Hur mycket vill du satsa? "))
    if cost <= 0 or cost > money:
        print("Ogiltigt vad.")
        continue
    money -= cost
    prize = cost * 10
    for spinner in range(10):
        a = random.randint(1, 6)
        print(f" tärning\r{a}", end="", flush=True)
        time.sleep(0.15)

    print()

 else:
     continue

 print(f"Du har slagit {a}")

 play = input("input (X/x) om du vill kasta din tärning. (A/a) om du vill avsluta: ")
 if play.lower() == "x":
    for spinner in range(10):
        b = random.randint(1, 6)
        print(f" tärning\r{b}", end="", flush=True)
        time.sleep(0.15)

    print()

 elif play.lower() == "a":
    print(f"Fegis du fick bara {a}.")
    continue

 else:
     continue

 print(f"Du har slagit {a + b}")


 play = input("input (X/x) om du vill kasta din tärning. (A/a) om du vill avsluta: ")
 if play.lower() == "x":
    for spinner in range(10):
        c = random.randint(1, 6)
        print(f" tärning\r{c}", end="", flush=True)
        time.sleep(0.15)

    print()

 elif play.lower() == "a":
    print(f"Fegis du fick bara {a + b}.")
    continue


 else:
     continue

 print(f"Du har slagit {a + b + c}")

 play = input("input (X/x) om du vill kasta din tärning. (A/a) om du vill avsluta: ")
 if play.lower() == "x":
    for spinner in range(10):
        d = random.randint(1, 6)
        print(f" tärning\r{d}", end="", flush=True)
        time.sleep(0.15)

    print()

 elif play.lower() == "a":
    print(f"Fegis du fick bara {a + b + c}.")
    continue


 else:
     continue

 print(f"Du har slagit {a + b + c + d}")
 if (a + b + c + d == 21):
     money += prize
     print(f"You won! Du fick {prize} och har nu {money} mynt")

 elif (a + b + c + d > 21):
    print("You lost")

 play = input("input (X/x) om du vill kasta din tärning. (A/a) om du vill avsluta: ")
 if play.lower() == "x":
    for spinner in range(10):
        e = random.randint(1, 6)
        print(f" tärning\r{e}", end="", flush=True)
        time.sleep(0.15)

    print()

 elif play.lower() == "a":
    print(f"Fegis du fick bara {a + b + c + d}.")
    continue


 else:
     continue

 print(f"Du har slagit {a + b + c + d + e}")
 if (a + b + c + d + e == 21):
     money += prize
     print(f"You won! Du fick {prize} och har nu {money} mynt")

 elif (a + b + c + d + e > 21):
     print("You lost")

 play = input("input (X/x) om du vill kasta din tärning. (A/a) om du vill avsluta: ")
 if play.lower() == "x":
     for spinner in range(10):
         f = random.randint(1, 6)
         print(f" tärning\r{f}", end="", flush=True)
         time.sleep(0.15)
 
     print()
 
 elif play.lower() == "a":
     print(f"Fegis du fick bara {a + b + c + d + e}.")
     continue
 
 
 else:
      continue
 
 print(f"Du har slagit {a + b + c + d + e + f}")
 if (a + b + c + d + e + f== 21):
      money += prize
      print(f"You won! Du fick {prize} och har nu {money} mynt")
 
 elif (a + b + c + d + e + f > 21):
      print("You lost")

 play = input("input (X/x) om du vill kasta din tärning. (A/a) om du vill avsluta: ")
 if play.lower() == "x":
     for spinner in range(10):
         g = random.randint(1, 6)
         print(f" tärning\r{g}", end="", flush=True)
         time.sleep(0.15)
 
     print()
 
 elif play.lower() == "a":
     print(f"Fegis du fick bara {a + b + c + d + e + f}.")
     back = int(cost / a + b + c + d + e + f)
     money += back
     print(f"Du får tillbaka {back} mynt")
     continue
 
 
 else:
      continue
 
 print(f"Du har slagit {a + b + c + d + e + f + g}")
 if (a + b + c + d + e + f + g == 21):
      money += prize
      print(f"You won! Du fick {prize} och har nu {money} mynt")
 
 else:
      print(f"You lost! Du tappa {cost} mynt")
      continue
