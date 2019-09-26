# Firefly
Program created with the purpose of analysing a video and creating 40 second long snippets based on the status of a lightbulb.  More specifically, when the lightbulb is first found to be on, the code createws a wmv file of the preceeding 20 seconds and the 20 seconds following the activation of said lightbulb.  The program works its magic on every single wmv file in its directory creating an OUTPUT folder in which files with the format  `output_<filename>-<clip#>.wmv` are saved. As you can see, the program creates a clip for every single lightbulb activation within a file, no matter how many, **as long as they do not occur within 20 seconds of the previous lightbulb activation** (as this would be part of the previous truncated clip.
  
## Notice
__For a proper reading, it is necessary for the lightbulb to be within the region shown below__. Moreover, if possible, place lightbulb in such a way as to eliminate extraneous light in its immediate vicinity whether it be caused by other lights or the lightbulb's own reflection <br>
*Tip: An electrical tape square under the light solves both of these problems*.

For future reference: the framing of mouse 61's recall test under the effects of Citalopram was spot on! ;)

![alt text](https://raw.githubusercontent.com/ftondolo/Firefly/master/image.png)

## Windows Install
_Administrator Privileges Required_
1) Download and install all of the following files **in the order in which they appear:**<br>
    - Visual Studio 2019 : https://aka.ms/vs/16/release/vc_redist.x64.exe<br>
    - Python 3.7.3 : https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe<br> 
      > Custom->Next->Add Python to environment variables
   
    - NumPy : Open CMD and type `pip install numpy`<br>
    - ffmpy : Open CMD and type `pip install ffmpy`<br>
    - OpenCV : Open CMD and type `pip install opencv-python`<br>
    - ffmpeg : https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-20190620-86f04b9-win64-static.zip<br>
      - Follow instructions found here : https://www.wikihow.com/Install-FFmpeg-on-Windows
2) Download firefly.py and position it in a folder with all of the .wmv files you want examined<br>
3) Open firefly.py in IDLE (Python 3.7 64-bit)
   > File->Open...
  
4) Run firefly.py
    > Run->Run Module
  
5) Wait for completion, should take about 20 seconds per 10-minute video <br>
**DO NOT MANIPULATE THE FILE STRUCTURE UNTIL THE PROGRAM FINISHES**


## Debian Install
_Administrator Privileges Required_
1) Download and install all of the following files **in the order in which they appear:**<br>
    - Pip : `sudo apt-get install python-pip`<br> 
    - ffmpeg : `sudo apt-get install ffmpeg`<br>
    - ffmpy :`pip install ffmpy`<br>
    - NumPy : `pip install  numpy`<br>
    - OpenCV : `pip install opencv-python`<br>
2) Download firefly.py and position it in a folder with all of the .wmv files you want examined<br>
3) Open a Terminal window and navigate to the directory which you have selected
   > `cd /...`
  
4) Run firefly.py
    > `python firefly.py`
  
5) Wait for completion, should take about 20 seconds per 10-minute video <br>
**DO NOT MANIPULATE THE FILE STRUCTURE OR THE TERMINAL WINDOW UNTIL THE PROGRAM FINISHES**<br>
**IF YOU WISH TO PLAY THE .WMV FILES THEN YOU WILL NEED TO INSTALL UBUNTU RESTRICTED EXTRAS**
