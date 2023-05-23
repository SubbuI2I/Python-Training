import toml
from logger.log import Log

class Configurations:
    server_ip = ''
    server_name = ''
    size = 0

    def __init__(self):
        config = toml.load('config.toml')      
        server_name = config['server_name'] 
        server_ip = config['server_ip'] 
        size = config['size'] 
        log = Log()
        log.write_log(f'{server_ip} - {server_name}', 20)

    def logging_display(self):
        config = toml.load('config.toml')
        log = Log()
        log.write_log(f'{config}', 20)
        return config
    
