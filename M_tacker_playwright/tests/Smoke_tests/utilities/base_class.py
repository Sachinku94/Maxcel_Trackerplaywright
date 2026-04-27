import inspect
import logging
import pytest

@pytest.mark.usefixtures("setup")
class BaseClass:
    """Base class for all test classes"""
    
    def getLogger(self):
        """Get logger instance for current test"""
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        
        if not logger.handlers:
            file_handler = logging.FileHandler("logfile.log")
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.setLevel(logging.DEBUG)
        
        return logger