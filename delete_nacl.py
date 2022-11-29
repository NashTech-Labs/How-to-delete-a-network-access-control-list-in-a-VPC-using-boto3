import logging
import boto3
from botocore.exceptions import ClientError
import time


REGION= input("Please, Enter the region name where you want to Delete this NACL:-\n=")

# setup the logger 
logger_info = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(message)s')

client = boto3.client("ec2", region_name=REGION)

# function to delete a 
def delete_nacl(nacl_id):

    try:
        response = client.delete_network_acl(NetworkAclId=nacl_id)

    except ClientError:
        logger_info.exception('Sorry, We are not able to delete your NACL in ')
        raise
    
    
    else:
        return response


if __name__ == '__main__':
    # taking the NACL id from user
    NACL_ID=input("Please, Enetr the ID to delete the NACL:- \n=")
    for i in range(3):
        logger_info.info(f'Please wait ...... \nWe are deleting your NACL...\U0001F570')
        time.sleep(5)
    nacl = delete_nacl(NACL_ID)
    logger_info.info(f'Hurry, Your given NACL:{NACL_ID} has been deleted successfully \U0001F44D')

