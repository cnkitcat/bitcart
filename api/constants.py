VERSION = "0.2.3.0"  # Version, used for openapi schemas and update checks
WEBSITE = "https://bitcartcc.com"  # BitcartCC official site
GIT_REPO_URL = "https://github.com/bitcartcc/bitcart"  # BitcartCC github repository
LOG_FILE_NAME = "bitcart-log.log"  # base log file name
MAX_CONFIRMATION_WATCH = 6  # maximum number of confirmations to save
FEE_ETA_TARGETS = [25, 10, 5, 2, 1]  # supported target blocks confirmation ETA fee
EVENTS_CHANNEL = "events"  # default redis channel for event system (inter-process communication)
LOGSERVER_PORT = 9020  # port for logserver in the worker
