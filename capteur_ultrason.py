import RPi.GPIO as GPIO
import time

# Set GPIO pin numbers
ultrasonic_trigger = 23
ultrasonic_echo = 24
buzzer_pin = 25

# Set GPIO mode and warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up ultrasonic sensor pins
GPIO.setup(ultrasonic_trigger, GPIO.OUT)
GPIO.setup(ultrasonic_echo, GPIO.IN)

# Set up buzzer pin
GPIO.setup(buzzer_pin, GPIO.OUT)

def distance():
    # Send a 10us pulse to trigger
    GPIO.output(ultrasonic_trigger, True)
    time.sleep(0.00001)
    GPIO.output(ultrasonic_trigger, False)

    # Measure the time it takes for the echo to go high
    start_time = time.time()
    while GPIO.input(ultrasonic_echo) == 0:
        start_time = time.time()

    # Measure the time it takes for the echo to go low
    while GPIO.input(ultrasonic_echo) == 1:
        stop_time = time.time()

    # Calculate distance in centimeters
    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2
    return distance

try:
    while True:
        dist = distance()
        print("Distance:", dist, "cm")

        # Check if distance is below 1.5m (150 cm)
        if dist < 150:
            GPIO.output(buzzer_pin, GPIO.HIGH) # Turn on buzzer
        else:
            GPIO.output(buzzer_pin, GPIO.LOW) # Turn off buzzer

        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()