---
title: "Exchange on-prem Hybrid Issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/147635/exchange-on-prem-hybrid-issues
question_id: 147635
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Exchange on-prem Hybrid Issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/147635/exchange-on-prem-hybrid-issues (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey All,  

So i have setup a brand new Exchange 2019 Standard On-Prem and O365 Hybrid setup. Currently we are 100% O365 mailboxes this on-prem will not host any mailboxes it will just be used for Admin purposes of Schema, Powershell ect...   

My issue is I cannot see any Office365 mailboxes in EAC. I can create new O365 mailboxes from EAC.   

The setup was just a mailbox and management install. Hybrid is minimal setup.  

Thanks,  

Ben

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-05*

Hi,  

Just to check if there are any updates. If the above suggestion helps, please click on "Accept Answer" and upvote it. Thanks for understanding.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-03*

@Anonymous  

Currently we are 100% O365 mailboxes this on-prem will not host any mailboxes

Are those mailboxes created on Exchange online? If so, it will be an expected behavior that cannot see those Office 365 mailboxes from Exchange on-premises EAC.

For Exchange on-premises EAC, you can only see mailboxes which AD account hosted on local AD. Such as:  

-  Exchange on-premises mailbox created in Exchange on-premises, then migrated to Exchange online later.  

-  Office 365 type mailbox which created from Exchange on-premises EAC.  

Those two kind mailboxes‘ AD account are all hosted on local AD and sync with AAD.

So, if you want to from Exchange on-premises manage Office 365 mailboxes which created on Exchange online, you need to create local AD account for those mailbox, then match local AD account with AAD account.  

For more detailed information, you can have a look about this article: https://www.codetwo.com/admins-blog/how-to-merge-an-office-365-account-with-an-on-premises-ad-account-after-hybrid-configuration/#no-local-account

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-02*

Hi,    

Please find below my suggestions,    

-  Are you getting any error messages while accessing the EAC in on-premise exchange - Kindly check if required permissions are in place for the administrator    

-  How are those mailboxes created which aren't showing in EAC? If its directly created in Office 365, then it might be missing the msExch attributes on the Active directory and not showing in EAC    

-  Is your Active directory is syncing with Azure AD    

References:    

https://learn.microsoft.com/en-us/exchange/permissions    

https://www.azure365pro.com/office-365-mailbox-not-showing-in-hybrid-exchange-server/    

If the above suggestion helps, please click on "Accept Answer" and upvote it.
