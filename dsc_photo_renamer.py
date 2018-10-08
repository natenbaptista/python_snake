#!/usr/bin/env python
import os
import time

dpath = '/home/atp/Downloads/'
for filename in os.listdir(dpath):
    if filename.startswith("DSC_"):
        nstamp = time.strftime("%Y%m%d",time.localtime(os.path.getmtime(dpath+filename)))
        nfile = nstamp+'_'+filename[4:]
        print nfile
        os.rename(dpath+filename, dpath+nfile)


