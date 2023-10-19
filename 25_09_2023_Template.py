import os
FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
TEMPALE_DIR = os.path.join(BASE_DIR, "templates")

class Template:
    template_name = ""
    context = None
    def __init__(self, template_name, context = None, *args, **kwargs) -> None:
        self.template_name = template_name
        self.context = context
    def get_template(self):
        template_path = os.path.join(TEMPALE_DIR, self.template_name)
        if not os.path.exists(template_path):
            raise Exception("Invalid Path")
        template_string = ""
        with open(template_path, 'r') as f :
            template_string = f.read()
        return template_string
    def render(self, context = {}):
        render_ctx = {}
        self.context != None
        render_ctx = self.context
        return  