aws_cli_result = aws ec2 run-instances --image-id ami-864d84ee --key-name JeffLee --security-group-ids sg-8c4607e9 sg-0a57116f --user-data file://~/git/sewealthement/cloudinit.sh --instance-type t2.micro --placement AvailabilityZone=us-east-1a --block-device-mappings file://~/git/sewealthement/blockmappings.json --subnet-id subnet-ff7ebf88 --associate-public-ip-address

print aws_cli_result