import os
from memory import *



class RabbitMqProcess():
    def __init__(self) -> None:
        try:
            self.local_id = os.getpid()
            self.pa_log = get_logger('pa')
            self.mq_start()
        except Exception as ex:
            json_data = {'pid' : self.local_id, 'Error_Message' : ex}
            self.pa_log.error(L_ERR + f"RabbitMqProcess Init Exception : {json_data}" + L_NORMAL)
    
    def mq_start(self):
        pass





