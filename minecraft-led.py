#This is the main file

#Start all the initialisation stuff
import minecraft.minecraft as minecraft
import minecraft.block as block
import time

#Suggested code from GPIO google code site as easy to forget to run as root
#https://code.google.com/p/raspberry-gpio-python/wiki/BasicUsage
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
#Set GPIO to use the actual numbers NOT pins
GPIO.setmode(GPIO.BCM)

#Set GPIO Ports for LEDs
RED = 17
YELLOW = 27
GREEN = 22

#Setup the GPIO Pins
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

#Now start the actual program

if __name__ == "__main__":
    time.sleep(5)

    #Create the Minecraft object
    mc = minecraft.Minecraft.create()

    #Message to check it's all working
    mc.postToChat("LED position markers ready to start")
    time.sleep(5)

    #Determine the players position
    playerPos = mc.player.getPos()


    #Take that position data and subtract 1 from y value to get the position of the block below
    blockType = world.getBlock(playerPos.x, playerPos.y - 1, playerPos.z)

    if blockType == 0:
        GPIO.output(RED, True)
        GPIO.output(YELLOW, False)
        GPIO.output(GREEN, False)
    elif blockType == 8:
        GPIO.output(RED, False)
        GPIO.output(YELLOW, True)
        GPIO.output(GREEN, False)
    elif blockType == 9:
        GPIO.output(RED, False)
        GPIO.output(YELLOW, True)
        GPIO.output(GREEN, False)
    else:
        GPIO.output(RED, True)
        GPIO.output(YELLOW, False)
        GPIO.output(GREEN, False)


#If block is
#   Air -> Shine Red LED  |  Dec 0 Hex 0
#   GPIO.output(RED, True)

#   Water -> Shine Yellow LED |  Dec 8 OR 9  Hex 8 OR 9
#   GPIO.output(YELLOW, True)

#   Any other block -> Shine Green LED
#   GPIO.output(GREEN, True)