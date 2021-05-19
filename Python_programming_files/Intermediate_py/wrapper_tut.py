'''
@app.route('/contact')
def contact():
    return render_template("contact.html")
'''

def add_wrapping(item):
    def wrapped_item():
        return 'a wrapped up box of {}'.format(str(item()))
    return wrapped_item

@add_wrapping
def new_gpu():
    return 'a new Tesla P100d'

print(new_gpu())
