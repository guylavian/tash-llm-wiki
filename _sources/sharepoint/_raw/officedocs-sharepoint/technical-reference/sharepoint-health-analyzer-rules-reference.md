---
title: "SharePoint Health Analyzer rules reference for SharePoint Server 2016 - SharePoint Server"
description: "Learn how to troubleshoot problems in SharePoint Server using SharePoint Health Analyzer rules."
ms.topic: landing-page
---
Note

SharePoint Health Analyzer rules reference for SharePoint Server

# SharePoint Health Analyzer rules reference for SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The Health Analyzer rules in this section are arranged by categories, as they appear in the Health Analyzer Rule Definitions page in the SharePoint Central Administration website.

In this section:

Security

## Security

The following Health Analyzer rules relate to security in SharePoint Server:

Accounts used by application pools or service identities are in the local machine Administrators group (SharePoint Server)

Business Data Connectivity connectors are currently enabled in a partitioned environment (SharePoint Server)

Upcoming SSL certificate expirations (SharePoint Server Subscription Edition)

SSL certificates are about to expire (SharePoint Server Subscription Edition)

SSL certificates have expired (SharePoint Server Subscription Edition)

Web Applications using Claims authentication require an update (SharePoint Server)

The server farm account should not be used for other services (SharePoint Server)

The unattended Service Account Application ID is not specified or has an invalid value (SharePoint Server)

Antimalware Scan Interface (AMSI) protection may not be working (SharePoint Server)

Basic authentication is being deprecated (SharePoint Server)

Performance

## Performance

The following Health Analyzer rules relate to performance for SharePoint Server:

Application pools recycle when memory limits are exceeded (SharePoint Server)

Databases used by SharePoint have fragmented indices (SharePoint Server)

Databases exist on servers running SharePoint Foundation (SharePoint Server)

The paging file size should exceed the amount of physical RAM in the system (SharePoint Server)

Databases used by SharePoint have outdated index statistics (SharePoint Server)

The timer service failed to recycle (SharePoint Server)

The Visio Graphics Service has a maximum cache age setting that will adversely impact performance (SharePoint Server)

The Visio Graphics Service has a maximum Web Drawing Size setting that will adversely impact performance (SharePoint Server)

The Visio Graphics Service has a maximum recalc duration setting that will adversely impact user perceived performance (SharePoint Server)

The Visio Graphics Service has a minimum cache age setting that will adversely impact performance (SharePoint Server)

The Visio Graphics Service has a minimum cache age setting that may cause a security issue (SharePoint Server)

The Visio Graphics Service has a maximum cache size setting that may adversely impact performance (SharePoint Server)

Search - One or more crawl databases may have fragmented indices (SharePoint Server)

Configuration

## Configuration

The following Health Analyzer rules relate to configuration of SharePoint Server.

Alternate access URLs have not been configured (SharePoint Server)

The Application Discovery and Load Balancer Service is not running in this farm (SharePoint Server)

Automatic Update setting inconsistent across farm servers (SharePoint Server 2016)

Built-in accounts are used as application pool or service identities (SharePoint Server)

Certificate notification contacts haven't been configured (SharePoint Server Subscription Edition)

Missing server side dependencies (SharePoint Server)

Databases running in compatibility range, upgrade recommended (SharePoint Server)

Databases require upgrade or not supported (SharePoint Server)

One or more categories are configured with Verbose trace logging (SharePoint Server)

One or more servers can't retrieve the outgoing email credentials (SharePoint Server 2019)

Outbound e-mail has not been configured (SharePoint Server)

Product / patch installation or server upgrade required (SharePoint Server)

Databases within this farm are set to read only and will fail to upgrade unless it is set to a read-write state (SharePoint Server)

Web.config file has incorrect settings for the requestFiltering element (SharePoint Server)

Server role configuration isn't correct (SharePoint Server 2016)

Dedicated crawl target configuration has one or more invalid servers (SharePoint Server)

Distributed cache service is not configured on server(s) (SharePoint Server 2016)

Distributed cache service is unexpectedly configured on server(s) (SharePoint Server 2016)

The number of Distributed Cache hosts in the farm exceeds the recommended value (SharePoint Server)

This Distributed Cache host may cause cache reliability problems (SharePoint Server)

Firewall client settings on the cache host are incorrect (SharePoint Server)

More cache hosts are running in this deployment than are registered with SharePoint (SharePoint Server)

Distributed cache service is not enabled in this deployment (SharePoint Server)

Web.config files are not identical on all machines in the farm (SharePoint Server)

One or more app domains for web applications aren't configured correctly (SharePoint Server)

One or more web applications are configured to use Windows Classic authentication (SharePoint Server)

The InfoPath Forms Services Maintenance timer job is not enabled (SharePoint Server)

InfoPath form library forms cannot be filled out in a Web browser (SharePoint Server)

InfoPath Forms Services forms cannot be filled out in a Web browser because no State Service connection is configured (SharePoint Server)

Expired sessions are not being deleted from the ASP.NET Session State database (SharePoint Server)

The State Service Delete Expired Sessions timer job is not enabled (SharePoint Server)

Verify each User Profile Service Application has an associated Managed Metadata Service Connection (SharePoint Server)

Verify each User Profile Service Application has an associated Search Service Connection (SharePoint Server)

Verify each User Profile service application has a My Site host configured (SharePoint Server)

Verify that the critical User Profile Application and User Profile Proxy Application timer jobs are available and have not been mistakenly deleted (SharePoint Server)

Validate the My Site Host and individual My Sites are on a dedicated Web application and separate URL domain (SharePoint Server)

Verify that the Activity Feed Timer Job is enabled (SharePoint Server)

People Search relevance is not optimized when the Active Directory has errors in the manager reporting structure (SharePoint Server)

The settings for the Machine Translation Service are not within the recommended limits (SharePoint Server)

Verify that OAuth is configured correctly for the Machine Translation Service application proxy (SharePoint Server)

Verify that OAuth is configured correctly for the Machine Translation Service application (SharePoint Server)

Immediate translations for the Machine Translation service are disabled (SharePoint Server)

The Machine Translation Service is not running when it should be running (SharePoint Server)

XLIFF translations for the Machine Translation Service is disabled (SharePoint Server)

Certificate Management is not managing the nonce cookie certificate (SharePoint Server)

Availability

## Availability

The following Health Analyzer rules relate to availability of SharePoint Server.

Content databases contain orphaned Apps (SharePoint Server)

Drives are running out of free space (SharePoint Server)

Drives are at risk of running out of free space (SharePoint Server)

Content databases contain orphaned items (SharePoint Server)

Some content databases are growing too large (SharePoint Server)

Database has large amounts of unused space (SharePoint Server)

The Net.Pipe Listener Adapter isn't available (SharePoint Server)

The Security Token Service is not available (SharePoint Server)

One or more servers is not responding (SharePoint Server)

One or more services have started or stopped unexpectedly (SharePoint Server)

One of the cache hosts in the cluster is down (SharePoint Server)

Cached objects have been evicted (SharePoint Server)

The current server is running low on memory (SharePoint Server)

Drives used for SQL databases are running out of free space (SharePoint Server)

All State Service databases are paused for a State Service Application (SharePoint Server)

A State Service Application has no database defined (SharePoint Server)

The settings for Word Automation Services are not within the recommended limits (SharePoint Server)

Critical state of this rule indicates that the Word Automation Services is not running when it should be running (SharePoint Server)

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
