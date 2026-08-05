---
title: "Migrate Active Directory Server 2012 to 2022"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2287747/migrate-active-directory-server-2012-to-2022
question_id: 2287747
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-networking-networking-other"]
answer_author_roles: ["Q&A User"]
---
# Migrate Active Directory Server 2012 to 2022

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2287747/migrate-active-directory-server-2012-to-2022 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

I am planning to migrate our Active Directory Server from Windows Server 2012 to 2022 and I would like to ensure a smooth transition, especially since we have several applications link like ADFS, Accops, SAP, Firewall, and ISP that are linked to our current AD.

My main concern is with keeping the hostname and IP address the same as the existing 2012 server. If I were to demote or shut down the 2012 server, it could potentially disrupt these applications. Could you please provide guidance on how to approach this migration while maintaining the same hostname and IP address?

Note - I have a few questions regarding the process of creating a new Windows Server 2022 and joining it as an Additional Domain Controller (ADC). If I assign a separate IP address and hostname to the new server and then transfer all roles to it, will my applications experience downtime or be closed during this transition?

Additionally, once the transfer of roles is complete and everything is functioning as expected, am I able to revert the new ADC’s hostname and IP to the original settings? Furthermore, can I demote the old server and give it the same hostname and IP as the old server?

Thanks and Regards

Ravinder Makkar

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-06-27*

Thank you so much for your positive response

I wanted to clarify that I have a total of 15 servers, including 14 ADC servers at different locations and one PDC in my corporate office. I am set to migrated the 14 ADC (Windows Server 2022) servers at their respective locations, which are all functioning perfectly.

Regarding the migration of the PDC, I want to confirm that following the steps you provided will not adversely affect the other servers that have already been migrated to Windows Server 2022 at different locations.
