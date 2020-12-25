"""This file is used in setting config."""

# import relation package.
import os
import sys
import logging
import logging.config
from datetime import datetime
import yaml

# import project package.


class LoggerSetting:
    """This class is used in setting config."""

    def __init__(self):
        """Initial some variable and module"""
        self.project_path = os.environ['PROJECT_PATH']

    def set_logger(self, class_name="[LoggerSetting]", class_name_enable=False, logger_path_enabled=False,
                   log_dir=os.path.join("tmp", "logs"), logger_config_path='config/yaml/logger_config.yml'):
        """set_logger: parser the yaml file.
        Arguments:
            class_name: str, the name of class.
            class_name_enable: bool, See the name of class or not.
            log_dir: str, The path of log storage.
            logger_config_path: str, the path of logger config yaml.
        Returns:
            logging: The logger setting variable.
        """
        logger_config_path = self.path_join(logger_config_path)

        # Save the log to file.
        if os.path.exists(logger_config_path) and (logger_path_enabled):
            with open(logger_config_path, 'r') as f:
                yaml_config = yaml.safe_load(f.read())

            log_dir = self.path_join(log_dir)
            self.make_directory(log_dir)
            yaml_config["handlers"]["file"]["filename"] = self.path_join(
                log_dir, 'project.log'+'.'+datetime.strftime(datetime.now(), '%Y%m%d'))

            logging.config.dictConfig(yaml_config)
            logging.getLogger(class_name)

        if class_name_enable:
            # Add class name into log information.
            logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s][%(class_name)s][%(module)s][%(funcName)s]%(message)s',
                                datefmt='%a, %d %b %Y %H:%M:%S', stream=sys.stdout)
        else:
            # Basic logger config setting.
            logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s][%(module)s][%(funcName)s]%(message)s',
                                datefmt='%a, %d %b %Y %H:%M:%S', stream=sys.stdout)
        return logging

    def path_join(self, *folder_name):
        """path_join: Join two path together.
        Arguments:
            folder_name: tuple, the folder name.
        Returns:
            path: string, the join of path.
        """
        # Check the first folder name contains the PROJECT_PATH or not.
        if self.project_path not in folder_name[0]:
            path = self.project_path
        else:
            path = ''
        # Join the folder name to be a path directory.
        for item in list(folder_name):
            path = os.path.join(path, item)
        return path

    def make_directory(self, *path_dir):
        """make_directory: Make the folder directory.
        Arguments:
            path_dir: tuple, the path directory.
        """
        for item in list(path_dir):
            # Check the first folder name contains the PROJECT_PATH or not.
            if self.project_path not in item:
                self.path_join(item)
            # Make the folder directory.
            if not os.path.exists(item):
                os.makedirs(item)

logger_setting = LoggerSetting()
log = logger_setting.set_logger()
