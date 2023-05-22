from django.shortcuts import render
from config import Configurations
import logging

# Create your views here.


def index(request):
    config_details =  Configurations.logging_display(request)
    server_name = Configurations.server_name
    server_ip = Configurations.server_ip # Read from class properties
    size = config_details['size']  # Read from class method
    # logging.log(1, f" {config_details} '-' {server_ip} '->' {server_name} {size}")
    
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    file_handler = logging.FileHandler('debug.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(file_handler)
    return render(request, 'api_integration/index.html', {'config': config_details })