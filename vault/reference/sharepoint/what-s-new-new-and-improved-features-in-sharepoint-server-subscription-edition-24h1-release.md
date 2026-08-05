---
title: "New and improved features in SharePoint Server Subscription Edition Version 24H1 - SharePoint Server"
type: reference
domain: sharepoint
slug: what-s-new-new-and-improved-features-in-sharepoint-server-subscription-edition-24h1-release
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/what-s-new/new-and-improved-features-in-sharepoint-server-subscription-edition-24h1-release
family: what-s-new
documentKind: "overview"
abstract: "Learn about the new features and updates to existing features in SharePoint Server Subscription Edition Version 24H1."
---

# New and improved features in SharePoint Server Subscription Edition Version 24H1 - SharePoint Server

Note

New and improved features in SharePoint Server Subscription Edition Version 24H1

# New and improved features in SharePoint Server Subscription Edition Version 24H1

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Learn about the new features and updates introduced in the SharePoint Server Subscription Edition Version 24H1 feature update.

Summary of the features

## Summary of the features

The following table provides a summary of the new features introduced in the SharePoint Server Subscription Edition Version 24H1 feature update.

| **Feature** | **Release ring** | **More information** |
| --- | --- | --- |
| **Custom branding in the Suite Bar** | Standard release | For more information, see Custom branding in the Suite Bar.
 
This was part of *Early release* in the Version 23H2 feature update. |
| **Search vertical customization in modern search results** | Early release | For more information, see Search vertical customization in modern search results. |
| **OpenID Connect (OIDC) integration with SharePoint certificate management** | Early release | For more information, see OpenID Connect (OIDC) integration with SharePoint certificate management. |
| **Customer feedback experience in Central Administration** | Early release | For more information, see Customer feedback experience in Central Administration. |

Detailed description of features

## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server Subscription Edition Version 24H1.

Note

Features previously introduced in the Version 23H2 feature update will not be described here. For more information on Version 23H2, see New and improved features in SharePoint Server Subscription Edition Version 23H2.

Search vertical customization in modern search results

### Search vertical customization in modern search results

SharePoint Server Subscription Edition Version 24H1 introduces search vertical customization to the modern search experience, previously available only in the classic search experience. This customization feature allows users to add a custom search vertical to their search results page at the site and organizational levels.

The configuration of this feature is based on the same architecture as the existing classic UI, so the steps to configure this feature in the modern UI are similar to the classic UI.

For more information, see How to add a custom search vertical to your search results page in SharePoint Server.

OpenID Connect (OIDC) integration with SharePoint certificate management

### OpenID Connect (OIDC) integration with SharePoint certificate management

OpenID Connect (OIDC) is a modern authentication protocol that seamlessly integrates applications and devices with identity and authentication management solutions to keep pace with the evolving security and compliance needs of your organization.

SharePoint Server Subscription Edition Version 24H1 allows administrators to manage OIDC nonce cookie certificates via SharePoint Certificate Management. The nonce cookie certificate is part of the infrastructure that ensures OIDC authentication tokens are secure.

SharePoint farm administrators can now use the SharePoint Certificate Management feature to manage the full lifecycle of the OIDC nonce cookie certificate. This will automatically deploy the OIDC nonce cookie certificate to all servers in the farm and automatically configure the necessary permissions. A new SharePoint Health Analyzer health rule has been added to notify administrators if the nonce cookie certificate is not managed through SharePoint Certificate Management.

For more information, see Set up OIDC authentication in SharePoint Server with Microsoft Entra ID.

Customer feedback experience in Central Administration

### Customer feedback experience in Central Administration

SharePoint Server Subscription Edition Version 24H1 introduces One Customer Voice (OCV) into the SharePoint Central Administration site to collect customer feedback from the SharePoint farm administrators. The feedback goes directly to the SharePoint Server product team at Microsoft to help us to continue to improve the product to meet customer needs.

The OCV experience currently offers a two-question survey, which automatically appears in SharePoint Central Administration based on these rules:

- The first survey appears two weeks after a farm administrator visits the Central Admin site after the update is installed.

- The second survey will appear after six months if the SharePoint farm administrator completes the first survey.

- If the SharePoint Administrator chooses to skip the survey, it will appear again every two weeks until the survey is completed.

For more information, see Configure the One Customer Voice (OCV) feedback.

Additional resources

## Additional resources

- Last updated on 
		2024-03-12
