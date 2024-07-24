import logging
from tenacity import before_sleep_log, after_log, retry, stop_after_attempt, wait_fixed
from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_attempts = 60 * 5
wait_seconds = 1


@retry(
    before_sleep=before_sleep_log(logger, logging.INFO),
    after=after_log(logger, logging.INFO),
    stop=stop_after_attempt(max_attempts),
    wait=wait_fixed(wait_seconds),
)
def init() -> None:
    try:
        db = SessionLocal()
        db.execute("SELECT 1")
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
