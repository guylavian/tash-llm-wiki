---
title: "Exchange recovery of all servers - 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1108729/exchange-recovery-of-all-servers-2016
question_id: 1108729
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange recovery of all servers - 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1108729/exchange-recovery-of-all-servers-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear experts,    

Trying to write an instruction for how to perform a complete disaster recovery of all our (4 in one DAG) Exchange 2016 servers in the same organisation. Let us say they all have had complete software failure at the same time and needs to be completely reinstalled.    

As I understand I need to follow https://learn.microsoft.com/en-us/exchange/high-availability/disaster-recovery/recover-exchange-servers?view=exchserver-2019 and then set up the DAG again before restoreing mailbox databases. Is this correct?    

Thanks for input and assistance.    

Regards,    

Mrtro

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-07*

Hi @mrtro-1199  ,    

Yes.    

If you do not have the installation media for the Cumulative Update (CU) version that was installed on the server to be recovered, you can recover a server using the latest available Cumulative Update.     

You could refer to the detailed information of the following articles:    

recover-exchange-dag-member-server    

 Please Note: Since these web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-06*

Thanks again for your input. So if I understand this correctly, the procedure for recovery from scratch (but with a recovered AD) would be:    

-  Install OS and latest updates on each of the four servers.     

-  Run setup .exe /Mode:RecoverServer on each of the four servers.    

-  Run commands listed above.    

Am I on the right track?    

Regards,    

Mrtro

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-30*

Thanks for your answer AndyDavid    

I'm not sure how I could run those commands if I first have an Exchange server, see 1-3 powershell commands.     

Would I not have to start with the first server (after OS installation) and run setup.exe /Mode:RecoverServer to get a Exchange server up and running?    

Regards,    

Mrtro

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-11-29*

You prob would want to follow this instead and recover each server one at a time and re-add to the DAG.    

https://learn.microsoft.com/en-us/exchange/high-availability/disaster-recovery/recover-dag-member-servers?view=exchserver-2019
