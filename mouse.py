from win32api import mouse_event, SetCursorPos
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP


def mouseClick(x, y):
    
    SetCursorPos((x, y))
    mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    mouse_event(MOUSEEVENTF_LEFTUP, x, y, 0, 0)
