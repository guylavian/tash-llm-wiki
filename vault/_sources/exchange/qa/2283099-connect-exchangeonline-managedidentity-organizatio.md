---
title: "Connect-ExchangeOnline -ManagedIdentity -Organization will raise this error \" The role assigned to application ** isn't supported in this scenario. Please check online documentation for assigning correct Directory Roles\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2283099/connect-exchangeonline-managedidentity-organizatio
question_id: 2283099
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Connect-ExchangeOnline -ManagedIdentity -Organization will raise this error " The role assigned to application ** isn't supported in this scenario. Please check online documentation for assigning correct Directory Roles"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2283099/connect-exchangeonline-managedidentity-organizatio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have created an Azure Function of type PowerShell core. the code will get user emails from sharepoint list, and remove the user from all the groups (Security group, Mail-Enabled security group, distribution list & Office 365 group)...

here is my power-shell code:-

```
#using namespace System.Net
# Input bindings are passed in via param block.
param($Timer)
#Import-Module PnP.PowerShell
# Get the current universal time in the default string format.
$currentUTCtime = (Get-Date).ToUniversalTime()

# The 'IsPastDue' property is 'true' when the current function invocation is later than scheduled.
if ($Timer.IsPastDue) {
    Write-Host "PowerShell timer is running late!"
}

# Write an information log with the current time.
Write-Host "PowerShell timer trigger function ran! TIME: $currentUTCtime"
# Connect to Microsoft Graph with required delegated scopes

Import-Module PnP.PowerShell
Write-Host "Start to connect to SharePoint"
$siteUrl = "https://B***.sharepoint.com/sites/analytics"
Connect-PnPOnline -Url $siteUrl -ManagedIdentity

# Get all items from the 'emails' list

$items = Get-PnPListItem -List "RemoveUserFromGroups" -Query "OpenError"

Import-Module Microsoft.Graph.Authentication
Import-Module Microsoft.Graph.Groups

 Write-Host "Start to connect to graph"
Connect-MgGraph -Identity
 Write-Host "Connected to Graph"

 # Connect to Exchange Online
 Write-Host "Start to Connect to exchange"
Connect-ExchangeOnline -ManagedIdentity -Organization b***.onmicrosoft.com
 Write-Host "Connected to exchange"

# Loop through items and delete each one

foreach ($item in $items) {
    $userEmail = $item["Title"]
     Write-Host "Current User is = $userEmail" 

     Write-Host "Start to Get-MgUser"
# --- PART 1: Azure AD + Office 365 Groups ---
$userList = Get-MgUser -Filter "mail eq '$userEmail' or userPrincipalName eq '$userEmail'"  -ConsistencyLevel eventual -All -Property Id, DisplayName, UserPrincipalName, Mail
 Write-Host "Get-MgUser completed"
$userObj = $userList | Select-Object -First 1

if (-not $userObj) {
    Write-Host "User $userEmail not found in Microsoft Graph. Skipping AAD removal."
} elseif (-not $userObj.Id) {
    Write-Host "User objectId missing even after lookup. Skipping AAD removal."
} else {
    Write-Host "Found user: $($userObj.DisplayName) ($($userObj.UserPrincipalName))"

    $groups = Get-MgUserMemberOf -UserId $userObj.Id -All
	$groupsAsOwner = Get-MgUserOwnedObject -UserId $userObj.Id -All

    foreach ($group in $groups) {
        if ($group.AdditionalProperties.'@odata.type' -ne '#microsoft.graph.group') {
            continue
        }

        $groupId = $group.Id
        $groupName = $group.AdditionalProperties.DisplayName

        if (-not $groupId) {
            Write-Host "Skipping group with empty ID"
            continue
        }

        $fullGroup = Get-MgGroup -GroupId $groupId

        if ($fullGroup.GroupTypes -contains "DynamicMembership") {
            Write-Host "Skipping dynamic group: ${groupName}"
            continue
        }

        # Remove as MEMBER
        try {
            Remove-MgGroupMemberByRef -GroupId $groupId -DirectoryObjectId $userObj.Id -ErrorAction Stop
            Write-Host "Removed as MEMBER from ${groupName}"
        }
        catch {
            Write-Host "Failed MEMBER removal from ${groupName}: $($_.Exception.Message)"
            Set-PnPListItem -List "RemoveUserFromGroups" -Identity $item.Id -Values @{ ProcessStatus = "Error" }
        }}
foreach ($group2 in $groupsAsOwner) {
$groupId2 = $group2.Id
$groupName2 = $group2.AdditionalProperties.DisplayName
        # Remove as OWNER
        try {
            Remove-MgGroupOwnerByRef -GroupId $groupId2 -DirectoryObjectId $userObj.Id -ErrorAction Stop
            Write-Host "Removed as OWNER from ${groupName2}"
        }
        catch {
            Write-Host "Failed OWNER removal from ${groupName2}: $($_.Exception.Message)"
            Set-PnPListItem -List "RemoveUserFromGroups" -Identity $item.Id -Values @{ ProcessStatus = "Error" }
        }
    }
	}

# --- PART 2: Exchange Distribution Groups + Mail-enabled Security Groups ---

Write-Host "Start Get-DistributionGroup"
$dlGroups = Get-DistributionGroup -ResultSize Unlimited
Write-Host "completed Get-DistributionGroup"

foreach ($dl in $dlGroups) {
    try {
        # Remove as MEMBER
        $members = Get-DistributionGroupMember -Identity $dl.Identity -ResultSize Unlimited
        $memberMatch = $members | Where-Object { $_.PrimarySmtpAddress -ieq $userEmail }

        if ($memberMatch) {
            Remove-DistributionGroupMember -Identity $dl.Identity -Member $userEmail -BypassSecurityGroupManagerCheck -Confirm:$false
            Write-Host "Removed as MEMBER from Exchange group: $($dl.DisplayName)"
        }

        # Remove as OWNER
        # $owners = (Get-DistributionGroup -Identity $dl.Identity).ManagedBy
		$owners = (Get-DistributionGroup -Identity $dl.Identity).ManagedBy | Foreach-Object { Get-Mailbox $_ }
        $ownerMatch = $owners | Where-Object { $_.PrimarySmtpAddress -ieq $userEmail }

        if ($ownerMatch) {
            Set-DistributionGroup -Identity $dl.Identity -ManagedBy @{ Remove = "$userEmail" }  –BypassSecurityGroupManagerCheck
            Write-Host "Removed as OWNER from Exchange group: $($dl.DisplayName)"
        }
    }
    catch {
        Write-Host "Failed Exchange removal for group: $($dl.DisplayName) - $($_.Exception.Message)"
        Set-PnPListItem -List "RemoveUserFromGroups" -Identity $item.Id -Values @{ ProcessStatus = "Error" }
    }
}
#$current = [int]$item["ProcessCount"]
#$newValue = $current + 1
Set-PnPListItem -List "RemoveUserFromGroups" -Identity $item.Id -Values @{ ProcessStatus = "Done" }
}

Write-Host "Cleanup script completed."
```

and i run those commands to assign the permission for the azure function to access SharePoint, graph & exchange..

where I enabled the managed identity of the azure function, and i got those Ids (AppId & ObjectID) from the Enterprise applications:-

```
# This script requires the modules Microsoft.Graph.Authentication, Microsoft.Graph.Applications, Microsoft.Graph.Identity.SignIns, which can be installed with the cmdlet Install-Module below:
# Install-Module Microsoft.Graph.Authentication, Microsoft.Graph.Applications, Microsoft.Graph.Identity.SignIns -Scope CurrentUser -Repository PSGallery -Force
Connect-MgGraph -Scope "Application.Read.All", "AppRoleAssignment.ReadWrite.All"
$managedIdentityObjectId = "fc***" # 'Object (principal) ID' of the managed identity
$scopeName = "Sites.Selected"
$resourceAppPrincipalObj = Get-MgServicePrincipal -Filter "displayName eq 'Office 365 SharePoint Online'" # SPO
$targetAppPrincipalAppRole = $resourceAppPrincipalObj.AppRoles | ? Value -eq $scopeName
 
$appRoleAssignment = @{
    "principalId" = $managedIdentityObjectId
    "resourceId"  = $resourceAppPrincipalObj.Id
    "appRoleId"   = $targetAppPrincipalAppRole.Id
}
New-MgServicePrincipalAppRoleAssignment -ServicePrincipalId $managedIdentityObjectId -BodyParameter $appRoleAssignment | Format-List
```

```
# This script requires the modules Microsoft.Graph.Authentication, Microsoft.Graph.Applications, Microsoft.Graph.Identity.SignIns, which can be installed with the cmdlet Install-Module below:
# Install-Module Microsoft.Graph.Authentication, Microsoft.Graph.Applications, Microsoft.Graph.Identity.SignIns -Scope CurrentUser -Repository PSGallery -Force
Connect-MgGraph -Scope "Application.Read.All", "AppRoleAssignment.ReadWrite.All"
$managedIdentityObjectId = "fc***" # 'Object (principal) ID' of the managed identity
$scopeName = "Sites.FullControl.All"
$resourceAppPrincipalObj = Get-MgServicePrincipal -Filter "displayName eq 'Office 365 SharePoint Online'" # SPO
$targetAppPrincipalAppRole = $resourceAppPrincipalObj.AppRoles | ? Value -eq $scopeName
 
$appRoleAssignment = @{
    "principalId" = $managedIdentityObjectId
    "resourceId"  = $resourceAppPrincipalObj.Id
    "appRoleId"   = $targetAppPrincipalAppRole.Id
}
New-MgServicePrincipalAppRoleAssignment -ServicePrincipalId $managedIdentityObjectId -BodyParameter $appRoleAssignment | Format-List
```

```
Connect-PnPOnline -Url "https://b***.sharepoint.com/sites/analytics" -Interactive -ClientId "6***" 

Grant-PnPAzureADAppSitePermission -AppId "c4***" -DisplayName "removeuserfromgroups" -Permissions Manage
 
Connect-MgGraph -Scopes Application.Read.All, RoleManagement.ReadWrite.Directory, AppRoleAssignment.ReadWrite.All

$msiObjectId = 'fc**' # Your Azure Function's managed identity Object ID

	# Get Exchange Online service principal

	$exoSp = Get-MgServicePrincipal -Filter "appId eq '00000002-0000-0ff1-ce00-000000000000'"

	# Get appRoleId for Exchange.ManageAsApp

	$role = $exoSp.AppRoles | Where-Object { $_.Value -eq "Exchange.ManageAsApp" }

	$params = @{

	    principalId = $msiObjectId

	    resourceId  = $exoSp.Id

	    appRoleId   = $role.Id

	}

	New-MgServicePrincipalAppRoleAssignment -ServicePrincipalId $msiObjectId -BodyParameter $params
```

```
# Connect to Graph
	Connect-MgGraph -Scopes "Application.Read.All", "AppRoleAssignment.ReadWrite.All", "RoleManagement.ReadWrite.Directory"
	# Set your managed identity Object ID (Azure Function’s identity)
	$msiObjectId ='fc**'   	# Get Microsoft Graph Enterprise App object
	$graphSp = Get-MgServicePrincipal -Filter "appId eq '00000003-0000-0000-c000-000000000000'"
	# Define app role IDs you want to assign
	$appRolesToAssign = @(
	    "62a82d76-70ea-41e2-9197-370581804d09", # Group.ReadWrite.All
	    "7ab1d382-f21e-4acd-a863-ba3e13f7da61", # Directory.Read.All
	    "df021288-bdef-4463-88db-98f22de89214"  # User.Read.All
	)
	# Assign each role
	foreach ($roleId in $appRolesToAssign) {
	    $params = @{
	        principalId = $msiObjectId
	        resourceId  = $graphSp.Id
	        appRoleId   = $roleId
	    }
	    try {
	        New-MgServicePrincipalAppRoleAssignment -ServicePrincipalId $msiObjectId -BodyParameter $params
	        Write-Host "Assigned appRoleId $roleId successfully"
	    }
	    catch {
	        Write-Host "Error assigning appRoleId "
	    }
	}
```

And i grant the app Exchange Admin role, here are all the permissions:-

but i am getting this error :-

```
2025-06-12T01:09:02Z   [Information]   INFORMATION: Start to Connect to exchange
2025-06-12T01:09:03Z   [Information]   INFORMATION: 

----------------------------------------------------------------------------------------

This V3 EXO PowerShell module contains new REST API backed Exchange Online cmdlets which doesn't require WinRM for Client-Server communication. You can now run these cmdlets after turning off WinRM Basic Auth in your client machine thus making it more secure. 

Unlike the EXO* prefixed cmdlets, the cmdlets in this module support full functional parity with the RPS (V1) cmdlets.

V3 cmdlets in the downloaded module are resilient to transient failures, handling retries and throttling errors inherently. 

REST backed EOP and SCC cmdlets are also available in the V3 module. Similar to EXO, the cmdlets can be run without WinRM basic auth enabled. 

For more information check https://aka.ms/exov3-module

Starting with EXO V3.7, use the LoadCmdletHelp parameter alongside Connect-ExchangeOnline to access the Get-Help cmdlet, as it will not be loaded by default

----------------------------------------------------------------------------------------

2025-06-12T01:09:03Z   [Error]   EXCEPTION: The role assigned to application c4** isn't supported in this scenario. Please check online documentation for assigning correct Directory Roles to Azure AD Application for EXO App-Only Authentication.

Exception             : 

    Type       : System.SystemException

    TargetSite : 

        Name          : ProcessRecord

        DeclaringType : [Microsoft.Exchange.Management.ExoPowershellSnapin.NewEXOModule]          MemberType    : Method          Module        : Microsoft.Exchange.Management.ExoPowershellGalleryModule.dll      Message    : The role assigned to application c4** isn't supported in this scenario. Please check online documentation for assigning correct Directory Roles to Azure AD Application for EXO App-Only Authentication.

    Source     : Microsoft.Exchange.Management.ExoPowershellGalleryModule

    HResult    : -2146233087

    StackTrace : 

   at Microsoft.Exchange.Management.ExoPowershellSnapin.NewEXOModule.ProcessRecord()

   at System.Management.Automation.Cmdlet.DoProcessRecord()

   at System.Management.Automation.CommandProcessor.ProcessRecord()

CategoryInfo          : OperationStopped: (:) [], SystemException  FullyQualifiedErrorId : The role assigned to application c4** isn't supported in this scenario. Please check online documentation for assigning correct Directory Roles to Azure AD Application for EXO App-Only Authentication.

InvocationInfo        : 

    ScriptLineNumber : 758

    OffsetInLine     : 21

    HistoryId        : 1

    ScriptName       : C:\home\data\ManagedDependencies\2506112334311249599.r\ExchangeOnlineManagement\3.8.0\netCore\ExchangeOnlineManagement.psm1

    Line             : throw $_.Exception;

                       

    Statement        : throw $_.Exception

    PositionMessage  : At C:\home\data\ManagedDependencies\2506112334311249599.r\ExchangeOnlineManagement\3.8.0\netCore\ExchangeOnlineManagement.psm1:758 char:21

                       +                     throw $_.Exception;

                       +                     ~~~~~~~~~~~~~~~~~~

    PSScriptRoot     : C:\home\data\ManagedDependencies\2506112334311249599.r\ExchangeOnlineManagement\3.8.0\netCore

    PSCommandPath    : C:\home\data\ManagedDependencies\2506112334311249599.r\ExchangeOnlineManagement\3.8.0\netCore\ExchangeOnlineManagement.psm1

    CommandOrigin    : Internal

ScriptStackTrace      : at Connect-ExchangeOnline, C:\home\data\ManagedDependencies\2506112334311249599.r\ExchangeOnlineManagement\3.8.0\netCore\ExchangeOnlineManagement.psm1: line 758

                        at , C:\home\site\wwwroot\PowerShellRemoveUserFromGroups\run.ps1: line 35

2025-06-12T01:09:03Z   [Error]   Executed 'Functions.PowerShellRemoveUserFromGroups' (Failed, Id=c9bc0baa-44a1-4649-8c16-4b54e9003ac7, Duration=1691ms)
```

So what is causing this error? on the `Connect-ExchangeOnline -ManagedIdentity -Organization bi**.onmicrosoft.com`

## Answers

_No answers on this thread._
