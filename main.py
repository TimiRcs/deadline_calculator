#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from appeal_calculator import AppealCalculator

key_pressed = ""
while key_pressed != "x":
    print("************************************************")
    mydate = input("Irja be a hatarozat idopontjat kotojelekkel elvalasztva: ")
    hatarozat1 = AppealCalculator(mydate)
    hatarozat1.WriteDate()
    key_pressed = input("Kilepeshez nyomja meg az 'x' gombot vagy folytatashoz nyomjon 'Enter'-t. ")
    