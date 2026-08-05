---
title: "Active directory schema downgrade"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/239107/active-directory-schema-downgrade
question_id: 239107
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Active directory schema downgrade

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/239107/active-directory-schema-downgrade (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

How to schema downgrade active directory from 2019 to 2008 R2 because I unable migration from 2008 R2 to 2016 I'm not sure that schema is root cause for this issue  

Thank you.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-21*

Hello @NK WANG  ，

Thank you for posting here.

In order to further troubleshoot this issue, please help provide the following information at your convenience:  

1.What is your forest functional level?  

2.What is your domain functional level?  

3.Is your AD forest a single with a single domain? If so, how many DCs in your entire forest? Please run nltest /dclist:domain.com to check.  

For example:

4.What are the operating system of these DCs?

5.Based on the description "because I unable migration from 2008 R2 to 2016 I'm not sure that schema is root cause for this issue", what is your actual issue?

6.What is your SYSVOL replication type ? Is it FRS or DFSR, we can check as below:

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), DFSR is being used. If the subkey does not exist, or if it has a different value, FRS is being used.

Thank you for your understanding.

Best Regards,  

Daisy Zhou

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-21*

What problem are you having? A schema update just prepares the domain to accept a domain controller with the higher operating system.
