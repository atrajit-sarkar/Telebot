import subprocess

process=subprocess.Popen(fr"python instaviddownload1.py",shell=True,text=True,stdout=subprocess.PIPE)
        
process.wait()
output, _=process.communicate()
