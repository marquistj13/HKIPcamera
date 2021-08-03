import HKIPcamera
import cv2

#ip地址、用户名和密码请自己修改
# modify to your own account
ip = str('192.168.1.8')
name = str('admin')     #usr name
pw = str('12345')        #password
HKIPcamera.init(ip, name, pw)

while True:
    orig_image= HKIPcamera.getframe()
    cv2.imshow('capture', orig_image) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
HKIPcamera.release()
