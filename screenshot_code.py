# Import the libraries
import cv2
import numpy as np
import win32gui
import win32ui
import win32con
import win32api

# Hide the console window
def hide_console():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

# Call the hide_console function to hide the console window
hide_console()

# Get the handle to the main desktop window
hdesktop = win32gui.GetDesktopWindow()

# Get the dimensions of the main desktop window
width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

# Create a device context for the desktop window
desktop_dc = win32gui.GetWindowDC(hdesktop)
img_dc = win32ui.CreateDCFromHandle(desktop_dc)

# Create a memory device context for the desktop window
mem_dc = img_dc.CreateCompatibleDC()

# Create a bitmap object
screenshot = win32ui.CreateBitmap()
screenshot.CreateCompatibleBitmap(img_dc, width, height)
mem_dc.SelectObject(screenshot)

# Copy the screen into the memory device context
mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

# Save the bitmap to a file
screenshot.SaveBitmapFile(mem_dc, "screen_capture.bmp")

# Clean up
mem_dc.DeleteDC()
win32gui.DeleteObject(screenshot.GetHandle())
