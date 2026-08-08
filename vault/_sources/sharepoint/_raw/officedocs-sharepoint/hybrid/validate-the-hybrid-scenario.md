---
title: "Validate the Business Connectivity Services hybrid scenario - SharePoint Server"
description: "How to validate the Business Connectivity Services (BCS) hybrid solution is working."
ms.topic: how-to
---
Note

Validate the Business Connectivity Services hybrid scenario

# Validate the Business Connectivity Services hybrid scenario

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Now that you have created an external list or deployed an app for SharePoint in Microsoft 365, you need to test the security you put in place. Every account that will be accessing and manipulating the external data must have three properties:

It must have user or greater permissions to the SharePoint in Microsoft 365 site and the external list or app for SharePoint in Microsoft 365.

It must be a federated account.

It must be a member of the on-premises global security group that you are using to control access to the OData service endpoint. For example, it must be a member of **ODataGroup**.

In this procedure, you will open the SharePoint in Microsoft 365 site and the external list or app for SharePoint in Microsoft 365 with four different accounts.

To validate security on the BCS hybrid

## To validate security on the BCS hybrid

Identify or create one account for each of the account types listed in the following table.

| **Account** | **Expected outcome** | **Troubleshooting step** |
| --- | --- | --- |
| **Account A** 
  Has site/list/app permissions.  
  Is federated.  
  Is a member of the on-premises global security group ( **ODataGroup**). | External data displayed and editable. | If the external data does not display or you cannot edit it, check the site permissions, your federation setup, and the membership of your on-premises global security group; for example, the **ODataGroup**. |
| **Account B** 
  Does not have site/list/app permissions.  
  Is federated.  
  Is a member of the on-premises global security group ( **ODataGroup**). | External data does not display. | If the external data does display and you can edit it, check the site/list/app permissions. |
| **Account C** 
  Has site/list/app permissions.  
  Is not federated (is a Microsoft 365 account only).  
  Cannot be added to the on-premises global security group ( **ODataGroup**). | External data does not display. | If the external data does display and you can edit it, check your federation setup and membership of your on-premises global security group ( **Odata Group**). |
| **Account D** 
  Has site/list/app permissions.  
  Is federated.  
  Is not a member of your on-premises global security group ( **ODataGroup**). | External data does not display. | If the external data does display and you can edit it, check the membership of your on-premises global security group ( **ODataGroup**) and the permissions that you set on the OData service endpoint that you configure in Deploy a Business Connectivity Services hybrid solution in SharePoint |

Open (by using In-Private browsing if possible) the SharePoint in Microsoft 365 site that contains the external list or app for SharePoint in Microsoft 365 by using each of the accounts in turn. Be sure to completely log out and close your browser in between tests.

If you don't see the expected outcome, refer to the troubleshooting step in the previous table, fix the issue, and repeat all four tests until you achieve the expected outcome.

If you see the error message:

ResourceBudgetExceeded, sending throttled status code. Exception=Microsoft.SharePoint.SPResourceBudgetExceededException: ResourceBudgetExceeded at Microsoft.SharePoint.SPResourceTally.Check(Int32 value) at Microsoft.SharePoint.SPAggregateResourceTally.Check(SPResourceKind kind, Int32 value) at Microsoft.SharePoint.Client.SPClientServiceHost.OnBeginRequest()

You can either remove the throttling:

```
$webapp = Get-SPWebApplication -Identity http://<URL of your on-premises farm>
$rule = $webapp.AppResourceTrackingSettings.Rules.Get([Microsoft.SharePoint.SPResourceKind]::ClientServiceRequestDuration)
$rule.Remove()
```

Or change the throttling value:

```
$webapp = Get-SPWebApplication -Identity http://<URL of your on-premises farm>
$webapp. AppResourceTrackingSettings.Rules.Add([Microsoft.SharePoint.SPResourceKind]::ClientServiceRequestDuration, 150000, 150000)
$webapp.AppResourceTrackingSettings.WindowCount = 10
$webapp.AppResourceTrackingSettings.WindowSize = [System.TimeSpan]::FromSeconds(30)
$webapp.Update()
```

where the 150000 means 150 seconds.

See also

## See also

Concepts

#### Concepts

Deploy a Business Connectivity Services hybrid solution in SharePoint

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
