from dotenv import load_dotenv
from imagekitio import ImageKit
import os

load_dotenv()

image_kit = ImageKit(private_key=os.environ["IMAGEKIT_PRIVATE_KEY"])
