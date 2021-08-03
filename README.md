HKIPcamera linux python interface (only implement the function to capture the opencv image mat)
==================

## Reference of haikang vision sdk libs
1. [PBCVT (Python-Boost-OpenCV Converter)](https://github.com/Algomorph/pyboostcvconverter)
1. HKIPcamera.cpp file is from [linux下实现Python调用海康威视SDK](https://www.cnblogs.com/deeplearning1314/p/10617840.html)


## How to use
### dependency
see the `CMakeLists.txt` file for details.

On my ubuntu20.04 machine, I install boost, opencv, and also activate an Ananconda python3 environment.

### copy hkvison libs to the /usr/lib or /us/local/lib directory
Here I extract some lib files in the `lib_to_root` directory from `CH-HCNetSDKV6.1.6.3_build20200925_Linux64/lib`.
So you only need to copy them to the system directory.
```sh
cd lib_to_root
sudo cp * /usr/local/lib/
sudo ldconfig
```

### build the library
just run `sh build.sh`, this will generate `HKIPcamera.so` in the `python_test` directory.

### use the library
1. put `HKIPcamera.so` anywhere you want, and your python script should in the same directory, here `HKIPcamera.so` is in `python_test`, so we will work in `python_test`.
2. run the `test.py` script


```python
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
```

