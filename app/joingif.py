import imageio.v2 as imageio
import os
import argparse
import sys

def join_gif(path:str, fps:float, filename:str):
    files=[path+f for f in os.listdir(path)]
    files=sorted(files)
    images=[]
    print("Processing images...")
    try:
        for f in files:        
            images.append(imageio.imread(f))
    except FileNotFoundError:
        print("An error occured while processing the .png files. Check if the folder exists or the path informed is correct.")
        sys.exit(1)
    except:
        print("An error occured.")
        sys.exit(1)
    else:
        print ("Saving file...")
        try:
            imageio.mimsave(filename, images, format='GIF', fps=fps)
        except PermissionError:
            print("An error occured while saving the file. Check folder path permissions.")
            sys.exit(1)
        else:
            print("File saved.")

def execute():
    parser = argparse.ArgumentParser(prog="Join gif", description="Join .png files in given folder into animated GIF.")
   
    parser.add_argument("-fps","--fps",
                    default="none",                     
                    help="Frames per second of the GIF.",
                    type=str                    
                    )

    parser.add_argument("-f","--filename",
                    default="none",                     
                    help="The full path folder where the .gif file will be saved.",
                    type=str                    
                    )

    parser.add_argument("-p","--path",
                default="none",                     
                help="The full path folder where are the .pngs files.",
                type=str                    
                )
    
    args = parser.parse_args()

    res=join_gif(args.path, args.fps, args.filename)

if __name__=="__main__":
    execute()