
from board import SCL, SDA
import busio
import time

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

# Create the I2C bus interface.
i2c_bus = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c_bus, address=0x74)

# Set the PWM frequency to 60hz.
pca.frequency = 60

# duty_cycle is 16 bits to match other PWM objects
# but the PCA9685 will only actually give 12 bits of resolution.
pca.channels[1].duty_cycle = 0xFFFF #RB Led
pca.channels[2].duty_cycle = 0xFFFF #B Led
pca.channels[3].duty_cycle = 0xFFFF #C Led
pca.channels[4].duty_cycle = 0xFFFF #R Led
pca.channels[5].duty_cycle = 0xFFFF #DR Led
pca.channels[7].duty_cycle = 0xFFFF #W Led

time.sleep(3)

pca.channels[1].duty_cycle = 0x0000 #RB Led
pca.channels[2].duty_cycle = 0x0000 #B Led
pca.channels[3].duty_cycle = 0x0000 #C Led
pca.channels[4].duty_cycle = 0x0000 #R Led
pca.channels[5].duty_cycle = 0x0000 #DR Led
pca.channels[7].duty_cycle = 0x0000 #W Led
