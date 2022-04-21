from board import SCL, SDA
import busio
import time

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

# Create the I2C bus interface.
i2c_bus = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c_bus, address=0x76)

# Set the PWM frequency to 60hz.
pca.frequency = 60

# duty_cycle is 16 bits to match other PWM objects
# but the PCA9685 will only actually give 12 bits of resolution.
pca.channels[1].duty_cycle = 0xFFFF # N2 "PHD" Bottle 2
pca.channels[2].duty_cycle = 0xFFFF # N3 "A" Bottle 3
pca.channels[3].duty_cycle = 0xFFFF # N4 "B" Bottle 4
pca.channels[4].duty_cycle = 0xFFFF # N5 "CMG" Bottle 5
pca.channels[5].duty_cycle = 0xFFFF # Drain
pca.channels[6].duty_cycle = 0xFFFF # Fill
pca.channels[7].duty_cycle = 0xFFFF # N3 "A" Bottle 3
pca.channels[8].duty_cycle = 0xFFFF # Fan2
pca.channels[9].duty_cycle = 0xFFFF # Fan1

time.sleep(3)

pca.channels[1].duty_cycle = 0x0000 # N2 "PHD" Bottle 2
pca.channels[2].duty_cycle = 0x0000 # N3 "A" Bottle 3
pca.channels[3].duty_cycle = 0x0000 # N4 "B" Bottle 4
pca.channels[4].duty_cycle = 0x0000 # N5 "CMG" Bottle 5
pca.channels[5].duty_cycle = 0x0000 # Drain
pca.channels[6].duty_cycle = 0x0000 # Fill
pca.channels[7].duty_cycle = 0x0000 # N3 "A" Bottle 3
pca.channels[8].duty_cycle = 0x0000 # Fan2
pca.channels[9].duty_cycle = 0x0000 # Fan1