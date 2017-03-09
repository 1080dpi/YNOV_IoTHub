# -*- coding: utf-8 -*-
#!/usr/bin/python3.7
import DeviceClient

# START: Azure IoT Hub settings
KEY = "PRA5Z7Wt5VgyZpbLyShjBFVtRm4zZXkpv1yPm5HHGss=";
HUB = "IoTpy.azure-devices.net";
DEVICE_NAME = "PetitPython";
# END: Azure IoT Hub settings

device = DeviceClient.DeviceClient(HUB, DEVICE_NAME, KEY)

device.create_sas(600)

# Device to Cloud
print(device.send(b"{message: 'Hello from Python'}"))

# Cloud to Device
message = device.read_message()
print(message['body'])

device.complete_message(message['etag'])