#!/system/bin/sh

echo "Content-type: text/html"
echo ""

svc power stayon false && echo "Success"||echo "Fail"
