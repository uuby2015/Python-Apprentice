price=500
price2=200


def askUserWhichTask():
    answer=input("check in (1), check out (2)")
    return answer

def check_in():

    answer==input("do you want to be a premium member or a normal member")
    if answer=="premium member":
        print(f"premium member costs ${price} per night")
        input('what is your last name')
    if answer=='normal member':
        print(f"normal member costs ${price2} per night")
        answer=input("what is your last name")
  
def checkout():
    pass



while True :
    task=askUserWhichTask()
    if task=="1":
        check_in()
    if task=="2":
        checkout()

