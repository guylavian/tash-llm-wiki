---
title: "One or more web applications are configured to use Windows Classic authentication (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-one-or-more-web-applications-are-configured-to-use-windows-classic-authenticatio
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/one-or-more-web-applications-are-configured-to-use-windows-classic-authenticatio
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: One or more web applications are configured to use Windows Classic authentication, for SharePoint Server."
---

# One or more web applications are configured to use Windows Classic authentication (SharePoint Server) - SharePoint Server

Note

One or more web applications are configured to use Windows Classic authentication (SharePoint Server)

# One or more web applications are configured to use Windows Classic authentication (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** One or more web applications are configured to use Windows Classic authentication.

**Summary:** This health rule is triggered when at least one Web application is configured to use Windows Classic authentication mode. Windows Classic authentication is deprecated in SharePoint Server. We recommend that you migrate to claims-based authentication, because many of the features in SharePoint Server require the claims-based authentication mode.

**Cause:** Web applications are configured to use Windows Classic authentication mode.

**Resolution: Migrate Web applications from classic mode to claims-based authentication.**

- You have to migrate Web applications from classic mode to claims-based authentication. For more information, see Migrate from classic-mode to claims-based authentication in SharePoint Server.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
