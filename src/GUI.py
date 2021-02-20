from tkinter import *

def main(n):
    x = n
    y = 0
    while(x > 0):
        y = y * 10 + (x % 10)
        x = x // 10
    print(y)