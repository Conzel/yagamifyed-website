import jinja2 as ji
import os

file_base = os.path.abspath(__file__)
print(file_base)
print(os.path.dirname(file_base))

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

rend_cv = Renderer("curriculum_vitae", env)
rend_cv.write(title="Curriculum Vitae", cv_active="active")

rend_books = Renderer("books", env)
rend_books.write(title="Books", books_active="active")

rend_intro = Renderer("intro", env)
rend_intro.write(title="Intro", intro_active="active")

rend_work = Renderer("work", env)
rend_work.write(title="Work", work_active="active")
