# evalscreen - check for aborted Chromium kiosk screen

Inspired by [Scott Hanselmans wall mounted Family Calendar](https://www.hanselman.com/blog/HowToBuildAWallMountedFamilyCalendarAndDashboardWithARaspberryPiAndCheapMonitor.aspx) I installed a monitor with an attached Raspberry Pi Zero W 2 years back and been experimenting with various technical approaches to host the web page for this family board. Currently it is [Blazor WebAssembly](https://dotnet.microsoft.com/apps/aspnet/web-apps/blazor).

This app occasionally breaks (or has to recover from a wireless connection loss). Surely I will invest some time in the future to get down to the actual root cause of the problem, but until then I wanted to have a more or less intelligent way of refreshing when the kiosk app breaks. 

## setup required

- Linux `scrot` utility to capture screen
- Python 3 with `PIL` library installed to evaluate color of captured screen
- `xdotool` to refresh Chromium page

## shell script to drive the process

The script `evalscreen.sh`

1. uses `scrot` to capture a low quality (20% is sufficient for evaluation) screen image
2. runs image through Python script `evalimage.py` (see below)
3. with Python script signals an error level not equal to 0 a refresh with `xdotool` is initiated

This script is scheduled each minute with `cron`:

```
# m h  dom mon dow   command
*/1 *   *   *   *    /home/pi/evalscreen/evalscreen.sh >> /home/pi/evalscreen/evalscreen.log 2>&1
```

## Python script to evaluate the image

Based on this [StackOverflow post](https://stackoverflow.com/a/2271013/4947644) I created this Python script `evalimage.py` that determines the most present color in the captured image. As my family board has a black background I assume when the most present color is not black, it is broken. When assumed broken it exits with error level 1.

## cleaning up

Not to forget that the growing log file needs to be kept in check. For that I added a file `/etc/logrotate.d/evalscreen`:

```
/home/pi/evalscreen/evalscreen.log {
  rotate 12
  daily
  compress
  missingok
  notifempty
}
```

## closing

After looking into the issue itself after some days it turned out that I just needed to do a clean reinstall of `chromium-browser` and `rpi-chromium-mods`.
