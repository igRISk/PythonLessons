from user_interface import temperature_view
from user_interface import pressure_view
from user_interface import wind_speed_view
path = 'D:\GeekBrainsLessons\PythonProjects\Lection_04\L4P2_DataFromSensorsInHTML\Data\index.html'
newpath = 'D:/GeekBrainsLessons/PythonProjects/Lection_04/L4P2_DataFromSensorsInHTML/Data/new_index.html'

def create(device = 1):
    style = 'style="font-size:22px;"'
    html = '<html>\n <head><head>\n <body>\n'
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, pressure_view(device))
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, wind_speed_view(device))

    with open(path, 'w') as page:
        page.write(html)

    return html

def newcreate(data, device = 1):
    t, p, w = data
    style = 'style="font-size:22px;"'
    html = '<html>\n <head><head>\n <body>\n'
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, t)
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, p)
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, w)

    with open(newpath, 'w') as page:
        page.write(html)

    return data