"""This file is for application config"""
# import relation package.
import base64
from pydantic import BaseSettings

# import project package.


class ServiceConfigSettings(BaseSettings):
    """This class define the application baseconfig"""
    unittest: bool = False
    service_host: str = "0.0.0.0"
    service_port: int = 5000


def __config_variable_value_decoding(config_variable):
    """__config_variable_value_decoding: Use base64 to decode the variable value.
    Arguments:
        config_variable: string, the variable need to decode.`
    Returns:
        the value which is decoded.
    """
    return base64.b64decode(config_variable).decode("utf-8")


service_config = ServiceConfigSettings()
