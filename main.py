# First attempt at an Advice Application using a free API.

import json, requests
from time import sleep

print("Welcome to Alex Shegstad's Advice Application!\n")
name = input("What is  your name? ")
url = "https://api.adviceslip.com/advice"

sleep(2.5)
print(f"Retrieving advice from {url}")
print()
sleep(2.5)
print()
print("Thank you for your patience...")
print("\n")



def display_advice(unformatted_data):

    # response = requests.get(url)
    # unformatted_data = response.json()

    print(unformatted_data)

def main():
    # Obtain information to display to guest

    response = requests.get(url)
    advice: any = response.json()


    adviceID = advice["slip"]["id"]
    pieceOfAdvice = advice["slip"]["advice"]
    print(f"Okay, listen up, {name}...")
    print()
    sleep(3)
    print()
    print(f"Bit of advice #{adviceID} :")
    print()
    sleep(1)
    print()
    print(pieceOfAdvice)

main()
