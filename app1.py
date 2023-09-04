from flask import Flask, render_template
import random

app = Flask(__name__, template_folder="D:\\Flask_Course\\Templete")

@app.route('/')
def index():
    return render_template('bg.html')

@app.route('/generate')
def generate_color():
    random_color = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))

    # Generate gradient colors
    gradient_color = generate_gradient_color()

    return render_template('bg.html', color=random_color, gradient_color=gradient_color)

def generate_gradient_color():
    color1 = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))
    color2 = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))
    gradient_color = f'linear-gradient(to right, {color1}, {color2})'
    return gradient_color

if __name__ == '__main__':
    app.run(debug=True)
    