from time import sleep


def raspberry(rasber: int):
    print('Hello and I have a question. How did you find the code to enter raspberry mode?')
    sleep(0.5)
    print("Well right now I dont have any of those stuff and well can't finish raspberry mode.")
    sleep(0.5)
    print("ill put you back to the main menu")
    sleep(0.2)
    import src.modules.main as main
    main.start()