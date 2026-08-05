---
title: "RDP, SYSVOL, Remote PowerShell Issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/903023/rdp-sysvol-remote-powershell-issue
question_id: 903023
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-remote-desktop-terminal-services", "windows-business-windows-server-user-experience-powershell", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# RDP, SYSVOL, Remote PowerShell Issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/903023/rdp-sysvol-remote-powershell-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a server that is experiencing strange issues.    

We loose the ability to RDP into it a day or two after it's rebooted. It cannot access the \domain\sysvol share and when we can't RDP into it any use of remote powershell to it results in a hung powershell session.    

CPU usage is minimal. Printer and Files shares continue to function correctly. We just can't seem to login to the server using RDP at all.     

Some times we can attach the Services.msc to it remotely. When we can do that it takes forever for any refresh to take place. I restarted a single service this way and it took almost 5 minutes to get control back again in the services.msc.    

There isn't anything in the Even Logs that is jumping out as to what the problem is.    

Have you seen anything like this before, how did you troubleshoot it?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-28*

Hi there,     

Try using the shutdown command from another server to do the reboot and see if it behaves normal after the reboot.    

Does the server have multiple NICs? You might face these issues when terminal services service binds to the wrong one. Also if you have made any recent updates try uninstalling them and see if that is helpful.    

The below thread discusses the same issue and you can try out some troubleshooting steps from this and see if that helps you to sort the Issue.    

https://learn.microsoft.com/en-us/answers/questions/360403/rdp-stopped-after-update-must-reboot-server-repeat.html    

Remote Desktop Connection Broker not starting after reboot     

https://social.technet.microsoft.com/Forums/en-US/45324bc4-87a8-490d-807e-af9da283fcb2/remote-desktop-connection-broker-not-starting-after-reboot?forum=winserverTS    

------------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-24*

We loose the ability to RDP into it a day or two after it's rebooted. It cannot access the \domain\sysvol share     

Sounds like a firewall profile change was likely. When NLA starts to detect the network location, the machine will contact a domain controller via port 389. If this detection is successful, it will get the domain firewall profile (allowing for correct ports) and we cannot change the network location profile.     

If the domain was not found or process failed, NLA will let you to determine which firewall profile will be used, private or public.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-24*

Nope, that's not it. DNS is clean and there are no IP conflicts and both have static IP's with static DNS entries for them.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-24*

I'd check the domain controller and problem member both have the static ip address of DC listed for DNS and no others such as router or public DNS.     

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
