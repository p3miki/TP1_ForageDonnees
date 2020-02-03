from .loader import loader
from .view import viewer
from .parser import parser


class Main:
    """Used to contain the assembly and starts the project"""

    def __init__(self):
        self.hello_world = "hello_world"
        self.file = ""
        self.start()

    def start(self):
        """Starts the application"""
        print(self.hello_world)
        self.file = loader.load_file()
        parser.parse_data(self.file)
        viewer.update_view()
