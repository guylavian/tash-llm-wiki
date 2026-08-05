---
title: "Exchange Web Services (EWS)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2085038/exchange-web-services-ews
question_id: 2085038
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Exchange Web Services (EWS)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2085038/exchange-web-services-ews (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

I have the script below that was working fine but recently stopped functioning. I am unsure if this is due to the deprecation of basic authentication or because Exchange Web Services (EWS) is no longer supported as it's a legacy client. The purpose of the script is to forward calendar invites to newly joined employees. Is there any other way to achieve this? Please guide me.(i am not using password  in plain text like the below, i have encrypted it. just for understanding i have put password)

```
Start-Transcript -Path "C:\temp\transcript.txt"
$OU = "contoso.com/OU1"
$CSV = ".\userlist.csv"
$Users = Import-Csv '.\userlist.csv'
$MBX = '******@contoso.com'
$Items = 50
$DaysInTheFuture = 300
$Now = [System.DateTime]::Now
$Then = [System.DateTime]::Now.AddDays($DaysInTheFuture)
$username = "******@contoso.com"
$password = "somepwd"
$TenantPass = $password | ConvertTo-SecureString -AsPlainText -Force
$EWSServicePath = 'C:\Program Files\Microsoft\Exchange\Web Services\2.2\Microsoft.Exchange.WebServices.dll'
Import-Module $EWSServicePath
$Service = New-Object Microsoft.Exchange.WebServices.Data.ExchangeService
$ExchVer = [Microsoft.Exchange.WebServices.Data.ExchangeVersion]::Exchange2010_SP1
$Service = New-Object Microsoft.Exchange.WebServices.Data.ExchangeService($exchver)
$Credentials = New-Object System.Net.NetworkCredential($username, $password)
$service.Credentials = $Credentials
 
#Setting up EWS URL
$EWSurl = "https://outlook.office365.com/EWS/Exchange.asmx"
$Service.URL = $EWSurl
$service.ImpersonatedUserId = New-Object Microsoft.Exchange.WebServices.Data.ImpersonatedUserId ([Microsoft.Exchange.WebServices.Data.ConnectingIdType]::SMTPAddress,$MBX);
 
$folderid = new-object Microsoft.Exchange.WebServices.Data.FolderId([Microsoft.Exchange.WebServices.Data.WellKnownFolderName]::Calendar,$MailboxToImpersonate)
$calendarFolder = [Microsoft.Exchange.WebServices.Data.CalendarFolder]::Bind($service,$folderid)
$calendarView = new-object Microsoft.Exchange.WebServices.Data.CalendarView($Now, $Then)
$calendarView.MaxItemsReturned = $Items;
$calendarView.PropertySet = new-object Microsoft.Exchange.WebServices.Data.PropertySet([Microsoft.Exchange.WebServices.Data.BasePropertySet]::FirstClassProperties)
$findItemResults = $calendarFolder.FindAppointments($calendarView)
if ($findItemResults) {
   $FutureMeetings = @()
   Foreach ($CalItem in $findItemResults) {
      If ($CalItem.IsMeeting -eq $True) {$FutureMeetings += $CalItem}
   }
   if ($FutureMeetings) {
        $emaillist = @()
      foreach ($user in $Users) {
         $EmpType = $null
         $EmpType = get-qaduser $user.UserPrincipalName -properties employeeType | select employeeType
            If (($user.RecipientTypeDetails -eq 'UserMailbox')) { $emaillist += $user.emailaddress }
         }
      if ($emaillist.count -gt 0) {
         foreach ($item in $FutureMeetings) {
            [void]$item.Forward("shared meeting invite with you.",$emaillist)
            ("Date: "+$Now) | out-file ".\fwreport.csv" -append
            ("Addresses: "+$emaillist) | out-file ".\fwreport.csv" -append
            ("Subject: "+$item.Subject) | out-file ".\fwreport.csv" -append
            ("Start: "+$item.Start) | out-file ".\fwreport.csv" -append
            ("End: "+$item.End) | out-file ".\fwreport.csv" -append
            ("Location: "+$item.Location) | out-file ".\fwreport.csv" -append
            ("--------------------------------------------------------------") | out-file ".\fwreport.csv" -append
         }
      }
   }
}
Stop-Transcript
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-10-01*

Added Graph tag
