---
title: "In the Group Policy of a domain controller, running the Group Policy Result Wizard, it prompts “You do not have permission to perform this action”."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2076103/in-the-group-policy-of-a-domain-controller-running
question_id: 2076103
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# In the Group Policy of a domain controller, running the Group Policy Result Wizard, it prompts “You do not have permission to perform this action”.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2076103/in-the-group-policy-of-a-domain-controller-running (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The issue has been resolved, but the problem could not be removed, sorry!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-25*

Hello,

 

Thank you for posting in Q&A forum.

To further troubleshoot this issue, please kindly try below steps:

1.Check if WMI service is running on the remote computer correctly which is used for Group Policy Result Wizard.

2.Ensure that the account in use is a member of the local Administrators group on the remote computer.

3.Disable the firewall temporarily and check if issue persists.

 

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

 

Best regards，

Jill Zhou

 

If the Answer is helpful, please click "Accept Answer" and upvote it.
