## What is
* CLI application that join several .png files into a .gif file.

* The application was created to generate animated GIFs showing the small games i started to develop. It can be used after capture png files of the screen.

## Installation
* Clone this repository and use in the terminal

## Usage
```console
 $ python screencap -d 20 -p /usr/temp/


 $ python screencap -d 30 -p /usr/temp/ -ar "(320, 2240)" "(0, 1080)"
```

## Flags
```console
  -h, --help            Show this help message and exit
  
  -fps, --fps           Frames per second of the GIF                   

  -f, --filename        The full path folder where the .gif file will be saved
  
  -p, --path            The full path folder where the .png files will be saved. 
                        Ex.:/usr/temp/ Note that if a path is informed without bar at the end, the last word will be a file prefix. 
                        Ex.: /usr/temp files will be saved at /usr with names temp1.png, temp2.png and so on.
```