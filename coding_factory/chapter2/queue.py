"""Implimentation of a FIFO queue"""

import re
import time

def enqueue(queue, item):
    queue.append(item)

def dequeue(queue):
    if queue:
        return queue.pop(0)
    else:
        print("Queue is empty")

def menu_pacing():
    # Skip first call, to avoid slowing down initial menu display
    if not hasattr(flavor, "has_run"):  
        flavor.has_run = True 
        return
    
    # Add a short pause and newline on subsequent calls, to improve visual pacing
    time.sleep(0.5)
    print()

def print_menu():
    menu_pacing()  # Adds delay and spacing after the first menu render
    print("1. Insert in the back of the queue")
    print("2. Get from the front of the queue")
    print("q/Q for Quit\n")

def get_choice():
    return input("Please provide a choice: ").strip()

def is_valid_digit(choice):
    pattern = r'^\d$'
    return re.match(pattern, choice)

def is_valid_number(num):
    pattern = r'^[+-]?\d+$'
    return re.match(pattern, num)

def insert_number(queue):
    num = input("Please insert a num: ").strip()
    if not is_valid_number(num):
        print("Error in num")
        return
    num = int(num)
    enqueue(queue, num)
    print("Num inserted")

def get_from_queue(queue):
    out_num = dequeue(queue)
    if out_num is not None:
        print("You got:", out_num)

def handle_choice(choice, queue):
    match choice:
        case 1:
            insert_number(queue)
        case 2:
            get_from_queue(queue)
        case _:
            print("Choice not valid")

def main():
    queue =[]

    while True:
        print_menu()
        choice = get_choice()

        if choice.lower() == 'q':
            break

        if not is_valid_digit(choice):
            print("Error in choice")
            continue

        handle_choice(int(choice), queue)

    print("   ----- Goodbye -----   ")

if __name__ == '__main__':
    main()