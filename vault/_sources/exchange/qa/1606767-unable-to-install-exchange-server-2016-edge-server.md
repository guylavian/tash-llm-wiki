---
title: "Unable to install exchange server 2016 edge server role"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1606767/unable-to-install-exchange-server-2016-edge-server
question_id: 1606767
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Unable to install exchange server 2016 edge server role

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1606767/unable-to-install-exchange-server-2016-edge-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Error:

There was a problem accessing the registry on this computer. This may happen if the Remote Registry service isn't running. It may also indicate a network problem or that the TCP/IP Netbios Helper service isn't running.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-04*

@Srinivasa K  

According to your error message,  we recommend you check the following aspects to troubleshoot your issue:

-  The Remote Registry Server is not running. In this case, we recommend you try to restart the remote registry service.

-  Verify that the required ports are open in the firewall. SMTP: port 25/TCP; Secure LDAP: non-standard port 50636/TCP

-  Verify that the Mailbox servers and the Edge Transport server can locate one another using DNS name resolution.

If the above suggestion is not working, it recommends you go to the ExchangeSetup.log (C:\ExchangeSetupLogs) file to check if there are any specific errors for further analysis.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
