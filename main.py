#!/usr/bin/python
# -*- coding: utf-8 -*-

from appeal_calculator import AppealCalculator

key_pressed = ""
while key_pressed != "x":
    print("************************************************")
    mydate = input("Írja be a határozat időpontját kötőjelekkel elválasztva: ")
    hatarozat1 = AppealCalculator(mydate)
    hatarozat1.WriteDate()
    key_pressed = input("Kilépéshez nyomja meg az 'x' gombot vagy folytatáshoz nyomjon 'Enter'-t. ")
    