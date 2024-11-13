#Wiring can be found at: https://learn.adafruit.com/adafruit-sharp-memory-display-breakout/python-setup
#Code from https://learn.adafruit.com/adafruit-sharp-memory-display-breakout/python-usage

# --------------
# This code initialize the SPI bus
# --------------

import board
import busio
import digitalio
import adafruit_sharpmemorydisplay

spi = busio.SPI(board.SCK, MOSI=board.MOSI)
scs = digitalio.DigitalInOut(board.D6) # inverted chip select

display = adafruit_sharpmemorydisplay.SharpMemoryDisplay(spi, scs, 144, 168)
