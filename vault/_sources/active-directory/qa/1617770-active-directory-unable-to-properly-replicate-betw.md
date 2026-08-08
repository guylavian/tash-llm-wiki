---
title: "Active Directory unable to properly replicate between 3 DCs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1617770/active-directory-unable-to-properly-replicate-betw
question_id: 1617770
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Active Directory unable to properly replicate between 3 DCs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1617770/active-directory-unable-to-properly-replicate-betw (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 3 DCs, 01 is the primary Windows 2012 Server while 02 and 23-2 are the others. I've tried quite a few different methods I've seen for fixing things with no luck. I always get Server Down, or target name is incorrect when trying them. 

I've run the repadmin /showrepl command and will attach the results below. Any advice would be greatly appreciated

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-03-18*

Hello,

 

Thank you for posting in Q&A forum.

According to the screenshot provided, there were lots of AD replication failure in the history. Pleas kindly try:

 

1.Run repadin /replsum to get a summary of replication error and insights.

 

2.Run repadin /syncall and check if manual replication is available or not. If it's not available, let's further dig the network connection between the DC.

 

3.Check the TCP connection on port 135 by CMD command: Ping DC IP or Telnet DC IP Port

 

4.Disable the firewall temporarily and check if it works.

Hope this answer can help you well.

 

Best regards，

Jill Zhou

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-03-14*

Majority of AD replication problems stem from misconfigured DNS. 

Start by configuring each of the domain controllers with the same DNS client settings - by pointing them to the IP address of the DNS server on the domain controller that servers as the PDC Emulator and then restart the following services on each domain controller:

-  Netlogon service

-  DHCP service 

-  DNS service

Finally, run ipconfig /registerdns on each domain controller.

If this doesn't resolve the issue, follow

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/troubleshoot/troubleshooting-active-directory-replication-problems

hth

Marcin
