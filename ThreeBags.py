import random
Bag =[ 10 , 10 , 10 ]
print(Bag)
user_plays=0
comp_plays=0
def remove(bag_no,items):
    new_bag=Bag[bag_no]-items
    Bag[bag_no]=new_bag
    return
def bag_is_empty(bag):
    if Bag[bag]== 0:
        return False
    else:
        return True
while Bag[0] !=0 or Bag[1] !=0 or Bag[2] !=0:
    bag_validity=False
    item_validity=False
    while bag_validity==False:
        while True:
            try:
                Bag_user=int(input("Choose a bag from 1 to 3: "))
            except Exception:
                print("Invalid number, sorry!")
            else:
                break
        Bag_user-=1
        if Bag_user != 0 and Bag_user !=1 and Bag_user !=2:
            print("incorrect bag!")
        elif Bag[Bag_user]==0:
            print("The bag choosen is out of items!")
        else:
            bag_validity=True
    while item_validity==False:
        while True:
            try:
                item_choosen=int(input("choose number of items from 0 to 5 from the bag: "))
            except Exception:
                print("Invalid number, sorry!")
            else:
                break
        if item_choosen<0 or item_choosen>5:
            print("Number of items should be between 1 to 5!")
        elif item_choosen>Bag[Bag_user]:
            print("choose number of items from the available in the bag!")
        else:
            item_validity=True 

    remove(Bag_user,item_choosen)
    print(f"you took {item_choosen} from bag {Bag_user+1}\n")
    print(Bag)
    user_plays+=1
    empty=False
    while not empty:
        bag_computer=random.randint(0,2)
        empty=bag_is_empty(bag_computer)
    if Bag[bag_computer]>5:
        items_choosen_computer=random.randint(1,5)
    else:
        items_choosen_computer=random.randint(1,Bag[bag_computer])
    remove(bag_computer,items_choosen_computer)
    print(f"Computer took {items_choosen_computer} from bag {bag_computer+1}\n")
    print(Bag)
    comp_plays+=1
    
if(comp_plays>=user_plays):
    print("The computer won!")
else:
    print("you won!") 
