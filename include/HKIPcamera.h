//HKIPcamera.h
#include <opencv2/opencv.hpp>
using namespace cv;
 
void init_device(char* ip, char* usr, char* password);
Mat get_one_frame();
void release_device();
