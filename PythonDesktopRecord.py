from PIL import ImageGrab
import numpy as np
import cv2
p = ImageGrab.grab()#��õ�ǰ��Ļ
k=np.zeros((200,200),np.uint8)
a,b=p.size#��õ�ǰ��Ļ�Ĵ�С
fourcc = cv2.VideoWriter_fourcc(*'XVID')#�����ʽ
video = cv2.VideoWriter('test.avi', fourcc, 16, (a, b))#����ļ�����Ϊtest.mp4,֡��Ϊ16�������Լ�����
while True:
    im = ImageGrab.grab()
    imm=cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)#תΪopencv��BGR��ʽ
    video.write(imm)
    cv2.imshow('imm', k)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()