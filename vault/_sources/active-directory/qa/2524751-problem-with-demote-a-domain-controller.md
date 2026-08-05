---
title: "Problem with Demote a domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2524751/problem-with-demote-a-domain-controller
question_id: 2524751
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Problem with Demote a domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2524751/problem-with-demote-a-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear all,

I tried today to demote a DC, but my domain environment is still need this DC to work.

I have windows server 2003 Small Business DC as DC1 & lately I added windows server 2008 R2 DC as DC2 in new box as Additional domain. Now, I need to demote the windows server 2003 SB ( DC1) in old Box.

I transferred FSMO ( All 5 Roles) and delete DC1 from the AD. Also, remove it from AD users & computers and from AD Sites & Services and from DNS... I used the steps in this link: http://www.petri.co.il/delete_failed_dcs_from_ad.htm

When Dc1 is not connected to the network, I receive this error ( See this pic from this link http://i41.tinypic.com/30upoxj.png) whenever I opened any AD consoles ( AD users & computers,
 etc...).

Also, When I tried to change Domain Controller, it seems that it could not located the Domain or any DCs. Please, see this pic from this link: http://i43.tinypic.com/2n6afx1.png

I can solve it be reconnecting DC1 to the network, but I don't want to keep it any longer and I don't know what I am missing?. Moreover, I tried to use dcpromo in DC1 to delete the DC, but I receive an error that tells me this is not the last DC in the
 forest and cannot proceed deleting the DC.

Can you help me ASAP, I am stack here.

Waiting for  your reply.... Thank you!

## Answers

_No answers on this thread._
