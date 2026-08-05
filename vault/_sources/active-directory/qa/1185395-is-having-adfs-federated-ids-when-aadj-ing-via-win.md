---
title: "Is having ADFS (federated IDs) when AADJ-ing via Windows Autopilot Supported?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1185395/is-having-adfs-federated-ids-when-aadj-ing-via-win
question_id: 1185395
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "microsoft-security-windows-autopilot"]
answer_author_roles: ["Q&A User"]
---
# Is having ADFS (federated IDs) when AADJ-ing via Windows Autopilot Supported?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1185395/is-having-adfs-federated-ids-when-aadj-ing-via-win (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, everyone.

I was wondering if there’s any information on whether using ADFS federated ID when doing Azure AD Join via Autopilot is supported or not. 

I've seen some MS Learn documents and they were clear on the things below, but I couldn't find an answer to my question which connects the dots.

-  Using a federated ID for AADJ / HAADJ is supported

-  Autopilot User Driven mode supports both AADJ / HAADJ scenario

-  in Autopilot HAADJ scenario, ADFS is supported

A company that I'm working with is planning to pilot-use Autopilot, but their domain is federated; we wanted to know if doing the staged roll out and making the federated IDs managed should come before tyring out Autopilot AADJ, or if we could keep the environment as it is and still try out.

Thank you for your support in advance. Any insight would be helpful.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-05*

Hi, 

You can continue testing Autopilot without problem, once  the domain is federated AADJ will use ADFS to authenticate the administrated users only.

If the users are 100% cloud-based you can use AADJ to continue with the test. The administrated users can use both AADJ and HAADJ.
