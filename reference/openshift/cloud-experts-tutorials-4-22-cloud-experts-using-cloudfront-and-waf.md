---
title: "Tutorial: Using AWS WAF and Amazon CloudFront to protect {product-title} workloads"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-using-cloudfront-and-waf
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-using-cloudfront-and-waf
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Using AWS WAF and Amazon CloudFront to protect {product-title} workloads

[id="cloud-experts-using-cloudfront-and-waf"]
= Tutorial: Using AWS WAF and Amazon CloudFront to protect OpenShift Container Platform workloads

[role="_abstract"]
AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to your protected web application resources.

You can use an Amazon CloudFront to add a Web Application Firewall (WAF) to your OpenShift Container Platform workloads. Using an external solution protects OpenShift Container Platform resources from experiencing denial of service due to handling the WAF.

[NOTE]
====
WAFv1, WAF classic, is no longer supported. Use WAFv2.
====

== Prerequisites

* A OpenShift Container Platform cluster.
* You have access to the OpenShift CLI (`oc`).
* You have access to the AWS CLI (`aws`).

// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-using-cloudfront-and-waf.adoc

[id="cloud-experts-using-cloudfront-and-waf-setup-environ_{context}"]
= Setting up your environment

[role="_abstract"]
You can use environment variables to ensure consistency across the commands within this lab.

.Procedure
. In your terminal, configure the following environment variables:
+
[source,terminal]
----
$ export DOMAIN=apps.example.com
$ export AWS_PAGER=""
$ export CLUSTER_NAME=$(oc get infrastructure cluster -o=jsonpath="{.status.infrastructureName}"  | sed 's/-[a-z0-9]\{5\}$//')
$ export REGION=$(oc get infrastructure cluster -o=jsonpath="{.status.platformStatus.aws.region}")
$ export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
$ export SCRATCH="/tmp/${CLUSTER}/cloudfront-waf"
$ mkdir -p ${SCRATCH}
$ echo "Cluster: ${CLUSTER}, Region: ${REGION}, AWS Account ID: ${AWS_ACCOUNT_ID}"
----

. Replace the `DOMAIN` value `apps.example.com` with the custom domain you want to use for the `IngressController`.
+
[NOTE]
====
The "Cluster" output from the previous command might be the name of your cluster, the internal ID of your cluster, or the cluster's domain prefix. If you prefer to use another identifier, you can manually set this value by running the following command:
[source,terminal]
----
$ export CLUSTER=my-custom-value
----
====
// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-using-cloudfront-and-waf.adoc

[id="cloud-experts-using-cloudfront-and-waf-secondary_ingress_controller_setup_{context}"]
= Setting up the secondary ingress controller

[role="_abstract"]
It is necessary to configure a secondary ingress controller to segment your external WAF-protected traffic from your standard (and default) cluster ingress controller.

.Prerequisites
* A publicly trusted SAN or wildcard certificate for your custom domain, such as `CN=*.apps.example.com`
+
[IMPORTANT]
====
Amazon CloudFront uses HTTPS to communicate with your cluster's secondary ingress controller. As explained in the Amazon CloudFront documentation, you cannot use a self-signed certificate for HTTPS communication between CloudFront and your cluster. Amazon CloudFront verifies that the certificate was issued by a trusted certificate authority.
====

.Procedure
. Create a new TLS secret from a private key and a public certificate, where `fullchain.pem` is your full wildcard certificate chain (including any intermediaries) and `privkey.pem` is your wildcard certificate's private key.
+
.Example
[source,terminal]
----
$ oc -n openshift-ingress create secret tls waf-tls --cert=fullchain.pem --key=privkey.pem
----

. Create a new `IngressController` resource:
+
**For example** `waf-ingress-controller.yaml`:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: cloudfront-waf
  namespace: openshift-ingress-operator
spec:
  domain: apps.example.com
  defaultCertificate:
    name: waf-tls
  endpointPublishingStrategy:
    loadBalancer:
      dnsManagementPolicy: Unmanaged
      providerParameters:
        aws:
          type: NLB
        type: AWS
      scope: External
    type: LoadBalancerService
  routeSelector:
    matchLabels:
     route: waf
----
+
--
where:

* `domain: apps.example.com`:: Replace with the custom domain you want to use for the `IngressController`.
* `routeSelector`:: Filters the set of routes serviced by the Ingress Controller. In this tutorial, we will use the `waf` route selector, but if no value was to be provided, no filtering would occur.
--
. Apply the `IngressController`:
+
.Example
[source,terminal]
----
$ oc apply -f waf-ingress-controller.yaml
----

. Verify that your IngressController has successfully created an external load balancer:
+
[source,terminal]
----
$ oc -n openshift-ingress get service/router-cloudfront-waf
----
+
.Example output
[source,terminal]
----
NAME                    TYPE           CLUSTER-IP      EXTERNAL-IP                                                                     PORT(S)                      AGE
router-cloudfront-waf   LoadBalancer   172.30.16.141   a68a838a7f26440bf8647809b61c4bc8-4225395f488830bd.elb.us-east-1.amazonaws.com   80:30606/TCP,443:31065/TCP   2m19s
----
// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-using-cloudfront-and-waf.adoc

[id="cloud-experts-using-cloudfront-and-waf-configure-aws-waf_{context}"]
= Configure the AWS WAF

[role="_abstract"]
The AWS WAF service is a web application firewall that lets you monitor, protect, and control the HTTP and HTTPS requests that are forwarded to your protected web application resources, like OpenShift Container Platform.

.Procedure
. Create a AWS WAF rules file to apply to our web ACL:
+
[source,terminal]
----
$ cat << EOF > ${SCRATCH}/waf-rules.json
[
    {
      "Name": "AWS-AWSManagedRulesCommonRuleSet",
      "Priority": 0,
      "Statement": {
        "ManagedRuleGroupStatement": {
          "VendorName": "AWS",
          "Name": "AWSManagedRulesCommonRuleSet"
        }
      },
      "OverrideAction": {
        "None": {}
      },
      "VisibilityConfig": {
        "SampledRequestsEnabled": true,
        "CloudWatchMetricsEnabled": true,
        "MetricName": "AWS-AWSManagedRulesCommonRuleSet"
      }
    },
    {
      "Name": "AWS-AWSManagedRulesSQLiRuleSet",
      "Priority": 1,
      "Statement": {
        "ManagedRuleGroupStatement": {
          "VendorName": "AWS",
          "Name": "AWSManagedRulesSQLiRuleSet"
        }
      },
      "OverrideAction": {
        "None": {}
      },
      "VisibilityConfig": {
        "SampledRequestsEnabled": true,
        "CloudWatchMetricsEnabled": true,
        "MetricName": "AWS-AWSManagedRulesSQLiRuleSet"
      }
    }
]
EOF
----
+
This will enable the Core (Common) and SQL AWS Managed Rule Sets.
+
. Create an AWS WAF Web ACL using the rules we specified above:
+
[source,terminal]
----
$ WAF_WACL=$(aws wafv2 create-web-acl \
  --name cloudfront-waf \
  --region ${REGION} \
  --default-action Allow={} \
  --scope CLOUDFRONT \
  --visibility-config SampledRequestsEnabled=true,CloudWatchMetricsEnabled=true,MetricName=${CLUSTER}-waf-metrics \
  --rules file://${SCRATCH}/waf-rules.json \
  --query 'Summary.Name' \
  --output text)
----
// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-using-cloudfront-and-waf.adoc

[id="cloud-experts-using-cloudfront-and-waf-configure_amazon_cloudfront_{context}"]
= Configure Amazon CloudFront

[role="_abstract"]
You can use the `aws` CLI tool as well as the {oc-first} tool to configure Amazon Cloudfront.

.Procedure
. Retrieve the newly created custom ingress controller's NLB hostname:
+
[source,terminal]
----
$ NLB=$(oc -n openshift-ingress get service router-cloudfront-waf \
  -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
----

. Import your certificate into Amazon Certificate Manager, where `cert.pem` is your wildcard certificate, `fullchain.pem` is your wildcard certificate's chain and `privkey.pem` is your wildcard certificate’s private key.
+
[NOTE]
====
Regardless of what region your cluster is deployed, you must import this certificate to `us-east-1` as Amazon CloudFront is a global AWS service.
====
+
.Example
[source,terminal]
----
$ aws acm import-certificate --certificate file://cert.pem \
  --certificate-chain file://fullchain.pem \
  --private-key file://privkey.pem \
  --region us-east-1
----

. Log into the AWS console to create a CloudFront distribution.
+
. Configure the CloudFront distribution by using the following information:
+
[NOTE]
====
If an option is not specified in the table below, leave them the default (which may be blank).
====
+
[cols="2",options="header"]
|===
|Option
|Value

|Origin domain
|Output from the previous command ^[a]^

|Name
|rosa-waf-ingress ^[b]^

|Viewer protocol policy
|Redirect HTTP to HTTPS

|Allowed HTTP methods
|GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE

|Cache policy
|CachingDisabled

|Origin request policy
|AllViewer

|Web Application Firewall (WAF)
|Enable security protections

|Use existing WAF configuration
|true

|Choose a web ACL
|`cloudfront-waf`

|Alternate domain name (CNAME)
|*.apps.example.com ^[c]^

|Custom SSL certificate
|Select the certificate you imported from the step above ^[d]^
|===
+
[.small]
--
a. Run `echo ${NLB}` to get the origin domain.
b. If you have multiple clusters, ensure the origin name is unique.
c. This should match the wildcard domain you used to create the custom ingress controller.
d. This should match the alternate domain name entered above.
--
+
. Retrieve the Amazon CloudFront Distribution endpoint:
+
[source,terminal]
----
$ aws cloudfront list-distributions --query "DistributionList.Items[?Origins.Items[?DomainName=='${NLB}']].DomainName" --output text
----

. Update the DNS of your custom wildcard domain with a CNAME to the Amazon CloudFront Distribution endpoint from the step above.
+
.Example
[source,text]
----
*.apps.example.com CNAME d1b2c3d4e5f6g7.cloudfront.net
----
// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-using-cloudfront-and-waf.adoc

[id="cloud-experts-using-cloudfront-and-waf-deploy-sample-application_{context}"]
= Deploy a sample application

[role="_abstract"]
You can use the {oc-first} tool to deploy your application.

.Procedure
. Create a new project for your sample application by running the following command:
+
[source,terminal]
----
$ oc new-project hello-world
----
+
. Deploy a hello world application:
+
[source,terminal]
----
$ oc -n hello-world new-app --image=docker.io/openshift/hello-openshift
----
+
. Create a route for the application specifying your custom domain name:
+
.Example
[source,terminal]
----
$ oc -n hello-world create route edge --service=hello-openshift hello-openshift-tls \
--hostname hello-openshift.${DOMAIN}
----
+
. Label the route to admit it to your custom ingress controller:
+
[source,terminal]
----
$ oc -n hello-world label route.route.openshift.io/hello-openshift-tls route=waf
----
// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-using-cloudfront-and-waf.adoc

[id="cloud-experts-using-cloudfront-and-waf-test-waf_{context}"]
= Test the WAF

[role="_abstract"]
Use the `curl` command to test the WAF app.

.Procedure
. Test that the app is accessible behind Amazon CloudFront:
+
.Example
[source,terminal]
----
$ curl "https://hello-openshift.${DOMAIN}"
----
+
.Example output
[source,text]
----
Hello OpenShift!
----

. Test that the WAF denies a bad request:
+
.Example
[source,terminal]
----
$ curl -X POST "https://hello-openshift.${DOMAIN}" \
  -F "user='<script><alert>Hello></alert></script>'"
----
+
.Example output
[source,text]
----
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<HTML><HEAD><META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=iso-8859-1">
<TITLE>ERROR: The request could not be satisfied</TITLE>
</HEAD><BODY>
<H1>403 ERROR</H1>
<H2>The request could not be satisfied.</H2>
<HR noshade size="1px">
Request blocked.
We can't connect to the server for this app or website at this time. There might be too much traffic or a configuration error. Try again later, or contact the app or website owner.
<BR clear="all">
If you provide content to customers through CloudFront, you can find steps to troubleshoot and help prevent this error by reviewing the CloudFront documentation.
<BR clear="all">
<HR noshade size="1px">
<PRE>
Generated by cloudfront (CloudFront)
Request ID: nFk9q2yB8jddI6FZOTjdliexzx-FwZtr8xUQUNT75HThPlrALDxbag==
</PRE>
<ADDRESS>
</ADDRESS>
</BODY></HTML>
----
+
The expected result is a `403 ERROR`, which means the AWS WAF is protecting your application.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Adding Extra Security with AWS WAF, CloudFront and ROSA | Amazon Web Services on YouTube
