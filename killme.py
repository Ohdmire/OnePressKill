import win32gui
import win32process
import os
from pynput.keyboard import Listener,Key
import ctypes

#判断是否有管理员权限
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

#监听
def on_release(key):
    if key == Key.esc:      # 停止监听
        return False
    if key == Key.f2:       # 这里是按f2调用kill函数
        kill()

#杀死进程
def kill():
    now_win = win32gui.GetForegroundWindow()
    now_process=win32process.GetWindowThreadProcessId(now_win)[1]
    target=r'taskkill /pid {} /F /T'.format(now_process)
    os.system(target)

#开始判断管理员权限
if is_admin()==False:
    print("警告:当前非管理员身份运行,可能导致kill失败")

#开始监听
with Listener(
        on_release=on_release) as listener:
    listener.join()