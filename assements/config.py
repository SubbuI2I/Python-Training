import toml
import logging

class Configurations:
    server_ip = ''
    server_name = ''
    size = 0
    def __init__(self):
        print('config')
        config = toml.load('config.toml')      
        server_name = config['server_name'] 
        server_ip = config['server_ip'] 
        size = config['size'] 
        logging.log(1,server_ip, server_name)

    def logging_display(self):
        config = toml.load('config.toml')
        logging.log(2,config)
        return config
    
