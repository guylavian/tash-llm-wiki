---
title: "Remove SharePoint Server hybrid scenarios - SharePoint Server"
type: reference
domain: sharepoint
slug: hybrid-removing-sharepoint-hybrid-scenarios
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/hybrid/removing-sharepoint-hybrid-scenarios
family: hybrid
documentKind: "how-to"
abstract: "Removing SharePoint hybrid scenarios in SharePoint Server"
---

# Remove SharePoint Server hybrid scenarios - SharePoint Server

Note

Removing SharePoint hybrid scenarios

# Removing SharePoint hybrid scenarios

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This guide will walk you through removing SharePoint Hybrid functionality from your SharePoint in Microsoft 365 farm.

Cloud Hybrid Search

## Cloud Hybrid Search

Cloud Hybrid Search may be removed by deleting the Search Service Application.

Note

Before deleting the Search Service Application, make sure to delete the content sources. This ensures that SPO results won't include documents from your on-premises environment.

In the **Central Administration** website, select **Application Management**.

In the **Application Management** page, select **Manage service applications**.

In the **Service Application** page, highlight your Cloud Hybrid Search Service Application. The name of the Service Application may vary, but the **Type** will be **Search Service Application**.

Note

The **Type** is identical to the standard SharePoint in Microsoft 365 Search Service Application.

On the ribbon, select **Delete**.

You may then create a new non-Cloud Search Service Application. For info about how to create and manage your Search Service Application, see the SharePoint Server documentation in Search.

If you want to remove all hybrid documents from SharePoint Online search results, contact the support team for further guidance.

OneDrive and sites

## OneDrive and sites

After you have configured OneDrive and Sites hybrid, you can manage it in the SharePoint in Microsoft 365 Central Administration website.

- In the **Central Administration** website, select **Microsoft 365**.

- On the Microsoft 365 page, select **Configure hybrid OneDrive and Sites features**.

- On the **Configure hybrid OneDrive and Sites features** page, under the **Select hybrid features**, select **None**, and then select **OK**.

Setting the option to **None** also removes the Hybrid app launcher feature.

SharePoint hybrid taxonomy and hybrid content types

## SharePoint hybrid taxonomy and hybrid content types

See Stopping replication of taxonomy groups.

Hybrid self-service site creation

## Hybrid self-service site creation

See Manage hybrid self-service site creation.

Removing the Azure Access Control Service Application Proxy and SharePoint in Microsoft 365 Application Principal Management Service Application Proxy

## Removing the Azure Access Control Service Application Proxy and SharePoint in Microsoft 365 Application Principal Management Service Application Proxy

The final step to removing hybrid is to delete the **Azure Access Control Service Application Proxy** and **SharePoint Application Principal Management Service Application Proxy** created by the Hybrid Configuration Wizard.

- In the **Central Administration** website, select **Application Management**.

- In the **Application Management** page, select **Manage service applications**.

- In the **Service Applications** page, highlight the Service Application named **ACS**. On the ribbon, select **Delete**.

- In the **Service Applications** page, highlight the Service Application named **SharePoint App Management Proxy**. On the ribbon, select **Delete**.

- Perform an iisreset on all SharePoint Servers in the farm.

Additional resources

## Additional resources

- Last updated on 
		2025-02-17
