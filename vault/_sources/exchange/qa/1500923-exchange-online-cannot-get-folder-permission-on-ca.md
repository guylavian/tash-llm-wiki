---
title: "Exchange Online: cannot get folder permission on calendar folder only"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1500923/exchange-online-cannot-get-folder-permission-on-ca
question_id: 1500923
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 2
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Online: cannot get folder permission on calendar folder only

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1500923/exchange-online-cannot-get-folder-permission-on-ca (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, i have some issue with getting permission on calendar folder. Powershell returns this error with cannot convert to exchange version.
That resource is migrated to exchange online 2y ago and we didnt have some issue with permission settings in a past.  Add or remove work fine. Only get doesn´t work :-( 
It's weird then i can list inbox folder permission on same mailbox fine. 
Updating of exchangemanagement module doest help. Currently I am runnin on 3.4.0
Thanks for tips and advice... 
Get-EOMailboxFolderPermission "mailbox:\calendar"
Write-ErrorMessage : Cannot convert  to ExchangeVersion.
At C:\Users\profile\AppData\Local\Temp\tmpEXO_35i1xkyl.zpc\tmpEXO_35i1xkyl.zpc.psm1:1192 char:13
+             Write-ErrorMessage $ErrorObject
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Get-MailboxFolderPermission], Exception
    + FullyQualifiedErrorId : [Server=AS2PR05MB9773,RequestId=5c2b2397-bf77-ffeb-9477-5f4f00851a4f,TimeStamp=Thu, 18 Jan 2024 09:25:27 GMT],Write-ErrorMessage

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2024-01-22*

I found out that using Get-EXOMailboxFolderPermission instead of Get-MailboxFolderPermission works in my case. I am getting the above error on quite a few mailboxes now.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2024-01-23*

This seems to be a New issue with the Get-MailboxFolderPermission.   

Write-ErrorMessage : Cannot convert ExchangeVersion.  

however running the Get-EXOMailboxFolderPermission seems to work  

Get-EXOMailboxFolderPermission -Identity ******@contoso.com:\Calender | FL  

https://learn.microsoft.com/en-us/powershell/module/exchange/get-exomailboxfolderpermission?view=exchange-ps

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-01*

anyone facing similar  issue with Remove-MailboxFolderPermission -

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-01-26*

Hi, I had an open ticket to MS support and now I have information that the engineers have made changes on their side and it is now working fine. You can try it again. 
Thanks D

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-19*

Hello @Daniel Hnyk  

Recently, some people have indeed reported the same problem. However, Microsoft has not yet provided relevant official documents to explain it. It is recommended that you check service health yourself first to see if there are any related issues reported.

I have done some research and found that someone in this forum post provided a solution that you may could try:

Solution: gave his admin account temp full access permissions to the mailbox and then used the open another mailbox option in outlook.office.com and once that was done he could get the list and then remove his access and its working for all admins now.(Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in [our documentation] to enable e-mail notifications if you want to receive the related email notification for this thread.
