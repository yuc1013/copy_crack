import time
import keyboard
 
time.sleep(3)  # 等待3秒
with open('answer.txt', encoding='utf-8') as file:
    for line in file:
        keyboard.write(line)