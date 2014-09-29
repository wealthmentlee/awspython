import boto.ec2.elb
elb = boto.ec2.elb.connect_to_region('us-east-1')
balancers = elb.get_all_load_balancers()
print(balancers[0])
instance_health = balancers[0].get_instance_health()
instances = [state.instance_id for state in instance_health]
for i in instances:
	print i