# Load environment variables
from dotenv import dotenv_values
from typing import OrderedDict

# Load environment variables from .env file
CONFIG: OrderedDict = dotenv_values("./project.env")
