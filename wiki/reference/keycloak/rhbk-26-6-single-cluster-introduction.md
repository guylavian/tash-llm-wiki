---
title: "Chapter 2. Single-cluster deployments - Red Hat build of Keycloak 26.6 High Availability Guide"
type: reference
domain: keycloak
slug: rhbk-26-6-single-cluster-introduction
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/high_availability_guide/single-cluster-introduction-
guide: high_availability_guide
version: 26.6
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 2. Single-cluster deployments - Red Hat build of Keycloak 26.6 High Availability Guide

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
- OpenShift version 4.18.
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
- 1,000,000 users
- 300 requests per second
It is imperative that your production deployments are integrated with an observability stack in order to identify issues early and facilitate troubleshooting when they do arise. Additional demand on Red Hat build of Keycloak makes isolating issues harder, therefore this becomes increasingly pertinent as the total number of users and requests per second increases.
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
2.8.3.1. Aurora
Blueprint: Deploying AWS Aurora in multiple availability zones.
2.8.3.2. CloudNativePG
Blueprint: Deploying CloudNativePG in multiple availability zones.
Blueprint: Deploying CloudNativePG with scheduled backups to S3.
Blueprint: Recovering a CloudNativePG cluster from an S3 backup.
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
JGroups communications, which is used in single-cluster setups for the communication between Red Hat build of Keycloak nodes, benefits from the use of virtual threads which are available in OpenJDK 21 or later when at least four cores are available for Red Hat build of Keycloak. This reduces the memory usage and removes the need to configure thread pool sizes. For best performance, use OpenJDK 25 or later.
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
2.11.1.1. Measure the activity of a running Red Hat build of Keycloak instance
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
2.12.3. Verify the connection
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
2.12.4. Next steps
After successful deployment of the Aurora database continue with Deploying Red Hat build of Keycloak across multiple availability-zones with the Operator
2.13. Deploying CloudNativePG in multiple availability zones
Deploy CloudNativePG as the database building block in a single-cluster deployment.
This topic describes how to deploy a CloudNativePG cluster across multiple availability zones to tolerate one or more availability zone failures in a given AWS region.
This deployment is intended to be used with the setup described in the Concepts for single-cluster deployments chapter. Use this deployment with the other building blocks outlined in the Building blocks single-cluster deployments chapter.
We provide these blueprints to show a minimal functionally complete example with a good baseline performance for regular installations. You would still need to adapt it to your environment and your organization’s standards and security best practices.
2.13.1. Architecture
CloudNativePG is an opensource operator that manages PostgreSQL clusters on OpenShift. It is designed to operate one primary writer instance and optional reader instances.
As this setup uses standard a PostgreSQL image that does not support Transparent Data Encryption (TDE), all storage devices for the database and write-ahead logs (WAL) should be placed on encrypted storage. See Configuring the database for more information.
2.13.2. Install CloudNativePG
2.13.2.1. Install the CloudNativePG Operator
Install the operator directly using the operator manifest:
Command:
oc apply --server-side -f \
https://raw.githubusercontent.com/cloudnative-pg/cloudnative-pg/release-1.29/releases/cnpg-1.29.0.yaml
Use the following command to verify the installation status:
Command:
oc rollout status deployment \
-n cnpg-system cnpg-controller-manager
Output:
deployment "cnpg-controller-manager" successfully rolled out
It is possible to install the operator using other supported methods such as Helm Chart, OLM, or cnpg
plugin for oc
. See the CloudNativePG documentation for details.
2.13.2.2. Install CloudNativePG Cluster
We recommend enabling backups for the CloudNativePG cluster to protect against data loss. See Deploying CloudNativePG with scheduled backups to S3 for instructions on configuring scheduled backups to AWS S3.
Installation and configuration of CloudNativePG cluster is done via a Cluster
resource.
Create a
cluster.yaml
file based on the following content:Cluster resource:
apiVersion: postgresql.cnpg.io/v1 kind: Cluster metadata: name: cnpg-keycloak spec: instances: 3
1 storage: size: 8Gi
2 affinity:
3 podAntiAffinityType: required topologyKey: topology.kubernetes.io/zone postgresql: synchronous:
4 method: any number: 1 parameters: max_connections: "100"
5 bootstrap: initdb:
6 database: keycloak owner: keycloak managed: services: disabledDefaultServices: ["ro", "r"]
7 - 1
- Number of instances.
- 2
- Pod storage size. This setting needs to take into account the expected size of the database and PostgreSQL WAL logs.
- 3
- Pod affinity rules for Kubernetes scheduler. The
topology.kubernetes.io/zone
value ensures the scheduler will spread the pods across different availability zones. - 4
- Enable quorum-based synchronous replication with a single standby server. For more information about synchronous replication follow the CloudNativePG documentation.
- 5
- Maximum number of concurrent connections to the database server. This value needs to be adjusted based on the expected maximum number of connections from the Red Hat build of Keycloak cluster. For example, if the Red Hat build of Keycloak cluster has 3 instances with a maximum of 30 JDBC connections per instance (see the Red Hat build of Keycloak option
db-pool-max-size
), the value ofspec.postgresql.max_connections
needs to be at least90
to account for the required connection capacity. For additional considerations about configuring database connections for Red Hat build of Keycloak see Concepts for database connection pools. - 6
- Creates a database
keycloak
owned by the userkeycloak
. - 7
- Disables the
-ro
and-r
default services which are intended for read-only applications. Since Red Hat build of Keycloak requires a read-write access it only connects to the-rw
service.
Create the
cnpg-keycloak
namespace.Command:
oc create ns cnpg-keycloak
Create the
cnpg-keycloak
cluster resource by applying thecluster.yaml
file.Command:
oc -n cnpg-keycloak apply -f cluster.yaml
Wait for the
cnpg-keycloak
cluster to get into theReady
state.Command:
oc -n cnpg-keycloak wait --for condition=Ready --timeout=300s cluster cnpg-keycloak
Output:
cluster.postgresql.cnpg.io/cnpg-keycloak condition met
Optionally, view the
cnpg-keycloak
cluster pods and their roles.Command:
oc -n cnpg-keycloak get pods -L role
Example output:
NAME READY STATUS RESTARTS AGE ROLE cnpg-keycloak-1 1/1 Running 0 10m primary cnpg-keycloak-2 1/1 Running 0 10m replica cnpg-keycloak-3 1/1 Running 0 10m replica
2.13.3. Next steps
After successful deployment of the CloudNativePG database continue with Deploying Red Hat build of Keycloak across multiple availability-zones with the Operator
2.14. Deploying CloudNativePG with scheduled backups to S3
Deploy CloudNativePG with the Barman Cloud plugin and scheduled backups to AWS S3.
This topic describes how to configure backup and restore for a CloudNativePG cluster using the Barman Cloud plugin with AWS S3 as the object store.
These instructions are intended for use with the setup described in the Concepts for single-cluster deployments chapter. Use it together with the other building blocks outlined in the Building blocks single-cluster deployments chapter.
We provide these blueprints to show a minimal functionally complete example with a good baseline performance for regular installations. You would still need to adapt it to your environment and your organization’s standards and security best practices.
2.14.1. Architecture
As this setup does not support encrypted backups, the S3 bucket should be encrypted. Newly created AWS S3 buckets are encrypted by default. See Configuring the database for more information.
2.14.2. Install the CloudNativePG Operator with Barman Cloud plugin
Both the CloudNativePG operator and the Barman Cloud plugin are required in order to enable backup and restore operations using an S3-compatible object store.
2.14.2.1. Install the CloudNativePG Operator
Install the CloudNativePG Operator as described in Deploying CloudNativePG in multiple availability zones.
2.14.2.2. Install cert-manager
The Barman Cloud plugin requires cert-manager. Install it using the following commands or, alternatively, any other method described in the cert-manager installation docs:
Command:
oc apply --filename=https://github.com/cert-manager/cert-manager/releases/download/v1.20.0/cert-manager.yaml
Wait for the cert-manager deployments to be ready:
Command:
oc rollout status deployment --namespace=cert-manager cert-manager-webhook
oc rollout status deployment --namespace=cert-manager cert-manager
Output:
deployment "cert-manager-webhook" successfully rolled out
deployment "cert-manager" successfully rolled out
2.14.2.3. Install the Barman Cloud plugin
Install the Barman Cloud plugin:
Command:
oc apply --filename=https://github.com/cloudnative-pg/plugin-barman-cloud/releases/download/v0.11.0/manifest.yaml
Wait for the Barman Cloud deployment to be ready:
Command:
oc rollout status deployment --namespace=cnpg-system barman-cloud
Output:
deployment "barman-cloud" successfully rolled out
2.14.3. Create the AWS credentials secret
This blueprint uses AWS S3 as the object store. Refer to the Barman Cloud plugin object stores documentation for details on how to configure other cloud providers.
This blueprint uses AWS access keys for authentication. Other authentication methods, such as IAM Roles for Service Accounts (IRSA), are also supported. Refer to the Barman Cloud plugin AWS S3 documentation for more details.
Create a Kubernetes secret with the AWS credentials required to access the S3 bucket. The secret must be created in the same namespace as the CloudNativePG cluster.
Command:
oc create secret generic aws-creds \
--namespace cnpg-keycloak \
--from-literal=ACCESS_KEY_ID=<access_key> \
--from-literal=ACCESS_SECRET_KEY=<secret_key> \
--from-literal=REGION=<region>
2.14.4. Create the ObjectStore
The ObjectStore
resource defines the S3 bucket destination and encryption settings for backups and WAL archiving. The example below uses AWS S3, but the Barman Cloud plugin also supports Azure Blob Storage and Google Cloud Storage. For details on configuring other cloud providers, refer to the Barman Cloud plugin object stores documentation.
The S3 bucket must be created before configuring the ObjectStore
resource. CloudNativePG does not create the bucket automatically. Refer to the AWS S3 documentation for instructions on creating a bucket. For recommended bucket configuration settings such as lifecycle policies, refer to the Barman Cloud plugin S3 lifecycle policy documentation.
Create an
object-store.yaml
file based on the following content:ObjectStore resource:
apiVersion: barmancloud.cnpg.io/v1 kind: ObjectStore metadata: name: cnpg-store spec: configuration: destinationPath: s3://<bucket-name>/<backup-path>/
1 s3Credentials: accessKeyId: name: aws-creds
2 key: ACCESS_KEY_ID secretAccessKey: name: aws-creds key: ACCESS_SECRET_KEY region: name: aws-creds key: REGION wal:
3 encryption: AES256 compression: gzip maxParallel: 8 data:
4 compression: gzip encryption: AES256
- 1
- The S3 bucket destination path for backups. Replace
<bucket-name>
and<backup-path>
with the appropriate values. - 2
- References the
aws-creds
secret created in the previous step. - 3
- WAL archiving configuration with server-side encryption and gzip compression.
maxParallel
controls the number of WAL files to be archived in parallel. For other supported compression algorithms, refer to the Barman Cloud plugin compression documentation. - 4
- Base backup data configuration with compression and encryption.
Apply the
ObjectStore
resource:Command:
oc apply --namespace=cnpg-keycloak --filename=object-store.yaml
2.14.5. Configure CloudNativePG cluster backups
Adding the Barman Cloud plugin to a running CloudNativePG cluster may cause downtime as the Pods are restarted.
Create the CloudNativePG Cluster
resource to enable backup and WAL archiving to the object store using the Barman Cloud plugin.
Create the
cluster.yaml
file to include theplugins
section:Cluster resource:
apiVersion: postgresql.cnpg.io/v1 kind: Cluster metadata: name: cnpg-keycloak spec: instances: 3
1 storage: size: 8Gi
2 affinity:
3 podAntiAffinityType: required topologyKey: topology.kubernetes.io/zone postgresql: synchronous:
4 method: any number: 1 dataDurability: required parameters: max_connections: "100"
5 bootstrap: initdb:
6 database: keycloak owner: keycloak managed: services: disabledDefaultServices: ["ro", "r"]
7 plugins:
8 - name: barman-cloud.cloudnative-pg.io isWALArchiver: true parameters: barmanObjectName: cnpg-store
- 1
- Number of instances.
- 2
- Pod storage size. This setting needs to take into account the expected size of the database and PostgreSQL WAL logs.
- 3
- Pod affinity rules for Kubernetes scheduler. The
topology.kubernetes.io/zone
value ensures the scheduler will spread the pods across different availability zones. - 4
- Enables quorum-based synchronous replication with a single standby server. For more information about synchronous replication, see the CloudNativePG documentation.
- 5
- Database connection limit. This value should be adjusted based on the expected total number of JDBC connections from the Red Hat build of Keycloak cluster.
- 6
- Creates a database
keycloak
owned by the userkeycloak
. - 7
- Disables the
-ro
and-r
default services, which are intended for read-only applications. Since Red Hat build of Keycloak requires read-write access, it only connects to the-rw
service. - 8
- Enables the Barman Cloud plugin for WAL archiving. The
barmanObjectName
references theObjectStore
resource created in the previous step.
Apply the updated cluster resource:
Command:
oc -n cnpg-keycloak apply -f cluster.yaml
Wait for the
cnpg-keycloak
cluster to get into theReady
state.Command:
oc -n cnpg-keycloak wait --for condition=Ready --timeout=300s cluster cnpg-keycloak
Output:
cluster.postgresql.cnpg.io/cnpg-keycloak condition met
2.14.6. Enable scheduled backups
The ScheduledBackup
resource enables automatic periodic backups of the CloudNativePG cluster. Scheduled backups are the recommended way to implement a reliable backup strategy.
Create a
scheduled-backup.yaml
file based on the following content:ScheduledBackup resource:
apiVersion: postgresql.cnpg.io/v1 kind: ScheduledBackup metadata: name: cnpg-keycloak-scheduled-backup spec: schedule: "0 0 0 * * *"
1 backupOwnerReference: self
2 cluster: name: cnpg-keycloak
3 method: plugin
4 pluginConfiguration: name: barman-cloud.cloudnative-pg.io
5 immediate: true
6 suspend: false
7 - 1
- Cron schedule expression using a six-field format that includes seconds:
seconds minutes hours day-of-month month day-of-week
. This example runs at midnight every day. Adjust the schedule based on the Recovery Point Objective (RPO) requirements. - 2
- Sets the ownership reference for the backup objects.
self
means theScheduledBackup
resource owns the created backups, and deleting it will also delete all associated backups. - 3
- The name of the CloudNativePG cluster to back up.
- 4
- The backup method.
plugin
delegates the backup operation to the configured plugin. - 5
- The Barman Cloud plugin that performs the backup to the object store.
- 6
- Triggers a backup immediately upon creation of the
ScheduledBackup
resource, in addition to the configured schedule. - 7
- When set to
true
, temporarily suspends scheduled backups without deleting the resource.
Apply the
ScheduledBackup
resource:Command:
oc apply --namespace=cnpg-keycloak --filename=scheduled-backup.yaml
Verify the scheduled backup has been created:
Command:
oc -n cnpg-keycloak get scheduledbackups
Example output:
NAME AGE CLUSTER LAST BACKUP cnpg-keycloak-scheduled-backup 30s cnpg-keycloak
2.14.7. Next steps
After successful configuration of the backup, continue with Deploying Red Hat build of Keycloak across multiple availability-zones with the Operator.
For details of how to restore a CloudNativePG cluster from a backup, see Recovering a CloudNativePG cluster from an S3 backup.
For more information about backup and recovery operations, refer to the CloudNativePG documentation.
2.15. Monitoring CloudNativePG
Observing standby health and replication status in a CloudNativePG cluster.
These instructions are intended for use with the setup described in the Concepts for single-cluster deployments chapter. Use it together with the other building blocks outlined in the Building blocks single-cluster deployments chapter.
We provide these blueprints to show a minimal functionally complete example with a good baseline performance for regular installations. You would still need to adapt it to your environment and your organization’s standards and security best practices.
2.15.1. When to use this procedure
In a CloudNativePG cluster deployed in high availability mode, standby instances are critical for both data durability and failover readiness. Monitoring standby health helps detect replication issues early and ensures a safe promotion candidate is available when needed.
2.15.2. Prerequisites
- A CloudNativePG cluster deployed according to steps described in the Deploying CloudNativePG in multiple availability zones chapter.
To see the status on the command line:
-
The
oc
command-line utility. -
The
oc cnpg
plugin. Please follow the CloudNativePG documentation for installation steps.
To monitor the status via metrics and dashboards:
- Prometheus and Grafana installed on the OpenShift cluster.
2.15.3. Review the status through command-line
Review the status of the CloudNativePG cluster using the
oc cnpg status
command.Command:
oc cnpg status -n cnpg-keycloak cnpg-keycloak
Output:
Cluster Summary Name cnpg-keycloak/cnpg-keycloak System ID: ******************* PostgreSQL Image: ghcr.io/cloudnative-pg/postgresql:18.3-system-trixie Primary instance: cnpg-keycloak-1 Primary promotion time: 2026-04-13 16:02:05 +0000 UTC (1h10m27s) Status: Cluster in healthy state
1 Instances: 3 Ready instances: 3 Size: 128M Current Write LSN: 0/7000000 (Timeline: 1 - WAL File: 000000010000000000000007) Continuous Backup status (Barman Cloud Plugin)
2 ObjectStore / Server name: cnpg-store/cnpg-keycloak First Point of Recoverability: 2026-04-13 16:07:54 UTC Last Successful Backup: 2026-04-13 17:00:04 UTC Last Failed Backup: - Working WAL archiving: OK WALs waiting to be archived: 0 Last Archived WAL: 000000010000000000000006 @ 2026-04-13T16:08:15.350313Z Last Failed WAL: - Streaming Replication status
3 Replication Slots Enabled Name Sent LSN Write LSN Flush LSN Replay LSN Write Lag Flush Lag Replay Lag State Sync State Sync Priority Replication Slot ---- -------- --------- --------- ---------- --------- --------- ---------- ----- ---------- ------------- ---------------- cnpg-keycloak-2 0/7000000 0/7000000 0/7000000 0/7000000 00:00:00.000438 00:00:00.00148 00:00:00.00148 streaming quorum 1 active cnpg-keycloak-3 0/7000000 0/7000000 0/7000000 0/7000000 00:00:00.000722 00:00:00.0017 00:00:00.0017 streaming quorum 1 active Instances status
4 Name Current LSN Replication role Status QoS Manager Version Node ---- ----------- ---------------- ------ --- --------------- ---- cnpg-keycloak-1 0/7000000 Primary OK BestEffort 1.29.0 ⋯ cnpg-keycloak-2 0/7000000 Standby (sync) OK BestEffort 1.29.0 ⋯ cnpg-keycloak-3 0/7000000 Standby (sync) OK BestEffort 1.29.0 ⋯ Plugins status Name Version Status Reported Operator Capabilities ---- ------- ------ ------------------------------ barman-cloud.cloudnative-pg.io 0.11.0 N/A Reconciler Hooks, Lifecycle Service
- 1
- The cluster status should read
Cluster in healthy state
. Any other value indicates a problem. - 2
- This section shows the status of the cluster’s backups, if configured.
- 3
- This section shows the status of the cluster’s standby instances and their replication health. It is based on the
pg_stat_replication
system view available on the primary node. - 4
- General status of individual instances and their roles in the cluster.
Verify standby health in the Streaming Replication status table.
The following fields help determine whether standbys are healthy and replication is working:
| Field | Expected value | What it means |
|---|---|---|
|
|
A two-part hexadecimal value like | A Log Sequence Number (LSN) is a pointer to a position in the Write-Ahead Log (WAL) stream.
The
The
The difference between a standby’s |
|
|
| Replication lag metrics. A non-zero value that grows over time indicates the standby is falling behind. |
|
|
| Current WAL sender state. Possible values are: -
startup : This WAL sender is starting up. -
catchup : This WAL sender’s connected standby is catching up with the primary. -
streaming : This WAL sender is streaming changes after its connected standby server has caught up with the primary. -
backup : This WAL sender is sending a backup. -
stopping : This WAL sender is stopping.
|
|
|
| Synchronous state of this standby server. Possible values are: -
async : This standby server is asynchronous. -
potential : This standby server is now asynchronous, but can potentially become synchronous if one of current synchronous servers fails. -
sync : This standby server is synchronous. -
quorum : This standby server is considered as a candidate for quorum standbys.
|
|
|
| Confirms the replication slot is in use and the standby is consuming WAL. |
2.15.4. Review the status via Prometheus and Grafana
2.15.4.1. Enable monitoring of the CloudNativePG cluster
Enable metric collection by creating a PodMonitor resource:
Command:
oc -n cnpg-keycloak apply -f - <<EOF apiVersion: monitoring.coreos.com/v1 kind: PodMonitor metadata: name: cnpg-keycloak-pod-monitor spec: selector: matchLabels: cnpg.io/cluster: cnpg-keycloak
1 podMetricsEndpoints: - port: metrics EOF
- 1
- Name of the CloudNativePG cluster to be monitored.
- Add the grafana-dashboard.json from the cloudnative-pg/grafana-dashboards GitHub project to your Grafana instance.
- Optionally, customize the monitoring according to the Monitoring section of the CloudNativePG documentation.
2.15.4.2. Observe replication status
Use the following metrics to observe standby health:
| Metric | Description |
|---|---|
|
|
Replication lag in seconds per standby instance. A value near |
|
|
Returns |
|
|
Returns |
|
| Time elapsed between WAL flushed on the primary and received by the standby. |
|
| Time elapsed between WAL flushed on the primary and replayed on the standby. |
2.15.4.3. Observe backups
If backups are enabled, use the metrics exposed by the Barman Cloud Plugin to monitor their status:
| Metric | Description |
|---|---|
|
| UNIX timestamp of the most recent successful backup. |
|
| UNIX timestamp of the most recent failed backup attempt. |
|
| UNIX timestamp of the earliest point in time available for cluster recovery. |
2.15.5. What a healthy standby looks like
A healthy standby setup typically shows:
-
Cluster status is
Cluster in healthy state
. -
All standby instances show
State: streaming
. -
Write Lag
,Flush Lag
, andReplay Lag
are low and stable, with no continuous upward trend. -
At least one standby has
Sync State: quorum
(for quorum-based synchronous replication as described in the Deploying CloudNativePG in multiple availability zones chapter). -
cnpg_pg_replication_in_recovery
is1
for all standby instances in Prometheus.
2.15.6. Signs of an unhealthy standby
The following are indicators that a standby requires attention:
-
The cluster
Status
is notCluster in healthy state
. -
A standby
State
is notstreaming
. -
Any of
Write Lag
,Flush Lag
, orReplay Lag
is continuously increasing over time. -
No standby is in
quorum
orsync
state when synchronous replication is expected. - A standby is missing from the Streaming Replication status table.
-
cnpg_pg_replication_in_recovery
is0
for any instance that is expected to be a standby in Prometheus.
If one or more standby instances show these symptoms, investigate using the following commands:
Verify that the standby pods are running:
Command:
oc -n cnpg-keycloak get pods -L role
Check recent events in the namespace for scheduling, image pull, storage, or networking problems:
Command:
oc -n cnpg-keycloak get events --sort-by=.lastTimestamp | tail -n 30
Inspect the CloudNativePG cluster resource for conditions and related messages:
Command:
oc -n cnpg-keycloak describe cluster cnpg-keycloak
For possible troubleshooting scenarios refer to the CloudNativePG documentation.
2.15.7. Next steps
- To perform a manual switchover after confirming standby readiness, see the CloudNativePG Switchover Procedure chapter.
2.16. Recovering a CloudNativePG cluster from an S3 backup
Recover a CloudNativePG cluster from a Barman Cloud backup stored in AWS S3.
This topic describes how to recover a CloudNativePG cluster from a backup stored in AWS S3 using the Barman Cloud plugin.
These instructions are intended for use with the setup described in the Concepts for single-cluster deployments chapter. Use it together with the other building blocks outlined in the Building blocks single-cluster deployments chapter.
We provide these blueprints to show a minimal functionally complete example with a good baseline performance for regular installations. You would still need to adapt it to your environment and your organization’s standards and security best practices.
2.16.1. Prerequisites
- A CloudNativePG cluster with scheduled backups configured as described in Deploying CloudNativePG with scheduled backups to S3.
- At least one successful backup exists in the S3 bucket.
- The CloudNativePG Operator, Barman Cloud plugin, and cert-manager are installed as described in Deploying CloudNativePG with scheduled backups to S3.
-
The AWS credentials secret and
ObjectStore
resource are configured as described in Deploying CloudNativePG with scheduled backups to S3.
2.16.2. Recover a CloudNativePG cluster from a backup
The recovery process creates a new CloudNativePG cluster by bootstrapping it from an existing backup in the object store. Instead of using bootstrap.initdb
to create a fresh database, the bootstrap.recovery
section instructs CloudNativePG to restore from a backup source.
The existing CloudNativePG cluster must be deleted before creating the recovered cluster with the same name.
Create a
cluster-recovery.yaml
file based on the following content:Cluster recovery resource:
apiVersion: postgresql.cnpg.io/v1 kind: Cluster metadata: name: cnpg-keycloak spec: instances: 3
1 storage: size: 8Gi
2 affinity:
3 podAntiAffinityType: required topologyKey: topology.kubernetes.io/zone postgresql: synchronous:
4 method: any number: 1 dataDurability: required parameters: max_connections: "100"
5 bootstrap: recovery:
6 source: source managed: services: disabledDefaultServices: ["ro", "r"]
7 plugins:
8 - name: barman-cloud.cloudnative-pg.io isWALArchiver: true parameters: barmanObjectName: cnpg-store serverName: cnpg-keycloak-recovery
9 externalClusters:
10 - name: source plugin: name: barman-cloud.cloudnative-pg.io parameters: barmanObjectName: cnpg-store serverName: cnpg-keycloak
11 - 1
- Number of instances.
- 2
- Pod storage size. This setting needs to take into account the expected size of the database and PostgreSQL WAL logs.
- 3
- Pod affinity rules for Kubernetes scheduler. The
topology.kubernetes.io/zone
value ensures the scheduler will spread the pods across different availability zones. - 4
- Enables quorum-based synchronous replication with a single standby server. For more information about synchronous replication, follow the CloudNativePG documentation.
- 5
- Database connection limit. This value should be adjusted based on the expected total number of JDBC connections from the Red Hat build of Keycloak cluster.
- 6
- Bootstraps the cluster by recovering from the external cluster named
source
instead of creating a new database withinitdb
. - 7
- Disables the
-ro
and-r
default services, which are intended for read-only applications. Since Red Hat build of Keycloak requires read-write access, it only connects to the-rw
service. - 8
- Enables the Barman Cloud plugin for WAL archiving on the recovered cluster.
- 9
- The
serverName
for the recovered cluster must be different from the source cluster to prevent accidental overwrites of the original backup data in the object store. - 10
- Defines an external cluster as the source for recovery. The
source
name must match the value inbootstrap.recovery.source
. - 11
- The
serverName
of the original cluster from which the backup was taken. This must match theserverName
used during the backup.
Apply the recovery cluster resource:
Command:
oc -n cnpg-keycloak apply -f cluster-recovery.yaml
Wait for the
cnpg-keycloak
cluster to get into theReady
state.Command:
oc -n cnpg-keycloak wait --for condition=Ready --timeout=300s cluster cnpg-keycloak
Output:
cluster.postgresql.cnpg.io/cnpg-keycloak condition met
Optionally, view the
cnpg-keycloak
cluster pods and their roles.Command:
oc -n cnpg-keycloak get pods -L role
Example output:
NAME READY STATUS RESTARTS AGE ROLE cnpg-keycloak-1 1/1 Running 0 10m primary cnpg-keycloak-2 1/1 Running 0 10m replica cnpg-keycloak-3 1/1 Running 0 10m replica
- Enable scheduled backups for the recovered cluster as described in Deploying CloudNativePG with scheduled backups to S3.
2.16.3. Point-in-Time Recovery (PITR)
Point-in-Time Recovery allows restoring the database to a specific moment in time rather than to the latest available state. This is useful in scenarios such as recovering from a corrupted database state, reverting changes caused by a failed Red Hat build of Keycloak upgrade, or undoing an unintended data modification.
PITR relies on continuous WAL archiving, which is already configured when using the Barman Cloud plugin as described in Deploying CloudNativePG with scheduled backups to S3. CloudNativePG automatically selects the base backup closest to the specified target time and replays the WAL logs up to that point.
Before upgrading Red Hat build of Keycloak, record the current timestamp or transaction ID so it can be used as a recovery target if the upgrade fails. The timestamp can be obtained by running:
date -u +"%Y-%m-%dT%H:%M:%SZ"
To perform a Point-in-Time Recovery, add a recoveryTarget
section to the bootstrap.recovery
configuration. The following example recovers the cluster to a specific timestamp:
Create a
cluster-recovery-pitr.yaml
file based on the following content:Cluster PITR resource:
apiVersion: postgresql.cnpg.io/v1 kind: Cluster metadata: name: cnpg-keycloak spec: instances: 3 storage: size: 8Gi affinity: podAntiAffinityType: required topologyKey: topology.kubernetes.io/zone postgresql: synchronous: method: any number: 1 dataDurability: required parameters: max_connections: "100" bootstrap: recovery: source: source recoveryTarget:
1 targetTime: "2026-03-30T10:00:00Z"
2 managed: services: disabledDefaultServices: ["ro", "r"] plugins: - name: barman-cloud.cloudnative-pg.io isWALArchiver: true parameters: barmanObjectName: cnpg-store serverName: cnpg-keycloak-pitr
3 externalClusters: - name: source plugin: name: barman-cloud.cloudnative-pg.io parameters: barmanObjectName: cnpg-store serverName: cnpg-keycloak
- 1
- The
recoveryTarget
section specifies the target state to which the database is recovered. See the table below for all supported target options. - 2
- The target timestamp in RFC 3339 format. Always include an explicit timezone to avoid ambiguity. Replace this value with the timestamp recorded before the upgrade or the desired recovery point.
- 3
- The
serverName
must be unique for each recovery to prevent overwriting backup data in the object store.The following table lists all supported recovery target options. Only one option can be used at a time:
Expand Option Description targetTime
Timestamp up to which recovery proceeds, expressed in RFC 3339 format (for example,
2026-03-30T10:00:00Z
). Always include an explicit timezone.targetXID
Transaction ID up to which recovery proceeds. Note that transactions may complete in a different numeric order than their assignment order.
targetName
Named restore point created with the PostgreSQL function
pg_create_restore_point()
to which recovery proceeds.targetLSN
Write-ahead log location (Log Sequence Number) up to which recovery proceeds.
targetImmediate
Recovery ends as soon as a consistent state is reached, that is, as early as possible.
Apply the PITR cluster resource:
Command:
oc -n cnpg-keycloak apply -f cluster-recovery-pitr.yaml
Wait for the
cnpg-keycloak
cluster to get into theReady
state.Command:
oc -n cnpg-keycloak wait --for condition=Ready --timeout=300s cluster cnpg-keycloak
Output:
cluster.postgresql.cnpg.io/cnpg-keycloak condition met
For more details on Point-in-Time Recovery options, refer to the CloudNativePG PITR documentation.
2.16.4. Stale data after recovery
After a recovery, any database modifications made after the last archived WAL segment or the PITR target time are lost. Some Red Hat build of Keycloak tables require attention because stale data may affect cluster behavior or security.
2.16.4.1. JGroups discovery table
The jgroups_ping
table stores the IP addresses and ports of Red Hat build of Keycloak instances and is used as a discovery mechanism for cluster formation. After a recovery, this table may contain references to instances that are no longer running. This causes Red Hat build of Keycloak to attempt to reach those instances during startup, resulting in a delay of up to 20 seconds (the default timeout).
Clear the table after recovery to avoid startup delays:
SQL:
TRUNCATE jgroups_ping;
2.16.4.2. Session tables
The offline_user_session
and offline_client_session
tables store sessions for logged-in users and clients. After a recovery, sessions that were invalidated (for example, by a user logging out) after the recovery point are restored to their previous state, effectively reviving those sessions.
Revived sessions are a security concern. If a user or client logged out after the recovery point, the recovery restores their session, granting access that should no longer be valid. Administrators should evaluate the impact based on their application’s security requirements.
There are three approaches to handle stale sessions:
Clear all sessions (recommended for security-sensitive applications): truncate both tables to force all users and clients to log in again.
SQL:
TRUNCATE offline_client_session; TRUNCATE offline_user_session;
Clear only regular sessions: delete sessions where the
offline_flag
column equals'0'
, preserving offline sessions while removing regular sessions.SQL:
DELETE FROM offline_client_session WHERE offline_flag = '0'; DELETE FROM offline_user_session WHERE offline_flag = '0';
- Leave tables untouched: if revived sessions are acceptable for the application, the stale sessions will expire automatically based on the configured session maximum idle timeout.
2.16.5. Next steps
After successful recovery of the CloudNativePG cluster, continue with Deploying Red Hat build of Keycloak across multiple availability-zones with the Operator.
For more information about recovery operations, refer to the CloudNativePG recovery documentation.
2.17. Deploying Red Hat build of Keycloak across multiple availability-zones with the Operator
Deploy Red Hat build of Keycloak for high availability with the Red Hat build of Keycloak Operator as a building block.
This chapter describes advanced Red Hat build of Keycloak configurations for OpenShift which are load tested and will recover availability-zone failures.
These instructions are intended for use with the setup described in the Concepts for single-cluster deployments chapter. Use it together with the other building blocks outlined in the Building blocks single-cluster deployments chapter.
2.17.1. Prerequisites
- OpenShift cluster deployed across multiple availability-zones with a worker-pool configured for each.
- Understanding of a Basic Red Hat build of Keycloak deployment of Red Hat build of Keycloak with the Red Hat build of Keycloak Operator.
A database deployed according to one of the following guides:
- Deploying AWS Aurora in multiple availability zones chapter,
- Deploying CloudNativePG in multiple availability zones chapter.
- Deploying CloudNativePG with scheduled backups to S3 chapter.
- Recovering a CloudNativePG cluster from an S3 backup chapter.
2.17.2. Procedure
Depending on the database you deployed use the relevant procedure for deploying Red Hat build of Keycloak.
2.17.2.1. Procedure for deploying Red Hat build of Keycloak with AWS Aurora
- Determine the sizing of the deployment using the Concepts for sizing CPU and memory resources chapter.
- Install the Red Hat build of Keycloak Operator as described in the Red Hat build of Keycloak Operator installation chapter.
- Build a custom Red Hat build of Keycloak image which is prepared for usage with the Amazon Aurora PostgreSQL database.
Secure the Amazon Aurora PostgreSQL database connection by downloading the certificate bundles. Create a
ConfigMap
with the certificate bundle using:oc --namespace keycloak create configmap keycloak-aurora-rootcert \ --from-file aurora.pem=/path/to/bundle.pem
Create a generic secret
keycloak-db-secret
containing username and password values defined when creating the Aurora database.oc --namespace keycloak create secret generic keycloak-db-secret \ --from-literal="username=keycloak" --from-literal="password=secret99"
1 - 1
- Note: These are sample values for demonstration purposes only. Please chose a unique password to secure your database.
Deploy the Red Hat build of Keycloak CR with the following values with the resource requests and limits calculated in the first step:
apiVersion: k8s.keycloak.org/v2beta1 kind: Keycloak metadata: labels: app: keycloak name: keycloak namespace: keycloak spec: hostname: hostname: <KEYCLOAK_URL_HERE> resources: requests: cpu: "2" memory: "1250M" limits: cpu: "6" memory: "2250M" db: vendor: postgres url: jdbc:aws-wrapper:postgresql://<AWS_AURORA_URL_HERE>:5432/keycloak
1 poolMinSize: 30
2 poolInitialSize: 30 poolMaxSize: 30 usernameSecret:
3 name: keycloak-db-secret key: username passwordSecret:
4 name: keycloak-db-secret key: password image: <KEYCLOAK_IMAGE_HERE>
5 startOptimized: false
6 additionalOptions: - name: log-console-output value: json - name: metrics-enabled
7 value: 'true' - name: event-metrics-user-enabled value: 'true' - name: db-driver value: software.amazon.jdbc.Driver - name: db-tls-mode
8 value: verify-server http: tlsSecret: keycloak-tls-secret instances: 3 truststores: aurora: configMap: name: keycloak-aurora-rootcert
9 - 1
- Set the Amazon Aurora PostgreSQL URL.
- 2
- The database connection pool initial, max and min size should be identical to allow statement caching for the database. Adjust this number to meet the needs of your system. As most requests will not touch the database due to the Red Hat build of Keycloak embedded cache, this change can serve several hundreds of requests per second. See the Concepts for database connection pools chapter for details.
- 3 4
- Utilise the Secret
keycloak-db-secret
created in the previous step for connecting to the database. - 5 6
- Specify the URL to your custom Red Hat build of Keycloak image. If your image is optimized, set the
startOptimized
flag totrue
. - 7
- Enable the metrics endpoint in order to effectively monitor the system under load.
- 8
- Secure the database connection.
- 9
- Specify the
ConfigMap
name that contains the Amazon Aurora PostgreSQL database certificate bundle. The Operator will automatically mount the file in directory/opt/keycloak/conf/truststores/configmap-<config map name>/<file-name>
2.17.2.2. Procedure for deploying Red Hat build of Keycloak with CloudNativePG
- Determine the sizing of the deployment using the Concepts for sizing CPU and memory resources chapter.
- Install the Red Hat build of Keycloak Operator as described in the Red Hat build of Keycloak Operator installation chapter.
Create a
ConfigMap
containing the generated CA certificate of the CloudNativePG cluster so that Red Hat build of Keycloak can secure the connection to the database.oc --namespace keycloak create configmap cnpg-keycloak-ca \ --from-literal=cert.pem="$(oc --namespace cnpg-keycloak get secrets cnpg-keycloak-ca -o jsonpath='{.data.ca\.crt}' | base64 -d)"
Create a generic secret
keycloak-db-secret
containing a username and password for accessing the database. We use the values from thecnpg-keycloak-app
Secret which is automatically generated during the installation of the CloudNativePG database cluster.oc get secret cnpg-keycloak-app --namespace cnpg-keycloak -o go-template=' apiVersion: v1 kind: Secret metadata: name: keycloak-db-secret namespace: keycloak type: Opaque data: username: {{ .data.username }} password: {{ .data.password }} ' | oc apply -f -
Deploy the Red Hat build of Keycloak CR with the following values with the resource requests and limits calculated in the first step:
apiVersion: k8s.keycloak.org/v2alpha1 kind: Keycloak metadata: labels: app: keycloak name: keycloak namespace: keycloak spec: hostname: hostname: <KEYCLOAK_URL_HERE> resources: requests: cpu: "2" memory: "1250M" limits: cpu: "6" memory: "2250M" db: vendor: postgres host: cnpg-keycloak-rw.cnpg-keycloak.svc.cluster.local
1 poolMinSize: 30
2 poolInitialSize: 30 poolMaxSize: 30 usernameSecret:
3 name: keycloak-db-secret key: username passwordSecret:
4 name: keycloak-db-secret key: password additionalOptions: - name: log-console-output value: json - name: metrics-enabled
5 value: 'true' - name: event-metrics-user-enabled value: 'true' - name: db-tls-mode
6 value: verify-server http: tlsSecret: keycloak-tls-secret instances: 3 truststores: cnpg: configMap: name: cnpg-keycloak-ca
7 - 1
- Set CloudNativePG read-write service URL.
- 2
- The database connection pool initial, max and min size should be identical to allow statement caching for the database. Adjust this number to meet the needs of your system. As most requests will not touch the database due to the Red Hat build of Keycloak embedded cache, this change can serve several hundreds of requests per second. See the Concepts for database connection pools chapter for details.
- 3 4
- Utilise the Secret
keycloak-db-secret
created in the previous step for connecting to the database. - 5
- Enable the metrics endpoint in order to effectively monitor the system under load.
- 6
- Secure the database connection.
- 7
- Specify the
ConfigMap
name that contains the CloudNativePG CA certificate. The Operator will automatically mount the file in directory/opt/keycloak/conf/truststores/configmap-<config map name>/<file-name>
2.17.3. Verify the deployment
Confirm that the Red Hat build of Keycloak deployment is ready.
oc wait --for=condition=Ready keycloaks.k8s.keycloak.org/keycloak
oc wait --for=condition=RollingUpdate=False keycloaks.k8s.keycloak.org/keycloak
2.17.4. Optional: Load shedding
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
2.17.5. Optional: Disable sticky sessions
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
2.18. CloudNativePG Switchover Procedure
Performing switchover of the CloudNativePG primary instance.
These instructions are intended for use with the setup described in the Concepts for single-cluster deployments chapter. Use it together with the other building blocks outlined in the Building blocks single-cluster deployments chapter.
We provide these blueprints to show a minimal functionally complete example with a good baseline performance for regular installations. You would still need to adapt it to your environment and your organization’s standards and security best practices.
2.18.1. When to use this procedure
The CloudNativePG operator is designed to perform an automated switchover in situations such as changing a cluster configuration that requires a rolling update (for example imageName
, resources
, or certain postgresql.paramaters
), an operator upgrade, or a OpenShift node maintenance (Pod eviction).
This procedure can be used to perform a switchover manually, outside of these situations, for example to test how Red Hat build of Keycloak behaves during switchovers.
In order to minimize service disruptions it is recommended to perform this procedure during a period of minimal load. As long as the primary database node is shut down gracefully, no committed data should be lost.
Initiating a switchover terminates existing connections to the primary instance. Red Hat build of Keycloak will available again once the new primary instance is promoted and new connections can be established. This should take less than one minute.
Shutdown of the primary instance may take some time, depending on how long it takes to finish its replication and possible archiving tasks. The maximum duration of this process can be controlled with the .spec.switchoverDelay
setting. See the CloudNativePG documentation for details.
2.18.2. Prerequisities
- A CloudNativePG cluster deployed according to steps described in the Deploying CloudNativePG in multiple availability zones chapter.
-
The
oc
command-line utility. -
The
oc cnpg
plugin. Please follow the CloudNativePG documentation for installation steps.
2.18.3. Procedure
Review the status of the CloudNativePG cluster using the
oc cnpg status
command.Command:
oc cnpg status -n cnpg-keycloak cnpg-keycloak
Output:
Cluster Summary Name cnpg-keycloak/cnpg-keycloak System ID: ******************* PostgreSQL Image: ghcr.io/cloudnative-pg/postgresql:18.1-system-trixie Primary instance: cnpg-keycloak-1
1 Primary promotion time: ****-**-** **:**:** +0000 UTC (*****) Status: Cluster in healthy state Instances: 3 Ready instances: 3 Size: **** Current Write LSN: 0/8000000 (Timeline: 1 - WAL File: 000000010000000000000008) Continuous Backup not configured Streaming Replication status
2 Replication Slots Enabled Name ⋯ Replay LSN ⋯ Replay Lag State Sync State Sync Priority ⋯ ---- ⋯ ---------- ⋯ ---------- ----- ---------- ------------- ⋯ cnpg-keycloak-2 ⋯ 0/8000000 ⋯ 00:00:00 streaming quorum 1 ⋯ cnpg-keycloak-3 ⋯ 0/8000000 ⋯ 00:00:00 streaming quorum 1 ⋯ Instances status
3 Name Current LSN Replication role Status QoS Manager Version Node ---- ----------- ---------------- ------ --- --------------- ---- cnpg-keycloak-1 0/8000000 Primary OK BestEffort 1.28.0 ⋯ cnpg-keycloak-2 0/8000000 Standby (sync) OK BestEffort 1.28.0 ⋯ cnpg-keycloak-3 0/8000000 Standby (sync) OK BestEffort 1.28.0 ⋯
Find a candidate for a new primary instance.
In the Streaming Replication status table note the values in the columns:
State
andSync State
.Before performing the switchover it is important to ensure that the candidate instance is in the
streaming
state, which means that it is actively receiving data from the primary, and that its Sync State is eitherquorum
orsync
.ImportantFor replicas with the Sync State value of
potential
orasync
the replication is asynchronous, which means that there is no guarantee that the particular replica has all the changes confirmed by the primary instance as committed. When selecting a new primary instance these replicas should be avoided.In case the cluster is configured for a quorum-based synchronous replication as described in the Deploying CloudNativePG in multiple availability zones chapter, it is possible to promote any of the available replicas.
In case the cluster is configured for a priority-based synchronous replication, select the replica with the Sync State value of
sync
.Expand Table 2.1. Sync State Sync State Replication Safe to promote quorum
Quorum Synchronous
Safe
sync
Synchronous
Safe
potential
Asynchronous 1
Unsafe
async
Asynchronous
Unsafe
Table footnotes:
1 May be promoted to a synchronous standby if the current synchronous standby fails.
Promote a new primary instance.
Once a candidate for the new primary instance is identified, for example
cnpg-keycloak-2
from the above example, use the following command to promote it.Command:
oc cnpg promote -n cnpg-keycloak cnpg-keycloak cnpg-keycloak-2
Output:
{"level":"info","ts":"****-**-*****:**:**.*********+**:**","msg":"Cluster has become unhealthy"} Node cnpg-keycloak-2 in cluster cnpg-keycloak will be promoted
Wait for the cluster to return to the Ready state.
Command:
oc -n cnpg-keycloak wait --for condition=Ready --timeout=30s cluster cnpg-keycloak
Output:
cluster.postgresql.cnpg.io/cnpg-keycloak condition met
Verify the switchover by checking the cluster status again.
Command:
oc cnpg status -n cnpg-keycloak cnpg-keycloak
Output:
Cluster Summary Name cnpg-keycloak/cnpg-keycloak System ID: ******************* PostgreSQL Image: ghcr.io/cloudnative-pg/postgresql:18.1-system-trixie Primary instance: cnpg-keycloak-2
1 Primary promotion time: ****-**-** **:**:** +0000 UTC (*****) Status: Cluster in healthy state Instances: 3 Ready instances: 3 Size: **** Current Write LSN: 1/2B011FB0 (Timeline: 2 - WAL File: 00000002000000010000002B) Continuous Backup not configured Streaming Replication status
2 Replication Slots Enabled Name ⋯ Replay LSN ⋯ Replay Lag State Sync State Sync Priority ⋯ ---- ⋯ ---------- ⋯ ---------- ----- ---------- ------------- ⋯ cnpg-keycloak-1 ⋯ 1/2B011FB0 ⋯ 00:00:00 streaming quorum 1 ⋯ cnpg-keycloak-3 ⋯ 1/2B011FB0 ⋯ 00:00:00 streaming quorum 1 ⋯ Instances status Name Current LSN Replication role Status QoS Manager Version Node ---- ----------- ---------------- ------ --- --------------- ---- cnpg-keycloak-2 1/2B011FB0 Primary OK BestEffort 1.28.0 ⋯ cnpg-keycloak-1 1/2B011FB0 Standby (sync) OK BestEffort 1.28.0 ⋯ cnpg-keycloak-3 1/2B011FB0 Standby (sync) OK BestEffort 1.28.0 ⋯
For possible troubleshooting scenarios refer to the CloudNativePG documentation.
