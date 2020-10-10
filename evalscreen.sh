#!/bin/sh

export DISPLAY=:0.0
export XAUTHORITY=/home/pi/.Xauthority

scrot -q 20 screen.png

$(dirname "$0")/evalimage.py

if [ $? -eq 0 ]
then
    echo $(date -u) "OK"
else
    echo $(date -u) "Aborted->Refresh"
    xdotool key --window $(xdotool getactivewindow) ctrl+R
fi