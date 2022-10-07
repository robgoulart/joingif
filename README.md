## What is
* CLI application that join several .png files into a .gif file.

* The application was created to generate animated GIFs showing the small games i started to develop. It can be used after capture png files of the screen.

## Installation
* Clone this repository and use in the terminal

## Usage
```console
 $ python joingif -p 20 -p '/usr/temp/' -fps 60 -f '/usr/temp/file.gif' 
```

## Flags
```console
  -h, --help            Show this help message and exit.
  
  -fps, --fps           Frames per second of the GIF.                   

  -f, --filename        The full path folder where the .gif file will be saved.
  
  -p, --path            The full path folder where the .png files will be saved. 
                        