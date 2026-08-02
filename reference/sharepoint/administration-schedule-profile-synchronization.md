---
title: "Schedule profile synchronization in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-schedule-profile-synchronization
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/schedule-profile-synchronization
family: administration
documentKind: "how-to"
abstract: "Learn how to schedule profile synchronization in SharePoint Server."
---

# Schedule profile synchronization in SharePoint Server - SharePoint Server

Note

Schedule profile synchronization in SharePoint Server

# Schedule profile synchronization in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Follow this procedure to schedule profile synchronization. You must have first performed a full synchronization before you can set the incremental synchronization schedule.

You need to be a farm administrator or an administrator of the User Profile service application to perform this procedure.

**To schedule profile synchronization**

On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.

On the Manage Service Applications page, click the link for the User Profile service application.

On the Manage Profile Service page, in the **Synchronization** section, click **Configure Synchronization Timer Job**.

On the Edit Timer Job page, in the **Recurring Schedule** section, select the frequency at which you want recurring profile synchronization to occur.

If you select **Minutes**, type the number of minutes that should pass between the start of each timer job.

If you select **Hourly**, type the number of minutes past every hour that the timer job should start to run at the earliest, and type the number of minutes past every hour that the timer job should start to run at the latest.

If you select **Daily**, select the time at which the timer job should start to run, at the earliest and at the latest, every day.

If you select **Weekly**, select the earliest and latest day and time at which the timer job should start to run every week.

If you select **Monthly**, either select the earliest and latest date and time at which the timer job should start to run every month, or select a day and time at which the timer job should start to run every month.

Note

If you want to specify an exact starting time for the timer job to run, set the same value in the start and end times of the interval in which the timer job should start.

- Click **OK**, or, if you want to start the profile synchronization immediately, click **Run Now**.

See also

## See also

Concepts

#### Concepts

Start profile synchronization manually in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
