#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: april, 2025
# The program that accepts a whole number.
# It then uses a for loop to calculate and
# display the “square” (power of 2) starting
# from 0 until this number
def main():
    user_num_str = input("Enter a whole number: ")
    try:
        user_num = int(user_num_str)
        if user_num < 0:
            print(user_num, "is not positive")
        else:
            counter = 0
            while counter <= user_num:
                print(counter, "^2 =", counter * counter)
                counter += 1
            print("Thanks for playing")
    except:
        print(user_num_str, "is not an integer")


if __name__ == "__main__":
    main()
