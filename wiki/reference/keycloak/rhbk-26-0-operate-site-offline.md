---
title: "Chapter 13. Take site offline - Red Hat build of Keycloak 26.0 High Availability Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-operate-site-offline
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/high_availability_guide/operate-site-offline-
guide: high_availability_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
---

# Chapter 13. Take site offline - Red Hat build of Keycloak 26.0 High Availability Guide

Chapter 13. Take site offline
13.1. When to use this procedure
During the deployment lifecycle it might be required that one of the sites is temporarily taken offline for maintenance or to allow for software upgrades. To ensure that no user requests are routed to the site requiring maintenance, it is necessary for the site to be removed from your load balancer configuration.
13.2. Procedure
Follow these steps to remove a site from the load balancer so that no traffic can be routed to it.
13.2.1. Global Accelerator
Determine the ARN of the Network Load Balancer (NLB) associated with the site to be kept online
Command:
NAMESPACE=
1 REGION=
2 HOSTNAME=$(oc -n $NAMESPACE get svc accelerator-loadbalancer --template="{{range .status.loadBalancer.ingress}}{{.hostname}}{{end}}") aws elbv2 describe-load-balancers \ --query "LoadBalancers[?DNSName=='${HOSTNAME}'].LoadBalancerArn" \ --region ${REGION} \ --output text
Output:
arn:aws:elasticloadbalancing:eu-west-1:606671647913:loadbalancer/net/a49e56e51e16843b9a3bc686327c907b/9b786f80ed4eba3d
Update the Accelerator EndpointGroup to only include a single site
List the current endpoints in the Global Accelerator’s EndpointGroup
Command:
ACCELERATOR_NAME=
1 ACCELERATOR_ARN=$(aws globalaccelerator list-accelerators \ --query "Accelerators[?Name=='${ACCELERATOR_NAME}'].AcceleratorArn" \ --region us-west-2 \
2 --output text ) LISTENER_ARN=$(aws globalaccelerator list-listeners \ --accelerator-arn ${ACCELERATOR_ARN} \ --query "Listeners[*].ListenerArn" \ --region us-west-2 \ --output text ) aws globalaccelerator list-endpoint-groups \ --listener-arn ${LISTENER_ARN} \ --region us-west-2
Output:
{ "EndpointGroups": [ { "EndpointGroupArn": "arn:aws:globalaccelerator::606671647913:accelerator/d280fc09-3057-4ab6-9330-6cbf1f450748/listener/8769072f/endpoint-group/a30b64ec1700", "EndpointGroupRegion": "eu-west-1", "EndpointDescriptions": [ { "EndpointId": "arn:aws:elasticloadbalancing:eu-west-1:606671647913:loadbalancer/net/a49e56e51e16843b9a3bc686327c907b/9b786f80ed4eba3d", "Weight": 128, "HealthState": "HEALTHY", "ClientIPPreservationEnabled": false }, { "EndpointId": "arn:aws:elasticloadbalancing:eu-west-1:606671647913:loadbalancer/net/a3c75f239541c4a6e9c48cf8d48d602f/5ba333e87019ccf0", "Weight": 128, "HealthState": "HEALTHY", "ClientIPPreservationEnabled": false } ], "TrafficDialPercentage": 100.0, "HealthCheckPort": 443, "HealthCheckProtocol": "TCP", "HealthCheckIntervalSeconds": 30, "ThresholdCount": 3 } ] }
Update the EndpointGroup to only include the NLB retrieved in step 1.
Command:
aws globalaccelerator update-endpoint-group \ --endpoint-group-arn arn:aws:globalaccelerator::606671647913:accelerator/d280fc09-3057-4ab6-9330-6cbf1f450748/listener/8769072f/endpoint-group/a30b64ec1700 \ --region us-west-2 \ --endpoint-configurations ' [ { "EndpointId": "arn:aws:elasticloadbalancing:eu-west-1:606671647913:loadbalancer/net/a49e56e51e16843b9a3bc686327c907b/9b786f80ed4eba3d", "Weight": 128, "ClientIPPreservationEnabled": false } ] '
