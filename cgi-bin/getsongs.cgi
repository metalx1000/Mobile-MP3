#!/system/bin/sh

echo "Content-type: text/html"
echo ""
find ../Music/ -iname "*.mp3"|sed 's/^..//g'
