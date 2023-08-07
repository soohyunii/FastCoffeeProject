from pathlib import Path
import logging
import logging.config





L_NORMAL    = '\033[0m'    # white
L_ERR       = '\033[31m'      # red
L_RECV      = '\033[36m'      # cyan
L_SEND      = '\033[33m'     # yellow
L_BOT       = '\033[32m'     # blue
L_MEM       = '\033[35m'     # purple
L_SYS       = '\033[34m'      # green
L_BOLD      = '\033[1m'      # bold



def get_logger(type):
    filepath =  str(Path.cwd().parent.parent.joinpath('config', 'log_config.ini'))
    logging.config.fileConfig(filepath)
    pa_log = logging.getLogger(type)
    return pa_log