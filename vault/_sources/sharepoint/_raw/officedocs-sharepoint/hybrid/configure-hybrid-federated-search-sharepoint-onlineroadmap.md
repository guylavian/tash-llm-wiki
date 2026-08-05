---
title: "Configure hybrid federated search from SharePoint in Microsoft 365 to SharePoint Server - roadmap - SharePoint Server"
description: "Learn how to configure hybrid federated search from SharePoint in Microsoft 365 to SharePoint Server."
ms.topic: article
---
Note

Configure hybrid federated search from SharePoint in Microsoft 365 to SharePoint Server - roadmap

# Configure hybrid federated search from SharePoint in Microsoft 365 to SharePoint Server - roadmap

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Important

Hybrid Federated Search in SharePoint for Microsoft 365 (Inbound), the capability to display search results from SharePoint on-premises content in SharePoint Online, has been retired as of September 2024. Hybrid Federated Search for SharePoint Server (Outbound), the ability to view SharePoint Online search results in SharePoint on-premises, and Cloud hybrid search remain operational. If you need to display search results from external content in SharePoint Online, we recommend you use Microsoft Search Graph Connectors or Cloud hybrid search.

This article provides the roadmap for configuring hybrid search from SharePoint in Microsoft 365 for enterprises to SharePoint Server, which allows your users to see search results from SharePoint Server when searching from Microsoft 365.

Follow these steps in the order shown. If you already completed a step when you did a different roadmap, skip that step and go to the next.

| **Step** | **Description** |
| --- | --- |
| **1. Configure Microsoft 365 for SharePoint in Microsoft 365 hybrid** | Configure your Microsoft 365 organization for a hybrid environment, including registering your domain, configuring UPN suffixes, and synchronizing your user accounts. |
| **2. Set up SharePoint in Microsoft 365 services for hybrid environments** | Configure the needed SharePoint in Microsoft 365 services for hybrid search, including User Profiles, MySites, and the Application Management service. |
| **3. Configure server-to-server authentication from SharePoint Server to SharePoint in Microsoft 365** | Configure server-to-server authentication between SharePoint Server and Microsoft 365. |
| **4. Synchronize user profiles** | Run SharePoint in Microsoft 365 user profile synchronization to update the SharePoint in Microsoft 365 User Profile Store with the new account UPNs that you added when you configured Microsoft 365. For information about how to run profile sync, see Manage user profile synchronization in SharePoint Server. |
| **5. Configure inbound connectivity** | Configure authentication from Microsoft 365 to SharePoint Server. |
| **6. Configure a reverse proxy device for SharePoint Server hybrid** | Configure a reverse proxy device for your on-premises environment. |
| **7. Display hybrid federated search results in SharePoint in Microsoft 365** | Configure your search service application to display search results from SharePoint Server in Microsoft 365. |

See also

## See also

Concepts

#### Concepts

Plan SharePoint Server hybrid

Additional resources

## Additional resources

- Last updated on 
		2024-09-19
