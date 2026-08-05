---
title: "[Migrated from MSDN Exchange Dev] Outlook 2016 - Exchange 2010 - Keeps prompting for password..."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/200093/migrated-from-msdn-exchange-dev-outlook-2016-excha
question_id: 200093
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] Outlook 2016 - Exchange 2010 - Keeps prompting for password...

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/200093/migrated-from-msdn-exchange-dev-outlook-2016-excha (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

[MSDN thread link] Outlook 2016 - Exchange 2010 - Keeps prompting for password...  

Hi, I've read similar scenarios, just looking for more opinions on mine...  

We have Exchange 2016 co-existing with 2010 as well as 365 mailboxes...  

my mailbox was on 2010 & recently, maybe caused by an update (couldn't confirm yet), Outlook 2016 been asking for password every few minutes... or on open...  mail is flowing & I believe only happens in Cached mode...  

I cleared all credentials and such, recreated profile and tried different machines... from the connection status window it seems like it happens when it tries to connect to "Public Folders" on the 2010 server.  

If I move the mailbox to 2016 DB, it resolves the issue... interestingly I moved it back to 2010 (Same DB) and it still works only this time in connection status I'm showing it still connecting via the 2016 server (but it works)  

again nothing changed on Exchange as far as I know, it happened to random users all connecting to the 2010 server...

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-16*

Hi,    

According to the information above, your issue seems to be related to the authentication method configured in outlook anywhere, try using the command below to get the   configuration of your environment:    

Get-OutlookAnywhere | fl identity,host, auth    

Please make sure the -IISAuthenticationMethods for 2010 set as Basic,NTLM    

Set-OutlookAnywhere -Identity "Exchange2010/Rpc (Default Web Site)" -ExternalHostname webmail.domain.com -ClientAuthenticationMethod NTLM -IISAuthenticationMethods Basic,NTLM    

Here is also an article introduces about the similar issue as yours: Microsoft Exchange 2016 and 2010 coexistence – Outook shows login promt    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
