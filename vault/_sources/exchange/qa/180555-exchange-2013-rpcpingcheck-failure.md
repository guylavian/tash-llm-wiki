---
title: "Exchange 2013 RPCPingCheck Failure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/180555/exchange-2013-rpcpingcheck-failure
question_id: 180555
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2013 RPCPingCheck Failure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/180555/exchange-2013-rpcpingcheck-failure (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have two Exchange servers running on Server 2012 R2 in a DAG configuration. When I run the Test-MRSHealth cmdlet the RPCPingCheck fails. The error message states "The Endpoint for the Microsoft Exchange Mailbox Replication service couldn't respond: The call to 'net.tcp//<my server name>/Microsoft.Exchange.MailboxReplicationService' failed. Error details: Access is denied."  

This seems like it would be a permssions issue but I don't think it is, my account is an Exchange admin and also a member of Organization Management. I found a couple of things on other Microsoft technet articles that basically just said to either restart the service and/or server. Obviously I've done this be to no avail. The only thing that I can see that changed were a couple of Windows server patches were installed last night. Any suggestions?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-01*

That's the thing, I don't know if Test-MRSHealth used to work because I never had a reason to run it. I'm only running it now because I can't export a mailbox to a PST file.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-01*

@Mike Contumelio       

Hi,    

Can you find some related events generated in the application log and system log after you run the "Test-MRSHealth" cmdlet?    

And please run the Test-ServiceHealth cmdlet to check if the required services are running on the server.    

If the Test-MRSHealth used to work fine and the problem just occurs after installing the windows server patches,please uninstall the patches and see if the problem persists.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
