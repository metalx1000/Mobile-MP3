#!/bin/sh
echo "Content-type: text/html"
echo ""
find ../ -iname "*.mp3"|sed 's/^..//g'
