---
title: "Dedicated crawl target configuration has one or more invalid servers (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: Dedicated crawl target configuration has one or more invalid servers, for SharePoint Server."
ms.topic: troubleshooting
---
Note

Dedicated crawl target configuration has one or more invalid servers (SharePoint Server)

# Dedicated crawl target configuration has one or more invalid servers (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Dedicated crawl target configuration has one or more invalid servers.

**Summary:** Dedicated crawl target configuration has one or more invalid servers. This may degrade search crawl performance.

**Cause:** The URI is incorrect, or the server is not joined with a valid role to the SharePoint farm.

**Resolution: Make sure the uniform resource identifier (URI) is correct, and the server is joined with a valid role to the SharePoint farm.**

- Make sure that the URI is correct. A valid URI meets the following criteria:

The host portion of the URI should be the name of a server that has joined the SharePoint farm.

The URI Scheme should be HTTP.

The URI must not contain an absolute path.

For more information, see URI class.

- Make sure that the server is joined with a valid role to the SharePoint farm. The server can be any of the following:

Front-end

Application server

Distributed cache

Search

Custom

Single-server farm or a stand-alone server in the SharePoint farm

For more information, see Overview of MinRole Server Roles in SharePoint Server 2016 and Description of MinRole and associated services in SharePoint Server 2016.

See also

## See also

Concepts

#### Concepts

Add a server to a SharePoint Server 2016 farm

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
