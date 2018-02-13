import time
import device

### USE FOR SETUP ###

sensor = device.Device(20.8, 20.8)


### USE FOR LOOP ###
while True:
### ### ### #### ###
    time.sleep(1)
    sensor.update()
    
    if (sensor.isFingerIn()):        
        if (not sensor.isActive()):
            sensor.activate()            
        print(" ------------ ")
        print("red      = " + sensor.getRed())
        print("ir         = " + sensor.getIR())
        print("ShO2  = " + sensor.getShO2())
        
    else:
        if (sensor.isActive()):
            sensor.disactivate()
        
        
    
    
    



