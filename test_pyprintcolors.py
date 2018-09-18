'''
  An astounding library of color foundations for printing formatted text to terminal in python3
  All code and credit goes to Saeed Zahedian Abroodi (https://stackoverflow.com/users/8584198/saeed-zahedian-abroodi)
    via https://stackoverflow.com/questions/39473297/how-do-i-print-colored-output-with-python-3
  I copied the code here to share with others and keep for myself; but it was not apparently available elsewhere.
'''

from Color import *

if __name__ == '__main__':
    print("Base:")
    print(Base.FAIL,"This is a test!", Base.END)

    print("ANSI_Compatible:")
    print(ANSI_Compatible.Color(120),"This is a test!", ANSI_Compatible.END)

    print("Formatting:")
    print(Formatting.Bold,"This is a test!", Formatting.Reset)

    print("GColor:") # Gnome terminal supported
    print(GColor.RGB(204,100,145),"This is a test!", GColor.END)

    print("Color:")
    print(Color.F_Cyan,"This is a test!",Color.F_Default)
