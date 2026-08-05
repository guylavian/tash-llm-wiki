---
title: "exchange server 2012 update does not work"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/299042/exchange-server-2012-update-does-not-work
question_id: 299042
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# exchange server 2012 update does not work

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/299042/exchange-server-2012-update-does-not-work (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Greetings from Red Cross Germany!  

We have an exchange server 2013 with a connection to Microsoft 365 running locally on our network. We use Windows Server 2012 R2.  

This exchange server should now receive the cumulative update CU23. Unfortunately, the update process did not go through properly and the Exchange server services are no longer available locally.  

The installation ended with error 80040667  

Already googled possible workarounds unfortunately did not provide a solution.  

Error Logs: https://pastebin.com/raw/mghQ18zz   

https://pastebin.com/JdVBhutM  

https://i.stack.imgur.com/P0VtN.png (the update)  

https://i.stack.imgur.com/B2thA.png (Screenshot Error)

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-05*

Hi @Graham Miranda DRK  ,    

In addition to the links shared by Troy, as regards to the error code 80070643 in the last screenshot and the second log file which is related to the ServiceControl.ps1, I found the following links that hopefully can be helpful:    

Exchange 2019 CU2 KB4509408 - Error 0x80070643    

Exchange Server Security Update KB4540123 fails with 0x80070643    

Please Note: Since the second web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

You may make a backup of the ServiceContol.ps1, then modify it with reference to the links above and see if it works.    

Beside, the first error log file shows an error with the database "ITDBM1-21012019" cannot be mounted. As per this error, you can try renaming its database folder and then retry the update.     

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
