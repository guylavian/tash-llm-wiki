---
title: "Adding Windows Server 2022 as a Domain Controller in Windows Server 2016 Forest."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1867585/adding-windows-server-2022-as-a-domain-controller
question_id: 1867585
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Adding Windows Server 2022 as a Domain Controller in Windows Server 2016 Forest.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1867585/adding-windows-server-2022-as-a-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We have a Windows Server 2016 Active Directory Forest and want to introduce a Windows Server 2022 server as a Domain Controller within the forest, is it possible?

What are the steps to add a Windows Server 2022 server as a Domain Controller in a Windows Server 2016 forest (with Forest Functional Level 2016)?

Thank you.

Regards,

Raj

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 2 · updated: 2024-08-15*

Hello raj a,  

Thank you for posting in Q&A forum.

We have a Windows Server 2016 Active Directory Forest and want to introduce a Windows Server 2022 server as a Domain Controller within the forest, is it possible?

A: Yes, you can.

What are the steps to add a Windows Server 2022 server as a Domain Controller in a Windows Server 2016 forest (with Forest Functional Level 2016)?

A:

Step 1

Before we do any changes to our AD environment, we had better to check our AD environment health. So, we can try the following steps:

1.We need to check if all the DCs works fine, we can run Dcdiag /v on each DC to check. 

2.Run commands below on PDC to check AD replication status if you have multiple DCs in your domain.

repadmin /showrepl >C:\rep1.txt

repadmin /replsum >C:\rep2.txt

repadmin /showrepl * /csv >c:\repsum.csv

3.Check SYSVOL replication status if you have multiple DCs in your domain.

Step 2

1.Add new 2022 server to the existing domain. 

2.Promote this new 2022 server to Domain Controller (add AD DS role and DNS role). 

3.Also make this new 2022 DC as GC. 

4.Check the health status of new DC and old DC and AD replication status (if you have more than one DC) followed Steps 1. 

5.If everything is OK, transfer FSMO roles to the new 2022 DC if needed. 

You can check whether you have successfully transferred the FSMO roles by running the command as administrator on any DC: netdom query fsmo 

If you want to demote the 2016 DC later, you need to do:

1.If old 2016 DC was a DNS server, update the DNS client configuration on all member workstations, member servers, and other DCs that might have used this DNS server for name resolution. If it is required, modify the DHCP scope to reflect the removal of the DNS server.

2.If old 2016 DC was a DNS server, update the Forwarder settings and the Delegation settings on any other DNS servers that might have pointed to the old 2016 DC for name resolution. 3.Migrate all other roles on old 2016 DC to new 2022 DC (or other member servers) if you have or if you need.

4.After you transfer FSMO roles and update all DNS settings and migrate other roles if you have. And after a period of time, if everything is OK, you can consider demoting the old 2016 DC if needed.

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2024-08-18*

I think it's fine to follow the steps for installing Domain Control as normal, just make sure that when you install Domain Control, the forest functional level is the same as the existing forest, and the domain functional level is the same as the domain you want to join.
