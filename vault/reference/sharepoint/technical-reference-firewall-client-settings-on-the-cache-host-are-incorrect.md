---
title: "Firewall client settings on the cache host are incorrect (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-firewall-client-settings-on-the-cache-host-are-incorrect
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/firewall-client-settings-on-the-cache-host-are-incorrect
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: Firewall client settings on the cache host are incorrect, for SharePoint Server."
---

# Firewall client settings on the cache host are incorrect (SharePoint Server) - SharePoint Server

Note

Firewall client settings on the cache host are incorrect (SharePoint Server)

# Firewall client settings on the cache host are incorrect (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Firewall client settings on the cache host are incorrect.

**Summary:** Firewall rule settings for App fabric caching are disabled.

**Cause:** Firewall rule settings for App fabric caching are disabled.

**Resolution: Enable the firewall rules for the AppFabric Caching service.**

Verify that the user account that is performing this procedure is a member of the Administrators group on the local computer.

On **Server Manager**, click **Tools**, and then select **Windows Firewall with Advanced Security**.

In the **Windows Firewall with Advanced Security** console tree, click **Inbound Rules**.

In the **Inbound Rules** list, right-click **AppFabric Caching Service (TCP-In)**, and then select **Enable Rule**.

In the **Windows Firewall with Advanced Security** console tree, click **Outbound Rules**.

In the **Outbound Rules** list, right-click **AppFabric Caching Service (TCP-Out)** and then select **Enable Rule**.

By default, the **Repair Automatically** option is enabled for this rule. You can restore the default setting for this rule by doing the following:

On the SharePoint Central Administration website, click **Monitoring**.

On the Monitoring page, in the **Health Analyzer** section, click **Review rule definitions**.

On the Health Analyzer Rule Definitions - All Rules page, in the **Category: Configuration** section, click the name of the rule.

On the **Health Analyzer Rule Definitions** page, click **Edit Item**.

Select the **Repair Automatically** check box, and then click **Save**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
