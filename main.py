# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
number = int(input("Press Number something."))

if number > 5:
    print("X is more than 5.")
else:
    print("X is less than 5.")

#for
for i in range(5):
    print("Numbers now", i)

#range()
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)

def central_league(central_team):
    central_team = ["Tigers", "Bay stars", "Giants", "Dragons", "Carp", "Swallows"]
    for team in central_team:
        print(team)

def pacific_league(pacific_team):
    pacific_team = ["Hawks", "Fighters", "Buffallows", "Eagls", "Lions", "Marrines"]
    for team in pacific_team:
        print(team)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    name = input("What's your name?")
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    car = input("What do you want a wheel?")
    print(f'I want {car}')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    npb = input("Which do you know them?")
    for select in npb:
        if npb == "central":
            print(central_league('team'))
        elif npb == "pacific":
            print(pacific_league('team'))
        else:
            npb


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
