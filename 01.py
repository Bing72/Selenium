from selenium import webdriver
from tkinter import *



#GUI FRAME
root = Tk()
root.title("RAFFLE")
root.geometry("200x200+200+200")
#URL Entry
op = StringVar()
in_entry = Entry(root, textvariable=op).pack()
btn=Button(root, text="입력", command=root.quit).pack()
root.mainloop()

driver = webdriver.Chrome("C:\Python\chromedriver\chromedriver.exe")
# 웹 자원로드 대기 3초
driver.implicitly_wait(3)
driver.get(op.get())
