---
title: "Windows Server 2019 - Firewall GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1005428/windows-server-2019-firewall-gpo
question_id: 1005428
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-devices-deployment-config-app-groups", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-high-availability-clustering-high-availability", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
---
# Windows Server 2019 - Firewall GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1005428/windows-server-2019-firewall-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,     

I have 2 Windows Server 2019 with Failover Clustering set up.    

Based on the hardening benchmark, I have to set these GPO settings via AD GPO to 'No'.    

-  Ensure 'Windows Firewall: Public: Settings: Apply local connection security rules' is set to 'No'    

-  Ensure 'Windows Firewall: Public: Settings: Apply local firewall rules' is set to 'No'    

I have created inbound/outbound rules to allow specific ports necessary for MSSQL for 'Domain' and 'Private' profile only in the AD GPO.    

However, if I were to apply the above GPO settings (1 and 2), my failover cluster node goes down.    

How does the GPO setting (1 and 2) affect my failover cluster?    

Which GPO setting (1 or 2) can I set to 'No' without affecting my failover cluster?    

Thank you.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-13*

Hi,    

MS Cluster will require additional ports and access to communicate, you are just allowing MSSQL so it is not going to work.    

Check required ports and dynamic ports that will require connectivity for MSSQL and Windows Cluster ports too.    

configure-the-windows-firewall-to-allow-sql-server-access    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
