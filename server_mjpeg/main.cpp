#include "MJPEGWriter.h"
#include "env.h"
int main(){
    MJPEGWriter test(8080);

    VideoCapture cap;
    bool ok = cap.open(CAM0);
    if (!ok){
        printf("no cam found ;(.\n");
        pthread_exit(NULL);
    }
    Mat frame;
    cap >> frame;
    test.write(frame);
    frame.release();
    test.start();
    while(cap.isOpened()){
        try{
            cap >> frame; 
            test.write(frame); 
            frame.release();
            if(waitKey(30) >= 0) break;
        }
        catch(int e){
            break;
        }
    }
    cap.release();
    test.stop();
    return 0;

}
