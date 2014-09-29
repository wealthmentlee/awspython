import time
import boto.ec2

conn = boto.ec2.connect_to_region("us-east-1")

instance_id = 'i-9d781976'

# Create AMI from instance
newAMIid=conn.create_image(instance_id, 'Third Boto Launched LAMP Instance')
print(newAMIid)
newImage=conn.get_image(newAMIid)
while newImage.state == "pending":
    print newAMIid, newImage.state
    time.sleep(5)
    newImage.update()

print "done", newAMIid