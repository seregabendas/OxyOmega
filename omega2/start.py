import time
import device
import monitor

### USE FOR SETUP ###

sensor = device.Device(20.8, 20.8)
oled = monitor.Monitor()
counter = 0

### USE FOR LOOP ###
while True:
### ### ### #### ###
    counter += 1
    time.sleep(0.05)
    sensor.update()
    
    if (sensor.isFingerIn()):        
        if (not sensor.isActive()):
            sensor.activate()            
        print(" ------------ ")
        print("red      = " + str(sensor.getRed()))
        print("ir         = " + str(sensor.getIR()))
        print("ShO2  = " + str(sensor.getShO2()))
        if counter > 10:
            oled.write("      ShO2 = " + str(sensor.getShO2()) + "      ")
            counter = 0
        
    else:
        print(time.strftime("%H : %M"))
        if counter > 10:
            oled.time()
            counter = 0
            
        if (sensor.isActive()):
            sensor.disactivate()
        
        
    
    
    



