from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('show_form'))

@app.route('/form', methods=['GET', 'POST'])
def show_form():
    if request.method == 'POST':
        # Process form submission here
        # For now, let's just print the form data
        print(request.form)
        return redirect(url_for('index'))
    return render_template('form.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Process form data here if needed
    # Redirect to loading.html
    return redirect(url_for('loading'))  # Redirect to loading route

@app.route('/loading')
def loading():
    return render_template('loading.html')  # Render loading.html template

if __name__ == '__main__':
    app.run(debug=True)
