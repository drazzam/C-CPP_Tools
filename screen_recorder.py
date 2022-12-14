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

# Set the video resolution
width = 640
height = 480

# Set the video frame rate
fps = 60

# Set the video codec
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

# Set the output file name
output_file = "screen_capture.avi"

# Get the handle to the main desktop window
hdesktop = win32gui.GetDesktopWindow()

# Get the dimensions of the main desktop window
screen_width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
screen_height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

# Create a device context for the desktop window
desktop_dc = win32gui.GetWindowDC(hdesktop)
img_dc = win32ui.CreateDCFromHandle(desktop_dc)

# Create a memory device context for the desktop window
mem_dc = img_dc.CreateCompatibleDC()

# Create a bitmap object
screenshot = win32ui.CreateBitmap()
screenshot.CreateCompatibleBitmap(img_dc, screen_width, screen_height)
mem_dc.SelectObject(screenshot)

# Create a VideoWriter object
video_writer = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Capture and record video frames
while True:
    # Copy the screen into the memory device context
    mem_dc.BitBlt((0, 0), (screen_width, screen_height), img_dc, (left, top), win32con.SRCCOPY)

    # Create a numpy array from the bitmap
    img = np.frombuffer(screenshot.GetBitmapBits(True), np.uint8)

    # Resize the image to the specified width and height
    img = cv2.resize(img, (width, height))

    # Convert the image to BGR color space (OpenCV uses BGR by default)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Write the frame to the video file
    video_writer.write(img)

# Clean up
video_writer.release()
mem_dc.DeleteDC()
win32gui.DeleteObject(screenshot.GetHandle())
img_dc.DeleteDC()
desktop_dc.DeleteDC()
