name = (input("Entre your name--->"))
age = int(input("Entre your age--->"))
question = input("What are you going to use it for ?")
def addhabit():
    while True:
        
        print(f"\n------- New Entry of",(name),"-------")
        habitname = input("Entre tasks name--> ")
        try:
           auto = input("Do you want to automate your exp in equel numbers")
           if auto == "yes":
               number = int(input("Entre total number of tasks ---> "))
               exp2 = 100/number
               exp = exp2   
           else:
               exp = (int(input("Entre the exp--> ")))
        except ValueError:
            print("you have entered wrong ")
            continue
        status = input("entre status(else press entre)---> ").lower
        if status == "":
            status = "active"
        with open("solotrackser.txt", "a") as f:
            f.write(f"{habitname},{exp},{status}\n")    
        with open("solotrackser.txt","a")as f:
         f.write(f"{habitname},{exp},{status}\n")
        choice = input("Do you want to add another task?")
        if choice !="yes":
                break
addhabit()
def totalexp ():
    total = 0
    with open("solotrackser.txt","r")as f:
        for line in f:
            data = line.split(",")
            if len(data) == 3 :
                exp_value = float(data[1])
                tasks_status = data[2].strip()
                if tasks_status == "done":
                   total = total + exp_value
    print(f"Your Total Power is: {total}")








