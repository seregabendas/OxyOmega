def calculateShO2(red, ir):
    if red + ir == 0:
        return 0
    shO2 = 100 * red / (red + ir)
    return shO2

def getLastValue(arr):
    value1 = arr[-1:]
    value = value1[0]
    return value
    
