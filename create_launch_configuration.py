import time
import boto.ec2
import boto.ec2.autoscale
from boto.ec2.autoscale import LaunchConfiguration

#Variable Init

amiID = 'ami-b63184de'
pemKey = 'JeffLee'
sgIDs = ['sg-8c4607e9','sg-0a57116f']
instanceType = 't2.micro'
origLcName = 'WealthmentTest'
newLcName = 'WealthmentRenameTest'
conn = boto.ec2.autoscale.connect_to_region('us-east-1')

def create_launch_configuration(name="",amiID="",pemKey="",sgIDs="",instanceType="",connection=""):
	if not connection:
		print "You MUST provide a connection!"
		exit(0)
	if not name:
		print "You need to provide a name for the new Launch Config"
		exit(0)
	if not amiID:
		amiID = lc.image_id
	if not pemKey:
		pemKey = lc.key_name
	if not sgIDs:
		sgIDs = lc.security_groups
	if not instanceType:
		instanceType=lc.instance_type

	newlc = LaunchConfiguration(name=name,image_id=amiID,key_name=pemKey,security_groups=sgIDs,instance_type=instanceType,associate_public_ip_address=True)
	connection.create_launch_configuration(newlc)

	return newlc

def change_launch_configuration(lc,name="",amiID="",pemKey="",sgIDs="",instanceType="",connection=""):
	if not connection:
		print "You MUST provide a connection!"
		exit(0)
	if not name:
		print "You need to change the name for the new Launch Config"
		exit(0)
	if not amiID:
		amiID = lc.image_id
	if not pemKey:
		pemKey = lc.key_name
	if not sgIDs:
		sgIDs = lc.security_groups
	if not instanceType:
		instanceType=lc.instance_type

	newlc = LaunchConfiguration(name=name,image_id=amiID,key_name=pemKey,security_groups=sgIDs,instance_type=instanceType,associate_public_ip_address=True)
	connection.create_launch_configuration(newlc)

	return newlc

#lc = conn.get_all_launch_configurations(names=[origLcName])[0]
testLc = create_launch_configuration(name="newWealthmentLC",amiID=amiID,pemKey=pemKey,sgIDs=sgIDs,instanceType=instanceType,connection=conn)
print testLc.name
print testLc.image_id

"""
newLaunchConfig = change_launch_configuration(lc[0],name=newLcName,amiID=amiID,connection=conn)
"""