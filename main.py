#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from appeal_calculator import AppealCalculator

idopont = input("Irja be a hatarozat idopontjat kotojelekkel elvalasztva: ")
hatarozat1 = AppealCalculator(idopont)
hatarozat1.WriteDate()