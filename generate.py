###--- IMPORTS ---###
import subprocess
import csv
import shutil
import settings


###--- GLOBAL VARIABLES ---###
path = settings.PATH


###--- FUNCTIONS ---###
def draw_tree():
    '''
     runs command and saves output/tree in file
    '''
    # Alternative 1: tree
    subprocess.run('tree > tree.html', shell=True)


def delete_tree():
    '''
     removes directory specified in path
    '''
    global path
    shutil.rmtree(path, ignore_errors=True)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    # draw_tree()
    delete_tree()
