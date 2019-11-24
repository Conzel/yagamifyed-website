import jinja2 as ji
import os

file_base = os.path.abspath(__file__)

env = ji.Environment(
    loader=ji.FileSystemLoader(os.path.join(
        os.path.dirname(file_base), "templates"))
)

# Utility class for easier rendering of template files
class Renderer:
    def __init__(self, name, env):
        self.template_file = name+"_template.html"
        self.file_name = name + ".html"
        self.env = env

    def write(self, **kwargs):
        template = env.get_template(self.template_file)
        rendered_template = template.render(kwargs)
        with open(self.file_name, "w+") as file:
           file.write(rendered_template)

# rend_cv = Renderer("curriculum_vitae", env)
# rend_cv.write(title="Curriculum Vitae", cv_active="active")

rend_books = Renderer("personal", env)
rend_books.write(title="Personal", personal_active="active")

rend_intro = Renderer("about", env)
rend_intro.write(title="About", about_active="active")

rend_work = Renderer("research", env)
rend_work.write(title="Research", research_active="active")
