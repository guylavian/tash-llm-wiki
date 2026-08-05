---
title: "Exchange 2013 certificates expired"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1641333/exchange-2013-certificates-expired
question_id: 1641333
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2013 certificates expired

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1641333/exchange-2013-certificates-expired (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've got an old Exchange 2013 box which is running hybrid for our on-prem AD. Several of it's built-in certs are expired.

The one highlighted is from our local CA, I have another test box and this is just called "Microsoft Exchange" and it's a self-signed cert. I'm not sure why this one is from our CA, why would it be? can I convert it back to self-signed?

The other ones, there are multiple copies of, the Exchange Delegation one, the new cert has no roles.

the MS Exchange Server Auth one, I tried to delete the duplicate and it gives error about RPC in use by Transport service

Should I just run the HCW again?

Any advice on how to repair these certs appreciated.  I can't even upgrade the box as it is now as the upgrade will fail while the certs are all borked.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-04-03*

Hi @ Bob Pants 

You mentioned you have an old Exchange 2013 server, did you have any other on-premises Exchange server, such as Exchange 2019? Or do you want to upgrade Exchange 2013 to Exchange 2016 or 2019?

The other ones, there are multiple copies of, the Exchange Delegation one, the new cert has no roles.

I am not sure what is you meaning of it. Could you please describe more details to us?

Based on my research, the "Microsoft Exchange" certificate itself is an self-signed certificate. So you don’t need to convert it to back. When you install Exchange 2016 or Exchange 2019 on a server, two self-signed certificates are created and installed by Exchange. In this official document, it describes two self-signed certificates:

Digital certificates and encryption in Exchange Server | Microsoft Learn

the MS Exchange Server Auth one, I tried to delete the duplicate and it gives error about RPC in use by Transport service

This is also the self-signed certificate and still have the service running and we don't recommend you delete it. If this certificate has been expired, we suggest you renew it.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
