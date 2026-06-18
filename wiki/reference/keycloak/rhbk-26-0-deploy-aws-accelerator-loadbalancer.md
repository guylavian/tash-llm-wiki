---
title: "Chapter 11. Deploy an AWS Global Accelerator load balancer - Red Hat build of Keycloak 26.0 High Availability Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-deploy-aws-accelerator-loadbalancer
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/high_availability_guide/deploy-aws-accelerator-loadbalancer-
guide: high_availability_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
---

# Chapter 11. Deploy an AWS Global Accelerator load balancer - Red Hat build of Keycloak 26.0 High Availability Guide

Chapter 11. Deploy an AWS Global Accelerator load balancer
This topic describes the procedure required to deploy an AWS Global Accelerator to route traffic between multi-site Red Hat build of Keycloak deployments.
This deployment is intended to be used with the setup described in the Concepts for multi-site deployments chapter. Use this deployment with the other building blocks outlined in the Building blocks multi-site deployments chapter.
We provide these blueprints to show a minimal functionally complete example with a good baseline performance for regular installations. You would still need to adapt it to your environment and your organization’s standards and security best practices.
11.1. Audience
This chapter describes how to deploy an AWS Global Accelerator instance to handle Red Hat build of Keycloak client connection failover for multiple availability-zone Red Hat build of Keycloak deployments.
11.2. Architecture
To ensure user requests are routed to each Red Hat build of Keycloak site we need to utilise a load balancer. To prevent issues with DNS caching on the client-side, the implementation should use a static IP address that remains the same when routing clients to both availability-zones.
In this chapter we describe how to route all Red Hat build of Keycloak client requests via an AWS Global Accelerator load balancer. In the event of a Red Hat build of Keycloak site failing, the Accelerator ensures that all client requests are routed to the remaining healthy site. If both sites are marked as unhealthy, then the Accelerator will “fail-open” and forward requests to a site chosen at random.
Figure 11.1. AWS Global Accelerator Failover
An AWS Network Load Balancer (NLB) is created on both ROSA clusters in order to make the Keycloak pods available as Endpoints to an AWS Global Accelerator instance. Each cluster endpoint is assigned a weight of 128 (half of the maximum weight 255) to ensure that accelerator traffic is routed equally to both availability-zones when both clusters are healthy.
11.3. Prerequisites
- ROSA based Multi-AZ Red Hat build of Keycloak deployment
11.4. Procedure
Create Network Load Balancers
Perform the following on each of the Red Hat build of Keycloak clusters:
- Login to the ROSA cluster
Create a Kubernetes load balancer service
Command:
cat <<EOF | oc apply -n $NAMESPACE -f -
1 apiVersion: v1 kind: Service metadata: name: accelerator-loadbalancer annotations: service.beta.kubernetes.io/aws-load-balancer-additional-resource-tags: accelerator=${ACCELERATOR_NAME},site=${CLUSTER_NAME},namespace=${NAMESPACE}
2 service.beta.kubernetes.io/aws-load-balancer-type: "nlb" service.beta.kubernetes.io/aws-load-balancer-healthcheck-path: "/lb-check" service.beta.kubernetes.io/aws-load-balancer-healthcheck-protocol: "https" service.beta.kubernetes.io/aws-load-balancer-healthcheck-interval: "10"
3 service.beta.kubernetes.io/aws-load-balancer-healthcheck-healthy-threshold: "3"
4 service.beta.kubernetes.io/aws-load-balancer-healthcheck-unhealthy-threshold: "3"
5 spec: ports: - name: https port: 443 protocol: TCP targetPort: 8443 selector: app: keycloak app.kubernetes.io/instance: keycloak app.kubernetes.io/managed-by: keycloak-operator sessionAffinity: None type: LoadBalancer EOF
- 1
$NAMESPACE
should be replaced with the namespace of your Red Hat build of Keycloak deployment- 2
- Add additional Tags to the resources created by AWS so that we can retrieve them later.
ACCELERATOR_NAME
should be the name of the Global Accelerator created in subsequent steps andCLUSTER_NAME
should be the name of the current site. - 3
- How frequently the healthcheck probe is executed in seconds
- 4
- How many healthchecks must pass for the NLB to be considered healthy
- 5
- How many healthchecks must fail for the NLB to be considered unhealthy
Take note of the DNS hostname as this will be required later:
Command:
oc -n $NAMESPACE get svc accelerator-loadbalancer --template="{{range .status.loadBalancer.ingress}}{{.hostname}}{{end}}"
Output:
abab80a363ce8479ea9c4349d116bce2-6b65e8b4272fa4b5.elb.eu-west-1.amazonaws.com
Create a Global Accelerator instance
Command:
aws globalaccelerator create-accelerator \ --name example-accelerator \
1 --ip-address-type DUAL_STACK \
2 --region us-west-2
3 Output:
{ "Accelerator": { "AcceleratorArn": "arn:aws:globalaccelerator::606671647913:accelerator/e35a94dd-391f-4e3e-9a3d-d5ad22a78c71",
1 "Name": "example-accelerator", "IpAddressType": "DUAL_STACK", "Enabled": true, "IpSets": [ { "IpFamily": "IPv4", "IpAddresses": [ "75.2.42.125", "99.83.132.135" ], "IpAddressFamily": "IPv4" }, { "IpFamily": "IPv6", "IpAddresses": [ "2600:9000:a400:4092:88f3:82e2:e5b2:e686", "2600:9000:a516:b4ef:157e:4cbd:7b48:20f1" ], "IpAddressFamily": "IPv6" } ], "DnsName": "a099f799900e5b10d.awsglobalaccelerator.com",
2 "Status": "IN_PROGRESS", "CreatedTime": "2023-11-13T15:46:40+00:00", "LastModifiedTime": "2023-11-13T15:46:42+00:00", "DualStackDnsName": "ac86191ca5121e885.dualstack.awsglobalaccelerator.com"
3 } }
Create a Listener for the accelerator
Command:
aws globalaccelerator create-listener \ --accelerator-arn 'arn:aws:globalaccelerator::606671647913:accelerator/e35a94dd-391f-4e3e-9a3d-d5ad22a78c71' \ --port-ranges '[{"FromPort":443,"ToPort":443}]' \ --protocol TCP \ --region us-west-2
Output:
{ "Listener": { "ListenerArn": "arn:aws:globalaccelerator::606671647913:accelerator/e35a94dd-391f-4e3e-9a3d-d5ad22a78c71/listener/1f396d40", "PortRanges": [ { "FromPort": 443, "ToPort": 443 } ], "Protocol": "TCP", "ClientAffinity": "NONE" } }
Create an Endpoint Group for the Listener
Command:
CLUSTER_1_ENDPOINT_ARN=$(aws elbv2 describe-load-balancers \ --query "LoadBalancers[?DNSName=='abab80a363ce8479ea9c4349d116bce2-6b65e8b4272fa4b5.elb.eu-west-1.amazonaws.com'].LoadBalancerArn" \
1 --region eu-west-1 \
2 --output text ) CLUSTER_2_ENDPOINT_ARN=$(aws elbv2 describe-load-balancers \ --query "LoadBalancers[?DNSName=='a1c76566e3c334e4ab7b762d9f8dcbcf-985941f9c8d108d4.elb.eu-west-1.amazonaws.com'].LoadBalancerArn" \
3 --region eu-west-1 \
4 --output text ) ENDPOINTS='[ { "EndpointId": "'${CLUSTER_1_ENDPOINT_ARN}'", "Weight": 128, "ClientIPPreservationEnabled": false }, { "EndpointId": "'${CLUSTER_2_ENDPOINT_ARN}'", "Weight": 128, "ClientIPPreservationEnabled": false } ]' aws globalaccelerator create-endpoint-group \ --listener-arn 'arn:aws:globalaccelerator::606671647913:accelerator/e35a94dd-391f-4e3e-9a3d-d5ad22a78c71/listener/1f396d40' \
5 --traffic-dial-percentage 100 \ --endpoint-configurations ${ENDPOINTS} \ --endpoint-group-region eu-west-1 \
6 --region us-west-2
Output:
{ "EndpointGroup": { "EndpointGroupArn": "arn:aws:globalaccelerator::606671647913:accelerator/e35a94dd-391f-4e3e-9a3d-d5ad22a78c71/listener/1f396d40/endpoint-group/2581af0dc700", "EndpointGroupRegion": "eu-west-1", "EndpointDescriptions": [ { "EndpointId": "arn:aws:elasticloadbalancing:eu-west-1:606671647913:loadbalancer/net/abab80a363ce8479ea9c4349d116bce2/6b65e8b4272fa4b5", "Weight": 128, "HealthState": "HEALTHY", "ClientIPPreservationEnabled": false }, { "EndpointId": "arn:aws:elasticloadbalancing:eu-west-1:606671647913:loadbalancer/net/a1c76566e3c334e4ab7b762d9f8dcbcf/985941f9c8d108d4", "Weight": 128, "HealthState": "HEALTHY", "ClientIPPreservationEnabled": false } ], "TrafficDialPercentage": 100.0, "HealthCheckPort": 443, "HealthCheckProtocol": "TCP", "HealthCheckPath": "undefined", "HealthCheckIntervalSeconds": 30, "ThresholdCount": 3 } }
Optional: Configure your custom domain
If you are using a custom domain, pointed your custom domain to the AWS Global Load Balancer by configuring an Alias or CNAME in your custom domain.
Create or update the Red Hat build of Keycloak Deployment
Perform the following on each of the Red Hat build of Keycloak clusters:
- Login to the ROSA cluster
Ensure the Keycloak CR has the following configuration
apiVersion: k8s.keycloak.org/v2alpha1 kind: Keycloak metadata: name: keycloak spec: hostname: hostname: $HOSTNAME
1 ingress: enabled: false
2 To ensure that request forwarding works as expected, it is necessary for the Keycloak CR to specify the hostname through which clients will access the Red Hat build of Keycloak instances. This can either be the
DualStackDnsName
orDnsName
hostname associated with the Global Accelerator. If you are using a custom domain, point your custom domain to the AWS Globa Accelerator, and use your custom domain here.
11.5. Verify
To verify that the Global Accelerator is correctly configured to connect to the clusters, navigate to hostname configured above, and you should be presented with the Red Hat build of Keycloak admin console.
