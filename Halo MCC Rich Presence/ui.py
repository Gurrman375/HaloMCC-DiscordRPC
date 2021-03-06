import authenticate, Rich_Presence, removetoken, os, time, xbox, sys, ui, Debug
from os import system, name
os.system('color 2')

# UI strings that tell the user what to do
def UI():
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Halo: MCC Rich Presence")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("List: ")
    print("1. Create a Token")
    print("2. Launch the Rich Presence (Requires a Token)")
    print("3. Debug Rich Presenece (Heavy Debug)")
    print("4. Delete your Token")
    print("5. Exit")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Current Build: 0.2.7")
    print("Current issue might require you to type a number hit enter and repeat.")
    print("------------------------------------------------------------------------------------------------------------------------")
    selection = int(input("Select from list: "))
    return selection

# Conditional Tree for UI
def option(selection):
    try:
        if(selection == 1):
            clear()
            authenticate.main()
            clear()
            UI()
        elif(selection == 2):
            clear()
            Rich_Presence.main()
            clear()
            UI()
        elif(selection == 3):
            # clear()
            # Debug.main()
            print("Under construction. Please report on GitHub.")
            time.sleep(5)
            clear()
            UI()
        elif(selection == 4):
            clear()
            removetoken.main()
            clear()
            UI()
        elif(selection == 5):
            print("Goodbye")
            time.sleep(2)
            sys.exit(0)
        elif(selection == 6810511599111114100):
            print("The truth will be revealed one day but 8,311,111,111*10 is a fun number.")
            clear()
            UI()
        else:
            print("Invalid Input.")
            clear()
            UI()
            return selection
    except Exception as e:
        print(e)
        sys.exit(-1)

# The splash screen that you see when the program opens.
def splashScreen():
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Halo: MCC Rich Presence")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Created by kay-el-zed.")
    print("Maintained by Gurrman375D.")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Current Build: 0.2.7")
    print("------------------------------------------------------------------------------------------------------------------------")
    time.sleep(5)
    clear()

# This clears all the outputed strings within the console.
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    # MacOs support and Linux Support someday 
    else: 
        _ = system('clear')