import RPi.GPIO as GPIO
import time
import os
import requests
import json

EMAIL=""
PASSWORD=""
SERIAL_NUMBER=""
PIN_NUMBER=11

def login():
    url = 'http://localhost:9000/api/v1/login'
    payload = json.dumps({'email': EMAIL, 'password': PASSWORD})
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=payload, headers=headers)
    return response.text == "success"

def publish(value):
    print("publishing message...")
    url = 'http://localhost:9000/api/v1/messages/' + SERIAL_NUMBER
    payload = json.dumps({'msgs': [{'message': value}]})
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=payload, headers=headers)
    print(response.text)

def pause():
  time.sleep(0.1)

def setup():
  if login():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_NUMBER, GPIO.IN) # Read output from PIR motion sensor
    print("GPIO setup done")
  else:
    raise "error in login"

def run():
  while True:
    if GPIO.input(PIN_NUMBER):
      while GPIO.input(PIN_NUMBER):
        publish("HIGH")
      publish("LOW")
    pause()

try:
  setup()
  run()
except KeyboardInterrupt:
  pass
finally:
  print "Exit: Cleanup"
  GPIO.cleanup()
