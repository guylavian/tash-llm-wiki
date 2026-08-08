---
title: "OWA webmail not redirect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/337731/owa-webmail-not-redirect
question_id: 337731
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# OWA webmail not redirect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/337731/owa-webmail-not-redirect (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,    

Today the electricity in the company has been broken, and when electricity it returns again, I can login to ECP and create, remove, edit, etc... . But can't login to owa after put credential "user\pass" redirect to:    

    

Also I check all services is running and IIS running, and make     

01- IISReset     

02- Restart-WebAppPool MSExchangeOWAAppPool    

03- Restart-WebAppPool MSExchangeECPAppPool    

But nothing :(     

    

In the end, I tried install CU 19 again but the next button not active    

    

===============================    

NB: Exchange server 2016 CU 19, On-prem

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-31*

@AHMAD HASSAN      

First, it is an expected behavior that you cannot click the "Next"(Because you have installed all server roles, there doesn't exist other server role to be installed):    

    

After installing security update for Exchange 2016 CU 19, some user may get ECP/OWA 500 error. (The detailed error message is different from yours). You can try to reinstall this security update with administrator permission.    

If this issue still exist, you can try to install Exchange 2016 CU 20 directly: Cumulative Update 20 for Exchange Server 2016 (KB4602569)    

After that, it this issue doesn't gone, I would suggest you try to recreate OWA virtual directory.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
