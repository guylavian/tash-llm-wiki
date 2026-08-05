---
title: "Sysvol replication not working properly"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1179143/sysvol-replication-not-working-properly
question_id: 1179143
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
---
# Sysvol replication not working properly

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1179143/sysvol-replication-not-working-properly (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we seem to have an issue with replication of the sysvol folder between 2 DCs in AWS  to each other and on prem.

odd thing is if i create a GPO or script in AWS Server it replicates down to on prem fine but not back up

PDC on prem. DC1 

ADDC-01 from DC-02 and From ADDC-02

ADDC-02 from ADDC-01

DC2 from ADDC-01 and From DC1

DC1 from DC2 and DC

There are no errors in the eventlog and replsum shows no replication issues and up to date.

Forcing the replication doesnt make a difference. Ports in AWS security groups are fine, windows firewall is off. 

would rather not do an authoritive force replication since the DC's are critical at the moment and didnt want to make it worse.

Any ideas?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-09*

Did the non Authoritative replication on the AWS DC's 

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-02-09*

Hi,

Seems like a inbound network rule issue if the replicaiton is not working fro Onprem to AWS? Review your port connectivity both ways and also check AWS guidance on the ports.https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_network_security.html

Hope this helps.

JS

==

Please Accept the answer if the information helped you. This will help us and others in the community as well.
