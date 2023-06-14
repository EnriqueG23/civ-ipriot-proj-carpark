import mqtt_device
import time
import json

from config_parser import parse_config
class Display(mqtt_device.MqttDevice):
    """Displays the number of cars and the temperature"""
    def __init__(self, config):
        super().__init__(config)
        self.client.on_message = self.on_message
        self.client.subscribe('display')
        self.client.loop_forever()

    def display(self, *args):
        print('*' * 20)
        for val in args:
            print(val)
            time.sleep(1)

        print('*' * 20)

       # TODO: Parse the message and extract free spaces,\
       #  temperature, time

    def on_message(self, client, userdata, msg):
        data = msg.payload.decode()
        values = data.split(',')

        if len(values) >= 3:
            free_spaces = values[0].strip()
            temperature = values[1].strip()
            timestamp = values[2].strip()

            # TODO: Use the extracted values as needed
            print("Free Spaces:", free_spaces)
            print("Temperature:", temperature)
            print("Timestamp:", timestamp)

        self.display(*values)

if __name__ == '__main__':

    # TODO: Read config from file
    CONFIG_FILE = "config_file.json"
    config1 = parse_config(CONFIG_FILE)["Display"]
    # with open('config_file.json') as f:
    #   config1 = json.load(f)["Display"]

    display = Display(config1)

