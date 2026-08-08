---
title: "ADFS (WAP / STS) not working after migration from Hyper-V to Vmware ESXi"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/476163/adfs-wap-sts-not-working-after-migration-from-hype
question_id: 476163
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS (WAP / STS) not working after migration from Hyper-V to Vmware ESXi

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/476163/adfs-wap-sts-not-working-after-migration-from-hype (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everybody,  

I have 4 ADFS servers hosted on Hyper-V and I need to migrate them to VmWare ESXi.  

2 of the servers are the WAP servers and they have a cluster between the network interfaces.  

The other 2 are the STS servers and they have a cluster between the network interfaces as well.  

I tried to migrate them many times with the Vmware Converter. After the migration, I created a new virtual network adapter (for vmware) for each server. I used the same IP addresses and the same MAC Addresses for each network adapter. The clusters between the network adapters of the servers are working perfectly. But the email services stopped working. Outlook can't connect to Office 365, and when we try to access using the browser, an error message appears when it tries to contact the STS server (inside and outsite the private network).   

All the servers respond to ping and have access to internet.  

I don't know if the problem is something with the network adapters that changed from Hyper-V to Vmware, or if I have to do something to reconnect to Office365.   

I already migrated more than 100 VM's and had no problems at all. Only with these ADFS servers, and I don't know what else to do.  

Does anybody have any suggestions?  

Thanks in advance!

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-07-23*

Hi! Thanks for your answer and your help.  

I found what was the problem and I'll say what I did in case anyone have the same issue.  

After migrating from Hyper-V to VmWare, I had to reconfigure the trust certificate between the server that WAP (web application proxy) is installed and the ADFS server.  

Some windows services related to ADFS wasn't being able to start without this reconfiguration and I could see this issue on event viewer.  

But that was not enough. In VMWare, I had to change the type of my network adapter from "VMXNET3" to "E1000E".  

To be honest I don't know why I couldn't use the VMXNET3 adapter, but is working fine now with the E1000E.  

Thank you for your suggestion and pacience.  

Rodrigo Passini.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-07-14*

Nothing in this scenario let us to think the issue could be the ADFS service.  

We needs traces, error messages, something. It's mor elikely to be a network/DNS issue. To confirm, connect locally on the ADFS box and navigate to the /adfs/ls/IDPInitiatedSignon.aspx page. Can you log in there? (note that this page has to be enabled with Set-ADFSProperties -EnableIdPInitiatedSignonPage:$true for that test)
