import logging as log
import traceback


if __name__ == '__main__':
    log_format = "%(asctime)s [%(levelname)s] line %(lineno)d): %(message)s"
    log_level = log.INFO
    log.basicConfig(level=log_level, format=log_format)
    log.info("Python exception logging example")
    print("-" * 80)
    log.info("log.exception:")
    try:
        x = 1 / 0
    except Exception:
        log.exception("Encountered an exception.")
        """
        2022-07-12 06:10:38,503 [ERROR] line 18): Encountered an exception.
        Traceback (most recent call last):
          File ".../exception_logging.py", line 18, in <module>
            x = 1 / 0
        ZeroDivisionError: division by zero
        """

    print("-" * 80)
    log.info("traceback.print_exc:")
    try:
        x = 1 / 0
    except Exception as e:
        traceback.print_exc()
        """
        Traceback (most recent call last):
          File ".../exception_logging.py", line 27, in <module>
            x = 1 / 0
        ZeroDivisionError: division by zero
        """

