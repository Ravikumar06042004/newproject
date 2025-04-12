import RPi.GPIO as GPIO
import time
import spidev
import smbus  # For I2C communication with MPU6050
import smtplib  # For sending email
from email.mime.text import MIMEText

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

# GPIO Pins for two motor control
MOTOR_A_FORWARD = 17
MOTOR_A_BACKWARD = 18
MOTOR_B_FORWARD = 22
MOTOR_B_BACKWARD = 23

# GPIO Pin for IR sensor
IR_SENSOR_PIN = 26  # Adjust pin number as necessary

# Setup GPIO pins for motor control
GPIO.setup(MOTOR_A_FORWARD, GPIO.OUT)
GPIO.setup(MOTOR_A_BACKWARD, GPIO.OUT)
GPIO.setup(MOTOR_B_FORWARD, GPIO.OUT)
GPIO.setup(MOTOR_B_BACKWARD, GPIO.OUT)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)  # Set up IR sensor pin as input

# MCP3008 setup
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, chip select 0 (CS0)
spi.max_speed_hz = 1350000

# MPU6050 setup
MPU6050_ADDR = 0x68
bus = smbus.SMBus(1)
bus.write_byte_data(MPU6050_ADDR, 0x6B, 0)  # Wake up MPU6050

def read_mpu6050():
    accel_x = bus.read_word_data(MPU6050_ADDR, 0x3B)
    accel_y = bus.read_word_data(MPU6050_ADDR, 0x3D)
    accel_z = bus.read_word_data(MPU6050_ADDR, 0x3F)
    gyro_x = bus.read_word_data(MPU6050_ADDR, 0x43)
    gyro_y = bus.read_word_data(MPU6050_ADDR, 0x45)
    gyro_z = bus.read_word_data(MPU6050_ADDR, 0x47)
    
    # Convert the values to signed 16-bit
    accel_x = (accel_x - 65536) if accel_x > 32768 else accel_x
    accel_y = (accel_y - 65536) if accel_y > 32768 else accel_y
    accel_z = (accel_z - 65536) if accel_z > 32768 else accel_z
    gyro_x = (gyro_x - 65536) if gyro_x > 32768 else gyro_x
    gyro_y = (gyro_y - 65536) if gyro_y > 32768 else gyro_y
    gyro_z = (gyro_z - 65536) if gyro_z > 32768 else gyro_z
    
    return accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z

def send_email_alert(subject, body):
    sender_email = "gummabhupalraj114341@gmail.com"
    receiver_email = "guvvalagopireddy51@gmail.com"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    # Send email using Gmail's SMTP server
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login("gummabhupalraj114341@gmail.com", "vcei mjaq nnnj tzqk")
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def read_channel(channel):
    """Reads data from a specific MCP3008 channel."""
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

try:
    while True:
        # Read joystick values from MCP3008
        x_value = read_channel(0)  # Joystick X-axis is connected to channel 0
        y_value = read_channel(1)  # Joystick Y-axis is connected to channel 1
        
        print(f"X: {x_value}, Y: {y_value}")

        # Adjusted motor control for forward/backward based on Y-axis
        if y_value < 400:  # Joystick moved up (forward)
            GPIO.output(MOTOR_A_FORWARD, GPIO.HIGH)
            GPIO.output(MOTOR_A_BACKWARD, GPIO.LOW)
            print("Moving FORWARD")
        elif y_value > 600:  # Joystick moved down (backward)
            GPIO.output(MOTOR_A_FORWARD, GPIO.LOW)
            GPIO.output(MOTOR_A_BACKWARD, GPIO.HIGH)
            print("Moving BACKWARD")
        else:  # Center position (stop Motor A)
            GPIO.output(MOTOR_A_FORWARD, GPIO.LOW)
            GPIO.output(MOTOR_A_BACKWARD, GPIO.LOW)

        # Adjusted motor control for left/right based on X-axis
        if x_value < 400:  # Joystick moved left
            GPIO.output(MOTOR_B_FORWARD, GPIO.HIGH)
            GPIO.output(MOTOR_B_BACKWARD, GPIO.LOW)
            print("Turning LEFT")
        elif x_value > 600:  # Joystick moved right
            GPIO.output(MOTOR_B_FORWARD, GPIO.LOW)
            GPIO.output(MOTOR_B_BACKWARD, GPIO.HIGH)
            print("Turning RIGHT")
        else:  # Center position (stop Motor B)
            GPIO.output(MOTOR_B_FORWARD, GPIO.LOW)
            GPIO.output(MOTOR_B_BACKWARD, GPIO.LOW)

        # Read MPU6050 sensor values
        accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z = read_mpu6050()
        print(f"Accel: X={accel_x}, Y={accel_y}, Z={accel_z} | Gyro: X={gyro_x}, Y={gyro_y}, Z={gyro_z}")

        # Check if there's sudden movement
        if abs(accel_x) > 20000 or abs(accel_y) > 20000 or abs(accel_z) > 20000:
            print("Sudden movement detected! Sending email...")
            send_email_alert("MPU6050 Alert: Sudden Movement Detected", "Sudden movement has been detected by the MPU6050 sensor!")

        # Check IR sensor for emergency situation
        if GPIO.input(IR_SENSOR_PIN) == GPIO.HIGH:  # Adjust based on your IR sensor's output
            print("Emergency! IR sensor triggered! Sending email...")
            send_email_alert("IR Sensor Alert: Emergency Detected", "An emergency situation has been detected by the IR sensor!")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program stopped by User")
finally:
    GPIO.cleanup()
