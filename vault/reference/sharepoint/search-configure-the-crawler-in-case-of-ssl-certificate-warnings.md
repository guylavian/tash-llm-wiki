---
title: "Configure the crawler in case of SSL certificate warnings in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: search-configure-the-crawler-in-case-of-ssl-certificate-warnings
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/search/configure-the-crawler-in-case-of-ssl-certificate-warnings
family: search
documentKind: "how-to"
abstract: "Specify whether a SharePoint Server crawler will crawl a site if there's a problem with the site's Secure Sockets Layer (SSL) certificate."
---

# Configure the crawler in case of SSL certificate warnings in SharePoint Server - SharePoint Server

Note

Configure the crawler in case of SSL certificate warnings in SharePoint Server

# Configure the crawler in case of SSL certificate warnings in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

When a crawler requests a connection to crawl a site, the system generates a warning if there's a problem with the site's SSL certificate. By default, the crawler doesn't crawl the site when this happens. For security reasons, we strongly recommend that you don't change this default crawler behavior unless you have sufficient reason to do so.

An SSL certificate problem can occur due to the following reasons:

The certificate is expired.

The certificate isn't signed by a trusted authority.

The name in the certificate doesn't match the site name.

A name mismatch could be the result of an attempt to spoof the validity of a site and trick users into opening documents from the site or into providing passwords and other information that could allow a hacker to access the system.

However, if you're only crawling internal sites, you might expect SSL warnings in certain cases. For example, you might know that some site names and certificate names are mismatched for legitimate reasons, such as if the organization changed a server name or site name, or if the organization is using a single certificate for multiple sites. In such cases, it might be safe to change the default crawler behavior and thus ignore SSL certificate warnings.

Use the following procedure to specify whether the crawler will crawl sites in the event of SSL certificate warnings. The setting applies to all content sources in all Search service applications in a farm. After you change this setting, you must recrawl all affected sites so that the appropriate content is in the search index.

**To configure the crawler for SSL certificate warnings**

Verify that the user account that is performing this procedure is a member of the Farm Administrators Group.

In Central Administration, in the Quick Launch, select **General Application Settings**.

On the General Application Settings page, in the **Search** section, select **Farm Search Administration**.

On the Farm Search Administration page, in the **Farm-Level Search Settings** section, click the value of the **Ignore SSL Warnings** setting ( **Yes** or **No**). The default setting is **No**.

In the **Search SSL Settings** dialog, do one of the following:

If you don't want the crawler to crawl a site when there's an SSL certificate warning, make sure that the **Ignore SSL certificate name warnings** check box is cleared. For security reasons, the check box is cleared by default.

If you want the crawler to crawl a site even if there's an SSL certificate warning, make sure that the **Ignore SSL certificate name warnings** check box is selected.

- Select **OK**.

See also

## See also

Concepts

#### Concepts

Manage crawling in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
