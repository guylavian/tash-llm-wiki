---
title: "laps deploying through GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/452929/laps-deploying-through-gpo
question_id: 452929
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# laps deploying through GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/452929/laps-deploying-through-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

Deploying LAPS into a large(ish) environment where availability is fairly tightly controlled. From all the guides I've seen it looks as though all the target systems need to be restarted (with possible gpupdate /force) for LAPS to become effective. This also seems to be the case from my basic testing using a GPO deployment.   

Is there anyway I can deploy the LAPS client via GPO without the target systems requiring a reboot?  

Regards

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-28*

Hi,  

Based on my research, we can deploy the LAPS client via a variety of methods including the Software Installation feature of Group Policy, SCCM, login script, manual install, etc.   

How about install the LAPS client via the login script.  

Best Regards,
