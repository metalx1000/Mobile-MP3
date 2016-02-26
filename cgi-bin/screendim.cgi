#!/system/bin/sh

echo "Content-type: text/html"
echo ""



echo 0 > /sys/devices/fd900000.qcom,mdss_mdp/qcom,mdss_fb_primary.155/leds/lcd-backlight/brightness

echo "Screen dimmed all the way"
