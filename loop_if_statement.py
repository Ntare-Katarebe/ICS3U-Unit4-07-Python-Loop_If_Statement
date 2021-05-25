#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program prints the RGB
#    with numbers inputted from the user


def main():
    # This function prints the RGB

    # process & output
    for num in range(1001, 2000 + 2):
        if num % 5 == 0:
            print(num - 1)
        else:
            print(num - 1, end=" ")


if __name__ == "__main__":
    main()
