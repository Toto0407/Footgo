#!/usr/bin/env python
import boto3
import os
os.environ['AWS_DEFAULT_REGION'] = 'eu-west-2'
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIA5RC4NBGTUTG44Y6U'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'

client = boto3.client('rds')
instances = client.describe_db_instances(DBInstanceIdentifier='footgo')
rds_host = instances.get('DBInstances')[0].get('Endpoint').get('Address')

newstring='spring.datasource.url=jdbc:mysql://'+str(rds_host) +':3306/footgo'
print(newstring)
f1 = open('/home/webapp/src/main/resources/application.properties.example', 'r')
f2 = open('/home/webapp/src/main/resources/application.properties', 'w')
for line in f1:
    f2.write(line.replace('spring.datasource.url=jdbc:mysql://localhost:3306/footgo?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC', str(newstring)))
f1.close()
f2.close()

