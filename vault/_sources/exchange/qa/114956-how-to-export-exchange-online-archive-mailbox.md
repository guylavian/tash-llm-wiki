---
title: "How to export Exchange Online archive mailbox?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/114956/how-to-export-exchange-online-archive-mailbox
question_id: 114956
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# How to export Exchange Online archive mailbox?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/114956/how-to-export-exchange-online-archive-mailbox (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a request to export the archive mailbox only of a user in Exchange Online.  

In Exchange on-prem I can use the New-MailboxExportRequest commandlet, but this commandlet is unavailable in EO.  

The only option that I can find is an eDiscovery search, but it doesn't have an archive-only search option.  

Therefore I must still use eDiscovery and play around with a criterion based on received date, estimating when archived emails were received.  

This approach will either result in data loss, or data duplication.  

Is there a targeted way to export the full content of the archive mailbox only?  

Thanks.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-04-12*

Hi.  

Using Windows Azure Active Directory Module for Windows PowerShell, you can use the following commands to move the online in-place archive to your local exchange server.  

To Connect to O365 Servers  

-  $LiveCred = Get-Credential  

(This account must be a onmicrosoft.com account)  

-  $Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://ps.outlook.com/powershell/ -Credential $LiveCred -Authentication Basic -AllowRedirection  

-  Import-PSSession $Session -allowclobber  

-  Connect-MsolService -Credential $LiveCred  

-  $opcred = get-credential  

This account needs to be normal AD account.  

New Move request:  

New-MoveRequest -Identity (Email address goes here) -Outbound -ArchiveOnly -RemoteArchiveTargetDatabase (Database name) -RemoteHostName "mail.example.co.za" -RemoteCredential $opcred -TargetDeliveryDomain "domain.co.za" -BadItemLimit 100  

After you move the archive to your local exchange will you be able to export it from your exchange server using:  

New-MailboxExportRequest -mailbox (Alias goes here e.g Joe.Blogs or JoeB) -filepath "\server\folder(Name.surname e.g Joe.Blogs)_archive.pst" -isarchive -Priority Highest

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 1 · updated: 2020-10-05*

@Zoltan Erszenyi       

What about exporting to pst files from Outlook? Except eDiscovery, you can export items manually from Outlook. For your reference: Export or backup email, contacts, and calendar to an Outlook .pst file. Otherwise, you may have to use the third-party tool to reach your requirement.    

Here are also some similar threads for more information:    

Export Online Archive from o365 to pst,    

How to Export Office 365 Mailboxes to PST- 3 Ultimate Solutions.    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-02*

You can export the entire content of the mailbox, the resulting PST will preserve the folder structure and will have a separate node for the Online archive, so you can just keep that. Alternatively, you can select the option to export to individual items, which again will give you the full folder structure and you can remove anything unneeded.
