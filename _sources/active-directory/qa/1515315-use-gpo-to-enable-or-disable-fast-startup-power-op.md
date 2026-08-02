---
title: "Use GPO to Enable or Disable \"Fast Startup\" power option in Windows Failed and not sync to users PC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1515315/use-gpo-to-enable-or-disable-fast-startup-power-op
question_id: 1515315
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Use GPO to Enable or Disable "Fast Startup" power option in Windows Failed and not sync to users PC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1515315/use-gpo-to-enable-or-disable-fast-startup-power-op (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all, 

An administrator applied this gpo (Enable or Disable "Fast Startup" Always On in Local Group Policy Editor Windows) but it failed to sync to the users PC. 

I am having trouble for fixing an gpo issue 

-  When I check the GPO in Active Directory Server the GPO is Enforced and Link Enabled as well yet the GPO is not sync to the users pc as you can refer below picture.

-  When I run dcdiag in CMD some kind of error I have notice in the CMD.

-  When I run repadmin /showrepl and also repadmin /replsummary everything looks fine with no error.       

-  When I check gpresults /r in the user PC seems like everything looks fine but somehow the gpo is fail to sync to the users PC.          

-  The below link is what is how they apply in the Active Directory Server.    https://www.youtube.com/watch?v=fZ7Q5mNAAYs   Could someone provide me a solution to fix this issue. 

-  Can provide me steps to fix DFSR Sysvol Replication issue!

-  Can provide me to fix this issue with GPO!

-  Please provide me any solution to fix this issue!

I hope to hear soon from anyone.

Thank you.

Best regards,

Jay

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-01-28*

Hi @Jnarthan Govindasamy  

Check event viewer you should get more details about the issue.
If the partner cannot be cpntected it should be network flows issue.
Try to check network flow with impacted domain controller.

Please don't forget to accept helpful answer
