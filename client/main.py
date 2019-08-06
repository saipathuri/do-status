import socketio
import psutil
import time
import platform

sio = socketio.Client()
sio.connect('http://server:5000')

with open('/etc/hostname') as f:
    hostname = f.read().strip()

while(True):
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