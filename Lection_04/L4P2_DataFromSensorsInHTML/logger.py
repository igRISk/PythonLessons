from datetime import datetime as dt
path = 'D:\GeekBrainsLessons\PythonProjects\Lection_04\L4P2_ DataFromSensorsInHTML\Data\log.csv'

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(path, 'a') as file:
        file.write('{};temperature;{}\n'
                    .format(time, data))

def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(path, 'a') as file:
        file.write('{};pressure;{}\n'
                    .format(time, data))

def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(path, 'a') as file:
        file.write('{};wind_speed;{}\n'
                    .format(time, data))