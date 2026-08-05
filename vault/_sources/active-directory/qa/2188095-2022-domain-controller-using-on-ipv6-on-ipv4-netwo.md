---
title: "2022 Domain Controller using on IPv6 on IPv4 network.  Replication issues."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188095/2022-domain-controller-using-on-ipv6-on-ipv4-netwo
question_id: 2188095
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 11
qa_tags: []
---
# 2022 Domain Controller using on IPv6 on IPv4 network.  Replication issues.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188095/2022-domain-controller-using-on-ipv6-on-ipv4-netwo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have 3 2012R2 Domain controllers communicating via IPv4.  We recently added 2 2022 Domain Controllers and the are having replication issues with each other  as it appears they are trying to replicate via DNS lookups using the IPv6 AAAA host record which returns no host.

Replication:

2012R2 - 2022 Success

2022 -2022 Fail.

 I noticed that these two new 2022 Domain Controllers are the only two with IPv6 DNS entries as well as IPv4, and I am pretty sure this is where the issue is.  

Am I ok to delete the two IPv6 AAAA host records referencing the new 2022 DC's?  We are only using IPv4 on our network and no IPv6 address is assigned to any domain controller.

## Answer (community) — community member

*upvotes: 2 · updated: 2023-09-25*

Hello dzrtthunder,  

Thank you for posting in Microsoft Community forum.  

Usually, you can uncheck the IPv6 setting to see if it helps.  

  

If it does not work, you can try to delete the two IPv6 AAAA host records referencing the new 2022 DC's and check if it helps.  

Note: Please back up all DNS settings or Domain Controller system status (at least two 2022 DC) before you make any change in your AD domain.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
