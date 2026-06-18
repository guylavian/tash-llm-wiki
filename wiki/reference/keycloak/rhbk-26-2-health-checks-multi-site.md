---
title: "Chapter 16. Health checks for multi-site deployments - Red Hat build of Keycloak 26.2 High Availability Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-health-checks-multi-site
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/high_availability_guide/health-checks-multi-site-
guide: high_availability_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "Validate the health of a multi-site deployment. When running the Multi-site deployments in a Kubernetes environment, you should automate checks to see if everything is up and running as expected. This page provides an overview of URLs, Kubernetes resources, and Healthcheck endpoints available to verify a multi-site setup of Red Hat build of Keycloak. 16.1. Overview A proactive monitoring strategy …"
---

# Chapter 16. Health checks for multi-site deployments - Red Hat build of Keycloak 26.2 High Availability Guide

Chapter 16. Health checks for multi-site deployments
Validate the health of a multi-site deployment.
When running the Multi-site deployments in a Kubernetes environment, you should automate checks to see if everything is up and running as expected.
This page provides an overview of URLs, Kubernetes resources, and Healthcheck endpoints available to verify a multi-site setup of Red Hat build of Keycloak.
16.1. Overview
A proactive monitoring strategy aims to detect and alert about issues before they impact users. This strategy is the key for a highly resilient and highly available Red Hat build of Keycloak application.
Health checks across various architectural components (such as application health, load balancing, caching, and overall system status) are critical for:
- Ensuring high availability
- Verifying that all sites and the load balancer are operational is a key to ensure that a system can handle requests even if one site goes down.
- Maintaining performance
- Checking the health and distribution of the Data Grid cache ensures that Red Hat build of Keycloak can maintain optimal performance by efficiently handling sessions and other temporary data.
- Operational resilience
- By continuously monitoring the health of both Red Hat build of Keycloak and its dependencies within the Kubernetes environment, the system can quickly identify and possibly auto-remediate issues, reducing downtime.
16.2. Prerequisites
- Kubectl CLI is installed and configured.
- Install jq if it is not already installed on your operating system.
16.3. Specific health checks
16.3.1. Red Hat build of Keycloak load balancer and sites
Verifies the health of the Red Hat build of Keycloak application through its load balancer and both primary and backup sites. This ensures that Red Hat build of Keycloak is accessible and that the load balancing mechanism is functioning correctly across different geographical or network locations.
This command returns the health status of the Red Hat build of Keycloak application’s connection to its configured database, thus confirming the reliability of database connections. This command is available only on the management port and not from the external URL. In a Kubernetes setup, the sub-status health/ready
is checked periodically to make the Pod as ready.
curl -s https://keycloak:managementport/health
This command verifies the lb-check
endpoint of the load balancer and ensures the Red Hat build of Keycloak application cluster is up and running.
curl -s https://keycloak-load-balancer-url/lb-check
These commands will return the running status of the Site A and Site B of the Red Hat build of Keycloak in a multi-site setup.
curl -s https://keycloak_site_a_url/lb-check
curl -s https://keycloak_site_b_url/lb-check
16.3.2. Data Grid Cache health
Check the health of the default cache manager and individual caches in an external Data Grid cluster. This check is vital for Red Hat build of Keycloak performance and reliability, as Data Grid is often used for distributed caching and session clustering in Red Hat build of Keycloak deployments.
This command returns the overall health of the Data Grid cache manager, which is useful as the Admin user does not need to provide user credentials to get the health status.
curl -s https://infinispan_rest_url/rest/v2/cache-managers/default/health/status
In contrast to the preceding health checks, the following health checks require the Admin user to provide the Data Grid user credentials as part of the request to peek into the overall health of the external Data Grid cluster caches.
curl -u <infinispan_user>:<infinispan_pwd> -s https://infinispan_rest_url/rest/v2/cache-managers/default/health \
| jq 'if .cluster_health.health_status == "HEALTHY" and (all(.cache_health[].status; . == "HEALTHY")) then "HEALTHY" else "UNHEALTHY" end'
The jq
filter is a convenience to compute the overall health based on the individual cache health. You can also choose to run the above command without the jq
filter to see the full details.
16.3.3. Data Grid Cluster distribution
Assesses the distribution health of the Data Grid cluster, ensuring that the cluster’s nodes are correctly distributing data. This step is essential for the scalability and fault tolerance of the caching layer.
You can modify the expectedCount 3
argument to match the total nodes in the cluster and validate if they are healthy or not.
curl <infinispan_user>:<infinispan_pwd> -s https://infinispan_rest_url/rest/v2/cluster\?action\=distribution \
| jq --argjson expectedCount 3 'if map(select(.node_addresses | length > 0)) | length == $expectedCount then "HEALTHY" else "UNHEALTHY" end'
16.3.4. Overall, Data Grid system health
Uses the oc
CLI tool to query the health status of Data Grid clusters and the Red Hat build of Keycloak service in the specified namespace. This comprehensive check ensures that all components of the Red Hat build of Keycloak deployment are operational and correctly configured within the Kubernetes environment.
oc get infinispan -n <NAMESPACE> -o json \
| jq '.items[].status.conditions' \
| jq 'map({(.type): .status})' \
| jq 'reduce .[] as $item ([]; . + [keys[] | select($item[.] != "True")]) | if length == 0 then "HEALTHY" else "UNHEALTHY: " + (join(", ")) end'
16.3.5. Red Hat build of Keycloak readiness in Kubernetes
Specifically, checks for the readiness and rolling update conditions of Red Hat build of Keycloak deployments in Kubernetes, ensuring that the Red Hat build of Keycloak instances are fully operational and not undergoing updates that could impact availability.
oc wait --for=condition=Ready --timeout=10s keycloaks.k8s.keycloak.org/keycloak -n <NAMESPACE>
oc wait --for=condition=RollingUpdate=False --timeout=10s keycloaks.k8s.keycloak.org/keycloak -n <NAMESPACE>
