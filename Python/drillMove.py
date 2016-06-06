import shutil, os
from datetime import datetime, timedelta
from time import time


##srcpath = '/Users/Naj/Desktop/TA/DailyFile/test.txt'

destpath = '/Users/Naj/Desktop/TA/MoveFile'

##print curDir

os.chdir('/Users/Naj/Desktop/TA/DailyFile')


checkfolder = os.listdir('/Users/Naj/Desktop/TA/DailyFile')

##print checkfolder


##movefile = shutil.move(destpath, srcpath)


checkLastAccess = os.stat(srcpath)

##print checkLastAccess


for f in checkfolder:

    modtime = os.stat(f).st_mtime

    modtimets = (datetime.fromtimestamp(modtime))

    check = modtimets - timedelta(hours = 24)

    if check < modtimets:

        shutil.copy(f, destpath)

        print('files have been copied at the correct folder')
