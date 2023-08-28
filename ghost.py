import cyberpi
import time
import math, random

def pi_print(message):
    cyberpi.display.show_label(message, 16, int(8*0 + 5), int(17 * 0))

def run():
    pi_print("Hello World!")


def main():
    try:
        run()
    except Exception as e:
        cyberpi.display.show_label("Exeption on Mbot 2", 16, int(8 * 0 + 5), int(17 * 0))
        cyberpi.display.show_label(e, 16, int(8 * 0 + 5), int(17 * 1))
        raise
    #Ich mach nur einen Commit
    #Und jetzt einen Push
    #Hallo
main()
