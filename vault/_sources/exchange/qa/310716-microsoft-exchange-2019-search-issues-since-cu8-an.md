---
title: "Microsoft Exchange 2019 search issues since CU8 and HAFNIUM patches"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/310716/microsoft-exchange-2019-search-issues-since-cu8-an
question_id: 310716
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Microsoft Exchange 2019 search issues since CU8 and HAFNIUM patches

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/310716/microsoft-exchange-2019-search-issues-since-cu8-an (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have on-premises  Exchange 2019 which was at CU6.  When then HAFNIUM news broke I immediately updated to CU 8 and then installed the HAFNIUM patches overnight.  The upgrade appeared to go well and after a bit of fiddling with IIS to get OWA and Exchange Admin working again all appeared normal.  

Since then though users have been reporting that Outlook 2019 searches on their desktop PCs are NOT returning all results, specifically nothing after the date of the patch (3rd March 2021).  Also when you sign in remotely using OWA the same thing is happening.  No recent emails are returned by a search.  

I have an email from a colleague dated yesterday with the subject line being about their birthday.  If I put 'birthday' as the search term nothing is returned when restricting the search to 'within the last week' on OWA, yet I can clearly see & open the email in the Inbox view.  If I don't restrict the date only old emails from January this year and earlier are returned.  

The same happens in Outlook 2019, the first search result returned is the same as the one in OWA from January.  

If you use the Advanced Search function then the email from yesterday IS found!!  

If you use Apple Mail on an iPhone linked to the Exchange server then the email is found during a search.  

I've rebuilt the Windows Search index on Windows 10 (all the desktop PCs are on Windows 10) and this hasn't worked, even though it took hours to re-index Outlook.  Checking the Indexing Status in Outlook 2019 shows zero items still to be indexed.  

I've tried turning off cached Exchange Mode and turning it back on again.  It was the same with the cache on as well as off.  

My last ditch try is turning the cache off, deleting the OST file, then turning it back on.  This will force Outlook 2019 to re-download all the email from the server.  I presume the local Windows Search only indexes the OST file so if that's corrupt it will miss items out.  I'm not hopeful that this will work as the search doesn't work in OWA and that has NOTHING to do with desktop Outlook and it's local OST cache file.  

Anyone else got any other ideas?    

Would a repair of the Exchange database work?  How dangerous is that?  Is it worth trying Isinteg ?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-01*

I am facing the same problem in a 2013/2019 hybrid environment and I am sort of at a loss... How is it possible that MS pivoted search to Bing/mailbox index and now you only have one opportunity to index a mailbox - if for some reason that doesn't work, you are out of luck and have to move the mailbox???    

This is beyond ridiculous. Why is Bing not persistently crawling mailboxes as part of db maintenance?     

It makes no sense to me. I am supposed to move 1000 mailboxes to a temp db? We will need to hire someone specifically for that job.    

What is MS going to do about this? This is not a small problem...

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-13*

For me, the box migration solution was not applicable, so I found another way.    

Start EMS from Admin    

Add-PSSnapin Microsoft.Exchange.Management.PowerShell.SnapIn    

Start-MailboxAssistant -Identity admin@Company portal   .com -AssistantName BigFunnelRetryFeederTimeBasedAssistant    

Or a loop for OU. But reindexing is slow. 4TB of boxes re-indexed 2 weeks    

$name = Get-Mailbox -OrganizationalUnit Users    

foreach ($names in $name)    

{    

Start-MailboxAssistant -Identity $names -AssistantName BigFunnelRetryFeederTimeBasedAssistant    

}    

Tracking reindexing    

Get-Mailbox -ResultSize Unlimited | Get-MailboxStatistics | ? {$_.BigfunnelNotIndexedCount -ge "1"} | Start-MailboxAssistant -AssistantName BigFunnelRetryFeederTimeBasedAssistant

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-15*

Hi @Phil Tyler  ,    

Is there any relevant event logs recorded in the Event Viewer on the server?    

Please have a check and make sure the services below are running properly on the Exchange 2019 CU8 servers and the startup type is "automatic":    

-  Microsoft Exchange Search Host Controller Service    

-  Microsoft Exchange Search     

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
