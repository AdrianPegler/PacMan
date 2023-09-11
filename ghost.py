import cyberpi
import time
import math, random
#Das ist mein Branch!!
#Sendet eine Nachricht an den CyberPi-Display
def pi_print(message):
    cyberpi.display.show_label(message, 16, int(8*0 + 5), int(17 * 0))

#Hier kommt alles rein, was der Pi / mBot ausführen soll
def run():
    pi_print("Hello World!")
    
def hello():
    pi_print("Hello from the other side")

#Vom Pi vorgegebene Main-Funktion
def main():
    try:
        run()
    except Exception as e:
        cyberpi.display.show_label("Exeption on Mbot 2", 16, int(8 * 0 + 5), int(17 * 0))
        cyberpi.display.show_label(e, 16, int(8 * 0 + 5), int(17 * 1))
        raise

main()#didi
# Hawaii Pizza ist lecker 
# Alohaaaaaaaaaaaaaaaaa