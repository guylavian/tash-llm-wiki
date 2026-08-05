---
title: "We are unable to update gpo policy to client system"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2169378/we-are-unable-to-update-gpo-policy-to-client-syste
question_id: 2169378
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# We are unable to update gpo policy to client system

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2169378/we-are-unable-to-update-gpo-policy-to-client-syste (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Support team,

 We are unable to update gpo policy to client system getting failed, this clients are located in other location main branch nad sub branch both connected through Firewall Site to Site configuration both are comunicating well but whenever we are applying any GPO policy in client system it's not syncing getting failed.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-20*

Hello 

Thank you for posting in Q&A forum. 

Here are some steps you can try to troubleshoot the issue with your Group Policy Object (GPO) updates failing for clients in different locations connected via a site-to-site VPN: 

-  Ensure that the clients can communicate with the domain controllers over the VPN。 

-  Ensure that the necessary ports for Active Directory and Group Policy are open on the firewall: 

Ports to Check: 

• TCP/UDP 135 (RPC) 

• TCP 139 (NetBIOS Session Service) 

• TCP/UDP 389 (LDAP) 

• TCP 445 (SMB) 

• TCP 636 (LDAP SSL) 

• TCP/UDP 3268-3269 (Global Catalog) 

• TCP/UDP 53 (DNS) 

-  Check the Event Viewer on the client systems for any Group Policy-related errors。 

-  Use the gpresult and rsop.msc tools to diagnose GPO application issues. 

-  Ensure that both computer and user authentication are working correctly. 

References:

Applying Group Policy troubleshooting guidance - Windows Server ...

Group Policy via vpn connection | Microsoft Community Hub

I hope the information above is helpful. 

If you have any questions or concerns, please feel free to let us know. 

Best Regards, 

Daisy Zhou 

============================================ 

If the Answer is helpful, please click "Accept Answer" and upvote it.
