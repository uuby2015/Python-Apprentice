premium_price=500
normal_price=200
taken={}
avail_rooms=[1,2,3,4,5]

def askUserWhichTask():
    answer=input("check in (1), check out (2)")
    return answer

def check_in():

    rate=input("do you want to be a premium member or a normal member")
    if rate=="premium member":
        print(f"premium member costs ${premium_price} per night")
        nightlyCost = premium_price
    if rate=='normal member':
        print(f"normal member costs ${normal_price} per night")
        nightlyCost = normal_price
    name=input("what is your last name")
    number_of_nights=int(input("how long do you want to stay"))


    taken[1]=[name,number_of_nights,nightlyCost]
    # store the info for this guest's reservation in the hotel's reservation dictionary
  
def checkout():
    



while True :
    task=askUserWhichTask()
    if task=="1":
        check_in()
        print(taken)


    if task=="2":
        checkout()
        