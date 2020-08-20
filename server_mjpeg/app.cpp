#include<stdio.h>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include "opencv2/opencv.hpp"
#include "env.h"

using namespace cv;
//using namespace std;

int main(){
    namedWindow("Cam0", CV_WINDOW_NORMAL);
    VideoCapture cap(CAM0); // open the default camera
    if(!cap.isOpened()){  // check if we succeeded
	printf("No entre csm!");
        return -1;
    }
    //Mat edges;
    namedWindow("Cam0",1);
    while(true){
        Mat frame;
        cap.read(frame); // get a new frame from camera
        //cvtColor(frame, edges, COLOR_BGR2GRAY);
        //GaussianBlur(edges, edges, Size(7,7), 1.5, 1.5);
        //Canny(edges, edges, 0, 30, 3);
        imshow("Cam0", frame);
        if(waitKey(30) >= 0) break;
    }
    // the camera will be deinitialized automatically in VideoCapture destructor
    return 0;
}
