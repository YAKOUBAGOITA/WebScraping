import pyautogui
import time
print(pyautogui.size())
x, y= pyautogui.position()
'''
print(pyautogui.onScreen(x,y))
pyautogui.moveTo(300, 500,)
pyautogui.moveRel(100, 500,2)
'''
pyautogui.moveTo(150, 1079, 2)
time.sleep(2)
pyautogui.click()
pyautogui.write("notepad",1)
pyautogui.moveTo(270,229,2)
pyautogui.click(clicks=2) 
time.sleep(3)
pyautogui.write("My name Yakouba Goita, Hashim is my roommate from SPT,\n This trial and error method involves visually observing the movement \n of the window and noting the coordinates as you move it around. You may want to refine your movements \nto narrow down the exact position. Keep in mind that this method can be time-consuming, and there are more precise ways to obtain window coordinates programmatically \n using scripting languages or third-party") 