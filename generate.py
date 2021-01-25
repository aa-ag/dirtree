###--- IMPORTS ---###
import subprocess
import csv


###--- FUNCTIONS ---###
def draw_tree():
    '''
     runs command and saves output/tree in file
    '''
    subprocess.run('tree > tree.html', shell=True)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    draw_tree()
