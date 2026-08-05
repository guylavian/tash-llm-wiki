---
title: "Configure authoritative pages in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: search-configure-authoritative-pages
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/search/configure-authoritative-pages
family: search
documentKind: "how-to"
abstract: "Learn how to specify authoritative pages and non-authoritative URLs and sites. Search uses the list of authoritative pages to calculate the ranking of results."
---

# Configure authoritative pages in SharePoint Server - SharePoint Server

Note

Configure authoritative pages in SharePoint Server

# Configure authoritative pages in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Static rank determines the relative importance of a page, and it is computed as the smallest number of clicks it would take a user to navigate from an authoritative page to a document. The closer a document is to the most authoritative page, the higher its static rank is.

An administrator provides a small set of authoritative pages. An example of an authoritative page could be the home page of a company portal.

An administrator with specific knowledge of an area can influence the relative importance of pages by specifying additional authoritative and non-authoritative pages. An example of non-authoritative pages could be URLs of sites that contain outdated information that are kept for record-keeping

Specify pages as authoritative or non-authoritative

## Specify pages as authoritative or non-authoritative

Use the following procedure to specify pages as authoritative or non-authoritative.

**To specify pages as authoritative or non-authoritative**

Verify that the user account that is performing this procedure is an administrator for the Search service application.

In Central Administration, in the **Application Management** section, click **Manage service applications**.

Click the Search service application.

On the Search Administration page, in the Quick Launch, click **Authoritative Pages**.

On the Specify Authoritative Pages page, in the **Most authoritative pages** box in the **Authoritative Web Pages** section, type the URLs of pages that are the most authoritative. Separate the URLs with returns so that there is one URL per line.

In the **Second-level authoritative pages** box, type the URLs of any pages that should be seen as second-level.

In the **Third-level authoritative pages** box, type the URLs of any pages that should be seen as third-level.

In the **Non-authoritative Sites** section, in the **Sites to demote** box, type the URLs of any sites that you want to be ranked lower than all of the other sites. Type one URL per line.

All URLs whose prefix matches the prefix of a URL in the **Sites to demote** box are demoted. Example: Entering http://archive/ demotes the rank of all URLs that begin with http://archive/.

In the **Relevance Ranking Analytics** section, select the **Refresh now** check box to run the ranking analytics you have defined or that you have updated.

If you clear the check box, ranking analytics run later according to a defined schedule.

Click **OK**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
