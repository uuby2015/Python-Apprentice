price=500
price2=200


def askUserWhichTask():
    answer=input("check in (1), check out (2)")
    return answer

def check_in():
    

while True :
    #ask the user what they want to do"
    # answer=input('do you want to check in or check out')
    # #depending on their choice:"

    # if answer=="check in":
    #     answer==input("do you want to be a premium member or a normal member")
    #     if answer=="premium member":
    #         print(f"premium member costs ${price} per night")
    #         input('what is your last name')
    #     if answer=='normal member':
    #         print(f"normal member costs ${price2} per night")
    #         answer=input("what is your last name")
    # if answer=='check out':
    #     answer==input('what is your last name')
    # if answer == 'quit':
    #     exit()

    task=askUserWhichTask()
    if task=="1":
        checkIn()
    if task=="2":
        checkout()

