from threading import Semaphore, Thread
import time

#Variables
no = 0                                  # Customer no who gets hair cut
chairs = 2                              # Waiting Room chairs(n)
cust_count = 0
total_cust = 0

#Semaphores
semWakeup = Semaphore(0)                # For Waking the Barber when first customer arrives
semOnlyOne = Semaphore(1)               # For allowing only 1 Customer to have hair cut at a time
semstartcut= Semaphore(0)               # For Telling Barber to start the hair cut



def getHairCut():
    global cust_count,total_cust, no
    print("Customer",no," wants to get a haircut ans sits on the Barber chair")
    


def cutHair():
        print("Barber is cutting Customer",no ,"hair")
        

def balk():
        global cust_count,total_cust, no
        print("customer",total_cust," leaves due to non-empty chairs.")
        

#Barber
def barber():
    global chairs,cust_count, no
    while True:
        if cust_count == 0:                                     # No customers in shop 
            print("Barber is sleeping")                         # Barber is sleeping

            semWakeup.acquire()                                 # First Customer arrives 
            print("Barber is awake")                            # Barber wakes up

            while semstartcut.acquire():
                cutHair()                                       # Barber starts cutting the hair when a customer asks for hair cut
        break


#Customer
def customer():
    global chairs, cust_count, total_cust, no
    while True:
        total_cust = total_cust + 1
        #cust_queue.append(total_cust)
        if chairs!=0:                                           # If Waiting Chairs are empty
            cust_count = cust_count + 1                             # No of Customers
            chairs=chairs-1                                     # Customer occupies one chair                             
            if cust_count == 1:                                 # First Customer arrives
                print("The first customer is here!")
                semWakeup.release()                             # Customer wakes the Barber
                time.sleep(10)
                
                
            else:                                               # Second and onward Customers arrives 
                print("Customer",total_cust,"arrives and sits on waiting chair")          
                #break
                

            semOnlyOne.acquire()                                # Only 1 Customer can ask Barber for Haircut at a time
            no = no + 1                                         # Customer no to get haircut
            getHairCut()                                        # Asks the Barber for HairCut
            chairs = chairs + 1                                 # Customer sits on the Barber chair for hair cut and one waiting chair gets emptied
            semstartcut.release()                               # Tells the Barber to start the haircut
            time.sleep(10)
            print("Customer",no,"leaves shop after haircut.")   # Customer leaves after the Hair Cut
            semOnlyOne.release()                                # Now any other customer waiting can ask for the hair cut
            

            cust_count = cust_count-1                           # 1 Customer leaves the shop after hair cut
            if cust_count == 0:                                 # No customers in the shop
                print("All Customers leave the shop")
                print("Barber goes back")
                barber()

        else:
            balk()                                              # If Waiting Chairs are full
            
        break

t1 = Thread(target = barber)                                    # Barber
t1.start()

t2 = Thread(target = customer)                                  # Customer 1
t2.start()
t3= Thread(target = customer)                                   # Customer 2
t3.start()
t4= Thread(target = customer)                                   # Customer 3
t4.start()
t5=Thread(target = customer)                                    # Customer 4
t5.start()

    







