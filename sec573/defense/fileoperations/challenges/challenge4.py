#read a gz file and read the first 5 lines
import gzip

x=gzip.open("/var/log/auth.log.1.gz","rt")
lines=x.readlines()
for i in range(5):
    print(lines[i])
x.close()