import boto.ec2.autoscale
from boto.ec2.autoscale import AutoScalingGroup

asgName = 'Wealthment US East'
lbName = ['WealthmentLB']
subnetIDs=['subnet-ff7ebf88','subnet-5de51004','subnet-450e106d']
conn = boto.ec2.autoscale.connect_to_region('us-east-1')

ag = AutoScalingGroup(group_name=asgName, vpc_zone_identifier=subnetIDs, load_balancers=lbName, launch_config=lc, min_size=3, max_size=9, connection=conn)
conn.create_auto_scaling_group(ag)

ag.get_activities()

group = conn.get_all_groups(names=[asgName])[0]
print group