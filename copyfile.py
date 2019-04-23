# encoding=utf-8
 2"""
 3文件copy demo
 4"""
 5import os
 6import shutil
 7from time import sleep
 8
 9def copyCopy(usb_path):
10    # os.listdir(dir)返回dir下所有文件夹及文件的名称
11    usb_file = os.listdir(usb_path)
12    while True:
13        new_usb_file = os.lisdir(usb_path)
14        if new_usb_file != usb_file:
15            break
16        sleep(5)  #每隔5s扫描一次
17    file = [f for f in new_usb_file if f not in usb_file]
18    shutil.copytree(os.path.join(usb_path, file[0]), '/home/work/copyCopy')
19
20if __name__ == "__main__":
21    usb_path = "/Volumes/"
22    copyCopy(usb_path)