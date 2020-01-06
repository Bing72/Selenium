from selenium import webdriver
from tkinter import *


#GUI FRAME
from selenium.webdriver.support.select import Select

root = Tk()
root.title("RAFFLE")
root.geometry("200x200+200+200")
#URL Entry
op = StringVar()
in_entry = Entry(root, textvariable=op).pack()
#<Enter>로 입력
root.bind("<Return>", lambda q:root.destroy())
#Button클릭
Button(root, text="입력", command=root.quit).pack()
root.mainloop()

#Web 로드
driver = webdriver.Chrome("C:\Python\chromedriver\chromedriver.exe")
# 웹 자원로드 대기 3초
driver.implicitly_wait(3)
driver.get(op.get())
driver.implicitly_wait(3)

#사이즈선택
