import shutil, os
from datetime import datetime, timedelta
import time



os.chdir('C:\\Users\\navjot.dhillon\\Desktop\DailyFile\\')

srcf = ('C:\\Users\\navjot.dhillon\\Desktop\DailyFile\\')
destf = ('C:\\Users\\navjot.dhillon\\Desktop\MoveFile\\')

for f in os.listdir(srcf):

    src = os.path.join(srcf,f)
    dest = os.path.join(destf,f)
    
    if f.endswith(".txt"):

        # Last Mod time calculation

        modtime = time.time() - (os.path.getmtime(src))

        #modtimets = (datetime.fromtimestamp(modtime)) - this was not working(ND)

        h24ago = time.time() - (24*60*60)

        last24 = time.time() - h24ago
        
        #check = modtime - timedelta(hours = 24)

        if modtime < last24:

                shutil.copy(src, dest)
                print '{} has been copied to {}'.format(src,dest)
                
                
