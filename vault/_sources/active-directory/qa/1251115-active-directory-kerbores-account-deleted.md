---
title: "Active directory Kerbores account deleted"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1251115/active-directory-kerbores-account-deleted
question_id: 1251115
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active directory Kerbores account deleted

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1251115/active-directory-kerbores-account-deleted (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

One of my customer are deleted the Kerberos account from AD and post the my all location RODC replication stopped and user are not able to login systems. 
customer are restore that account form old backup post that issue has been resolved. 
But after 15 days having issue with file sharing not able view the list of user while sharing the folder. Also KDC service stopped we tried to start the service but failed.KDC.JPG

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-21*

Hi,
I'd be happy to help you out with your question. Sorry for the inconvenience caused.
Based on the information you have provided, I think that restoring the Kerberos account from an old backup has resolved the initial login issue, but you are now experiencing issues with file sharing and the KDC service. These issues may be related to a corrupted Kerberos database, which can happen if there are problems with replication or other issues with the Active Directory infrastructure.
To resolve this issue, we will need to perform some troubleshooting steps to identify the root cause. This may involve checking the event logs on the affected servers, using tools like Repadmin or DCDiag to verify replication, and possibly performing a database recovery or restore from a known good backup if necessary.
For more Information, please refer to following resources :-
KDC service on an RODC can't start and generates error 1450 - https://learn.microsoft.com/troubleshoot/windows-server/windows-security/kdc-service-on-rodc-cant-start-error-1450
If you have any other questions or need assistance with anything, please don't hesitate to let me know. I'm here to help.

If the reply was helpful, please don’t forget to upvote or accept as answer, thank you.
