from .loader import loader
from .view import viewer
from .parser import parser


class Main:
    """Used to contain the assembly and starts the project"""

    def __init__(self):
        self.hello_world = "hello_world"
        self.data_frame = ""
        self.start()

    def start(self):
        """Starts the application"""
        print(self.hello_world)
        self.data_frame = loader.load_file()
        new_data_frame = parser.parse_data(self.data_frame)
        viewer.update_view(new_data_frame)
