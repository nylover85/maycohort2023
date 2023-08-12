import boto3

ec2 = boto3.resource('ec2')

# Create 3 instances
instances = ec2.create_instances(
        ImageId="ami-08a52ddb321b32a8c",
        MinCount=3,
        MaxCount=3,
        InstanceType="t2.micro",
        SubnetId='subnet-064a5001084e7d154'
    )

# Print instance IDs
for instance in instances:
    print(instance.id)








