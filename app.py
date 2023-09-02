from flask import Flask, render_template, request

app = Flask(__name__, template_folder="D:\\Flask_Course\\Templete")

def convert_to_celsius(temperature):
    return round((temperature - 32) * 5 / 9, 2)

def convert_to_fahrenheit(temperature):
    return round((temperature * 9 / 5) + 32, 2)

def convert_to_kelvin(temperature):
    return round(temperature + 273.15, 2)

@app.route('/', methods=['GET', 'POST'])
def temperature_converter():
    if request.method == 'POST':
        temperature = float(request.form['temperature'])
        selected_scale = request.form['scale']

        if selected_scale == 'celsius':
            converted_temperature = convert_to_celsius(temperature)
            converted_scale = '°C'
        elif selected_scale == 'fahrenheit':
            converted_temperature = convert_to_fahrenheit(temperature)
            converted_scale = '°F'
        elif selected_scale == 'kelvin':
            converted_temperature = convert_to_kelvin(temperature)
            converted_scale = 'K'
        else:
            converted_temperature = 'Invalid input'
            converted_scale = ''

        return render_template('index.html', converted_temperature=converted_temperature, converted_scale=converted_scale)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
