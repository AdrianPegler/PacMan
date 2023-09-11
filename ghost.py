import cyberpi
import time
import math, random

#Ab hier arbeite ich alleine auf dem main.

#Hilfsfunktion um eine Nachricht auf dem Pi anzuzeigen
def pi_print(message):
    cyberpi.display.show_label(message, 16, int(8*0 + 5), int(17 * 0))

#Hauptfunktion: Hier wir euer Code eingefügt
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
#hallo