---
title: "Exchange Web Services (EWS)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2087912/exchange-web-services-ews
question_id: 2087912
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Exchange Web Services (EWS)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2087912/exchange-web-services-ews (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I am using an Exchange 2016 hybrid environment. All my users have been migrated from on-prem to online. I have a requirement to forward meeting invites from a shared mailbox to users, and my input file changes daily. I need to schedule this script via Task Scheduler.I have downloaded the EWS Managed API from this URL: https://github.com/OfficeDev/ews-managed-api. Additionally, I have created an app registration in Azure with the delegated Microsoft Graph API permission EWS.AccessAsUser.All.  Below script is not throwing any error but meeting invites are not getting forwarded.

```
New-ServicePrincipal -AppId "111111111111111" -ObjectId "ooooobbbbbbbbb" -DisplayName Test1
New-ManagementScope -Name "CRS" -RecipientRestrictionFilter "Department -eq 'somedept'"
New-ManagementRoleAssignment -App  "111111111111111" -Role " Application EWS.AccessAsApp" -CustomResourceScope "CRS"

=====================================================================

Start-Transcript -Path "c:\temp\transcript.txt"
$ApplicationId = "111111111111111"
$ApplicatoinSecret = "sseeccrreett"
$TenantId = "222222222222222222"

# Get an access token
$body = @{
    grant_type    = "client_credentials"
    client_id     = $ApplicationId
    client_secret = $ApplicatoinSecret
    scope         = "https://outlook.office365.com/.default"
}

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$response = Invoke-RestMethod -Uri "https://login.microsoftonline.com/$TenantId/oauth2/v2.0/token" -Method Post -ContentType "application/x-www-form-urlencoded" -Body $body
$accessToken = $response.access_token

# Load EWS Managed API (Exchange 2016)
$EWSServicePath = 'C:\Temp\EWS\bin\Debug\Microsoft.Exchange.WebServices.dll'
Import-Module $EWSServicePath

# Connect to Exchange Online using EWS with OAuth
$ExchVer = [Microsoft.Exchange.WebServices.Data.ExchangeVersion]::Exchange2016
$Service = New-Object Microsoft.Exchange.WebServices.Data.ExchangeService($ExchVer)
$Service.Url = "https://outlook.office365.com/EWS/Exchange.asmx"
$Service.Credentials = New-Object Microsoft.Exchange.WebServices.Data.OAuthCredentials($accessToken)
 
# Define mailboxes and other parameters
$StartOU = "contoso.com/OU1"
$MoveCSV = ".\userlist.csv"
$Users = Import-Csv '.\userlist.csv'
$MeetingMBX = '******@contoso.com'
$Items = 50

$DaysInTheFuture = 200
$Now = [System.DateTime]::Now
$Then = $Now.AddDays($DaysInTheFuture)

# Set up impersonation
$service.ImpersonatedUserId = New-Object Microsoft.Exchange.WebServices.Data.ImpersonatedUserId([Microsoft.Exchange.WebServices.Data.ConnectingIdType]::SMTPAddress, $MeetingMBX)

# Define calendar view
$folderid = New-Object Microsoft.Exchange.WebServices.Data.FolderId([Microsoft.Exchange.WebServices.Data.WellKnownFolderName]::Calendar, $MeetingMBX)
$calendarFolder = [Microsoft.Exchange.WebServices.Data.CalendarFolder]::Bind($service, $folderid)
$calendarView = New-Object Microsoft.Exchange.WebServices.Data.CalendarView($Now, $Then)
$calendarView.MaxItemsReturned = $Items
$calendarView.PropertySet = New-Object Microsoft.Exchange.WebServices.Data.PropertySet([Microsoft.Exchange.WebServices.Data.BasePropertySet]::FirstClassProperties)
$findItemResults = $calendarFolder.FindAppointments($calendarView)

if ($findItemResults.Items.Count -gt 0) {
    $FutureMeetings = @()
    foreach ($CalItem in $findItemResults.Items) {
        if ($CalItem.IsMeeting -eq $True) {
            $FutureMeetings += $CalItem
        }
    }

if ($FutureMeetings) {
        $emaillist = @()
        foreach ($user in $Users) {
            $EmpType = $null
            $EmpType = Get-QADUser $user.UserPrincipalName -properties employeeType | select employeeType
            if (($user.RecipientTypeDetails -eq 'UserMailbox') -and (($EmpType.employeeType -eq 'emp1') -or ($EmpType.employeeType -eq 'emp2'))) {
                $emaillist += $user.emailaddress
            }
        }

if ($emaillist.Count -gt 0) {
            foreach ($item in $FutureMeetings) {
                [void]$item.Forward("Meeting invite forwarded.", $emaillist)
                "Date: $Now" | Out-File ".\FWReport.csv" -Append
                "Addresses: $emaillist" | Out-File ".\FWReport..csv" -Append
                "Subject: $item.Subject" | Out-File ".\FWReport..csv" -Append
                "Start: $item.Start" | Out-File ".\FWReport..csv" -Append
                "End: $item.End" | Out-File ".\FWReport..csv" -Append
                "Location: $item.Location" | Out-File ".\FWReport..csv" -Append
                "--------------------------------------------------------------" | Out-File ".\FWReport..csv" -Append
            }
        }
    }
}

Stop-Transcript
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-10-09*

i am getting error at Get-ADUser -Filter

Select-Object : A positional parameter cannot be found that accepts argument 'False'.

```
Start-Transcript -Path "C:\temp\transcript.txt"
$ApplicationId = "111111111111111"
$ApplicatoinSecret = "sseeccrreett"
$TenantId = "222222222222222222"
# Get an access token
$body = @{
    grant_type    = "client_credentials"
    client_id     = $ApplicationId
    client_secret = $$ApplicatoinSecret
    scope         = "https://outlook.office365.com/.default"
}
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$response = Invoke-RestMethod -Uri "https://login.microsoftonline.com/$TenantId/oauth2/v2.0/token" -Method Post -ContentType "application/x-www-form-urlencoded" -Body $body
$accessToken = $response.access_token
# Load EWS Managed API (Exchange 2016)
$EWSServicePath = 'D:\EWS\bin\Debug\Microsoft.Exchange.WebServices.dll'
Import-Module $EWSServicePath
 
# Connect to Exchange Online using EWS with OAuth
$ExchVer = [Microsoft.Exchange.WebServices.Data.ExchangeVersion]::Exchange2016
$Service = New-Object Microsoft.Exchange.WebServices.Data.ExchangeService($ExchVer)
$Service.Url = "https://outlook.office365.com/EWS/Exchange.asmx"
$Service.Credentials = New-Object Microsoft.Exchange.WebServices.Data.OAuthCredentials($accessToken)
 
# Define mailboxes and other parameters
$StartOU = "contoso.com/OU1"
$MoveCSV = ".\userlist.csv"
$Users = Import-Csv '.\userlist.csv'
$MeetingMBX = '******@contoso.com'
$Items = 50
$DaysInTheFuture = 200
$Now = [System.DateTime]::Now
$Then = [System.DateTime]::Now.AddDays($DaysInTheFuture)
 
# Set up impersonation
$service.ImpersonatedUserId = New-Object Microsoft.Exchange.WebServices.Data.ImpersonatedUserId([Microsoft.Exchange.WebServices.Data.ConnectingIdType]::SMTPAddress, $MeetingMBX)
 
# Define calendar view
$folderid = New-Object Microsoft.Exchange.WebServices.Data.FolderId([Microsoft.Exchange.WebServices.Data.WellKnownFolderName]::Calendar, $MeetingMBX)
$calendarFolder = [Microsoft.Exchange.WebServices.Data.CalendarFolder]::Bind($service, $folderid)
$calendarView = New-Object Microsoft.Exchange.WebServices.Data.CalendarView($Now, $Then)
$calendarView.MaxItemsReturned = $Items
$calendarView.PropertySet = New-Object Microsoft.Exchange.WebServices.Data.PropertySet([Microsoft.Exchange.WebServices.Data.BasePropertySet]::FirstClassProperties)
$findItemResults = $calendarFolder.FindAppointments($calendarView)
 
if ($findItemResults.Items.Count -gt 0) {
    $FutureMeetings = @()
        foreach ($CalItem in $findItemResults.Items) {
        if ($CalItem.IsMeeting -eq $True) {
            $FutureMeetings += $CalItem
        }
    }
    if ($FutureMeetings.Count -gt 0) {
        $emaillist = @()
        #$upn = $user.UserPrincipalName
        foreach ($user in $Users) {
        $EmpType = $null
        $EmpType = Get-ADUser -Filter "UserPrincipalName -eq '$($user.UserPrincipalName)'" -Properties employeeType |
        Select-Object -ExpandProperty employeeType if (($user.RecipientTypeDetails -eq 'UserMailbox') -and (($EmpType -eq 'emp1') -or ($EmpType -eq 'emp2'))) { $emaillist += $user.emailaddress } }
          if ($emaillist.Count -gt 0) {
            foreach ($item in $FutureMeetings) {
                [void]$item.Forward("Meeting invite forwarded.", $emaillist)
                "Date: $Now" | Out-File ".\ForwardReport.csv" -Append
                "Addresses: $emaillist" | Out-File ".\FWReport.csv" -Append
                "Subject: $item.Subject" | Out-File ".\FWReport.csv" -Append
                "Start: $item.Start" | Out-File ".\FWReport.csv" -Append
                "End: $item.End" | Out-File ".\FWReport.csv" -Append
                "Location: $item.Location" | Out-File ".\FWReport.csv" -Append
                "--------------" | Out-File ".\FWReport.csv" -Append
            }
        }
    }
}
Stop-Transcript
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-10-06*

Any help would be appreciated
