---
title: "IMAP issue after adding Exchange 2019 server to infrastructure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1399419/imap-issue-after-adding-exchange-2019-server-to-in
question_id: 1399419
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# IMAP issue after adding Exchange 2019 server to infrastructure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1399419/imap-issue-after-adding-exchange-2019-server-to-in (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello.   

After adding a test Exchange 2019 server to a system with 2 Exchange 2013 servers (CAS and MB), a problem arose with clients connecting to their mailboxes on the old (2013) MB server via IMAP. If the client's MB is on the new Ex2019 server, everything is OK, if the mailbox is on the old MB server, the client does not connect to it via IMAP. The IMAP configs (Get-ImapSettings -server ... | format-list) of the old CAS 2013 and the new CAS 2019 are identical. Services (IMAP4 and IMAP Backend) are running, all components are active. Test-ImapConnectivity -ClientAccessServer Ex2019 -MailboxCredential (Get-Credential) - passes successfully (if run on new Ex2019) and connects to mailboxes located on both the old and new MB. If, when running a test on a new Ex2019, I specify the old CAS, I get an error that it is not a client access server (perhaps this is how it should be). When I run this test on the old CAS, specifying the old or new CAS, I get the error in all options: FAILURE, Unable to create Mailbox.   

I currently still have the old CAS registered in Autodiscover.   

Is it possible to somehow fix IMAP access through the old CAS without changing it to a new CAS in autodiscover?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-10-23*

Hi @Alex Kyslov  ，

The IMAP configs (Get-ImapSettings -server ... | format-list) of the old CAS 2013 and the new CAS 2019 are identical. 

According to the explanation in this blog (It's talking about the client connectivity in the Exchange 2016 coexistence with Exchange 2010, but based on my knowledge, this part about POP and IMAP can be applied to Exchange 2019 coexistence with Exchange 2013 as well.), in coexistence scenario, IMAP and POP clients would be proxied from the newer version of Exchange Client Access component to a target server.   

Since in your case, the target mailbox is the old CAS 2013, you'll need to ensure that the `InternalConnectionSettings` maps to the target server's FQDN.

So, I'd recommend trying to configure the `InternalConnectionSettings` value as aforemention using the Set-ImapSettings cmdlet and then check the result.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
