import cv2
import time
try:
    import pyautogui
except:
    print("Please run 'pip install pyautogui' in a command prompt!")
    time.sleep(5)
    exit
try:
    import numpy
except:
    print("Please run 'pip install numpy' in a command prompy!")
    time.sleep(5)
    exit
print('If you are reading this, you are good to go and enter dust collection menu.')
image1_path = "Capture.PNG"
image2_path = "Capture2.PNG"
template1 = cv2.imread(image1_path)
template2 = cv2.imread(image2_path)
while True:
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(numpy.array(screenshot), cv2.COLOR_RGB2BGR)
    result1 = cv2.matchTemplate(screenshot, template1, cv2.TM_CCOEFF_NORMED)
    min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(result1)
    if max_val1 > 0.9:
        height1, width1, channels1 = template1.shape
        center_x1 = max_loc1[0] + width1 / 2
        center_y1 = max_loc1[1] + height1 / 2
        pyautogui.moveTo(center_x1, center_y1)
        pyautogui.click()
    result2 = cv2.matchTemplate(screenshot, template2, cv2.TM_CCOEFF_NORMED)
    min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result2)
    if max_val2 > 0.9:
        height2, width2, channels2 = template2.shape
        center_x2 = max_loc2[0] + width2 / 2
        center_y2 = max_loc2[1] + height2 / 2
        pyautogui.moveTo(center_x2, center_y2)
        pyautogui.click()