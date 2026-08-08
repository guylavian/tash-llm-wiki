---
title: "How to patch Windows 2012 domain controllers with legacy clients and avoid breaking stuff"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1379730/how-to-patch-windows-2012-domain-controllers-with
question_id: 1379730
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# How to patch Windows 2012 domain controllers with legacy clients and avoid breaking stuff

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1379730/how-to-patch-windows-2012-domain-controllers-with (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

 We have 2 domains with a 2 way transitive trust between them:

Domain A (main domain)  

4 x 2012 R2 DCs, 2008 domain functional level, 2003 forest functional level  

Domain B (legacy)  

2 x 2003 DCs, 2003 domain and forest functional levels

We haven't been patching the main domain due to the risk of breaking legacy infrastructure. Our Windows 2012 R2 DCs were last patched in July 2020. We stopped patching the DCs due to the netlogon vulnerability and our conversation with Microsoft support at the time mentioned that patching the DCs would break functionality with our legacy clients (Windows NT4 and Windows 2000). Fast forward and we've now almost removed all  of the NT4 and 2000.

How much of a risk do we run with patching our DCs and breaking client access? Here's a quick overview of the clients in our main domain:

81 Windows 2003 sp2 servers (1 x 2003 Windows servers SP1)  

45 Windows 2008 R2 SP1  

132 Windows 7 (SP1)

We have some clients using NTLM authentication  

We have smbv1 in use

Implies that 2008 R2 would be an issue as an ESU would be needed

https://support.microsoft.com/en-us/topic/how-to-manage-the-changes-in-netlogon-secure-channel-connections-associated-with-cve-2020-1472-f7e8cc17-0309-1d6a-304e-5ba73cd1a11e

We've also enabled a group policy to  "Allow cryptography algorithms compatible with Windows NT4 to a value of Enabled" for backward compatibility

How can I go about applying Domain Controller Windows updates and ensure backward compatibility\reduce risk?

What level of client OS do I need to achieve before being able to patch the DCs?

Thanks in advance

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-10-02*

can you clone backup&restore/virtualize to separate environment

-  one of your DCs

-  important servers

connect into this environment a few representative clients and test upgrade (small steps) there to see what breakts?

I do not know if you are just joking or is your environment a real relic... 2003 come on.

are you still using ntfrs or you migrated already to dfs-r AD replication?

you duplicated this question here: https://learn.microsoft.com/en-us/answers/questions/1379732/how-to-patch-windows-2012-domain-controllers-with

close one or the other

regards
