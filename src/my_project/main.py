from my_project.core.logic import Processor
from my_project.logging_config import setup_logging
import logging


def main() -> None:
    setup_logging()
    log = logging.getLogger(__name__)

    log.info("Application started")

    processor = Processor("Engine")
    result = processor.run()

    log.info("Result: %s", result)


if __name__ == "__main__":
    main()
