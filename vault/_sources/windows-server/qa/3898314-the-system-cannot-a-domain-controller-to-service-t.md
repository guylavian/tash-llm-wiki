---
title: "The System Cannot a domain controller to service the authentication request. Please try again later."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3898314/the-system-cannot-a-domain-controller-to-service-t
question_id: 3898314
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-home-windows-11-platform-files-folders-storage", "windows-server"]
answer_author_roles: ["Volunteer Moderator"]
---
# The System Cannot a domain controller to service the authentication request. Please try again later.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3898314/the-system-cannot-a-domain-controller-to-service-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

window 10 system is the act as server. and windows 11 as a client. windows 11 access data from windows 10 few days back now windows 11 not access data after new updates. First error ID 0x800704f8  then error id  change to 0x800700375  I had do change configuration in available in  source of internet. now "The System Cannot a domain controller to service the authentication request. Please try again later."  first error message. There is no password in server or (LAN Network). if ok clicked Authentication failed NTLM Authentication has been disabled. other windows 10 clients are able access the data.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2025-02-11*

Hello,

See if this fix helps you:

https://www.kapilarya.com/fix-the-system-cannot-contact-a-domain-controller-in-windows-11

Let us know if this helps!

Note: Included link in this reply refers to blog by a trusted Microsoft MVP.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2025-02-10*

Hi sharbin, welcome in community

I'm Alvise, an independent consultant and i'm eager to support you today

If The system cannot contact a domain controller to service the authentication request error occurs, you can first flush the DNS from the server and client machines, then restart the DNS server Service.

You can flush with the command

Ipconfig /flushdns

In addition, get targeted support in this dedicated platform 

https://learn.microsoft.com/en-us/answers/tags/...

Let me know 

Elvis
