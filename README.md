# Behaviour
Both scripts downloads the highest quality possible up to 1080p 60fps. Code is customizable to download higher qualities.

Both of the scripts will create a file named "Videos" at the same path that it exists. Both scripts do/can feed the same file. When moved, they will create a new "Videos" file in the new location. So its completely portable.

This project is implementable to an UI application. I was just too lazy to do it and i hate designing UI.


# Setup:
1. Install everything in folder "Before launch" (Select "ADD to PATH" when installing Python)
2. Start the application depending on your demand. (By order.exe, At once.exe)
3. Input single or multiple URLs and press Enter twice.
4. Done.

Be aware that the method "At once" downloads them at once it it suppose to be. So ridiculous amount of video links can slow down your internet if its not good enough.

# Possible modifications and rebuilding

If you want to modify this code and rebuild it by yourself just download the source package and install pyinstaller (pip install pyinstaller) package for building it.

pyinstaller --onefile --console --add-data "ffmpeg\\bin\\ffmpeg.exe;ffmpeg\\bin" "by order.py"

Running this command in source file will build it into one .exe file which will make the script work with ffmpeg package all the time.

# Known Issues
Working for shorts but not for playlist videos propably.
If you experience stutters on video, use different player.
