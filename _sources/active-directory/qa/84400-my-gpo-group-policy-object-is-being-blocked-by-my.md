---
title: "My GPO(Group Policy Object) is being blocked by my ACL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/84400/my-gpo-group-policy-object-is-being-blocked-by-my
question_id: 84400
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# My GPO(Group Policy Object) is being blocked by my ACL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/84400/my-gpo-group-policy-object-is-being-blocked-by-my (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all, I can't seem to find a way to allow my GPO to pass through my core router(which has ACL running). I was able to determine that the cause of this was the packets were being blocked by the ACL because if I remove the ACL on the VLAN, the GPO takes effect on the client PC going to my servers.   

here are the ACL commands I used in my lab environment, most of them are for AD  

permit udp any eq bootpc any eq bootps  

permit icmp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 echo-reply  

permit udp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 138  

permit udp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 138  

permit udp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 137  

permit udp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 137  

permit tcp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 138  

permit tcp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 138  

permit udp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 636  

permit udp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 636  

permit tcp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 636  

permit tcp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 636  

permit udp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 445  

permit udp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 445  

permit tcp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 445  

permit tcp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 445  

permit udp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 464  

permit udp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 464  

permit tcp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 464  

permit tcp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 464  

permit tcp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 123  

permit tcp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 88  

permit tcp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 389  

permit tcp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq domain  

permit tcp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq telnet  

permit tcp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 123  

permit tcp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 445  

permit tcp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 88  

permit tcp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 389  

permit tcp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq domain  

permit icmp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 echo-reply  

permit udp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq domain  

permit udp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq domain  

permit udp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 389  

permit udp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 389  

permit udp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 123  

permit udp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 123  

permit udp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 88  

permit udp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 88  

permit tcp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 135  

permit tcp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 135  

permit tcp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 3268  

permit tcp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 3268  

permit tcp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 25  

permit tcp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 25  

permit tcp 10.10.20.0 0.0.0.255 10.10.100.0 0.0.0.255 eq 3269  

permit tcp 10.10.100.0 0.0.0.255 10.10.20.0 0.0.0.255 eq 3269  

permit tcp any any eq 443  

Note: (10.10.100.0 is my server network and 10.10.20.0 is my Client pc network.)  

All of this is from my lab environment.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-09-03*

Hello @Amiel  ,    

Thank you for posting here.    

We can check whether all the ports AD required are open through the ACL on the VLAN.    

If no, we can remove the related entries of the ACL on the VLAN.    

And then check if the GPO takes effect on the client PC.    

For AD ports requirements, we can refer to the links below.    

Active Directory and Active Directory Domain Services Port Requirements    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd772723(v=ws.10)?redirectedfrom=MSDN    

Active Directory Replication over Firewalls    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/bb727063(v=technet.10)?redirectedfrom=MSDN    

Hope the information above is helpful.    

Best Regards,    

Daisy Zhou
