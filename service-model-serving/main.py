"""This is the main file for fastapi service"""

# import relation package.
import uvicorn

# import project package.
from src import create_app
from config.project_setting import service_config

#for gunicorn can get app.
app = create_app()

if __name__ == '__main__':
    uvicorn.run(app, host=service_config.service_host,
                port=service_config.service_port, debug=False, access_log=False)
