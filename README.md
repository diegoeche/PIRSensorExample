# PIR Sensor Example

This example creates uses the Geeny SDK to relay the PIR data using a Raspberry Pi
Zero.

# Step 0

[Connect to your Geeny Enabled Raspberry Pi Zero.](https://github.com/geeny/fu-workshop#step-0-ssh-to-your-rpi-zero-w)

# Step 1

Upload the pir.py to your Raspberry Pi.

# Step 2

## Connect the PIR to the Raspberry Pi

The PIR sensor has 3 pins. Signal, Ground and Vcc as shown in the picture.

![PIR](/pir.jpeg?raw=true "PIR")

We'll be pluging those to the 11th, 6th and 2nd pin which correspond to GPIO 17,
Ground and 5v.

![Pins](/pins.jpeg?raw=true "Pins")

# Credits

Most of this tutorial was created using the really nice tutorial from here:
https://maker.pro/education/bluetooth-basics-how-to-control-an-led-using-a-smartphone-and-arduino-1
