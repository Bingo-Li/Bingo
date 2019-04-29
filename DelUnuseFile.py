import sys
import os
import shutil
import stat
import win32api, win32con

currDir = r'Q:\transcripts'
#currDir = sys.path[0]

def removeFile(dir,folder,postfix):
    if os.path.isdir(dir):
        for file in os.listdir(dir):
            if file == folder:
                shutil.rmtree(dir+'/'+file, True)
                if os.path.exists(dir+'/'+file):
                    win32api.MessageBox(0,"{} folder still exists".format(file))          
            else:
                removeFile(dir+'/'+file,folder,postfix)   #递归处理
             

    else:
        if os.path.splitext(dir)[1] == postfix:
            os.remove(dir)

# def removeReadOnly(func, path, _):
#     os.chmod(path, stat.S_IWRITE)
#     func(path)

if __name__ == "__main__":
    os.chmod(currDir,stat.S_IWRITE)
    if os.path.exists(r"Q:\transcripts\UIAutomation\Temp"):
        shutil.rmtree(r"Q:\transcripts\UIAutomation\Temp", True)
        if os.path.exists(r"Q:\transcripts\UIAutomation\Temp"):
            win32api.MessageBox(0, "Temp folder still exists")
            
    fileTypeList = [".png",".bak",".lck"]
    folderList = ["GPUCache","OldVersions"]
    for fileType in fileTypeList:
        for folderName in folderList:
            removeFile(currDir, folderName, fileType)
	
    if os.path.exists(r"C:\Users\t_libin\OneDrive - autodesk\transcripts"):
        shutil.rmtree(r"C:\Users\t_libin\OneDrive - autodesk\transcripts", True)
    shutil.copytree(r"Q:\transcripts", r"C:\Users\t_libin\OneDrive - autodesk\transcripts")
	
