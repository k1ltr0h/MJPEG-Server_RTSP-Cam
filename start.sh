#!/bin/bash

trap start INT

start(){
	PID=$(pgrep server)
	echo Server ID: $PID
	sudo kill -9 $PID


}
cd ~/Proyectos/MJPEG-Server_RTSP-Cam/
sudo ./server_mjpeg/server & sudo node ./server_js/app.js




