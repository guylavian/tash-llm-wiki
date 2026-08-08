---
title: "The Machine Translation Service is not running when it should be running (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: The Machine Translation Service is not running when it should be running, for SharePoint Server."
ms.topic: troubleshooting
---
Note

The Machine Translation Service is not running when it should be running (SharePoint Server)

# The Machine Translation Service is not running when it should be running (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** The Machine Translation Service is not running when it should be running.

**Summary:** The Machine Translation Service batch mode uses a timer job to pull translation items from the Machine Translation Service database and then assign those translation items to individual application servers. If the timer job doesn't run, items can't be translated.

**Cause:** The Machine Translation Service timer job isn't enabled.

**Resolution: Enable the Machine Translation Service timer job.**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On Central Administration , click **Monitoring**.

On the Job Definitions page, in the list of timer jobs, click **Machine Translation Service Timer Job**.

On the Edit Timer Job page, in the **Recurring Schedule** section, specify when you want the timer job to run, and then click **Enable**.

The default is every 15 minutes.

See also

## See also

Concepts

#### Concepts

Default timer jobs in SharePoint Server 2019

Other Resources

#### Other Resources

Default timer jobs in SharePoint Server 2016

Default timer jobs in SharePoint 2013

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
