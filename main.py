from web_app import Webapp
from dotenv import load_dotenv

load_dotenv('.env')

app = Webapp()

if __name__ == '__main__':
    app.run()     