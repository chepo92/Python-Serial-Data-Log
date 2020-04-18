#!/usr/bin/env python3

import pygame
import sys
import serial
import keyboard

ser = serial.Serial('COM37', 38400, timeout=1)
verbose = True

while True:
    ser.write(b".") #* encode string to bytes
    line = ser.readline() 
    f = open("datalog.txt", "a")
    f.write("\n")
    f.write(str(line))
    f.close()
    if verbose:
        print (str(line))
    if keyboard.is_pressed('q'):
        break