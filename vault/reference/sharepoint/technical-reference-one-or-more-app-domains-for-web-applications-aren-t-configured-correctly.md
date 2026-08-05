---
title: "One or more app domains for web applications aren't configured correctly (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-one-or-more-app-domains-for-web-applications-aren-t-configured-correctly
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/one-or-more-app-domains-for-web-applications-aren-t-configured-correctly
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: One or more app domains for web applications aren't configured correctly, for SharePoint Server."
---

# One or more app domains for web applications aren't configured correctly (SharePoint Server) - SharePoint Server

Note

One or more app domains for web applications aren't configured correctly (SharePoint Server)

# One or more app domains for web applications aren't configured correctly (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** One or more app domains for web applications aren't configured correctly.

**Summary:** This health rule checks to see if the multiple app domains feature is enabled by looking at the state of the  *Microsoft.SharePoint.Administration.SPWebService.ContentService.SupportMultipleAppDomains* property. If this is enabled, the health rule then checks to see if there are multiple web application zones in each web application. If there are, it continues to check if there's an app domain defined for each web application zone. The health rule alert is triggered if the final condition isn't met. It's also triggered if the web application and app domain aren't using the same Internet Information Services (IIS) port binding, web application zone, application pool account, and authentication type.

**Cause:** The SharePoint Server environment isn't set to use multiple app domains, or the web application is incorrectly configured for multiple web application zones.

**Resolution:**

- You have to configure the app domains for web applications. For more information, see Enable apps in AAM or host-header environments for SharePoint 2016.

Additional resources

## Additional resources

- Last updated on 
		2024-05-30
