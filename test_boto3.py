import boto3

 

 

ssm = boto3.client('ssm')

 

access_key_id_aws = ssm.get_parameter(Name='access_key_id_aws')['Parameter']['Value']
secret_access_key_aws = ssm.get_parameter(Name='secret_access_key_aws')['Parameter']['Value']

 

cloud9 = boto3.client('cloud9',
aws_access_key_id=access_key_id_aws,
aws_secret_access_key=secret_access_key_aws,
)

 

response = cloud9.list_environments()

 

 

print(response)

