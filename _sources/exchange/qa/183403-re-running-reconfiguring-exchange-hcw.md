---
title: "Re-running/Reconfiguring Exchange HCW"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/183403/re-running-reconfiguring-exchange-hcw
question_id: 183403
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Re-running/Reconfiguring Exchange HCW

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/183403/re-running-reconfiguring-exchange-hcw (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our current setup can be described as below.  

-  We have 2 node Exchange Server 2013 CU15 already in Hybrid coexistence with O365 Exchange Online.  

-  The Exchange Hybrid Mail flow configured back then was Centralized.  

-  On premise Business application send mails to Exchange On premise those go to Internet via Onpremise Smarthost.  

-  MX points to O365.  

We now wish to change the mail flow, such that all outgoing mail will go out from O365 EOL.  

If we rerun/reconfigure the Hybrid Configuration Wizard, we wish to know the following.  

-  will we have to upgrade our Exchange 2013 CU 15 based servers to the latest CU before rerunning HCW?  

-  will we have to recreate a new [Token] TXT record in DNS to verify our domain ownership once again while running the HCW?  

-  will mails from onpremise applications also get routed via App--> ExHybrid-->O365 EOL-->Internet?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-06*

We got 4 mailbox server running Exchange 2013 CU23 in Exchange 2013 hybrid environment, two of these servers were designated as the "sendingtransportservers" in the HCW run before,  

We would like to add the other two mailbox servers to the "sendingtransportservers" in the hybrid environment, my question is:  

1): Do I have to re-run hcw to get this done or I can just use the Exchange cmdlet "set-hybridconfiguration" on Exchange 2013 on premise server to do it.  

and if I can just use cmdlet is there anything else I need to do besides running the "set-hybridconfiguration"?  

Thanks in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-03*

Hi @Anonymous   ,    

I agree with what Andy said.    

-  It’s recommend update your Exchange server to the last CU, because each CU is a full installation of Exchange that includes updates and changes from all previous CUs.    

-  According to the article provide by Microsoft, messages sent from on-premises recipients are always sent to directly to internet recipients using DNS, regardless of which of the methods (Centralized mail transport disabled or enable) you select in the Hybrid Configuration wizard. If the local mail flow is not as you expected, please following the steps in last link provide by Andy to create a connector on the on-premises to route the mail flow.    

For more information you could refer to: Outbound messages to the Internet    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
