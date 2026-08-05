---
title: "The timer service failed to recycle (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-the-timer-service-failed-to-recycle
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/the-timer-service-failed-to-recycle
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: The timer service failed to recycle, for SharePoint Server."
---

# The timer service failed to recycle (SharePoint Server) - SharePoint Server

Note

The timer service failed to recycle (SharePoint Server)

# The timer service failed to recycle (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Summary:** The last attempt to recycle the timer service failed. More than half of the attempts during the past week have also failed.

**Cause:** The Timer Service Recycle job conflicts with other long-running timer jobs.

**Resolution: Change the schedule for the Timer Service Recycle job so that it does not conflict with other long-running timer jobs.**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the SharePoint Central Administration website, click **Monitoring**.

On the Monitoring page, in the **Timer Jobs** section, click **Review job definitions**.

On the Job Definitions page, click **Timer Service Recycle**.

On the Edit Timer Job page, change the schedule so that it does not conflict with other long-running timer jobs, and then click **OK**. The default setting is to run daily at 6 AM.

For more information, see Default timer jobs in SharePoint Server 2019, Default timer jobs in SharePoint Server 2016, or Default timer jobs in SharePoint 2013.

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
