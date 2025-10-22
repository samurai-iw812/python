connected=False
port80attempts=0
while not connected:
    for port in [21,22,80,433,8000]:
        time.sllep(1)
        iftrytoconnect(port):
            connected=True
            break
        elif port != 80:
            continue
        port80attempts+=1
while True:
    interactwithconnection()