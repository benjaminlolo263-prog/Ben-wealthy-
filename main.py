import random
import time

money = 1000
day = 1

businesses = {
    "1": {"name": "Lemonade Stand", "cost": 500, "profit": 100},
    "2": {"name": "Car Wash", "cost": 2000, "profit": 400},
    "3": {"name": "Tech Startup", "cost": 10000, "profit": 2500},
    "4": {"name": "Real Estate", "cost": 50000, "profit": 10000}
}

print("=== BEN-WEALTHY: BECOME A BILLIONAIRE ===")
print(f"You start with ${money}. Goal: $1,000,000,000")

while money < 1000000000:
    print(f"\n--- Day {day} ---")
    print(f"Your Money: ${money}")
    print("\n1. Work (earn $200)")
    print("2. Invest in Business")
    print("3. Take a Risk (50/50 double or nothing)")
    print("4. Check Status")
    print("5. Quit")
    
    choice = input("Choose 1-5: ")

    if choice == "1":
        earn = random.randint(150, 300)
        money += earn
        print(f"You worked and earned ${earn}!")

    elif choice == "2":
        print("\n--- Businesses ---")
        for k, v in businesses.items():
            print(f"{k}. {v['name']} - Cost: ${v['cost']} - Daily Profit: ${v['profit']}")
        b_choice = input("Which business to buy? (1-4): ")
        if b_choice in businesses:
            b = businesses[b_choice]
            if money >= b['cost']:
                money -= b['cost']
                money += b['profit']
                print(f"You bought {b['name']}! You got first profit of ${b['profit']}")
            else:
                print(f"Not enough money! You need ${b['cost']}")
        else:
            print("Invalid choice")

    elif choice == "3":
        risk = int(money * 0.3)
        print(f"You are risking ${risk}...")
        time.sleep(1)
        if random.choice([True, False]):
            money += risk
            print(f"YOU WIN! You now have ${money}")
        else:
            money -= risk
            print(f"You lost! You now have ${money}")

    elif choice == "4":
        print(f"\nWealth: ${money}")
        print(f"Progress to Billionaire: {money/1000000000*100:.6f}%")

    elif choice == "5":
        break

    if money <= 0:
        print("\nYou went broke! Game Over.")
        break

    day += 1

if money >= 1000000000:
    print(f"\nCONGRATULATIONS! You became a BILLIONAIRE in {day} days!!!")
