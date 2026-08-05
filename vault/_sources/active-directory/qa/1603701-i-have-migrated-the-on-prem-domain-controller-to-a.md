---
title: "I have migrated the on-prem domain controller to Azure vm as ADC. after that I converted my Azure ADC to primary DC. then I turn off the on-prem ADC which was DC before the migration. now  Client computer(on-prem or Azure)  not able to join domain."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1603701/i-have-migrated-the-on-prem-domain-controller-to-a
question_id: 1603701
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# I have migrated the on-prem domain controller to Azure vm as ADC. after that I converted my Azure ADC to primary DC. then I turn off the on-prem ADC which was DC before the migration. now  Client computer(on-prem or Azure)  not able to join domain.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1603701/i-have-migrated-the-on-prem-domain-controller-to-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have migrated the on-prem domain controller to Azure vm as ADC. after that I converted my Azure ADC to primary DC. then I turn off the on-prem ADC which was DC before the migration. now  Client computer(on-prem or Azure)  not able to join domain. 
If I turn on my on prem ADC. then azure and on prem client pc's are able to join domain.
I am able to ping my new DC which is on azure from on prem via site to site tunnel. I have checked the replication as well which is working fine and I have checked the FSMO roles as well.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-03-05*

Hello svc.admin,

Thank you for posting in Q&A forum.

Based on your description, if you turn on the on-premises ADC, Azure and on-premises client computers are able to join the domain. This suggests that the local ADC is still working to some extent. Confirm that the on-premises ADC is properly shut down so that the primary DC on the Azure VM is the only domain controller.

In the meantime, you mentioned that client computers can't join domains, make sure that the client computers' DNS settings point to the primary DC on the Azure VM. The primary DNS server should be the primary DC on the Azure VM, and the standby DNS server should point to itself. Also ensure that there is connectivity between the client machines and the Azure VMs. You can use the ping command to test the network connectivity between the client and the primary DC.

In addition to this, you can use the "netdom query fsmo" command on the command prompt to verify the FSMO role assignment. Check that the primary DC on the Azure VM has successfully taken over the FSMO role.

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Yanhong Liu  

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
