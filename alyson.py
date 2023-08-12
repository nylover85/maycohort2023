import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Stop instances
response = ec2.stop_instances(
    InstanceIds=['i-03614d0b96022ce74', 'i-0a73d63de0b3f6360', 'i-008b223612674086d']
)

# Print response
print(response)







