---
title: "New health analyzer rules for SSL certificates - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-new-health-analyzer-rules-for-ssl-certificates
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/new-health-analyzer-rules-for-ssl-certificates
family: administration
documentKind: "article"
abstract: "Learn how SSL certificate implements health analyzer."
---

# New health analyzer rules for SSL certificates - SharePoint Server

Note

New health analyzer rules for SSL certificates

# New health analyzer rules for SSL certificates

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint has implemented the following four new health analyzer rules for SSL certificates:

- **Certificate notification contacts haven't been configured** health rule that provides notification through Central Administration when certificates are in use and no certificate notification contacts have been configured. This health rule will run weekly. Certificate notification contacts receive emails about SSL certificate expirations and can be configured by customers through the Configure certificate management settings page.

- **Upcoming SSL certificate expirations** health rule that provides advanced notification through both Central Administration and email of upcoming certificate expirations. This health rule will run weekly to notify certification notification contacts about certificates that are in use and will expire within the next 15 - 60 days. These thresholds are configurable by customers through the Configure certificate management settings page.

- **SSL certificates are about to expire** health rule that provides advanced notification through both Central Administration and email when certificates are about to expire. This health rule will run daily to notify certificate notification contacts about certificates that are in use and will expire within the next 15 days. This threshold is configurable by customers through the Configure certificate management settings page.

- **SSL certificates have expired** health rule that provides notification through both Central Administration and email when certificates have expired. This health rule will run daily to notify certificate notification contacts about certificates that are in use and have expired within the past 15 days. This threshold is configurable by customers through the Configure certificate management settings page.

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
