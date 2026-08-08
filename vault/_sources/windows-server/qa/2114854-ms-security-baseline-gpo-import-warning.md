---
title: "MS Security Baseline GPO Import Warning"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2114854/ms-security-baseline-gpo-import-warning
question_id: 2114854
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-high-availability-virtualization-hyper-v", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# MS Security Baseline GPO Import Warning

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2114854/ms-security-baseline-gpo-import-warning (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am running a Hyper-V test environment here. All devices (Hyper-V host as well as the VM's) are running under Windows Server 2022 Standard (with German interface). There is an AD DC as a VM via which I would like to distribute the MS Security Baselines to other member servers. I have created a GPO CentralStore for the ADMX/ADML files on the DC and copied all server ADMX/ADML files and the MS Security Baseline ADMX/ADML files to it. According to the Group Policy Editor, the CentralStore is used.

When importing the MS SecBaseline GPOs into a new group policy object, I receive error messages at the end of the import that various security principals could not be resolved -> see screenshot (in german...). To me it looks like it is a language problem - do I need a german version of the Security Baselines? How can I fix this?

Thanks in advance + best regards,

Sebastian

## Answers

_No answers on this thread._
