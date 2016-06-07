import shutil, os
from datetime import datetime, timedelta
import time


##srcpath = '/Users/Naj/Desktop/TA/DailyFile/test.txt'

##destpath = 'C:\\Users\\navjot.dhillon\\Desktop\MoveFile\\'

##print curDir

os.chdir('/Users/Naj/Desktop/TA/DailyFile/')


checkfolder = os.listdir('/Users/Naj/Desktop/TA/DailyFile/')

##print checkfolder


##movefile = shutil.move(destpath, srcpath)


#checkLastAccess = os.stat(srcpath)

##print checkLastAccess


for f in checkfolder:
    
    if f.endswith(".txt"):

        modtime = os.stat(f).st_mtime

        #modtimets = (datetime.fromtimestamp(modtime)) - this was not working(ND)

        
        check = time.time()- (24*60*60)
        
        #check = modtime - timedelta(hours = 24)

        if modtime >= check:

                src = '/Users/Naj/Desktop/TA/DailyFile/{}'.format(f)

                dst = '/Users/Naj/Desktop/TA/MoveFile/{}'.format(f) 

                shutil.copy(src, dst)

                print('files have been copied at the correct folder')
