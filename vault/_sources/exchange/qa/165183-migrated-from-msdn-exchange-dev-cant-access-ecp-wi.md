---
title: "[Migrated from MSDN Exchange Dev] Cant access ecp with FormsAuthentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/165183/migrated-from-msdn-exchange-dev-cant-access-ecp-wi
question_id: 165183
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] Cant access ecp with FormsAuthentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/165183/migrated-from-msdn-exchange-dev-cant-access-ecp-wi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

[MSDN thread link] Cant access ecp with FormsAuthentication  

i have a Exchange 2016 Server only for administration because all my Mailboxes are in Exchange Online.  

The Exchange 2016 exist for like 6 Months.  

Today i got the problem that i cannnot access the ecp of my Exchange 2016.  

I search already a lot in internet but i can not find a solution for me.  

If i try to access the ecp i get first the Login page. After i put my username and password in, i get Error 500.  

If i use WindowsAuthentication instead of FormsAuthentication it works.  

I already recreate the OWA and ECP VirtualDirectory:  

https://theitbros.com/recreate-owa-ecp-virtual-directories-exchange-server-2016/  

Have anyone an idea?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-17*

Hi,    

thank you for repy.    

I can not see any error in the application log after the login in ecp.    

Both links i already found and try the solitions but it dident work.    

Here are the Configs:

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-17*

Hi,    

What's the CU version of your Exchange 2016 server? If you are not in the latest CU version, you could try uptating it then access OWA and ECP again.    

Please provide the complete error information or the screenshot of your issue here.    

Use the command below to check if Authentication Settings for both Virtual Directories ECP and OWA are identical    

```
Get-EcpVirtualDirectory | fl identity, *url*, *auth*  
Get-OwaVirtualDirectory | fl identity, *url*, *auth*
```

We could also check the application log to get any related error information when we failed login OWA or ECP.    

The thread below discusses about the similar issue as yours:     

Exchange 2016 - Cannot Access OWA or ECP using Forms Authentication?    

And I also found a KB here, which introduces the configuration like yours.    

Cannot access Outlook on the Web or the EAC after you re-create the "owa" or "ECP" virtual directory on an Exchange Server Mailbox server    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
