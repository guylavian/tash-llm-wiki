---
title: "How to resolve Active Directory replication issue?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2185556/how-to-resolve-active-directory-replication-issue
question_id: 2185556
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# How to resolve Active Directory replication issue?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2185556/how-to-resolve-active-directory-replication-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, we have an environment of 30+ servers and all of a sudden all of them started giving Trust error. "The trust relationship between this workstation and the primary domain failed" Now I have found a temporary solution to rejoin the domain but it is not practical for 30+ servers. And then upon troubleshooting I found replications errors. After running "repadmin /replsummary" it is giving in the Source DSA PDC fails 1/5 with an error 8606, while SDC 0/5 and in the Destination DSA SDC fails 1/5 with an error 8606, while PDC 0/5. 

Now, SDC is also giving error in repadmin /showrepl SDC while PDC is ok.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-21*

Hello Masab Bin Nasir,  

Thank you for posting in Microsoft Community forum.

How many DCs did you have in your domain?  

For AD replication error 8606, you can refer to steps with possible solution in the similar thread. 

Prblems with DC Replication - Microsoft Q&A

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
