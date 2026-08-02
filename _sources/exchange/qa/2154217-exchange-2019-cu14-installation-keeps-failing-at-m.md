---
title: "Exchange 2019 CU14 Installation keeps Failing at Mailbox role: client access service"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2154217/exchange-2019-cu14-installation-keeps-failing-at-m
question_id: 2154217
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 CU14 Installation keeps Failing at Mailbox role: client access service

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2154217/exchange-2019-cu14-installation-keeps-failing-at-m (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I'm fairly new to dealing with servers and the world of IT, so please excuse my ignorance if this turns out to be a simple error, although I have done my research.

Exchange server keeps failing at mailbox role:client access service, error photo attached below. Event ID is 4027 and source is MSExchange ADAccess.

I'm currently working on VMware Workstation with the exchange server set up on a different machine than my Domain controller, and I'm setting up exchange server on a separate user (not Administrator because I kept getting a lot of errors about forest level, and it's not detecting domain) that is part of the domain and member of (Enterprise, Schema and Domain Admins). I've also made sure forest level and domain are 2016. Also made sure to prepare the AD beforehand and passed prerequisites check. Firewall is off, remote desktop is on, and I downloaded the latest exchange server update 

As a last resort I used Setup assist, it keeps failing at finding mailbox role, and I'm not sure where to go from there. Only other case I saw similar to this was solved by uninstalling via command line.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-14*

Hi，@Maryam

It's good to hear from you and I have a preliminary understanding of your environment. Since a case corresponds to a question, I would like to check with you if your Exchange 2019 CU14 installation issue has been resolved?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-05*

Hi,@Maryam

Thanks for posting your question in the Microsoft Q&A forum.

Based on the screenshot you provided, you can see that Exchange is unable to connect to the Microsoft Exchange Active Directory topology service.

When the error occurs, please have a go by manually starting the "Microsoft Exchange Active Directory Topology service" and see if it could help.

Second method: the following blog shares a solution and in the comments section, a user mentioned that after adding the key MinSuitableServer = “1” as suggested in the blog to the Microsoft.Exchange.Directory. TopologyService.exe.config file and then error 4027 stopped (“I added that key and then 4027 and 2142 stopped and all exchange servers worked.”) :)

Exchange 2013 Setup Fails With Error "An exception ocurred while setting shared config DC"

So I would recommend have a look at the article and give it a try to see the result.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
