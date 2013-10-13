#This is the main file

#Start all the initialisation stuff
import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import RPi.GPIO as GPIO

#Set GPIO to use the actual numbers NOT pins
GPIO.setmode(GPIO.BCM)

#Set GPIO Ports for LEDs
#17 Red
RED = 17
#27 Yellow
YELLOW = 27
#22 Green
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
    blockPos =


#Discover the block type at that location


#If block is
#   Air -> Shine Red LED  |  Dec 0 Hex 0
#   Water -> Shine Yellow LED |  Dec 8 OR 9  Hex 8 OR 9
#   Any other block -> Shine Green LED