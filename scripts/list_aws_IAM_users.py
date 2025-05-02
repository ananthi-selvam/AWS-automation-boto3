#importing boto3 modules
import boto3
from pprint import pprint

#opening AWS mangement console
aws_management_console = boto3.session.Session(profile_name='default')
iam_console = aws_management_console.client('iam')

result = iam_console.list_users() 
#pprint(result['Users'])

#iterating users
for user in result['Users']:
    print(user['UserName'])
