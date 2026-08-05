---
title: "Exchange Enhanced Filtering for Connectors - Exclude EXO?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1390208/exchange-enhanced-filtering-for-connectors-exclude
question_id: 1390208
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Enhanced Filtering for Connectors - Exclude EXO?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1390208/exchange-enhanced-filtering-for-connectors-exclude (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!

I have following Mailflow MX=EXO--->3rdPartyAppliance(Zertificon Z1 for S/MIME--->EXO

My problem is the inbound traffic. It works as shown in the picture, but all incoming mails get a SPF fail. I added the 3rd Party Application under "Enhanced Filtering for Connectors" for the inbound connector. I can see that it works in the message header, but i still get a spf fail because the recieving spf is always exo itself :-( Of course I cannot add the exo-ip since it changes every time. A problem-solver would be the option to exclude the last two ips instead of one, but I'm afraid there is no such option.

Any ideas?

Thank you!

Chris

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-10-13*

Hi @Christopher Stainczyk  ,

I can see that it works in the message header, but i still get a spf fail because the recieving spf is always exo itself 

Do you mean the IP address of the original external sender is not preserved even after you enable the Enhanced Filtering for Connectors? If this is the case, it's recommended to double confirm that all of the trusted IP addresses that are associated with the third-party product that send email into your tenant, including any intermediate hops with public IP addresses have been included. For more information, you can refer to: Configure Enhanced Filtering for Connectors.  

You can also consider following the document below and pointing the MX record to the 3rd party service instead and see if the mail flow can work as expected:

Manage mail flow using a third-party cloud service with Exchange Online

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
