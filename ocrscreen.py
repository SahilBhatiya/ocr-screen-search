import pytesseract
from PIL import ImageGrab
from selenium import webdriver
import threading as th
import win32gui
import keyboard
from tkinter import *
import sys
sys.setrecursionlimit(10**7)



window1 = Tk()
window1.configure(padx=2, pady=2, bg="#ffffff", borderwidth=0, relief="flat")
window1.attributes("-topmost", 1)
window1.resizable(0, 0)
window1.minsize(330, 40)
window1.maxsize(330, 40)
window1.wm_attributes('-alpha', 0.8525)
window1.title("SB Production: QuizSearch")
window1.iconbitmap("quizsearch.ico")


def startit():
    global startbtn
    startbtn.configure(bg="#3cba54", text="Select 1 point", padx=20)
    keyboard.wait('p')
    flags, hcursor, (x1, y1) = win32gui.GetCursorInfo()
    startbtn.configure(bg="#3cba54", text="Select 2 point", padx=20)
    keyboard.wait('p')
    flags, hcursor, (x2, y2) = win32gui.GetCursorInfo()
    screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    screenshot.save("screenshot.png", "PNG")
    startbtn.configure(bg="#3cba54", text="Done", padx=40)
    # search fast

    def startbrowser():
        global driver
        global startbtn
        driver = webdriver.Ie(executable_path=r'C:\SeleniumDrivers\IEDriverServer.exe')
        startbtn.configure(bg="#4885ed", text="Search", padx=40)
    # mltithreading
    p1 = th.Thread(target=startbrowser)
    p1.start()
    p1.join()
    # image to text
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    query = pytesseract.image_to_string('screenshot.png')
    print(query)
    # search in google
    driver.get("https://www.google.com/search?&q=" + "\"" + query + "\"")


def startit1(event):
    p69 = th.Thread(target=startit).start()


startbtn = Button(window1, text="Search", command=lambda : startit1(event=Event), padx=40, pady= 4, bg="#4885ed", bd=0, fg="#ffffff")
startbtn.pack()


window1.bind_all("o", startit1)
window1.mainloop()


