---
title: "Error Updating On-Prem Hybrid Exchange 2016: no mailbox role detected"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/321474/error-updating-on-prem-hybrid-exchange-2016-no-mai
question_id: 321474
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# Error Updating On-Prem Hybrid Exchange 2016: no mailbox role detected

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/321474/error-updating-on-prem-hybrid-exchange-2016-no-mai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hoping for some help with this.  

When we’re trying to upgrade our hybrid on-prem exchange server; the pre-req’s fail saying no mailbox role on the on-premise server. It also has loads of other errors saying the user isn’t a member of the exchange organization management group…but the user is definitely in that group. As well as schema admins too.  

I’m running as administrator too.   

Very confused.   

Anyone else had this issue?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-29*

@Stephen Clark      

Here are information about: A Restart from a Previous Installation is Pending    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-28*

I have found that out of date VC runtimes and general Exchange health issues can cause this.  Google dpaulson45 healthchecker.ps1, I have found this script or the tasks it performs essential during upgrades.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-27*

Still stuck after 2 hours:  

When trying to run /PrepareAD on the domain controller it just keeps saying the server is pending a reboot following a windows server role or feature. There's nothing pending so I have no idea what is going on.   

I give up. I'll just leave it on CU15 forever.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-27*

Came across this in the logs.   

[03/26/2021 18:49:13.0448] [0] [ERROR] Setup encountered a problem while validating the state of Active Directory: Exchange organization-level objects have not been created, and setup cannot create them because the local computer is not in the same domain and site as the schema master.  Run setup with the /prepareAD parameter on a computer in the domain *** and site **************, and wait for replication to complete.  

Trying this now...

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-19*

@Stephen Clark      

Take steps below to narrow down this issue:    

-  Double check on the account that you used to update Exchange contained in those group below:    

    

-  Make sure that you login Exchange computer with domain account "YourDomain/adminAccount"    

-  Try to run Prepare command before installing Exchange server:        E:\Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareSchema  

    E:\Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAD  

    E:\Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareDomain  

After that, try to update Exchange server again, if you still cannot update Exchange server, could you provide detail information about this error?    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
