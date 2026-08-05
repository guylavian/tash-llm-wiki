---
title: "One of the cache hosts in the cluster is down (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-one-of-the-cache-hosts-in-the-cluster-is-down
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/one-of-the-cache-hosts-in-the-cluster-is-down
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: One of the cache hosts in the cluster is down, for SharePoint Server."
---

# One of the cache hosts in the cluster is down (SharePoint Server) - SharePoint Server

Note

One of the cache hosts in the cluster is down (SharePoint Server)

# One of the cache hosts in the cluster is down (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** One of the cache hosts in the cluster is down.

**Summary:** One of the cache hosts in the cluster is down. This indicates that the SharePoint cache client is trying to connect to the wrong cache host.

**Cause:** The AppFabric Caching service is stopped.

**Resolution: Start the AppFabric Caching service.**

Verify that the user account that is performing this procedure is a member of the Administrators group on the local computer.

In **Server Manager**, click **Tools**, and then click **Services**.

In the **Services** list, make sure that the status of **AppFabric Caching Service** is **Started**. If not, right-click **AppFabric Caching Service**, and click **Start**.

By default, the **Repair Automatically** option is enabled for this rule. You can restore the default setting for this rule by doing the following:

**Set the Health Analyzer rule to repair automatically**

On the SharePoint Central Administration website , click **Monitoring**.

On the Monitoring page, in the **Health Analyzer** section, click **Review rule definitions**.

On the Health Analyzer Rule Definitions - All Rules page, in the **Category: Availability** section, click the name of the rule.

On the **Health Analyzer Rule Definitions** page, click **Edit Item**.

Select the **Repair Automatically** check box, and then click **Save**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
