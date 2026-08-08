---
title: "Active Directory Repl summery error \"(2148074306) The encryption type requested is not supported by the KDC\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/396732/active-directory-repl-summery-error-2148074306-the
question_id: 396732
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Repl summery error "(2148074306) The encryption type requested is not supported by the KDC"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/396732/active-directory-repl-summery-error-2148074306-the (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Active Directory Repl summery error "(2148074306) The encryption type requested is not supported by the KDC" I have restarted KDC service on source/destination DC but issue remain same. Please help me with with the solution

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-17*

Hi,  

To narrow down the issue, please help confirm the following information.  

How many DCs do you have in your environment?  

Did you restart the KDC service on all the DCs?  

What's the version for all your DCs?  

Did you upgrade the DCs with the latest patches?  

Any other errors on the DCs? Such as the event logs and dcdiag log?  

Best Regards,
