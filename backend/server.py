import socket
import sys
import zipfile
import os
import cv2
import numpy as np

port = 1337

ss = socket.socket()
print('[+] Server socket is created.')

ss.bind(('', port))
print('[+] Socket is binded to {}'.format(port))

ss.listen(5)
print('[+] Waiting for connection...')

con, addr = ss.accept()
print('[+] Got connection from {}'.format(addr[0]))

filename = con.recv(1024).decode()

f = open(filename, 'wb')
l = con.recv(1024)
while(l):
    f.write(l)
    l = con.recv(1024)
f.close()
# print('[+] Received file ' + filename)

with zipfile.ZipFile(filename, 'r') as file:
    # print('[+] Extracting files...')
    file.extractall()
    # print('[+] Done')

if os.path.isfile('1.png'):
    thres = 0.45  # Threshold to detect object
    nms_threshold = 0.2
    img = cv2.imread('1.png')  # su dung anh

    classNames = []
    objectLabels = []
    classFile = 'coco.names'
    with open(classFile, 'rt') as f:
        classNames = f.read().rstrip('\n').split('\n')

    configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightsPath = 'frozen_inference_graph.pb'

    net = cv2.dnn_DetectionModel(weightsPath, configPath)
    net.setInputSize(320, 320)
    net.setInputScale(1.0 / 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)

    classIds, confs, bbox = net.detect(img, confThreshold=thres)
    bbox = list(bbox)
    confs = list(np.array(confs).reshape(1, -1)[0])
    confs = list(map(float, confs))
    # print(type(confs[0]))
    # print(confs)

    indices = cv2.dnn.NMSBoxes(bbox, confs, thres, nms_threshold)
    # print(indices)

    for i in indices:
        i = i[0]
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        cv2.rectangle(img, (x, y), (x+w, h+y), color=(0, 255, 0), thickness=2)
        cv2.putText(img, classNames[classIds[i][0]-1].upper(), (box[0]+10, box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(img, str(round(confs[i]*100, 2)), (box[0]+250, box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        objectLabels.append(str(classNames[classIds[i][0]-1]))
    if len(objectLabels) > 0:
        print('[+] Object found', objectLabels)
    else:
        print('[+] Object not found')

    # cv2.imshow("Output", img)
    # cv2.imwrite('result.png', img)

    # imgResult = cv2.imread('./result.png')
    # cv2.imshow("Result", imgResult)
    cv2.waitKey(0)
else:
    print('[+] File not found')


os.remove(filename)
con.close()
ss.close()