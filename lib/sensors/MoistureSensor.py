import machine

# Sensor is completly unreliable for me and showing extremely different values in same condition when trying to get the max and min values

class MoistureSensor:
    """A class that can read set pins for a moisture sensor installed on Lopy4"""
    max_moisture_sensor_value = 1000 # From multiple manual callibration test in glas of water, the average value
    min_moisture_sensor_value = 4095 # From manual calibration in complety dry in air, average value
    range_sensor_value = min_moisture_sensor_value - max_moisture_sensor_value

    def __init__(self):
        """Default constructor"""
        adc = machine.ADC()
        adc.vref(1100)
        self.pin16 = adc.channel(pin='P16',attn=machine.ADC.ATTN_11DB)

    def get_value_in_procent(self):
        """Get the value in procent depending of the fixed max and min moisture values"""
        value = self.pin16.value()

        if value < self.max_moisture_sensor_value: return 1
        if value > self.min_moisture_sensor_value: return 0

        valueOverMax = value - self.max_moisture_sensor_value

        return round(1 - (valueOverMax / self.range_sensor_value), 2)
