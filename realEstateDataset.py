import os
from dotenv import load_dotenv

load_dotenv('./.env')

test = os.getenv("something")

print(test)