from flask_site.app import app
import logging

logger = logging.getLogger(__name__)


def configure_logging():
    """configure logging module"""
    logging.basicConfig(
        # filename=CONFIG["LOGGING_FILE"],
        level=logging.INFO,
        format="%(asctime)s: %(levelname)7s: [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


if __name__ == "__main__":
    configure_logging()
    try:
        app.run(debug=True)
    except Exception as e:
        logger.critical(f"App could not start! Error: {e}")
    else:
        logger.info(f"App started!")
