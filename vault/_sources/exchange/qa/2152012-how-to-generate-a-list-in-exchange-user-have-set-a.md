---
title: "How to generate a list in exchange, user have set a rules in Auto Forwarding emails to Another Mailbox using powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2152012/how-to-generate-a-list-in-exchange-user-have-set-a
question_id: 2152012
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to generate a list in exchange, user have set a rules in Auto Forwarding emails to Another Mailbox using powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2152012/how-to-generate-a-list-in-exchange-user-have-set-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Please help me to generate a report via in a powershell, to view the list of mailbox name, Inbox rule, Forward to, Redirect to Forward as Attachment and rule status.  

Thank you

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2025-01-30*

You can run the below script after connecting to Exchange Online PowerShell.

```
Get-Mailbox -ResultSize unlimited | foreach { Get-InboxRule -Mailbox $_.DisplayName | select mailboxownerid,redirectTo,ForwardTo,ForwardAsAttachmentTo }
```

To connect to Exchange Online PowerShell, run the below cmdlet.  

`Connect-ExchangeOnline`

If you need to export the report to a CSV file, you can download the script from GitHub. Since some properties include values with additional formats, extra handling is required for proper CSV export.  

https://github.com/admindroid-community/powershell-scripts/blob/master/Office%20365%20Email%20Forwarding%20Report/EmailForwardingReport.ps1

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-31*

Hi @JYLVEN TARRAJA  ,

Here is a PowerShell script that you can use to generate a report of mailbox names, inbox rules, forwarding addresses, and rule status in Exchange Online:

```
# Connect to Exchange Online
$UserCredential = Get-Credential
Connect-ExchangeOnline -UserPrincipalName $UserCredential.UserName -Password $UserCredential.GetNetworkCredential().Password
# Get all mailboxes
$mailboxes = Get-Mailbox -ResultSize Unlimited
# Initialize an array to store report data
$report = @()
foreach ($mailbox in $mailboxes) {
# Get the inbox rules for each mailbox
$rules = Get-InboxRule -Mailbox $mailbox.PrimarySmtpAddress
foreach ($rule in $rules) {
# Create a custom object for each rule
$ruleDetails = [PSCustomObject]@{
MailboxName = $mailbox.DisplayName
RuleName = $rule.Name
ForwardTo = ($rule.ForwardTo | ForEach-Object { $_.PrimarySmtpAddress }) -join ", "
RedirectTo = ($rule.RedirectTo | ForEach-Object { $_.PrimarySmtpAddress }) -join ", "
ForwardAsAttachmentTo = ($rule.ForwardAsAttachmentTo | ForEach-Object { $_.PrimarySmtpAddress }) -join ", "
RuleStatus = $rule.Enabled
}
# Add rule details to report array
$report += $ruleDetails
}
}
# Export report to CSV file
$report | Export-Csv -Path "C:\InboxRulesReport.csv" -NoTypeInformation
# Disconnect from Exchange Online
Disconnect-ExchangeOnline -Confirm:$false
```

This script will:

-  Connect to Exchange Online.

-  Retrieve all mailboxes.

-  For each mailbox, get the Inbox rules and their details.

-  Create a custom object for each rule that contains the required information.

-  Export the report to a CSV file named InboxRulesReport.csv.

Make sure you run this script in a PowerShell session that has the necessary permissions and the Exchange Online module installed.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
