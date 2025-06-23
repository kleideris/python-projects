"""Implimentation of a FIFO queue"""

import re
import time

queue = []
num = 0

def enqueue(list, item):
    list.append(item)

def dequeue(list):
    if list:
        return list.pop(0)
    else:
        print("Queue is empty")


def print_menu():
    flavor()  # adds delay and spacing after the menu after the first call.
    print("1. Insert in the back of the queue")
    print("2. Get from the front of the queue")
    print("q/Q for Quit")
    print()

def get_choice():
    return input("Please provide a choice: ")

def flavor():
    if not hasattr(flavor, "has_run"):
        flavor.has_run = True 
        return  # Skips the first call.
    
    # Logic that runs after the first call.
    time.sleep(0.5)
    print()


def main():
    choice = 0
    num = 0
    out_num = 0

    while True:
        print_menu()
        choice = get_choice()

        if choice == 'q' or choice == 'Q':
            break

        pattern = r'^\d$'
        match = re.match(pattern, choice)

        if not match:
            print("error in choice\n")
            continue

        choice = int(choice)
        match choice:
            case 1:
                num = input("Please insert a num: ")

                pattern = r'^\d+$'
                match = re.match(pattern, num)
                
                if not match:
                    print("Error in num")
                    continue

                num = int(num)
                enqueue(queue, num)
                print("Num inserted")            
            case 2:
                out_num = dequeue(queue)
                if out_num:
                    print("You got:", out_num)
            case _:
                print("Choice not valid")

    print("   ----- Goodbye -----   ")

if __name__ == '__main__':
    main()

