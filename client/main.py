import socketio
import psutil
import time
import platform
import os

sio = socketio.Client()
sio.connect('http://server:5000')

if 'DEBUG' in os.environ:
    import random
    hostname = f"host-{random.randint(0,1000)}"
else:
    with open('/etc/hostname') as f:
        hostname = f.read().strip()

while(True):
    if 'DEBUG' in os.environ:
        data = {
            "cpu": round(random.random()*100),
            "mem": round(random.random()*100),
            "disk": round(random.random()*100),
            "temp": round(random.random()*60),
            "hostname": hostname,
            "arch": platform.machine(),
            "os": platform.platform()
        }
    else:
        data = {
            "cpu": psutil.cpu_percent(),
            "mem": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage('/').percent,
            "temp": psutil.sensors_temperatures()['coretemp'][0].current,
            "hostname": hostname,
            "arch": platform.machine(),
            "os": platform.platform()
        }
    sio.emit("data", data)
    time.sleep(1)