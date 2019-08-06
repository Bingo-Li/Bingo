import os
import shutil
# def del_files(path):
#     for root, dir, files in os.walk(path):
#         for name in files:
#             if name.endswith(".png"):   #指定要删除的格式，这里是jpg 可以换成其他格式
#                 os.remove(os.path.join(root, name))
#                 print ("Delete File: " + os.path.join(root, name))
#     # test
# if __name__ == "__main__":
#     path = r'C:\UIA\Q\transcripts'
#     del_files(path)


# import os
# import glob
import os
import shutil
# def del_files(path):
#     for root, dir, files in os.walk(path):
#         for name in files:
#             if name.endswith(".png"):   #指定要删除的格式，这里是jpg 可以换成其他格式
#                 os.remove(os.path.join(root, name))
#                 print ("Delete File: " + os.path.join(root, name))
#     # test
# if __name__ == "__main__":
#     path = r'C:\UIA\Q\transcripts'
#     del_files(path)


# import os
# import glob

import sys
import os
currDir = r'C:\UIA\Q\transcripts'
#currDir = sys.path[0]
def removeFile(dir,postfix):
    if os.path.isdir(dir):
        for file in os.listdir(dir):
            removeFile(dir+'/'+file,postfix)    #递归处理
    else:
        if os.path.splitext(dir)[1] == postfix:
            os.remove(dir)







