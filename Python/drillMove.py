import shutil, os
from datetime import datetime, timedelta
import time


##srcpath = '/Users/Naj/Desktop/TA/DailyFile/test.txt'

destpath = 'C:\\Users\\navjot.dhillon\\Desktop\MoveFile\\'

##print curDir

os.chdir('C:\\Users\\navjot.dhillon\\Desktop\DailyFile\\')


checkfolder = os.listdir('C:\\Users\\navjot.dhillon\\Desktop\\DailyFile\\')

##print checkfolder


##movefile = shutil.move(destpath, srcpath)


#checkLastAccess = os.stat(srcpath)

##print checkLastAccess


for f in checkfolder:

    modtime = os.stat(f).st_mtime

    #modtimets = (datetime.fromtimestamp(modtime)) - this was not working(ND)

    
    check = time.time()- 3600
    
    #check = modtime - timedelta(hours = 24)

    if modtime <= check:
        
        if f.endswith(".txt"):

            shutil.copy(f, destpath)

            print('files have been copied at the correct folder')
