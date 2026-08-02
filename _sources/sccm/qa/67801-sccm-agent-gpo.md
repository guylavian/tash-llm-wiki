---
title: "SCCM Agent GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/67801/sccm-agent-gpo
question_id: 67801
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# SCCM Agent GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/67801/sccm-agent-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,    

I need some clarity on the what is the correct syntax to be put on below, i am getting a lot of info on how to fill this portion.    

also is there a switch i can add so it knows how to skip if there is an SCCM agent already installed on the machine.

## Answer (community) — community member

*upvotes: 1 · updated: 2020-08-16*

Hi,    

If you have extended already the Active Directory Schema and published the management point, you don't need to specify the MP information in the command line, otherwise, you can add /logon to top the installation if a version of the client already exists on the computer.    

It's recommended to push the client from the console, you can manage better and target only machines without ConfigMgr client.    

-  Group Policy installation    

-  Client installation methods in Configuration Manager    

-  Schema extensions for Configuration Manager    

Regards,    

Youssef Saad

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-08-17*

Hi,    

There is no absolutely correct syntax for the command, it depends on your own SCCM environment, usually a command like this works:    

ccmsetup.exe /mp=<management point> /logon SMSSITECODE=<site code> FSP = <fallback status point>    

Specifies the /logon, the client installation should stop if any version of the System Center Configuration Manager client is already installed.    

For more about client installation properties, you may refer to:    

https://learn.microsoft.com/en-us/previous-versions/system-center/system-center-2012-R2/gg699356(v=technet.10)?redirectedfrom=MSDN#BKMK_CCMSetupCommandLine    

Regards,    

Allen
