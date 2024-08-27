import logging

logging.basicConfig(
    filename='waf.log',  
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s'  
)

waf_logger = logging.getLogger('app')