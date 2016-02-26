#!/system/bin/sh

echo "Content-type: text/html"
echo ""

svc power stayon true && echo "Success"||echo "Fail"
