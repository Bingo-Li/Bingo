import requests
import os
import csv
import datetime


def trans(res_json):
    path = os.getcwd()
    ExistResult = os.path.exists(path+'\\computeDeviceStatus.csv')
    csvfile = open(path+'\\computeDeviceStatus.csv', 'a+', encoding='utf-8')
    writer = csv.writer(csvfile, delimiter=",")
    flag = True
    datas = res_json['data']
    for data in datas:
        if not ExistResult:
            if flag:
                keys = list(data.keys())
                writer.writerow(keys)
                flag = False
        value = list(data.values())
        writer.writerow(value)
    csvfile.close()

if __name__ == '__main__':
    url = 'http://139.198.168.213:8000/api/status'
    res = requests.get(url)
    res = res.json()
    trans(res)




