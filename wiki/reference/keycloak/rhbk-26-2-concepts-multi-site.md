---
title: "Chapter 2. Concepts for multi-site deployments - Red Hat build of Keycloak 26.2 High Availability Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-concepts-multi-site
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/high_availability_guide/concepts-multi-site-
guide: high_availability_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 2. Concepts for multi-site deployments - Red Hat build of Keycloak 26.2 High Availability Guide

Chapter 2. Concepts for multi-site deployments
Understand multi-site deployment with synchronous replication.
This topic describes a highly available multi-site setup and the behavior to expect. It outlines the requirements of the high availability architecture and describes the benefits and tradeoffs.
2.1. When to use this setup
Use this setup to provide Red Hat build of Keycloak deployments that are able to tolerate site failures, reducing the likelihood of downtime.
2.2. Deployment, data storage and caching
Two independent Red Hat build of Keycloak deployments running in different sites are connected with a low latency network connection. Users, realms, clients, sessions, and other entities are stored in a database that is replicated synchronously across the two sites. The data is also cached in the Red Hat build of Keycloak Infinispan caches as local caches. When the data is changed in one Red Hat build of Keycloak instance, that data is updated in the database, and an invalidation message is sent to the other site using the work
cache.
In the following paragraphs and diagrams, references to deploying Data Grid apply to the external Data Grid.
2.3. Causes of data and service loss
While this setup aims for high availability, the following situations can still lead to service or data loss:
- Red Hat build of Keycloak site failure may result in requests failing in the period between the failure and the loadbalancer detecting it, as requests may still be routed to the failed site.
- Once failures occur in the communication between the sites, manual steps are necessary to re-synchronize a degraded setup.
- Degraded setups can lead to service or data loss if additional components fail. Monitoring is necessary to detect degraded setups.
2.4. Failures which this setup can survive
| Failure | Recovery | RPO1 | RTO2 |
|---|---|---|---|
| Database node | If the writer instance fails, the database can promote a reader instance in the same or other site to be the new writer. | No data loss | Seconds to minutes (depending on the database) |
| Red Hat build of Keycloak node | Multiple Red Hat build of Keycloak instances run on each site. If one instance fails some incoming requests might receive an error message or are delayed for some seconds. | No data loss | Less than 30 seconds |
| Data Grid node | Multiple Data Grid instances run in each site. If one instance fails, it takes a few seconds for the other nodes to notice the change. Entities are stored in at least two Data Grid nodes, so a single node failure does not lead to data loss. | No data loss | Less than 30 seconds |
| Data Grid cluster failure |
If the Data Grid cluster fails in one of the sites, Red Hat build of Keycloak will not be able to communicate with the external Data Grid on that site, and the Red Hat build of Keycloak service will be unavailable. The loadbalancer will detect the situation as The setup is degraded until the Data Grid cluster is restored and the data is re-synchronized. | No data loss3 | Seconds to minutes (depending on load balancer setup) |
| Connectivity Data Grid | If the connectivity between the two sites is lost, data cannot be sent to the other site. Incoming requests might receive an error message or are delayed for some seconds. The Data Grid will mark the other site offline, and will stop sending data. One of the sites needs to be taken offline in the loadbalancer until the connection is restored and the data is re-synchronized between the two sites. In the blueprints, we show how this can be automated. | No data loss3 | Seconds to minutes (depending on load balancer setup) |
| Connectivity database | If the connectivity between the two sites is lost, the synchronous replication will fail. Some requests might receive an error message or be delayed for a few seconds. Manual operations might be necessary depending on the database. | No data loss3 | Seconds to minutes (depending on the database) |
| Site failure | If none of the Red Hat build of Keycloak nodes are available, the loadbalancer will detect the outage and redirect the traffic to the other site. Some requests might receive an error message until the loadbalancer detects the failure. | No data loss3 | Less than two minutes |
Table footnotes:
1 Recovery point objective, assuming all parts of the setup were healthy at the time this occurred.
2 Recovery time objective.
3 Manual operations needed to restore the degraded setup.
The statement “No data loss” depends on the setup not being degraded from previous failures, which includes completing any pending manual operations to resynchronize the state between the sites.
2.5. Known limitations
- Site Failure
- A successful failover requires a setup not degraded from previous failures. All manual operations like a re-synchronization after a previous failure must be complete to prevent data loss. Use monitoring to ensure degradations are detected and handled in a timely manner.
- Out-of-sync sites
- The sites can become out of sync when a synchronous Data Grid request fails. This situation is currently difficult to monitor, and it would need a full manual re-sync of Data Grid to recover. Monitoring the number of cache entries in both sites and the Red Hat build of Keycloak log file can show when resynch would become necessary.
- Manual operations
- Manual operations that re-synchronize the Data Grid state between the sites will issue a full state transfer which will put a stress on the system.
- Two sites restriction
- This setup is tested and supported only with two sites. Each additional site increases overall latency as it is necessary for data to be synchronously written to each site. Furthermore, the probability of network failures, and therefore downtime, also increases. Therefore, we do not support more than two sites as we believe it would lead to a deployment with inferior stability and performance.
2.6. Questions and answers
- Why synchronous database replication?
- A synchronously replicated database ensures that data written in one site is always available in the other site after site failures and no data is lost. It also ensures that the next request will not return stale data, independent on which site it is served.
- Why synchronous Data Grid replication?
- A synchronously replicated Data Grid ensures that cached data in one site are always available on the other site after a site failure and no data is lost. It also ensures that the next request will not return stale data, independent on which site it is served.
- Why is a low-latency network between sites needed?
- Synchronous replication defers the response to the caller until the data is received at the other site. For synchronous database replication and synchronous Data Grid replication, a low latency is necessary as each request can have potentially multiple interactions between the sites when data is updated which would amplify the latency.
- Is a synchronous cluster less stable than an asynchronous cluster?
An asynchronous setup would handle network failures between the sites gracefully, while the synchronous setup would delay requests and will throw errors to the caller where the asynchronous setup would have deferred the writes to Data Grid or the database on the other site. However, as the two sites would never be fully up-to-date, this setup could lead to data loss during failures. This would include:
- Lost changes leading to users being able to log in with an old password because database changes are not replicated to the other site at the point of failure when using an asynchronous database.
- Invalid caches leading to users being able to log in with an old password because invalidating caches are not propagated at the point of failure to the other site when using an asynchronous Data Grid replication.
Therefore, tradeoffs exist between high availability and consistency. The focus of this topic is to prioritize consistency over availability with Red Hat build of Keycloak.
2.7. Next steps
Continue reading in the Building blocks multi-site deployments chapter to find blueprints for the different building blocks.
