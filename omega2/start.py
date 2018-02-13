import time
import device

### USE FOR SETUP ###

sensor = device.Device(20.8, 20.8)


### USE FOR LOOP ###
while True:
### ### ### #### ###
    time.sleep(0.1)
    sensor.update()
    
    if (sensor.isFingerIn()):        
        if (not sensor.isActive()):
            sensor.activate()            
        print(" ------------ ")
        print("red      = " + str(sensor.getRed()))
        print("ir         = " + str(sensor.getIR()))
        print("ShO2  = " + str(sensor.getShO2()))
        
    else:
        print(time.strftime("%H : %M"))
        if (sensor.isActive()):
            sensor.disactivate()
        
        
    
    
    



