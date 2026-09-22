import json
import os
import time
# ANSI colors - work on all phones/terminals
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

SAVE_FILE = "wealthy_save.json"

businesses = {
    "1": {"name": "Lemonade Stand", "cost": 500, "profit": 80, "emoji": "🍋"},
    "2": {"name": "Car Wash", "cost": 2000, "profit": 350, "emoji": "🚗"},
    "3": {"name": "Food Truck", "cost": 5000, "profit": 900, "emoji": "🍔"},
    "4": {"name": "Mini Mart", "cost": 15000, "profit": 2500, "emoji": "🏪"},
    "5": {"name": "Tech Startup", "cost": 50000, "profit": 8000, "emoji": "💻"},
    "6": {"name": "Real Estate", "cost": 150000, "profit": 25000, "emoji": "🏠"},
    "7": {"name": "Luxury Cars", "cost": 500000, "profit": 70000, "emoji": "🏎️"},
    "8": {"name": "Private Jet Rental", "cost": 2000000, "profit": 300000, "emoji": "✈️"},
    "9": {"name": "Oil Company", "cost": 10000000, "profit": 1500000, "emoji": "🛢️"},
    "10": {"name": "SpaceX Competitor", "cost": 50000000, "profit": 10000000, "emoji": "🚀"}
}

def load_game():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)
                return data["money"], data["day"], data["owned"]
        except:
            pass
    return 1000, 1, []

def save_game(money, day, owned):
    with open(SAVE_FILE, "w") as f:
        json.dump({"money": money, "day": day, "owned": owned}, f)

money, day, owned = load_game()

print(f"{CYAN}{BOLD}========================================{RESET}")
print(f"{CYAN}{BOLD} BEN-WEALTHY TYCOON - BECOME A BILLIONAIRE {RESET}")
print(f"{CYAN}{BOLD}========================================{RESET}")
if day > 1:
    print(f"{YELLOW}Welcome back! Loaded your save - Day {day}, ${money:,}{RESET}")
else:
    print(f"You start with ${money:,}. Goal: {GREEN}$1,000,000,000{RESET}")
    print("Build your empire from Lemonade to Rockets!")
time.sleep(1)

while money < 1000000000:
    daily_income = sum([businesses[str(b)]["profit"] for b in owned]) if owned else 0
    if daily_income > 0 and day > 1:
        money += daily_income

    print(f"\n{BOLD}--- Day {day} | Cash: {GREEN}${money:,}{RESET}{BOLD} | Daily Income: ${daily_income:,}/day ---{RESET}")
    if owned:
        print(f"Owned: {', '.join([businesses[str(b)]['emoji']+businesses[str(b)]['name'] for b in owned])}")

    print(f"""
{YELLOW}1.{RESET} Work Hard (earn $200-$500)
{YELLOW}2.{RESET} Buy Business
{YELLOW}3.{RESET} Take Risk (30% of cash, 50/50 double or lose)
{YELLOW}4.{RESET} My Empire & Progress
{YELLOW}5.{RESET} Save & Quit
    """)

    choice = input(f"{BOLD}Choose (1-5): {RESET}").strip()

    if choice == "1":
        import random
        earn = random.randint(200, 500)
        money += earn
        print(f"{GREEN}You hustled hard and earned ${earn}!{RESET}")

    elif choice == "2":
        print(f"\n{BOLD}--- BUSINESS MARKET ---{RESET}")
        for k, v in businesses.items():
            owned_mark = f"{GREEN}[OWNED]{RESET}" if int(k) in owned or k in [str(x) for x in owned] else ""
            print(f"{YELLOW}{k}.{RESET} {v['emoji']} {v['name']} - Cost: ${v['cost']:,} - Profit: ${v['profit']:,}/day {owned_mark}")
        b_choice = input("Buy which? (1-10) or 0 to cancel: ").strip()
        if b_choice in businesses:
            b = businesses[b_choice]
            if int(b_choice) in owned:
                print(f"{RED}You already own this!{RESET}")
            elif money >= b['cost']:
                money -= b['cost']
                owned.append(int(b_choice))
                print(f"{GREEN}SUCCESS! You bought {b['emoji']} {b['name']} for ${b['cost']:,}!{RESET}")
            else:
                print(f"{RED}Not enough money! Need ${b['cost']:,}, you have ${money:,}{RESET}")
        elif b_choice!= "0":
            print("Invalid choice")

    elif choice == "3":
        if money < 100:
            print(f"{RED}You need at least $100 to take a risk!{RESET}")
            continue
        import random
        risk = int(money * 0.3)
        print(f"{RED}You are risking ${risk:,}...{RESET}")
        time.sleep(1.2)
        if random.choice([True][False]):
            money += risk
            print(f"{GREEN}JACKPOT! YOU WIN! You now have ${money:,}{RESET}")
        else:
            money -= risk
            print(f"{RED}You lost ${risk:,}... You now have ${money:,}{RESET}")

    elif choice == "4":
        progress = money / 1000000000 * 100
        print(f"\n{BOLD}YOUR EMPIRE:{RESET}")
        print(f"Cash: ${money:,}")
        print(f"Daily Passive Income: ${daily_income:,}")
        print(f"Businesses Owned: {len(owned)}/10")
        print(f"Progress to Billionaire: {GREEN}{progress:.6f}%{RESET}")
        print(f"Days Played: {day}")
        bar = int(progress/2) if progress < 50 else 25
        print(f"Progress: [{'#'*bar}{'-'*(50-bar)}]")

    elif choice == "5":
        save_game(money, day, owned)
        print(f"{YELLOW}Game saved! Come back tomorrow. Your empire awaits.{RESET}")
        break

    else:
        print("Invalid, choose 1-5")
        continue

    if money <= 0:
        print(f"\n{RED}{BOLD}You went broke! Game Over. But hustlers bounce back! Restarting with $1000...{RESET}")
        money = 1000
        owned = []
        save_game(money, day, owned)

    save_game(money, day, owned)
    day += 1
    time.sleep(0.5)

if money >= 1000000000:
    print(f"\n{GREEN}{BOLD}========================================{RESET}")
    print(f"{GREEN}{BOLD} CONGRATULATIONS!!! YOU ARE A BILLIONAIRE!!! {RESET}")
    print(f"{GREEN}{BOLD} You did it in {day} days with ${money:,}!{RESET}")
    print(f"{GREEN}{BOLD} Welcome to the Billionaire Club! {RESET}")
    print(f"{GREEN}{BOLD}========================================{RESET}")
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)
