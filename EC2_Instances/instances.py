import boto3

if __name__ == '__main__':

    session = boto3.Session(profile_name='selim')
    ec2 = session.resource('ec2',region_name='ap-southeast-2')

    for i in ec2.instances.all():
           print (i)
