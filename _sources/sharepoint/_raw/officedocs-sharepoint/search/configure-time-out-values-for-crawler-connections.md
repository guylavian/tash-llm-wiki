---
title: "Configure time-out values for crawler connections in SharePoint Server - SharePoint Server"
description: "Change how long the SharePoint Server search crawler will wait for a connection to a content repository or for a response to a connection attempt."
ms.topic: how-to
---
Note

Configure time-out values for crawler connections in SharePoint Server

# Configure time-out values for crawler connections in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

By default, when the crawler attempts to connect to a content repository, it waits 60 seconds for a connection or for a response to a connection attempt. Use the procedure in this article to change these crawler time-out values.

If the crawler does not connect or get a response within the time specified, it tries to connect again. If the crawler does not connect on the second attempt within the time specified, it does not crawl the repository during that crawl.

**To configure time-out settings for crawler connections**

Verify that the user account that is performing this procedure is a farm administrator.

In Central Administration, in the Quick Launch, click **General Application Settings**.

On the General Application Settings page, in the **Search** section, click **Farm Search Administration**.

On the Farm Search Administration page, in the **Farm-Level Search Settings** section, click either of the **Time-out (seconds)** setting values.

In the **Search Time-out Setting** dialog, do the following:

In the **Connection time (in seconds)** text box, type the number of seconds that you want the crawler to wait when it attempts to connect to a content repository. The default value is 60 seconds.

In the **Request acknowledgment time (in seconds)** text box, type the number of seconds that you want the crawler to wait for a content repository to respond to a connection attempt. The default value is 60 seconds.

Click **OK**.

See also

## See also

Manage crawling in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
