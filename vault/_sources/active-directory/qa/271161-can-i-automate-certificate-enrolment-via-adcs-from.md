---
title: "Can I automate certificate enrolment via ADCS from DMZ devices"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/271161/can-i-automate-certificate-enrolment-via-adcs-from
question_id: 271161
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
---
# Can I automate certificate enrolment via ADCS from DMZ devices

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/271161/can-i-automate-certificate-enrolment-via-adcs-from (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an infrastructure which builds servers and deploys them in a DMZ. We then need to make these servers automatically enroll for their first certificate from our ADCS PKI.   

We have investigated setting up a CEP/CES server in the domain, but it appears this methods requires each initial enrollment request to be manually approved/Issued by a PKI admin. This will of course break our automated certificate enrollment requirement.  

Is it possible to configure fully certificate enrollment to ADCS for devices outside the domain in a DMZ ?  

Any advice or pointers would be greatly appreciated

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-22*

Yes, if you have a trust between the DMZ forest and your internal forest.  Otherwise there's no way for the devices to automatically authenticate.
