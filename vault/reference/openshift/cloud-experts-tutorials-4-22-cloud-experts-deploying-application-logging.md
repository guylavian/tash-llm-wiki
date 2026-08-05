---
title: "Tutorial: Logging"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-deploying-application-logging
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-deploying-application-logging
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Logging

[id="cloud-experts-deploying-application-logging"]
= Tutorial: Logging

[role="_abstract"]
There are various methods to view your logs in {product-rosa}. Use the following procedures to forward the logs to AWS CloudWatch and view the logs directly through the pod by using `oc logs`.

[NOTE]
====
OpenShift Container Platform is not preconfigured with a logging solution.
====

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-application-logging.adoc

[id="cloud-experts-deploying-application-logging-forward-to-cloudwatch_{context}"]
= Forwarding logs to CloudWatch

[role="_abstract"]
Install the logging add-on service to forward the logs to AWS CloudWatch.

.Procedure
. Run the following script to configure your OpenShift Container Platform cluster to forward logs to CloudWatch:
+
[source,terminal]
----
$ curl https://raw.githubusercontent.com/openshift-cs/rosaworkshop/master/rosa-workshop/ostoy/resources/configure-cloudwatch.sh | bash
----
+
[NOTE]
====
Configuring OpenShift Container Platform to send logs to CloudWatch goes beyond the scope of this tutorial. Integrating with AWS and enabling CloudWatch logging are important aspects of OpenShift Container Platform, so a script is included to simplify the configuration process. The script will automatically set up AWS CloudWatch. You can examine the script to understand the steps involved.
====
+
**Example output**
+
[source,terminal]
----
Varaibles are set...ok.
Policy already exists...ok.
Created RosaCloudWatch-mycluster role.
Attached role policy.
Deploying the Red Hat OpenShift Logging Operator
namespace/openshift-logging configured
operatorgroup.operators.coreos.com/cluster-logging created
subscription.operators.coreos.com/cluster-logging created
Waiting for Red Hat OpenShift Logging Operator deployment to complete...
Red Hat OpenShift Logging Operator deployed.
secret/cloudwatch-credentials created
clusterlogforwarder.logging.openshift.io/instance created
clusterlogging.logging.openshift.io/instance created
Complete.
----
. After a few minutes, you should begin to see log groups inside of AWS CloudWatch. Run the following command to see the log groups:
+
[source,terminal]
----
$ aws logs describe-log-groups --log-group-name-prefix rosa-mycluster
----
+
**Example output**
+
[source,terminal]
----
{
    "logGroups": [
        {
            "logGroupName": "rosa-mycluster.application",
            "creationTime": 1724104537717,
            "metricFilterCount": 0,
            "arn": "arn:aws:logs:us-west-2:000000000000:log-group:rosa-mycluster.application:*",
            "storedBytes": 0,
            "logGroupClass": "STANDARD",
            "logGroupArn": "arn:aws:logs:us-west-2:000000000000:log-group:rosa-mycluster.application"
        },
        {
            "logGroupName": "rosa-mycluster.audit",
            "creationTime": 1724104152968,
            "metricFilterCount": 0,
            "arn": "arn:aws:logs:us-west-2:000000000000:log-group:rosa-mycluster.audit:*",
            "storedBytes": 0,
            "logGroupClass": "STANDARD",
            "logGroupArn": "arn:aws:logs:us-west-2:000000000000:log-group:rosa-mycluster.audit"
        },
----
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-application-logging.adoc

[id="cloud-experts-deploying-application-logging-output-data_{context}"]
= Outputting the data to the streams and logs

[role="_abstract"]
Output your data to the streams and logs in the OSToy application.

.Procedure
. Output a message to `stdout`.
.. In the OSToy application, click *Home* and then click the message box for *Log Message (stdout)*.
.. Write a message to output to the `stdout` stream, for example "All is well!".
.. Click *Send Message*.
+
image:cloud-experts-deploying-application-logging-ostoy-stdout.png[]
+
. Output a message to `stderr`.
.. Click the message box for *Log Message (stderr)*.
.. Write a message to output to the `stderr` stream, for example "Oh no! Error!".
.. Click *Send Message*.
+
image:cloud-experts-deploying-application-logging-ostoy-stderr.png[]
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-application-logging.adoc

[id="cloud-experts-deploying-application-logging-view-app-logs_{context}"]
= Viewing the application logs

[role="_abstract"]
You can view your application's logs by using the `oc` command.

.Procedure
. Enter the following command in the command-line interface (CLI) to retrieve the name of your frontend pod:
+
[source,terminal]
----
$ oc get pods -o name
----
+
**Example output**
+
[source,terminal]
----
pod/ostoy-frontend-679cb85695-5cn7x <1>
pod/ostoy-microservice-86b4c6f559-p594d
----
+
The pod name in this example is `ostoy-frontend-679cb85695-5cn7x`.
+
. Run the following command to see both the `stdout` and `stderr` messages:
+
[source,terminal]
----
$ oc logs <pod-name>
----
+
**Example output**
+
[source,terminal]
----
$ oc logs ostoy-frontend-679cb85695-5cn7x
[...]
ostoy-frontend-679cb85695-5cn7x: server starting on port 8080
Redirecting to /home
stdout: All is well!
stderr: Oh no! Error!
----
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-application-logging.adoc

[id="cloud-experts-deploying-application-logging-view-cloudwatch-logs_{context}"]
= Viewing the logs with CloudWatch

[role="_abstract"]
You can verify your logs within CloudWatch on the AWS web console.

.Procedure
. Navigate to *CloudWatch* on the AWS web console.
. In the left menu, click *Logs* and then *Log groups* to see the different groups of logs. You should see 3 groups:

** `rosa-<cluster-name>.application`
** `rosa-<cluster-name>.audit`
** `rosa-<cluster-name>.infrastructure`
+
image:cloud-experts-deploying-application-logging-cw.png[]
+
. Click `rosa-<cluster-name>.application`.
. Click the log stream for the frontend pod.
+
image:cloud-experts-deploying-application-logging-logstream2.png[]
+
. Filter for `stdout` and `stderr`.
. Expand the row to show the messages you entered earlier and other pertinent information.
+
image:cloud-experts-deploying-application-logging-stderr.png[]
+
. Return to the log streams and select the microservice.
. Enter "microservice" in the search bar to see other messages in your logs.
. Expand one of the entries to see the color the frontend pod received from microservice and which pod sent that color to the frontend pod.
+
image:cloud-experts-deploying-application-logging-messages.png[]

[role="_additional-resources"]
.Additional resources
* What is Amazon CloudWatch
