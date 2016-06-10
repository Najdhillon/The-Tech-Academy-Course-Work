
from tkinter import *
from tkinter import filedialog

def main():

    in_path = filedialog.askopenfilename()
    print(in_path)

if __name__ == "__main__":
    main()
