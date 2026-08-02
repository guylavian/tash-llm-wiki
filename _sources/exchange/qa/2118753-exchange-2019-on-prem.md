---
title: "Exchange 2019 on prem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2118753/exchange-2019-on-prem
question_id: 2118753
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 on prem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2118753/exchange-2019-on-prem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

did somebody else experience mail flow rules "if mail to..." then "add recipient to..." fail (do not processed),  after yesterdays windows update???

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-15*

Hey,

finished the uninstall yesterday - took the server ~30 Minutes to do so but afterwards everything worked just fine.  

My colleague also tried to disable / enable rules and also noticed it started working again.  

But ultimately I think uninstalling the updates fixes it for the moment being.  

Updates I did uninstall:  

KB3175339  

KB5044062  

KB5046612

Will let my users test today and see if this is the temporary solution... in the end we need an permanent fix that includes all the updates anyway - Please Microsoft....

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-14*

Lucas FYI: 

check it out https://techcommunity.microsoft.com/blog/Exchange/released-november-2024-exchange-server-security-updates/4293125 

the same issue, some suggested schedule transport rules restart as temp fix

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-14*

Hi,

I would like to add to this.  

We got the exact same issues here after the update.  

There where an 2016 CU13 Update and 2024-11 Cumulative Update for Windows Server 2016 for x64-based Systems (KB5046612).  

Right now I am trying to delete the updates and test again - will let you know.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-14*

Hi, @Alexander Petrovski

Thank you for posting your question in the Microsoft Q&A forum.

According to your description, you encountered the problem that the mail flow rule does not work after the Windows update. In order to better find the cause of the problem, I would like to confirm with you whether the Windows update you mentioned is the latest Exchange Server security update or the Windows operating system update?

-  If it is a security update for Exchange Server, the problem of the mail flow rule stopping has occurred in a previous security update. You can try the previous solution to see if it can be solved:

-  Use the command to check whether all Exchange services are enabled and running.     `Get-Service | Where {$_.DisplayName -like "*Exchange*"} | Where {$_.DisplayName -notlike "*Hyper-V*"} | Format-Table DisplayName, Name, Status`

-  Confirm that the server is not in maintenance mode.

-  Confirm that there is enough free space in the Exchange mail queue database.

-  If it is an update of the Windows operating system, you can check yesterday's update log to see if there are any changes or errors related to Exchange Server.

Refer to: https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/exchange-security-update-issues#mail-flow-has-stopped

If you have any questions, please feel free to contact me. If the answer is helpful, please click "Accept Answer" because it can help other members of the Microsoft Q&A community who have encountered similar problems and are looking for solutions. Thank you.

Best,

Jeanne
