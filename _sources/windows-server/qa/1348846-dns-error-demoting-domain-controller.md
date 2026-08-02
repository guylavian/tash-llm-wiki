---
title: "DNS error demoting Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1348846/dns-error-demoting-domain-controller
question_id: 1348846
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# DNS error demoting Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1348846/dns-error-demoting-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, when attempting to demote a domain controller I receive an error that says “ It appears this is the last dns server for the Active Directory integrated zone” we have over 5 dc’s in our environment and they are all replicating, Al’s the zone in question is only listed as a Conditional Forwarder, however we also utilize AD LDS so I am wondering if this zone is linked somehow to the Lightweight Directory Service. Not sure why this error is happening since all dc’s are replicating. Any help is appreciated.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-12-13*

Hello,

it seems to be some conditional forwarders are locally created in the dc. 

i hope you are trying to demote the domain controller using powershell , you may try  

$error[0] |select * and see which zones are local and enable them to replicate with other domain controllers.

once all resolved, i may use the blow command to demote 

Uninstall-ADDSDomainController -DemoteOperationMasterRole:$false  -RemoveDnsDelegation:$false 

it will break if any thing gets failed , never skip the prechecks in production envionment. 

Uninstall-ADDSDomainController -DemoteOperationMasterRole:$false  -RemoveDnsDelegation:$false 

if all tests passed , in this case i may use  -IgnoreLastDnsServerForZone

Uninstall-ADDSDomainController -DemoteOperationMasterRole:$false  -RemoveDnsDelegation:$false  -Force:$true  -IgnoreLastDnsServerForZone

Regards

Deepak,

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-08-21*

Hello Fenton, Mark,  

Thank you for posting in Q&A forum.  

If the DC to be demoted is also a DNS server, or if it also serves as another DNS function (such as conditional forwarder), you can remove the conditional forwarder function if you do not need it. And then can you demote it by using Dcpromo.exe.  

When you try to remove a domain controller from your Active Directory domain by using Dcpromo.exe and fail, you can also remove/delete this DC by Ntdsutil.exe tool.  

https://petri.com/delete_failed_dcs_from_ad/  

Before or after you remove this DC, if the removed DC was a DNS server, update the Forwarder settings and the Delegation settings on any other DNS servers that might have pointed to the removed DC for name resolution.

Hope the information above is helpful. If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
