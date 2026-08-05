---
title: "Verify each User Profile Service Application has an associated Search Service Connection (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-verify-each-user-profile-service-application-has-an-associated-search-service-co
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/verify-each-user-profile-service-application-has-an-associated-search-service-co
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: Verify each User Profile Service Application has an associated Search Service Connection, for SharePoint Server."
---

# Verify each User Profile Service Application has an associated Search Service Connection (SharePoint Server) - SharePoint Server

Note

Verify each User Profile Service Application has an associated Search Service Connection (SharePoint Server)

# Verify each User Profile Service Application has an associated Search Service Connection (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Summary:** The User Profile service presents URLs to end users in some Web Part and tag profile pages. These URLs are trimmed for security to make sure that users do not see URLs to which they do not have permissions. The User Profile service uses the Search service to perform this security trimming. If there is no Search service associated with the User Profile service application, security trimming does not work, and URLs are visible to everyone. Although users are denied access when they click a URL for which they do not have permissions, they nonetheless can see the URL in the search results.

**Cause:** A Search service connection is not included in the group of connections for the User Profile service application.

**Resolution: Edit the group of connections for the User Profile service application.**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the SharePoint Central Administration website, click **Application Management**.

On the Application Management page, in the **Service Applications** section, click **Configure service application associations**.

On the Service Application Associations page, in the **View** list, click **Service Applications**.

In the **Web Application/Service Application** column, click the User Profile service application for which you want to edit connections.

In the **Configure Service Application Associations** dialog, select the **Search Service** check box, or select **Default** in the **Edit the following group of connections** list, and then click **OK**. By default, all connections are included.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
