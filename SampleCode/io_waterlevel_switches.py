import time
import board
import busio
import digitalio

from adafruit_mcp230xx.mcp23008 import MCP23008

# Initialize the I2C bus:
i2c = busio.I2C(board.SCL, board.SDA)

# Create an instance of either the MCP23008 or MCP23017 class depending on
mcp = MCP23008(i2c, address=0x26)  

# Now call the get_pin function to get an instance of a pin on the chip.
# This instance will act just like a digitalio.DigitalInOut class instance
# and has all the same properties and methods (except you can't set pull-down
# resistors, only pull-up!).  For the MCP23008 you specify a pin number from 0
# to 7 for the GP0...GP7 pins.



pin0 = mcp.get_pin(0) # N1 BTN
pin1 = mcp.get_pin(1) # N2 BTN
pin2 = mcp.get_pin(2) # N3 BTN
pin3 = mcp.get_pin(3) # N4 BTN
pin4 = mcp.get_pin(4) # N5 BTN
pin5 = mcp.get_pin(5) # WLL
pin6 = mcp.get_pin(6) # WLM
pin7 = mcp.get_pin(7) # WLH

pin0.direction = digitalio.Direction.INPUT
pin1.direction = digitalio.Direction.INPUT
pin2.direction = digitalio.Direction.INPUT
pin3.direction = digitalio.Direction.INPUT
pin4.direction = digitalio.Direction.INPUT
pin5.direction = digitalio.Direction.INPUT
pin6.direction = digitalio.Direction.INPUT
pin7.direction = digitalio.Direction.INPUT

print("Pin0: " + str(pin0.value))
print("Pin1: " + str(pin1.value))
print("Pin2: " + str(pin2.value))
print("Pin3: " + str(pin3.value))
print("Pin4: " + str(pin4.value))
print("Pin5: " + str(pin5.value))
print("Pin6: " + str(pin6.value))
print("Pin7: " + str(pin7.value))

"""
# Setup pin0 as an output that's at a high logic level.
pin0.switch_to_output(value=True)

# Setup pin1 as an input with a pull-up resistor enabled.  Notice you can also
# use properties to change this state.
pin1.direction = digitalio.Direction.INPUT
pin1.pull = digitalio.Pull.UP

# Now loop blinking the pin 0 output and reading the state of pin 1 input.
while True:
    # Blink pin 0 on and then off.
    pin0.value = True
    time.sleep(0.5)
    pin0.value = False
    time.sleep(0.5)
    # Read pin 1 and print its state.
    print("Pin 1 is at a high level: {0}".format(pin1.value))
"""