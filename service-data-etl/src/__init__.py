"""This file creates the fastapi service."""
# coding=utf-8
# import relation package.
from fastapi import FastAPI

# import project package.
from config.logger_setting import log

def create_app():
    """The function to creates the fastapi service."""
    # Initial fastapi app
    app = FastAPI(title="Swagger API",
                  description="This is swagger api spec document.",
                  version=health_check_information.get_health_check_content()['version'])

    log.info("start fastapi service.")
    return app
