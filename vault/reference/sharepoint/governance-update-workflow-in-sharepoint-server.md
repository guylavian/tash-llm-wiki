---
title: "Update Workflow in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: governance-update-workflow-in-sharepoint-server
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/governance/update-workflow-in-sharepoint-server
family: governance
documentKind: "how-to"
abstract: "Walks through the steps required to keep workflow up to date in SharePoint Server."
---

# Update Workflow in SharePoint Server - SharePoint Server

Note

Update Workflow in SharePoint Server

# Update Workflow in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Run cmdlets after software updates are installed

## Run cmdlets after software updates are installed

It is important that any Cumulative Updates (CU) for SharePoint Server and Workflow Manager are installed in a coordinated fashion. After an update has been performed, several Microsoft PowerShell cmdlets must be run in order to maintain the connection between the SharePoint Server farm and the Workflow Manager farm.

Run the following PowerShell cmdlets as an administrator from the SharePoint Administration Shell after the updates have been installed for SharePoint Server, Workflow Manager, and Workflow Manager Client.

Important

The latest update level must be installed on SharePoint Server, Workflow Manager, and Workflow Manager Client before you run the update cmdlets.

```
$credential = [System.Net.CredentialCache]::DefaultNetworkCredentials
$site = Get-SPSite(<siteUri>)
$proxy = Get-SPWorkflowServiceApplicationProxy
$svcAddress = $proxy.GetWorkflowServiceAddress($site)
Copy-SPActivitiesToWorkflowService -WorkflowServiceAddress $svcAddress -Credential $credential -Force $true
```

Note

Because workflow supports environments with multiple Site Subscriptions, the  `$site` Site Collection address determines the proper configuration location for workflow settings.

Troubleshooting steps for workflow updates

## Troubleshooting steps for workflow updates

Make sure all components are on the latest patch level. This includes SharePoint Server, Workflow Manager, and Workflow Manager Client.

Verify the $proxy connection settings using the following commands:

```
$proxy = Get-SPWorkflowServiceApplicationProxy
$site = Get-SPSite(<siteUri>)
$proxy.GetWorkflowServiceAddress($site)
```

Inspect any errors displayed in the SharePoint Designer user interface or any errors shown in the SharePoint Workflow Status user interface.

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
