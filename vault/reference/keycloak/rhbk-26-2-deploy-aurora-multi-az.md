---
title: "Chapter 8. Deploying AWS Aurora in multiple availability zones - Red Hat build of Keycloak 26.2 High Availability Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-deploy-aurora-multi-az
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/high_availability_guide/deploy-aurora-multi-az-
guide: high_availability_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "Deploy an AWS Aurora as the database building block in a multi-site deployment. This topic describes how to deploy an Aurora regional deployment of a PostgreSQL instance across multiple availability zones to tolerate one or more availability zone failures in a given AWS region. This deployment is intended to be used with the setup described in the Concepts for multi-site deployments chapter. Use t…"
---

# Chapter 8. Deploying AWS Aurora in multiple availability zones - Red Hat build of Keycloak 26.2 High Availability Guide

Chapter 8. Deploying AWS Aurora in multiple availability zones
Deploy an AWS Aurora as the database building block in a multi-site deployment.
This topic describes how to deploy an Aurora regional deployment of a PostgreSQL instance across multiple availability zones to tolerate one or more availability zone failures in a given AWS region.
This deployment is intended to be used with the setup described in the Concepts for multi-site deployments chapter. Use this deployment with the other building blocks outlined in the Building blocks multi-site deployments chapter.
We provide these blueprints to show a minimal functionally complete example with a good baseline performance for regular installations. You would still need to adapt it to your environment and your organization’s standards and security best practices.
8.1. Architecture
Aurora database clusters consist of multiple Aurora database instances, with one instance designated as the primary writer and all others as backup readers. To ensure high availability in the event of availability zone failures, Aurora allows database instances to be deployed across multiple zones in a single AWS region. In the event of a failure on the availability zone that is hosting the Primary database instance, Aurora automatically heals itself and promotes a reader instance from a non-failed availability zone to be the new writer instance.
Figure 8.1. Aurora Multiple Availability Zone Deployment
See the AWS Aurora documentation for more details on the semantics provided by Aurora databases.
This documentation follows AWS best practices and creates a private Aurora database that is not exposed to the Internet. To access the database from a ROSA cluster, establish a peering connection between the database and the ROSA cluster.
8.2. Procedure
The following procedure contains two sections:
- Creation of an Aurora Multi-AZ database cluster with the name "keycloak-aurora" in eu-west-1.
- Creation of a peering connection between the ROSA cluster(s) and the Aurora VPC to allow applications deployed on the ROSA clusters to establish connections with the database.
8.2.1. Create Aurora database Cluster
Create a VPC for the Aurora cluster
Command:
aws ec2 create-vpc \ --cidr-block 192.168.0.0/16 \ --tag-specifications "ResourceType=vpc, Tags=[{Key=AuroraCluster,Value=keycloak-aurora}]" \
1 --region eu-west-1
- 1
- We add an optional tag with the name of the Aurora cluster so that we can easily retrieve the VPC.
Output:
{ "Vpc": { "CidrBlock": "192.168.0.0/16", "DhcpOptionsId": "dopt-0bae7798158bc344f", "State": "pending", "VpcId": "vpc-0b40bd7c59dbe4277", "OwnerId": "606671647913", "InstanceTenancy": "default", "Ipv6CidrBlockAssociationSet": [], "CidrBlockAssociationSet": [ { "AssociationId": "vpc-cidr-assoc-09a02a83059ba5ab6", "CidrBlock": "192.168.0.0/16", "CidrBlockState": { "State": "associated" } } ], "IsDefault": false } }
Create a subnet for each availability zone that Aurora will be deployed to, using the
VpcId
of the newly created VPC.NoteThe cidr-block range specified for each of the availability zones must not overlap.
Zone A
Command:
aws ec2 create-subnet \ --availability-zone "eu-west-1a" \ --vpc-id vpc-0b40bd7c59dbe4277 \ --cidr-block 192.168.0.0/19 \ --region eu-west-1
Output:
{ "Subnet": { "AvailabilityZone": "eu-west-1a", "AvailabilityZoneId": "euw1-az3", "AvailableIpAddressCount": 8187, "CidrBlock": "192.168.0.0/19", "DefaultForAz": false, "MapPublicIpOnLaunch": false, "State": "available", "SubnetId": "subnet-0d491a1a798aa878d", "VpcId": "vpc-0b40bd7c59dbe4277", "OwnerId": "606671647913", "AssignIpv6AddressOnCreation": false, "Ipv6CidrBlockAssociationSet": [], "SubnetArn": "arn:aws:ec2:eu-west-1:606671647913:subnet/subnet-0d491a1a798aa878d", "EnableDns64": false, "Ipv6Native": false, "PrivateDnsNameOptionsOnLaunch": { "HostnameType": "ip-name", "EnableResourceNameDnsARecord": false, "EnableResourceNameDnsAAAARecord": false } } }
Zone B
Command:
aws ec2 create-subnet \ --availability-zone "eu-west-1b" \ --vpc-id vpc-0b40bd7c59dbe4277 \ --cidr-block 192.168.32.0/19 \ --region eu-west-1
Output:
{ "Subnet": { "AvailabilityZone": "eu-west-1b", "AvailabilityZoneId": "euw1-az1", "AvailableIpAddressCount": 8187, "CidrBlock": "192.168.32.0/19", "DefaultForAz": false, "MapPublicIpOnLaunch": false, "State": "available", "SubnetId": "subnet-057181b1e3728530e", "VpcId": "vpc-0b40bd7c59dbe4277", "OwnerId": "606671647913", "AssignIpv6AddressOnCreation": false, "Ipv6CidrBlockAssociationSet": [], "SubnetArn": "arn:aws:ec2:eu-west-1:606671647913:subnet/subnet-057181b1e3728530e", "EnableDns64": false, "Ipv6Native": false, "PrivateDnsNameOptionsOnLaunch": { "HostnameType": "ip-name", "EnableResourceNameDnsARecord": false, "EnableResourceNameDnsAAAARecord": false } } }
Obtain the ID of the Aurora VPC route-table
Command:
aws ec2 describe-route-tables \ --filters Name=vpc-id,Values=vpc-0b40bd7c59dbe4277 \ --region eu-west-1
Output:
{ "RouteTables": [ { "Associations": [ { "Main": true, "RouteTableAssociationId": "rtbassoc-02dfa06f4c7b4f99a", "RouteTableId": "rtb-04a644ad3cd7de351", "AssociationState": { "State": "associated" } } ], "PropagatingVgws": [], "RouteTableId": "rtb-04a644ad3cd7de351", "Routes": [ { "DestinationCidrBlock": "192.168.0.0/16", "GatewayId": "local", "Origin": "CreateRouteTable", "State": "active" } ], "Tags": [], "VpcId": "vpc-0b40bd7c59dbe4277", "OwnerId": "606671647913" } ] }
Associate the Aurora VPC route-table each availability zone’s subnet
Zone A
Command:
aws ec2 associate-route-table \ --route-table-id rtb-04a644ad3cd7de351 \ --subnet-id subnet-0d491a1a798aa878d \ --region eu-west-1
Zone B
Command:
aws ec2 associate-route-table \ --route-table-id rtb-04a644ad3cd7de351 \ --subnet-id subnet-057181b1e3728530e \ --region eu-west-1
Create Aurora Subnet Group
Command:
aws rds create-db-subnet-group \ --db-subnet-group-name keycloak-aurora-subnet-group \ --db-subnet-group-description "Aurora DB Subnet Group" \ --subnet-ids subnet-0d491a1a798aa878d subnet-057181b1e3728530e \ --region eu-west-1
Create Aurora Security Group
Command:
aws ec2 create-security-group \ --group-name keycloak-aurora-security-group \ --description "Aurora DB Security Group" \ --vpc-id vpc-0b40bd7c59dbe4277 \ --region eu-west-1
Output:
{ "GroupId": "sg-0d746cc8ad8d2e63b" }
Create the Aurora DB Cluster
Command:
aws rds create-db-cluster \ --db-cluster-identifier keycloak-aurora \ --database-name keycloak \ --engine aurora-postgresql \ --engine-version ${properties["aurora-postgresql.version"]} \ --master-username keycloak \ --master-user-password secret99 \ --vpc-security-group-ids sg-0d746cc8ad8d2e63b \ --db-subnet-group-name keycloak-aurora-subnet-group \ --region eu-west-1
NoteYou should replace the
--master-username
and--master-user-password
values. The values specified here must be used when configuring the Red Hat build of Keycloak database credentials.Output:
{ "DBCluster": { "AllocatedStorage": 1, "AvailabilityZones": [ "eu-west-1b", "eu-west-1c", "eu-west-1a" ], "BackupRetentionPeriod": 1, "DatabaseName": "keycloak", "DBClusterIdentifier": "keycloak-aurora", "DBClusterParameterGroup": "default.aurora-postgresql15", "DBSubnetGroup": "keycloak-aurora-subnet-group", "Status": "creating", "Endpoint": "keycloak-aurora.cluster-clhthfqe0h8p.eu-west-1.rds.amazonaws.com", "ReaderEndpoint": "keycloak-aurora.cluster-ro-clhthfqe0h8p.eu-west-1.rds.amazonaws.com", "MultiAZ": false, "Engine": "aurora-postgresql", "EngineVersion": "15.5", "Port": 5432, "MasterUsername": "keycloak", "PreferredBackupWindow": "02:21-02:51", "PreferredMaintenanceWindow": "fri:03:34-fri:04:04", "ReadReplicaIdentifiers": [], "DBClusterMembers": [], "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-0d746cc8ad8d2e63b", "Status": "active" } ], "HostedZoneId": "Z29XKXDKYMONMX", "StorageEncrypted": false, "DbClusterResourceId": "cluster-IBWXUWQYM3MS5BH557ZJ6ZQU4I", "DBClusterArn": "arn:aws:rds:eu-west-1:606671647913:cluster:keycloak-aurora", "AssociatedRoles": [], "IAMDatabaseAuthenticationEnabled": false, "ClusterCreateTime": "2023-11-01T10:40:45.964000+00:00", "EngineMode": "provisioned", "DeletionProtection": false, "HttpEndpointEnabled": false, "CopyTagsToSnapshot": false, "CrossAccountClone": false, "DomainMemberships": [], "TagList": [], "AutoMinorVersionUpgrade": true, "NetworkType": "IPV4" } }
Create Aurora DB instances
Create Zone A Writer instance
Command:
aws rds create-db-instance \ --no-auto-minor-version-upgrade \ --db-cluster-identifier keycloak-aurora \ --db-instance-identifier "keycloak-aurora-instance-1" \ --db-instance-class db.t4g.large \ --engine aurora-postgresql \ --region eu-west-1
Create Zone B Reader instance
Command:
aws rds create-db-instance \ --no-auto-minor-version-upgrade \ --db-cluster-identifier keycloak-aurora \ --db-instance-identifier "keycloak-aurora-instance-2" \ --db-instance-class db.t4g.large \ --engine aurora-postgresql \ --region eu-west-1
Wait for all Writer and Reader instances to be ready
Command:
aws rds wait db-instance-available --db-instance-identifier keycloak-aurora-instance-1 --region eu-west-1 aws rds wait db-instance-available --db-instance-identifier keycloak-aurora-instance-2 --region eu-west-1
Obtain the Writer endpoint URL for use by Keycloak
Command:
aws rds describe-db-clusters \ --db-cluster-identifier keycloak-aurora \ --query 'DBClusters[*].Endpoint' \ --region eu-west-1 \ --output text
Output:
[ "keycloak-aurora.cluster-clhthfqe0h8p.eu-west-1.rds.amazonaws.com" ]
8.2.2. Establish Peering Connections with ROSA clusters
Perform these steps once for each ROSA cluster that contains a Red Hat build of Keycloak deployment.
Retrieve the Aurora VPC
Command:
aws ec2 describe-vpcs \ --filters "Name=tag:AuroraCluster,Values=keycloak-aurora" \ --query 'Vpcs[*].VpcId' \ --region eu-west-1 \ --output text
Output:
vpc-0b40bd7c59dbe4277
Retrieve the ROSA cluster VPC
-
Log in to the ROSA cluster using
oc
Retrieve the ROSA VPC
Command:
NODE=$(oc get nodes --selector=node-role.kubernetes.io/worker -o jsonpath='{.items[0].metadata.name}') aws ec2 describe-instances \ --filters "Name=private-dns-name,Values=${NODE}" \ --query 'Reservations[0].Instances[0].VpcId' \ --region eu-west-1 \ --output text
Output:
vpc-0b721449398429559
-
Log in to the ROSA cluster using
Create Peering Connection
Command:
aws ec2 create-vpc-peering-connection \ --vpc-id vpc-0b721449398429559 \
1 --peer-vpc-id vpc-0b40bd7c59dbe4277 \
2 --peer-region eu-west-1 \ --region eu-west-1
Output:
{ "VpcPeeringConnection": { "AccepterVpcInfo": { "OwnerId": "606671647913", "VpcId": "vpc-0b40bd7c59dbe4277", "Region": "eu-west-1" }, "ExpirationTime": "2023-11-08T13:26:30+00:00", "RequesterVpcInfo": { "CidrBlock": "10.0.17.0/24", "CidrBlockSet": [ { "CidrBlock": "10.0.17.0/24" } ], "OwnerId": "606671647913", "PeeringOptions": { "AllowDnsResolutionFromRemoteVpc": false, "AllowEgressFromLocalClassicLinkToRemoteVpc": false, "AllowEgressFromLocalVpcToRemoteClassicLink": false }, "VpcId": "vpc-0b721449398429559", "Region": "eu-west-1" }, "Status": { "Code": "initiating-request", "Message": "Initiating Request to 606671647913" }, "Tags": [], "VpcPeeringConnectionId": "pcx-0cb23d66dea3dca9f" } }
Wait for Peering connection to exist
Command:
aws ec2 wait vpc-peering-connection-exists --vpc-peering-connection-ids pcx-0cb23d66dea3dca9f
Accept the peering connection
Command:
aws ec2 accept-vpc-peering-connection \ --vpc-peering-connection-id pcx-0cb23d66dea3dca9f \ --region eu-west-1
Output:
{ "VpcPeeringConnection": { "AccepterVpcInfo": { "CidrBlock": "192.168.0.0/16", "CidrBlockSet": [ { "CidrBlock": "192.168.0.0/16" } ], "OwnerId": "606671647913", "PeeringOptions": { "AllowDnsResolutionFromRemoteVpc": false, "AllowEgressFromLocalClassicLinkToRemoteVpc": false, "AllowEgressFromLocalVpcToRemoteClassicLink": false }, "VpcId": "vpc-0b40bd7c59dbe4277", "Region": "eu-west-1" }, "RequesterVpcInfo": { "CidrBlock": "10.0.17.0/24", "CidrBlockSet": [ { "CidrBlock": "10.0.17.0/24" } ], "OwnerId": "606671647913", "PeeringOptions": { "AllowDnsResolutionFromRemoteVpc": false, "AllowEgressFromLocalClassicLinkToRemoteVpc": false, "AllowEgressFromLocalVpcToRemoteClassicLink": false }, "VpcId": "vpc-0b721449398429559", "Region": "eu-west-1" }, "Status": { "Code": "provisioning", "Message": "Provisioning" }, "Tags": [], "VpcPeeringConnectionId": "pcx-0cb23d66dea3dca9f" } }
Update ROSA cluster VPC route-table
Command:
ROSA_PUBLIC_ROUTE_TABLE_ID=$(aws ec2 describe-route-tables \ --filters "Name=vpc-id,Values=vpc-0b721449398429559" "Name=association.main,Values=true" \
1 --query "RouteTables[*].RouteTableId" \ --output text \ --region eu-west-1 ) aws ec2 create-route \ --route-table-id ${ROSA_PUBLIC_ROUTE_TABLE_ID} \ --destination-cidr-block 192.168.0.0/16 \
2 --vpc-peering-connection-id pcx-0cb23d66dea3dca9f \ --region eu-west-1
Update the Aurora Security Group
Command:
AURORA_SECURITY_GROUP_ID=$(aws ec2 describe-security-groups \ --filters "Name=group-name,Values=keycloak-aurora-security-group" \ --query "SecurityGroups[*].GroupId" \ --region eu-west-1 \ --output text ) aws ec2 authorize-security-group-ingress \ --group-id ${AURORA_SECURITY_GROUP_ID} \ --protocol tcp \ --port 5432 \ --cidr 10.0.17.0/24 \
1 --region eu-west-1
- 1
- The "machine_cidr" of the ROSA cluster
Output:
{ "Return": true, "SecurityGroupRules": [ { "SecurityGroupRuleId": "sgr-0785d2f04b9cec3f5", "GroupId": "sg-0d746cc8ad8d2e63b", "GroupOwnerId": "606671647913", "IsEgress": false, "IpProtocol": "tcp", "FromPort": 5432, "ToPort": 5432, "CidrIpv4": "10.0.17.0/24" } ] }
8.3. Verifying the connection
The simplest way to verify that a connection is possible between a ROSA cluster and an Aurora DB cluster is to deploy psql
on the Openshift cluster and attempt to connect to the writer endpoint.
The following command creates a pod in the default namespace and establishes a psql
connection with the Aurora cluster if possible. Upon exiting the pod shell, the pod is deleted.
USER=keycloak
PASSWORD=secret99
DATABASE=keycloak
HOST=$(aws rds describe-db-clusters \
--db-cluster-identifier keycloak-aurora \
--query 'DBClusters[*].Endpoint' \
--region eu-west-1 \
--output text
)
oc run -i --tty --rm debug --image=postgres:15 --restart=Never -- psql postgresql://${USER}:${PASSWORD}@${HOST}/${DATABASE}
8.4. Connecting Aurora database with Red Hat build of Keycloak
Now that an Aurora database has been established and linked with all of your ROSA clusters, here are the relevant Red Hat build of Keycloak CR options to connect the Aurora database with Red Hat build of Keycloak. These changes will be required in the Deploying Red Hat build of Keycloak for HA with the Operator chapter. The JDBC url is configured to use the Aurora database writer endpoint.
-
Update
spec.db.url
to bejdbc:aws-wrapper:postgresql://$HOST:5432/keycloak
where$HOST
is the Aurora writer endpoint URL. -
Ensure that the Secrets referenced by
spec.db.usernameSecret
andspec.db.passwordSecret
contain usernames and passwords defined when creating Aurora.
8.5. Next steps
After successful deployment of the Aurora database continue with Deploying Data Grid for HA with the Data Grid Operator
