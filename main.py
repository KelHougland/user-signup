import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),
    r'C:\Users\knhou\Google Drive\lc101\user-signup\templates')

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir))

def index():
    template = jinja_env.get_template('hello_form.html')
    return template.render()