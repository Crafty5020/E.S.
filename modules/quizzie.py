
def quiz():
    while True:
        try:
            creator = int(input("Enter 1 to use the creator or 2 if not(1, 2): "))
            if creator < 1 or creator  > 2:
                print("ERROR: value must be 1 or 2")
                continue
            break
        except ValueError:
            print("___________________________________________________________")
            print("ERROR: value must be an integer(a number without decimal point)")
            print("___________________________________________________________")
    
    if creator == 1:
        create()

def create():
    pass