---
title: "Accessing a ROSA cluster"
type: reference
domain: openshift
slug: rosa-install-access-delete-clusters-4-22-rosa-sts-accessing-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_install_access_delete_clusters/rosa-sts-accessing-cluster
version: 4.22
family: rosa_install_access_delete_clusters
documentKind: "Documentation"
---

# Accessing a ROSA cluster

[id="rosa-sts-accessing-cluster"]
= Accessing a ROSA cluster

[role="_abstract"]
It is recommended that you access your OpenShift Container Platform cluster using an identity provider (IDP) account. However, the cluster administrator who created the cluster can access it using the quick access procedure.

This document describes how to access a cluster and set up an IDP using the ROSA CLI (`rosa`). Alternatively, you can create an IDP account using {cluster-manager} console.

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-accessing-cluster.adoc

[id="rosa-accessing-your-cluster-quick_{context}"]
= Accessing your cluster quickly

[role="_abstract"]
Access your cluster by using the required administrative credentials and the {oc-first}.

[NOTE]
====
As a best practice, access your cluster with an IDP account instead.
====

.Procedure

. Enter the following command:
+
[source,terminal]
----
$ rosa create admin --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
W: It is recommended to add an identity provider to login to this cluster. See 'rosa create idp --help' for more information.
I: Admin account has been added to cluster 'cluster_name'. It may take up to a minute for the account to become active.
I: To login, run the following command:
oc login https://api.cluster-name.t6k4.i1.organization.org:6443 \
--username cluster-admin \
--password FWGYL-2mkJI-3ZTTZ-rINns
----

. Enter the `oc login` command, username, and password from the output of the previous command:
+
.Example output
[source,terminal]
----
$ oc login https://api.cluster_name.t6k4.i1.organization.org:6443 \
>  --username cluster-admin \
>  --password FWGYL-2mkJI-3ZTTZ-rINns
Login successful.

You have access to 77 projects, the list has been suppressed. You can list all projects with 'projects'
----

. Using the default project, enter this `oc` command to verify that the cluster administrator access is created:
+
[source,terminal]
----
$ oc whoami
----
+
.Example output
[source,terminal]
----
cluster-admin
----
// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-accessing-cluster.adoc

[id="rosa-accessing-your-cluster_{context}"]
= Accessing your cluster with an IDP account

[role="_abstract"]
To log in to your cluster, you can configure an identity provider (IDP). This procedure uses GitHub as an example IDP. To view other supported IDPs, run the `rosa create idp --help` command.

[NOTE]
====
Alternatively, as the user who created the cluster, you can use the quick access procedure.
====

.Procedure

. Add an IDP.
.. The following command creates an IDP backed by GitHub. After running the command, follow the interactive prompts from the output to access your GitHub developer settings and configure a new OAuth application.
+
[source,terminal]
----
$ rosa create idp --cluster=<cluster_name> --interactive
----
+
.. Enter the following values:
+
--
* Type of identity provider: `github`
* Restrict to members of: `organizations` (if you do not have a GitHub Organization, you can create one now)
* GitHub organizations: `rh-test-org` (enter the name of your organization)
--
+
.Example output
[source,terminal]
----
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
? Type of identity provider: github
? Restrict to members of: organizations
? GitHub organizations: rh-test-org
? To use GitHub as an identity provider, you must first register the application:
  - Open the following URL:
    https://github.com/organizations/rh-rosa-test-cluster/settings/applications/new?oauth_application%5Bcallback_url%5D=https%3A%2F%2Foauth-openshift.apps.rh-rosa-test-cluster.z7v0.s1.devshift.org%2Foauth2callback%2Fgithub-1&oauth_application%5Bname%5D=rh-rosa-test-cluster-stage&oauth_application%5Burl%5D=https%3A%2F%2Fconsole-openshift-console.apps.rh-rosa-test-cluster.z7v0.s1.devshift.org
  - Click on 'Register application'
...
----
+
.. Follow the URL in the output and select *Register application* to register a new OAuth application in your GitHub organization. By registering the application, you enable the OAuth server that is built into ROSA to authenticate members of your GitHub organization into your cluster.
+
[NOTE]
====
The fields in the *Register a new OAuth application* GitHub form are automatically filled with the required values through the URL that is defined by the OpenShift Container Platform (ROSA) CLI, `rosa`.
====
.. Use the information from the GitHub application you created and continue the prompts. Enter the following values:
+
--
* Client ID: `&lt;my_github_client_id&gt;`
* Client Secret: [? for help] `&lt;my_github_client_secret&gt;`
* Hostname: (optional, you can leave it blank for now)
* Mapping method: `claim`
--
+
.Continued example output
[source,terminal]
----
...
? Client ID: <my_github_client_id>
? Client Secret: [? for help] <my_github_client_secret>
? Hostname:
? Mapping method: claim
I: Configuring IDP for cluster 'rh_rosa_test_cluster'
I: Identity Provider 'github-1' has been created. You need to ensure that there is a list of cluster administrators defined. See 'rosa create user --help' for more information. To login into the console, open https://console-openshift-console.apps.rh-test-org.z7v0.s1.devshift.org and click on github-1
----
+
The IDP can take 1-2 minutes to be configured within your cluster.
.. Enter the following command to verify that your IDP has been configured correctly:
+
[source,terminal]
----
$ rosa list idps --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
NAME        TYPE      AUTH URL
github-1    GitHub    https://oauth-openshift.apps.rh-rosa-test-cluster1.j9n4.s1.devshift.org/oauth2callback/github-1
----
+
. Log in to your cluster.
.. Enter the following command to get the `Console URL` of your cluster:
+
[source,terminal]
----
$ rosa describe cluster --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
Name:        rh-rosa-test-cluster1
ID:          1de87g7c30g75qechgh7l5b2bha6r04e
External ID: 34322be7-b2a7-45c2-af39-2c684ce624e1
API URL:     https://api.rh-rosa-test-cluster1.j9n4.s1.devshift.org:6443
Console URL: https://console-openshift-console.apps.rh-rosa-test-cluster1.j9n4.s1.devshift.org
Nodes:       Master: 3, Infra: 3, Compute: 4
Region:      us-east-2
State:       ready
Created:     May 27, 2020
----
+
.. Navigate to the `Console URL`, and log in using your Github credentials.
.. In the top right of the OpenShift console, click your name and click **Copy Login Command**.
.. Select the name of the IDP you added (in our case **github-1**), and click **Display Token**.
.. Copy and paste the `oc` login command into your terminal.
+
[source,terminal]
----
$ oc login --token=z3sgOGVDk0k4vbqo_wFqBQQTnT-nA-nQLb8XEmWnw4X --server=https://api.rh-rosa-test-cluster1.j9n4.s1.devshift.org:6443
----
+
For a {hcp-title} cluster, use the port number `443`.
+
.Example output
[source,terminal]
----
Logged into "https://api.rh-rosa-cluster1.j9n4.s1.devshift.org:6443" as "rh-rosa-test-user" using the token provided.

You have access to 67 projects, the list has been suppressed. You can list all projects with 'oc projects'

Using project "default".
----
+
For a {hcp-title} cluster, the port number should be `443`.

.. Enter a simple `oc` command to verify everything is setup properly and that you are logged in.
+
[source,terminal]
----
$ oc version
----
+
.Example output
[source,terminal]
----
Client Version: 4.4.0-202005231254-4a4cd75
Server Version: 4.3.18
Kubernetes Version: v1.16.2
----
// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-accessing-cluster.adoc
// * using-rbac.adoc

[id="rosa-create-cluster-admins_{context}"]
= Granting `cluster-admin` access

[role="_abstract"]
As the user who created the cluster, add the `cluster-admin` user role to your account to have the maximum administrator privileges. These privileges are not automatically assigned to your user account when you create the cluster.

Additionally, only the user who created the cluster can grant cluster access to other `cluster-admin` or `dedicated-admin` users. Users with `dedicated-admin` access have fewer privileges. As a best practice, limit the number of `cluster-admin` users to as few as possible.

.Prerequisites

* You have added an identity provider (IDP) to your cluster.
* You have the IDP user name for the user you are creating.
* You are logged in to the cluster.

.Procedure

. Give your user `cluster-admin` privileges:
+
[source,terminal]
----
$ rosa grant user cluster-admin --user=<idp_user_name> --cluster=<cluster_name>
----
+
. Verify your user is listed as a cluster administrator:
+
[source,terminal]
----
$ rosa list users --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
GROUP             NAME
cluster-admins    rh-rosa-test-user
dedicated-admins  rh-rosa-test-user
----
+
. Enter the following command to verify that your user now has `cluster-admin` access. A cluster administrator can run this command without errors, but a dedicated administrator cannot.
+
[source,terminal]
----
$ oc get all -n openshift-apiserver
----
+
.Example output
[source,terminal]
----
NAME                  READY   STATUS    RESTARTS   AGE
pod/apiserver-6ndg2   1/1     Running   0          17h
pod/apiserver-lrmxs   1/1     Running   0          17h
pod/apiserver-tsqhz   1/1     Running   0          17h
NAME          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/api   ClusterIP   172.30.23.241   <none>        443/TCP   18h
NAME                       DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR                     AGE
daemonset.apps/apiserver   3         3         3       3            3           node-role.kubernetes.io/master=   18h
----

[role="_additional-resources"]
.Additional resources

* Cluster administration role

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-accessing-cluster.adoc
// * using-rbac.adoc

[id="rosa-create-dedicated-cluster-admins_{context}"]
= Granting `dedicated-admin` access

[role="_abstract"]
Only the user who created the cluster can grant cluster access to other `cluster-admin` or `dedicated-admin` users. Users with `dedicated-admin` access have fewer privileges. As a best practice, grant `dedicated-admin` access to most of your administrators.

.Prerequisites

* You have added an identity provider (IDP) to your cluster.
* You have the IDP user name for the user you are creating.
* You are logged in to the cluster.

.Procedure

. Enter the following command to promote your user to a `dedicated-admin`:
+
[source,terminal]
----
$ rosa grant user dedicated-admin --user=<idp_user_name> --cluster=<cluster_name>
----
+
. Enter the following command to verify that your user now has `dedicated-admin` access:
+
[source,terminal]
----
$ oc get groups dedicated-admins
----
+
.Example output
[source,terminal]
----
NAME               USERS
dedicated-admins   rh-rosa-test-user
----
+
[NOTE]
====
A `Forbidden` error displays if user without `dedicated-admin` privileges runs this command.
====

[role="_additional-resources"]
.Additional resources

* Customer administrator user

[role="_additional-resources"]
== Additional resources
* Configuring identity providers using {cluster-manager-first} console
* Understanding the ROSA with STS deployment workflow
* Adding notification contacts
