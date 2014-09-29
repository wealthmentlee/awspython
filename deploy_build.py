import boto.ec2.elb

def get_elb_instances(elb):
	connection = boto.ec2.elb.connect_to_region('us-east-1')
	balancers = connection.get_all_load_balancers(load_balancer_names=[elb])
	print(balancers[0])
	instance_health = balancers[0].get_instance_health()
	instances = [state.instance_id for state in instance_health]
	for i in instances:
		print i
	return instances

def create_ec2_instance():

def create_ec2_ami():

def create_auto_scaling_group():

def create_launch_configuration():

def change_launch_configuration():

def add_launch_configuration():

def delete_launch_configuration():



instances=get_elb_instances('WealthmentLB')
print(instances)
