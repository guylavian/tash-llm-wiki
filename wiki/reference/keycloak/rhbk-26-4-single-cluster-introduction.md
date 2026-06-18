---
title: "Chapter 2. Single-cluster deployments - Red Hat build of Keycloak 26.4 High Availability Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-single-cluster-introduction
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/high_availability_guide/single-cluster-introduction-
guide: high_availability_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
---

# Chapter 2. Single-cluster deployments - Red Hat build of Keycloak 26.4 High Availability Guide

Chapter 2. Single-cluster deployments
Deploy a single Keycloak cluster, optionally across multiple availability-zones.
2.1. When to use a single-cluster setup
The Red Hat build of Keycloak single-cluster setup is targeted at use cases that:
- Deploy to an infrastructure with transparent networking, like for example a single OpenShift cluster.
- Desire all healthy Red Hat build of Keycloak instances to handle user requests.
- Are constrained to a single region (e.g. a single AWS region)
- Permit planned outages for maintenance.
- Fit within a defined user and request count.
- Can accept the impact of periodic outages.
- Deployed in data centers with the required network latency and database configuration
2.2. Tested Configuration
We regularly test Red Hat build of Keycloak with the following configuration:
An OpenShift cluster deployed across three AWS availability zones in the same region.
- Provisioned with Red Hat OpenShift Service on AWS (ROSA), using ROSA HCP.
- At least one worker node for each availability-zone
- OpenShift version 4.17.
Amazon Aurora PostgreSQL database
- High availability with a primary DB instance in one availability zone, and synchronously replicated readers in the other availability zones
- Version 17.5
- Support for Red Hat build of Keycloak in these configurations may require replicating issues in this tested set up.
2.3. Configuration
Red Hat build of Keycloak deployed on an OpenShift cluster version 4.17 or later
- For cloud setups, Pods can be scheduled across up to three availability zones within the same region if OpenShift supports spanning multiple availability zones in that environment and Red Hat build of Keycloak’s latency requirements are met.
- For on-premise setups, Pods can be scheduled across up to three datacenters if OpenShift supports spanning multiple datacenters in that environment and Red Hat build of Keycloak’s latency requirements are met.
- Deployments require a round-trip latency of less than 10 ms between Red Hat build of Keycloak instances.
Database
- For a list of supported databases, see Configuring the database.
- Deployments spanning multiple availability zones must utilize a database that can tolerate zone failures and synchronously replicates data between replicas.
Any deviation from the configuration above is not tested and any issue with Red Hat build of Keycloak may need to be replicated in a tested environment for support.
Read more on each item in the Building blocks single-cluster deployments chapter.
2.4. Maximum load
We regularly test Red Hat build of Keycloak with the following load:
- 100,000 users
- 300 requests per second
See the Concepts for sizing CPU and memory resources chapter for more information.
2.5. Limitations
Even with the additional redundancy of three availability-zones, downtime can still occur when:
- Simultaneous node failures occur
- Rolling out Red Hat build of Keycloak upgrades
- Infrastructure fails, for example the OpenShift cluster
For more details on limitations see the Concepts for single-cluster deployments chapter.
2.6. Next steps
The different chapters introduce the necessary concepts and building blocks. For each building block, a blueprint shows how to deploy a fully functional example. Additional performance tuning and security hardening are still recommended when preparing a production setup.
2.7. Concepts for single-cluster deployments
Understand single-cluster deployment with synchronous replication.
This topic describes a single-cluster setup and the behavior to expect. It outlines the requirements of the high availability architecture and describes the benefits and tradeoffs.
2.7.1. When to use this setup
Use this setup to deploy Red Hat build of Keycloak to an OpenShift cluster.
2.7.2. Single or multiple availability-zones
The behaviour and high-availability performance of the Red Hat build of Keycloak deployment are ultimately determined by the configuration of the OpenShift cluster. Typically, OpenShift clusters are deployed on a single availability-zone, however in order to increase fault-tolerance, it is possible to deploy the cluster across multiple availability-zones.
The Red Hat build of Keycloak Operator defines the following topology spread constraints by default to prefer that Red Hat build of Keycloak pods are deployed on distinct nodes and distinct availability-zones when possible:
topologySpreadConstraints:
- maxSkew: 1
topologyKey: "topology.kubernetes.io/zone"
whenUnsatisfiable: "ScheduleAnyway"
labelSelector:
matchLabels:
app: "keycloak"
app.kubernetes.io/managed-by: "keycloak-operator"
app.kubernetes.io/instance: "keycloak"
app.kubernetes.io/component: "server"
- maxSkew: 1
topologyKey: "kubernetes.io/hostname"
whenUnsatisfiable: "ScheduleAnyway"
labelSelector:
matchLabels:
app: "keycloak"
app.kubernetes.io/managed-by: "keycloak-operator"
app.kubernetes.io/instance: "keycloak"
app.kubernetes.io/component: "server"
In order to configure high-availability with multiple availability-zones, it is crucial that the Database is also able to withstand zone failures as Red Hat build of Keycloak depends on the underlying database to remain available.
2.7.3. Failures which this setup can survive
Deploying Red Hat build of Keycloak on a single cluster in a single zone, or across multiple availability-zones, or data centers with the required network latency and database configuration, changes the high-availability characteristics significantly, therefore we consider these architectures independently.
2.7.3.1. Single Zone
During testing of the high availability Single-cluster deployments, we observed the following restore times for the events described:
| Failure | Recovery | RPO1 | RT2 |
|---|---|---|---|
| Red Hat build of Keycloak Pod | Multiple Red Hat build of Keycloak Pods run in a cluster. If one instance fails some incoming requests might receive an error message or are delayed for some seconds. | No data loss | Less than 30 seconds |
| OpenShift Node | Multiple Red Hat build of Keycloak Pods run in a cluster. If the host node dies, then all pods on that node will fail and some incoming requests might receive an error message or are delayed for some seconds. | No data loss | Less than 30 seconds |
| Red Hat build of Keycloak Clustering Connectivity | If the connectivity between OpenShift nodes is lost, data cannot be sent between Red Hat build of Keycloak pods hosted on those nodes. Incoming requests might receive an error message or be delayed for some seconds. The Red Hat build of Keycloak will eventually remove the unreachable pods from its local view and will stop sending data to them. | No data loss | Seconds to minutes |
Table footnotes:
1 Tested Recovery Point Objective, assuming all parts of the setup were healthy at the time this occurred.
2 Maximum Recovery Time observed.
2.7.3.2. Multiple Zones
During testing of the high availability Multi-cluster deployments, we observed the following restore times for the events described:
| Failure | Recovery | RPO1 | RT2 |
|---|---|---|---|
| Database node3 | If the writer instance fails, the database can promote a reader instance in the same or other zone to be the new writer. | No data loss | Seconds to minutes (depending on the database) |
| Red Hat build of Keycloak pod | Multiple Red Hat build of Keycloak instances run in a cluster. If one instance fails some incoming requests might receive an error message or are delayed for some seconds. | No data loss | Less than 30 seconds |
| OpenShift Node | Multiple Red Hat build of Keycloak pods run in a cluster. If the host node dies, then all pods on that node will fail and some incoming requests might receive an error message or are delayed for some seconds. | No data loss | Less than 30 seconds |
| Availability zone failure | If an availability-zone fails, all Red Hat build of Keycloak pods hosted in that zone will also fail. Deploying at least the same number of Red Hat build of Keycloak replicas as availability-zones should ensure that no data is lost and minimal downtime occurs as there will be other pods available to service requests. | No data loss | Seconds |
| Connectivity database | If the connectivity between availability-zones is lost, the synchronous replication will fail. Some requests might receive an error message or be delayed for a few seconds. Manual operations might be necessary depending on the database. | No data loss3 | Seconds to minutes (depending on the database) |
| Red Hat build of Keycloak Clustering Connectivity | If the connectivity between OpenShift nodes is lost, data cannot be sent between Red Hat build of Keycloak pods hosted on those nodes. Incoming requests might receive an error message or be delayed for some seconds. The Red Hat build of Keycloak will eventually remove the unreachable pods from its local view and will stop sending data to them. | No data loss | Seconds to minutes |
Table footnotes:
1 Tested Recovery Point Objective, assuming all parts of the setup were healthy at the time this occurred.
2 Maximum Recovery Time observed.
3 Assumes that the database is also replicated across multiple availability-zones
2.7.4. Known limitations
Downtime during rollouts of Red Hat build of Keycloak upgrades
This can be overcome for patch releases by enabling Checking if rolling updates are possible.
-
Multiple node failures can result in a loss of entries from the
authenticationSessions
,loginFailures
andactionTokens
caches if the number of node failures is greater than or equal to the cache’s configurednum_owners
, which by default is 2. Deployments using the default
topologySpreadConstraints
withwhenUnsatisfiable: ScheduleAnyway
, may experience data-loss on node/availability-zone failure if multiple pods are scheduled on the failed node/zone.Users can mitigate against this scenario by defining
topologySpreadConstraints
withwhenUnsatisfiable: DoNotSchedule
, to ensure that pods are always evenly scheduled across zones and nodes. However, this can result in some Red Hat build of Keycloak instances not being deployed if the constraints cannot be satisfied.As Infinispan is unaware of the network topology when distributing cache entries, it is still possible for data-loss to occur on node/availability-zone failure if all
num_owner
copies of cached data are stored in the failed node/zone. You can restrict the total number of Red Hat build of Keycloak instances to the number of nodes or availability-zones available by defining arequiredDuringSchedulingIgnoredDuringExecution
for nodes and zones. However, this comes at the expense of scalability as the number of Red Hat build of Keycloak instances that can be provisioned will be restricted to the number of nodes/availability-zones in your OpenShift cluster.See the Operator Advanced configuration details of how to configure custom anti-affinity
topologySpreadConstraints
policies.-
The Operator does not configure the site’s name (see Configuring distributed caches) in the Pods as its value is not available via the Downward API. The machine name option is configured using the
spec.nodeName
from the node where the Pod is scheduled.
2.7.5. Next steps
Continue reading in the Building blocks single-cluster deployments chapter to find blueprints for the different building blocks.
2.8. Building blocks single-cluster deployments
Learn about building blocks and suggested setups for single-cluster deployments.
The following building blocks are needed to set up a single-cluster deployment.
The building blocks link to a blueprint with an example configuration. They are listed in the order in which they need to be installed.
We provide these blueprints to show a minimal functionally complete example with a good baseline performance for regular installations. You would still need to adapt it to your environment and your organization’s standards and security best practices.
2.8.1. Prerequisites
- Understanding the concepts laid out in the Concepts for single-cluster deployments chapter.
2.8.2. Multiple availability-zones with low-latency connection
Red Hat build of Keycloak requires a low latency network connection for the synchronous replication of data by the database and Red Hat build of Keycloak clustering.
A round-trip latency of less than 5 ms is suggested and below 10 ms is required, together with a reliable network between the zones to avoid unexpected problems with latency, throughput or connectivity.
Network latency and latency spikes amplify in the response time of the service and can lead to queued requests, timeouts, and failed requests. Networking problems can cause downtimes until the failure detection isolates problematic nodes.
Suggested setup: OpenShift cluster consisting of two or more AWS Availability Zones within the same AWS Region.
Not considered: OpenShift clusters spread across multiple regions on the same or different continents, as it would increase the latency and the likelihood of network failures. Synchronous replication of databases as services with Aurora Regional Deployments on AWS is only available within the same region.
2.8.3. Database
A synchronously replicated database available across all availability-zones.
Blueprint: Deploying AWS Aurora in multiple availability zones.
2.8.4. Red Hat build of Keycloak
A clustered deployment of Red Hat build of Keycloak with pods distributed across availability-zones.
Blueprint: Deploying Red Hat build of Keycloak across multiple availability-zones with the Operator.
2.9. Concepts for database connection pools
Understand concepts for avoiding resource exhaustion and congestion.
This section is intended when you want to understand considerations and best practices on how to configure database connection pools for Red Hat build of Keycloak. For a configuration where this is applied, visit Deploying Red Hat build of Keycloak across multiple availability-zones with the Operator.
2.9.1. Concepts
Creating new database connections is expensive as it takes time. Creating them when a request arrives will delay the response, so it is good to have them created before the request arrives. It can also contribute to a stampede effect where creating a lot of connections in a short time makes things worse as it slows down the system and blocks threads. Closing a connection also invalidates all server side statements caching for that connection.
For the best performance, the values for the initial, minimal and maximum database connection pool size should all be equal. This avoids creating new database connections when a new request comes in which is costly.
Keeping the database connection open for as long as possible allows for server side statement caching bound to a connection. In the case of PostgreSQL, to use a server-side prepared statement, a query needs to be executed (by default) at least five times.
See the PostgreSQL docs on prepared statements for more information.
2.10. Concepts for configuring thread pools
Understand concepts for avoiding resource exhaustion and congestion.
This section is intended when you want to understand the considerations and best practices on how to configure thread pools connection pools for Red Hat build of Keycloak. For a configuration where this is applied, visit Deploying Red Hat build of Keycloak across multiple availability-zones with the Operator.
2.10.1. Concepts
2.10.1.1. JGroups communications
JGroups communications, which is used in single-cluster setups for the communication between Red Hat build of Keycloak nodes, benefits from the use of virtual threads which are available in OpenJDK 21 when at least four cores are available for Red Hat build of Keycloak. This reduces the memory usage and removes the need to configure thread pool sizes. Therefore, the use of OpenJDK 21 is recommended.
2.10.1.2. Quarkus executor pool
Red Hat build of Keycloak requests, as well as blocking probes, are handled by an executor pool. It has a default maximum size of 50 or more threads depending on the available CPU cores. Threads are created as needed, and will end when no longer needed, so the system will scale up and down automatically. Red Hat build of Keycloak allows configuring the maximum thread pool size by the http-pool-max-threads
configuration option.
2.10.1.3. Load Shedding
By default, Red Hat build of Keycloak will queue all incoming requests infinitely, even if the request processing stalls. This will use additional memory in the Pod, can exhaust resources in the load balancers, and the requests will eventually time out on the client side without the client knowing if the request has been processed. To limit the number of queued requests in Red Hat build of Keycloak, set an additional Quarkus configuration option.
Configure http-max-queued-requests
to specify a maximum queue length to allow for effective load shedding once this queue size is exceeded. Assuming a Red Hat build of Keycloak Pod processes around 200 requests per second, a queue of 1000 would lead to maximum waiting times of around 5 seconds.
When this setting is active, requests that exceed the number of queued requests will return with an HTTP 503 error. Red Hat build of Keycloak logs the error message in its log.
2.10.1.4. Probes
Red Hat build of Keycloak’s liveness probe is non-blocking to avoid a restart of a Pod under a high load.
The overall health probe and the readiness probe can in some cases block to check the connection to the database, so they might fail under a high load. Due to this, a Pod can become non-ready under a high load.
2.10.1.5. OS Resources
In order for Java to create threads, when running on Linux it needs to have file handles available. Therefore, the number of open files (as retrieved as ulimit -n
on Linux) need to provide head-space for Red Hat build of Keycloak to increase the number of threads needed. Each thread will also consume memory, and the container memory limits need to be set to a value that allows for this or the Pod will be killed by OpenShift.
2.11. Concepts for sizing CPU and memory resources
Understand concepts for avoiding resource exhaustion and congestion.
Use this as a starting point to size a product environment. Adjust the values for your environment as needed based on your load tests.
2.11.1. Performance recommendations
- Performance will be lowered when scaling to more Pods (due to additional overhead) and using a multi-cluster setup (due to additional traffic and operations).
- Increased cache sizes can improve the performance when Red Hat build of Keycloak instances running for a longer time. This will decrease response times and reduce IOPS on the database. Still, those caches need to be filled when an instance is restarted, so do not set resources too tight based on the stable state measured once the caches have been filled.
- Use these values as a starting point and perform your own load tests before going into production.
Summary:
- The used CPU scales linearly with the number of requests up to the tested limit below.
Recommendations:
- The base memory usage for a Pod including caches of Realm data and 10,000 cached sessions is 1250 MB of RAM.
- In containers, Keycloak allocates 70% of the memory limit for heap-based memory. It will also use approximately 300 MB of non-heap-based memory. To calculate the requested memory, use the calculation above. As memory limit, subtract the non-heap memory from the value above and divide the result by 0.7.
For each 15 password-based user logins per second, allocate 1 vCPU to the cluster (tested with up to 300 per second).
Red Hat build of Keycloak spends most of the CPU time hashing the password provided by the user, and it is proportional to the number of hash iterations.
For each 120 client credential grants per second, 1 vCPU to the cluster (tested with up to 2000 per second).*
Most CPU time goes into creating new TLS connections, as each client runs only a single request.
- For each 120 refresh token requests per second, 1 vCPU to the cluster (tested with up to 435 refresh token requests per second).*
- Leave 150% extra head-room for CPU usage to handle spikes in the load. This ensures a fast startup of the node, and enough capacity to handle failover tasks. Performance of Red Hat build of Keycloak dropped significantly when its Pods were throttled in our tests.
-
When performing requests with more than 2500 different clients concurrently, not all client information will fit into Red Hat build of Keycloak’s caches when those are using the standard cache sizes of 10000 entries each. Due to this, the database may become a bottleneck as client data is reloaded frequently from the database. To reduce the database usage, increase the
users
cache size by two times the number of concurrently used clients, and therealms
cache size by four times the number of concurrently used clients.
Red Hat build of Keycloak, which by default stores user sessions in the database, requires the following resources for optimal performance on an Aurora PostgreSQL multi-AZ database:
For every 100 login/logout/refresh requests per second:
- Budget for 1400 Write IOPS.
- Allocate between 0.35 and 0.7 vCPU.
The vCPU requirement is given as a range, as with an increased CPU saturation on the database host the CPU usage per request decreases while the response times increase. A lower CPU quota on the database can lead to slower response times during peak loads. Choose a larger CPU quota if fast response times during peak loads are critical. See below for an example.
2.11.1.1. Measuring the activity of a running Red Hat build of Keycloak instance
Sizing of a Red Hat build of Keycloak instance depends on the actual and forecasted numbers for password-based user logins, refresh token requests, and client credential grants as described in the previous section.
To retrieve the actual numbers of a running Red Hat build of Keycloak instance for these three key inputs, use the metrics Red Hat build of Keycloak provides:
-
The user event metric
keycloak_user_events_total
for event typelogin
includes both password-based logins and cookie-based logins, still it can serve as a first approximate input for this sizing guide. -
To find out number of password validations performed by Red Hat build of Keycloak use the metric
keycloak_credentials_password_hashing_validations_total
. The metric also contains tags providing some details about the hashing algorithm used and the outcome of the validation. Here is the list of available tags:realm
,algorithm
,hashing_strength
,outcome
. -
Use the user event metric
keycloak_user_events_total
for the event typesrefresh_token
andclient_login
for refresh token requests and client credential grants respectively.
See the Monitoring user activities with event metrics and HTTP metrics chapters for more information.
These metrics are crucial for tracking daily and weekly fluctuations in user activity loads, identifying emerging trends that may indicate the need to resize the system and validating sizing calculations. By systematically measuring and evaluating these user event metrics, you can ensure your system remains appropriately scaled and responsive to changes in user behavior and demand.
2.11.1.2. Calculation example (single cluster)
Target size:
- 45 logins and logouts per seconds
- 360 client credential grants per second*
- 360 refresh token requests per second (1:8 ratio for logins)*
- 3 Pods
Limits calculated:
CPU requested per Pod: 3 vCPU
(45 logins per second = 3 vCPU, 360 client credential grants per second = 3 vCPU, 360 refresh tokens = 3 vCPU. This sums up to 9 vCPU total. With 3 Pods running in the cluster, each Pod then requests 3 vCPU)
CPU limit per Pod: 7.5 vCPU
(Allow for an additional 150% CPU requested to handle peaks, startups and failover tasks)
Memory requested per Pod: 1250 MB
(1250 MB base memory)
Memory limit per Pod: 1360 MB
(1250 MB expected memory usage minus 300 non-heap-usage, divided by 0.7)
Aurora Database instance: either
db.t4g.large
ordb.t4g.xlarge
depending on the required response times during peak loads.(45 logins per second, 5 logouts per second, 360 refresh tokens per seconds. This sums up to 410 requests per second. This expected DB usage is 1.4 to 2.8 vCPU, with a DB idle load of 0.3 vCPU. This indicates either a 2 vCPU
db.t4g.large
instance or a 4 vCPUdb.t4g.xlarge
instance. A 2 vCPUdb.t4g.large
would be more cost-effective if the response times are allowed to be higher during peak usage. In our tests, the median response time for a login and a token refresh increased by up to 120 ms once the CPU saturation reached 90% on a 2 vCPUdb.t4g.large
instance given this scenario. For faster response times during peak usage, consider a 4 vCPUdb.t4g.xlarge
instance for this scenario.)
2.12. Deploying AWS Aurora in multiple availability zones
Deploy an AWS Aurora as the database building block in a single-cluster deployment.
This topic describes how to deploy an Aurora regional deployment of a PostgreSQL instance across multiple availability zones to tolerate one or more availability zone failures in a given AWS region.
This deployment is intended to be used with the setup described in the Concepts for single-cluster deployments chapter. Use this deployment with the other building blocks outlined in the Building blocks single-cluster deployments chapter.
We provide these blueprints to show a minimal functionally complete example with a good baseline performance for regular installations. You would still need to adapt it to your environment and your organization’s standards and security best practices.
2.12.1. Architecture
Aurora database clusters consist of multiple Aurora database instances, with one instance designated as the primary writer and all others as backup readers. To ensure high availability in the event of availability zone failures, Aurora allows database instances to be deployed across multiple zones in a single AWS region. In the event of a failure on the availability zone that is hosting the Primary database instance, Aurora automatically heals itself and promotes a reader instance from a non-failed availability zone to be the new writer instance.
Figure 2.1. Aurora Multiple Availability Zone Deployment
See the AWS Aurora documentation for more details on the semantics provided by Aurora databases.
This documentation follows AWS best practices and creates a private Aurora database that is not exposed to the Internet. To access the database from a ROSA cluster, establish a peering connection between the database and the ROSA cluster.
2.12.2. Procedure
The following procedure contains two sections:
- Creation of an Aurora Multi-AZ database cluster with the name "keycloak-aurora" in eu-west-1.
- Creation of a peering connection between the ROSA cluster(s) and the Aurora VPC to allow applications deployed on the ROSA clusters to establish connections with the database.
2.12.2.1. Create Aurora database Cluster
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
2.12.2.2. Establish Peering Connection with ROSA cluster
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
2.12.3. Verifying the connection
The simplest way to verify that a connection is possible between a ROSA cluster and an Aurora DB cluster is to deploy psql
on the OpenShift cluster and attempt to connect to the writer endpoint.
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
2.12.4. Connecting Aurora database with Red Hat build of Keycloak
Now that an Aurora database has been established and linked with all of your ROSA clusters, here are the relevant Red Hat build of Keycloak CR options to connect the Aurora database with Red Hat build of Keycloak. These changes will be required in the Deploying Red Hat build of Keycloak across multiple availability-zones with the Operator chapter. The JDBC url is configured to use the Aurora database writer endpoint.
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
2.12.5. Next steps
After successful deployment of the Aurora database continue with Deploying Red Hat build of Keycloak across multiple availability-zones with the Operator
2.13. Deploying Red Hat build of Keycloak across multiple availability-zones with the Operator
Deploy Red Hat build of Keycloak for high availability with the Red Hat build of Keycloak Operator as a building block.
This chapter describes advanced Red Hat build of Keycloak configurations for OpenShift which are load tested and will recover availability-zone failures.
These instructions are intended for use with the setup described in the Concepts for single-cluster deployments chapter. Use it together with the other building blocks outlined in the Building blocks single-cluster deployments chapter.
2.13.1. Prerequisites
- OpenShift cluster deployed across multiple availability-zones with a worker-pool configured for each.
- Understanding of a Basic Red Hat build of Keycloak deployment of Red Hat build of Keycloak with the Red Hat build of Keycloak Operator.
- AWS Aurora database deployed using the Deploying AWS Aurora in multiple availability zones chapter.
2.13.2. Procedure
- Determine the sizing of the deployment using the Concepts for sizing CPU and memory resources chapter.
- Install the Red Hat build of Keycloak Operator as described in the Red Hat build of Keycloak Operator installation chapter.
- Notice the configuration file below contains options relevant for connecting to the Aurora database from Deploying AWS Aurora in multiple availability zones
- Build a custom Red Hat build of Keycloak image which is prepared for usage with the Amazon Aurora PostgreSQL database.
Deploy the Red Hat build of Keycloak CR with the following values with the resource requests and limits calculated in the first step:
apiVersion: k8s.keycloak.org/v2alpha1 kind: Keycloak metadata: labels: app: keycloak name: keycloak namespace: keycloak spec: hostname: hostname: <KEYCLOAK_URL_HERE> resources: requests: cpu: "2" memory: "1250M" limits: cpu: "6" memory: "2250M" db: vendor: postgres url: jdbc:aws-wrapper:postgresql://<AWS_AURORA_URL_HERE>:5432/keycloak poolMinSize: 30
1 poolInitialSize: 30 poolMaxSize: 30 usernameSecret: name: keycloak-db-secret key: username passwordSecret: name: keycloak-db-secret key: password image: <KEYCLOAK_IMAGE_HERE>
2 startOptimized: false
3 additionalOptions: - name: log-console-output value: json - name: metrics-enabled
4 value: 'true' - name: event-metrics-user-enabled value: 'true' - name: db-driver value: software.amazon.jdbc.Driver http: tlsSecret: keycloak-tls-secret instances: 3
- 1
- The database connection pool initial, max and min size should be identical to allow statement caching for the database. Adjust this number to meet the needs of your system. As most requests will not touch the database due to the Red Hat build of Keycloak embedded cache, this change can server several hundreds of requests per second. See the Concepts for database connection pools chapter for details.
- 2 3
- Specify the URL to your custom Red Hat build of Keycloak image. If your image is optimized, set the
startOptimized
flag totrue
. - 4
- To be able to analyze the system under load, enable the metrics endpoint.
2.13.3. Verifying the deployment
Confirm that the Red Hat build of Keycloak deployment is ready.
oc wait --for=condition=Ready keycloaks.k8s.keycloak.org/keycloak
oc wait --for=condition=RollingUpdate=False keycloaks.k8s.keycloak.org/keycloak
2.13.4. Optional: Load shedding
To enable load shedding, limit the number of queued requests.
Load shedding with max queued http requests
spec:
additionalOptions:
- name: http-max-queued-requests
value: "1000"
All exceeding requests are served with an HTTP 503.
You might consider limiting the value for http-pool-max-threads
further because multiple concurrent threads will lead to throttling by OpenShift once the requested CPU limit is reached.
See the Concepts for configuring thread pools chapter about load shedding for details.
2.13.5. Optional: Disable sticky sessions
When running on OpenShift and the default passthrough Ingress setup as provided by the Red Hat build of Keycloak Operator, the load balancing done by HAProxy is done by using sticky sessions based on the IP address of the source. When running load tests, or when having a reverse proxy in front of HAProxy, you might want to disable this setup to avoid receiving all requests on a single Red Hat build of Keycloak Pod.
Add the following supplementary configuration under the spec
in the Red Hat build of Keycloak Custom Resource to disable sticky sessions.
spec:
ingress:
enabled: true
annotations:
# When running load tests, disable sticky sessions on the OpenShift HAProxy router
# to avoid receiving all requests on a single Red Hat build of Keycloak Pod.
haproxy.router.openshift.io/balance: roundrobin
haproxy.router.openshift.io/disable_cookies: 'true'
