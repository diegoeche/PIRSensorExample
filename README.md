# PIR Sensor Example

This example creates uses the Geeny SDK to relay the PIR data using a Raspberry Pi
Zero.

# Step 0

[Connect to your Geeny Enabled Raspberry Pi Zero.](https://github.com/geeny/fu-workshop#step-0-ssh-to-your-rpi-zero-w)

# Step 1

* Upload and configure the pir.py to your Raspberry Pi.

* Modify the pir.py and set the following variables:

```
EMAIL=""
PASSWORD=""
SERIAL_NUMBER=""
```

The `SERIAL_NUMBER` can be obtained by registering a new device through the
`geeny-hub` service running in the Rpi.


1. Log in to the `geeny-hub`.

```
curl -H "Content-Type: application/json" -X POST \
  -d '{"email":"<your-user>","password":"<your-password>"}' \
  'http://localhost:9000/api/v1/login'
```

2. Register the thing the instance will use.

```
curl -X POST \
    -H 'Content-Type: application/json' \
    -H 'Accept: application/json' \
    -d '{
        "name": "<name-of-your-thing>",
        "serial_number": "<your-serial-number>",
        "thing_type": "877827cc-0c78-4e55-80fe-2941479c681a"
        }' \
    'http://localhost:9000/api/v1/things' > thing.info
```

# Step 2

## Connect the PIR to the Raspberry Pi

The PIR sensor has 3 pins. Signal, Ground and Vcc as shown in the picture.

![PIR](/pir.jpeg?raw=true "PIR")

We'll be pluging those to the 11th, 6th and 2nd pin which correspond to GPIO 17,
Ground and 5v.

![Pins](/pins.jpeg?raw=true "Pins")

# Step 3 (Test)

Ssh into your raspberry pi.

`python pir.py`

Should output the following when motion is detected.

```
GPIO setup done
publishing message...
{"status":"success"}
```

# Credits

Most of this tutorial was created using the really nice tutorial from here:
https://maker.pro/education/bluetooth-basics-how-to-control-an-led-using-a-smartphone-and-arduino-1
