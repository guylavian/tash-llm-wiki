---
title: "Chapter 15. Synchronize Sites - Red Hat build of Keycloak 26.0 High Availability Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-operate-synchronize
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/high_availability_guide/operate-synchronize-
guide: high_availability_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
abstract: "15.1. When to use this procedure Use this when the state of Data Grid clusters of two sites become disconnected and the contents of the caches are out-of-sync. Perform this for example after a split-brain or when one site has been taken offline for maintenance. At the end of the procedure, the data on the secondary site have been discarded and replaced by the data of the active site. All caches in…"
---

# Chapter 15. Synchronize Sites - Red Hat build of Keycloak 26.0 High Availability Guide

Chapter 15. Synchronize Sites
15.1. When to use this procedure
Use this when the state of Data Grid clusters of two sites become disconnected and the contents of the caches are out-of-sync. Perform this for example after a split-brain or when one site has been taken offline for maintenance.
At the end of the procedure, the data on the secondary site have been discarded and replaced by the data of the active site. All caches in the offline site are cleared to prevent invalid cache contents.
15.2. Procedures
15.2.1. Data Grid Cluster
For the context of this chapter, site-a
is the currently active site and site-b
is an offline site that is not part of the AWS Global Accelerator EndpointGroup and is therefore not receiving user requests.
Transferring state may impact Data Grid cluster performance by increasing the response time and/or resources usage.
The first procedure is to delete the stale data from the offline site.
- Login into the offline site.
Shutdown Red Hat build of Keycloak. This will clear all Red Hat build of Keycloak caches and prevents the Red Hat build of Keycloak state from being out-of-sync with Data Grid.
When deploying Red Hat build of Keycloak using the Red Hat build of Keycloak Operator, change the number of Red Hat build of Keycloak instances in the Red Hat build of Keycloak Custom Resource to 0.
Connect into Data Grid Cluster using the Data Grid CLI tool:
Command:
oc -n keycloak exec -it pods/infinispan-0 -- ./bin/cli.sh --trustall --connect https://127.0.0.1:11222
It asks for the username and password for the Data Grid cluster. Those credentials are the one set in the Deploy Data Grid for HA with the Data Grid Operator chapter in the configuring credentials section.
Output:
Username: developer Password: [infinispan-0-29897@ISPN//containers/default]>
NoteThe pod name depends on the cluster name defined in the Data Grid CR. The connection can be done with any pod in the Data Grid cluster.
Disable the replication from offline site to the active site by running the following command. It prevents the clear request to reach the active site and delete all the correct cached data.
Command:
site take-offline --all-caches --site=site-a
Output:
{ "authenticationSessions" : "ok", "work" : "ok", "loginFailures" : "ok", "actionTokens" : "ok" }
Check the replication status is
offline
.Command:
site status --all-caches --site=site-a
Output:
{ "status" : "offline" }
If the status is not
offline
, repeat the previous step.WarningMake sure the replication is
offline
otherwise the clear data will clear both sites.Clear all the cached data in offline site using the following commands:
Command:
clearcache actionTokens clearcache authenticationSessions clearcache loginFailures clearcache work
These commands do not print any output.
Re-enable the cross-site replication from offline site to the active site.
Command:
site bring-online --all-caches --site=site-a
Output:
{ "authenticationSessions" : "ok", "work" : "ok", "loginFailures" : "ok", "actionTokens" : "ok" }
Check the replication status is
online
.Command:
site status --all-caches --site=site-a
Output:
{ "status" : "online" }
Now we are ready to transfer the state from the active site to the offline site.
- Login into your Active site
Connect into Data Grid Cluster using the Data Grid CLI tool:
Command:
oc -n keycloak exec -it pods/infinispan-0 -- ./bin/cli.sh --trustall --connect https://127.0.0.1:11222
It asks for the username and password for the Data Grid cluster. Those credentials are the one set in the Deploy Data Grid for HA with the Data Grid Operator chapter in the configuring credentials section.
Output:
Username: developer Password: [infinispan-0-29897@ISPN//containers/default]>
NoteThe pod name depends on the cluster name defined in the Data Grid CR. The connection can be done with any pod in the Data Grid cluster.
Trigger the state transfer from the active site to the offline site.
Command:
site push-site-state --all-caches --site=site-b
Output:
{ "authenticationSessions" : "ok", "work" : "ok", "loginFailures" : "ok", "actionTokens" : "ok" }
Check the replication status is
online
for all caches.Command:
site status --all-caches --site=site-b
Output:
{ "status" : "online" }
Wait for the state transfer to complete by checking the output of
push-site-status
command for all caches.Command:
site push-site-status --cache=actionTokens site push-site-status --cache=authenticationSessions site push-site-status --cache=loginFailures site push-site-status --cache=work
Output:
{ "site-b" : "OK" } { "site-b" : "OK" } { "site-b" : "OK" } { "site-b" : "OK" }
Check the table in this section for the Cross-Site Documentation for the possible status values.
If an error is reported, repeat the state transfer for that specific cache.
Command:
site push-site-state --cache=<cache-name> --site=site-b
Clear/reset the state transfer status with the following command
Command:
site clear-push-site-status --cache=actionTokens site clear-push-site-status --cache=authenticationSessions site clear-push-site-status --cache=loginFailures site clear-push-site-status --cache=work
Output:
"ok" "ok" "ok" "ok"
Now the state is available in the offline site, Red Hat build of Keycloak can be started again:
- Login into your secondary site.
Startup Red Hat build of Keycloak.
When deploying Red Hat build of Keycloak using the Red Hat build of Keycloak Operator, change the number of Red Hat build of Keycloak instances in the Red Hat build of Keycloak Custom Resource to the original value.
15.2.2. AWS Aurora Database
No action required.
15.2.3. AWS Global Accelerator
Once the two sites have been synchronized, it is safe to add the previously offline site back to the Global Accelerator EndpointGroup following the steps in the Bring site online chapter.
