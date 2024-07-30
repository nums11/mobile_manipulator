from time import sleep

print("Entering the package")
from robotiq_modbus_controller.driver import RobotiqModbusRtuDriver
driver = RobotiqModbusRtuDriver('COM6')
print(driver.connect())
driver.reset()
driver.activate()
print(driver.status())
sleep(2)
print(driver.status())

driver.move(pos=0, speed=255, force=1)
sleep(3)
driver.move(pos=255, speed=255, force=1)
sleep(3)

for i in range(0, 255, 50):
  driver.move(pos=i, speed=255, force=1)
  sleep(1)

driver.disconnect()
print("Exiting the package")
