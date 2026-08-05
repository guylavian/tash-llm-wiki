---
title: "One or more servers can't retrieve the outgoing email credentials (SharePoint Server 2019) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-one-or-more-servers-can-t-retrieve-the-outgoing-email-credentials
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/one-or-more-servers-can-t-retrieve-the-outgoing-email-credentials
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: One or more servers can't retrieve the outgoing email credentials for, SharePoint Server."
---

# One or more servers can't retrieve the outgoing email credentials (SharePoint Server 2019) - SharePoint Server

Note

One or more servers can't retrieve the outgoing email credentials (SharePoint Server 2019)

# One or more servers can't retrieve the outgoing email credentials (SharePoint Server 2019)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** One or more servers can't retrieve the outgoing email credentials.

**Summary:** At least one web application is configured to use authentication when sending email. There are one or more servers in this farm that can't retrieve the credentials used to authenticate to the outgoing email server. Without credentials, these servers can only send email anonymously.

**Cause:** The application credential key wasn't found on these servers or they don't have the same application credential key originally used to store the SMTP password. Every server in the farm must have an application credential key to store and retrieve the SMTP password. The application credential key must be identical on each server.

**Resolution:** Use the **Set-SPApplicationCredentialKey** cmdlet on each failing server to set the application credential key. If the current SMTP password was stored using a different application credential key, you must set the new application credential key on every server in the farm and then save the SMTP credentials again.

See also

## See also

Concepts

#### Concepts

Plan outgoing email for a SharePoint Server farm

Configure outgoing email for a SharePoint Server farm

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
