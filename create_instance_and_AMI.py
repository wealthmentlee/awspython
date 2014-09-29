import time
import boto
import boto.ec2.networkinterface

#Variable initialization for instance creation
userData = open("/Users/lee20/git/sewealthement/cloudinit.sh").read()
blockMappings = open("/Users/lee20/git/sewealthement/blockmappings.json").read()
subnetID='subnet-ff7ebf88'
securityGroupIDs = ['sg-8c4607e9','sg-0a57116f']
amiID = 'ami-864d84ee'
instanceType = 't2.micro'
keyName='JeffLee'
placement='us-east-1a'

#Creating connection to aws
conn = boto.ec2.connect_to_region("us-east-1")

#Creating network interface so associate_public_ip_address option can be used otherwise just define subnet id and security groups in the run_instance function
interface = boto.ec2.networkinterface.NetworkInterfaceSpecification(subnet_id=subnetID,
                                                                    groups=securityGroupIDs,
                                                                    associate_public_ip_address=True)
interfaces = boto.ec2.networkinterface.NetworkInterfaceCollection(interface)

#Run create an array of instances with variables
reservation = conn.run_instances(image_id=amiID,
                                instance_type=instanceType,
                                #the following two arguments are provided in the network_interface
                                #instead at the global level !!
                                #'security_group_ids': ['sg-8c4607e9','sg-0a57116f'],
                                #'subnet_id': 'subnet-ff7ebf88',
                                user_data=userData,
                                placement=placement,
                                network_interfaces=interfaces,
                                key_name=keyName)

instance = reservation.instances[0]
#Gets the status of instance to know when additional steps can be run on it
instance.update()
while instance.state == "pending":
    print instance, instance.state
    time.sleep(5)
    instance.update()
#Add tags to the instance
instance.add_tag("Name", "Boto Launched LAMP Instance")

print "done", instance