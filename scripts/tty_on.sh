#!/bin/bash
stty -F /dev/ttyUSB0 speed 9600 cs8
echo -ne "~0100 1\r" > /dev/ttyUSB0
