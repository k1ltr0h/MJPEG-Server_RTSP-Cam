# The files and modules that do nothing but still in the proyect are there because this born from experiment and days of search and work, please take the time to remove this things or wait to eventually commit(new version)

- https://github.com/JPery/MJPEGWriter
- i forgot the other repository, sorry for this guy(python Flask).

# Thanks to MJPEGWriter
OpenCV Video HTTP Streaming via MJPEG.
Based on the code found in 
[StackExchange -  CodeReview](http://codereview.stackexchange.com/questions/124321/multithreaded-mjpg-network-stream-server/156915#156915) and [Answers - OpenCV](http://answers.opencv.org/question/6976/display-iplimage-in-webbrowsers/)

# Compile server_mjpeg with and run

- g++ MJPEGWriter.cpp main.cpp -o MJPEG -lpthread -lopencv_highgui -lopencv_core -std=c++11

- ./server (Port 8080)

# Run server_js with

- sudo node app.js (To use port 80 :D)