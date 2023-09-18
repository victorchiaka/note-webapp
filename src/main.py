from dotenv import load_dotenv
from webapp import initialize_app
import os

load_dotenv()

IS_DEVELOPMENT = os.getenv("IS_DEVELOPMENT")

app = initialize_app()

if IS_DEVELOPMENT:
    if __name__ == "__main__":
        app.run(debug=False)
else:
    if __name__ == "__main__":
        app.run()
