---
title: "Verify that the Activity Feed Timer Job is enabled (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: Verify that the Activity Feed Timer Job is enabled, for SharePoint Server."
ms.topic: troubleshooting
---
Note

Verify that the Activity Feed Timer Job is enabled (SharePoint Server)

# Verify that the Activity Feed Timer Job is enabled (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Verify that the Activity Feed Timer Job is enabled.

**Summary:** You must enable the Activity Feed timer job if you want users to receive information about their colleagues, such as updates to profile properties and creation of social tags and notes.

**Cause:** The Activity Feed timer job is not enabled.

**Resolution: Enable the Activity Feed timer job**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the SharePoint Central Administration website, on the Quick Launch, click **Monitoring**.

On the Monitoring page, in the **Timer Jobs** section, click **Review job definitions**.

On the Job Definitions page, in the list of timer jobs, click **User Profile Service Application - Activity Feed Job**.

On the Edit Timer Job page, in the **Recurring Schedule** section, specify when you want the timer job to run, and then click **Enable**.

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
		2023-01-19
