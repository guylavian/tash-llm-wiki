---
title: "Unable to time-sync with Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1480474/unable-to-time-sync-with-domain-controller
question_id: 1480474
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# Unable to time-sync with Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1480474/unable-to-time-sync-with-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've recently un-joined a Windows 10 workstations from one AD domain and joined it to a new domain. I've used the ForensiT Profwiz to migrate the user profile. My problem is that when I checked the time sync using 'w32tm /query /source' it came back with time.windows.com, not my DC. This workstations did previous show connected to the previous DC. In an effort to reset the time souce I did:

net stop w32time   

 w32tm /unregister   

w32tm /register   

net start w32time

After that, the /query /source gave me 'Local CMOS Clock'. Nothing I have tried since changes this source. I also tried: 

w32tm /config /manualpeerlist:dc1,0x8 /syncfromflags:MANUAL   

w32tm /config /update

but that had no effoect. I also tried deleting the "Time Sources" GPO because a) someone said I didn't need a GPO and b) I though I'd try setting the Date & Time setting manually, but even after deleting the GPO and rebooting the workstations and the DC it still says, "Some of these settings are hidden or managed by your organization".

So, how to I reset the time sync to source from the Domain Controller? Is there some registry settings I have to tweak?

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2024-01-07*

Hi @Mark Foley 

If the machine is member of domain , the type should be NTDS5 and not NTP when you run the following command. 

```
w32tm /query /configuration
```

Is this already the case?

Please don't forget to accept helpful answer
