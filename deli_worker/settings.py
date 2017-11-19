import os

from dotenv import load_dotenv

load_dotenv(os.path.join(os.getcwd(), '.env'))

####################
# DATABASE         #
####################

DATABASE_DB = 'sandwich'
DATABASE_PORT = '5432'
DATABASE_POOL_SIZE = 20

if os.environ.get('CLI'):
    DATABASE_POOL_SIZE = -1

DATABASE_HOST = os.environ['DATABASE_HOST']
DATABASE_USERNAME = os.environ['DATABASE_USERNAME']
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']

####################
# RABBITMQ         #
####################

RABBITMQ_VHOST = '/'
RABBITMQ_PORT = 5672
RABBITMQ_HOST = os.environ['RABBITMQ_HOST']
RABBITMQ_USERNAME = os.environ['RABBITMQ_USERNAME']
RABBITMQ_PASSWORD = os.environ['RABBITMQ_PASSWORD']

####################
# VMWare           #
####################

VCENTER_HOST = os.environ['VCENTER_HOST']
VCENTER_PORT = os.environ['VCENTER_PORT']
VCENTER_USERNAME = os.environ['VCENTER_USERNAME']
VCENTER_PASSWORD = os.environ['VCENTER_PASSWORD']
