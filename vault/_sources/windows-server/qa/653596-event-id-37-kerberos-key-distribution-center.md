---
title: "Event ID 37 - Kerberos-Key-Distribution-Center"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/653596/event-id-37-kerberos-key-distribution-center
question_id: 653596
fetched: 2026-07-25
answer_count: 12
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Event ID 37 - Kerberos-Key-Distribution-Center

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/653596/event-id-37-kerberos-key-distribution-center (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,   

the events 35 and 37 started to appear in the event logs a couple of weeks ago and from what I researched, Microsoft should be providing a Windows Update for this issue. Can anyone confirm or have further insight on this issue?  

Event Id 37  

The Key Distribution Center (KDC) encountered a ticket that did not contain information about the account that requested the ticket while processing a request for another ticket. This prevented security checks from running and could open security vulnerabilities. See https://go.microsoft.com/fwlink/?linkid=2173051 to learn more.  

  Ticket PAC constructed by: <domain controller>  

  Client: <domain>\<computername>  

  Ticket for: krbtgt  

Event ID 35  

The Key Distribution Center (KDC) encountered a ticket-granting-ticket (TGT) from another KDC (<domain controller>) that did not contain a PAC attributes field. See https://go.microsoft.com/fwlink/?linkid=2173051 to learn more.  

Thank you

## Answer (community) — community member [Mvp]

*upvotes: 2 · updated: 2021-12-06*

Once all the members have been patched fully with latest cumulative update the event log warnings should go away.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-02-15*

In case you didn't find it already there is an update in the known issues section of the KB: https://support.microsoft.com/en-us/topic/kb5008380-authentication-updates-cve-2021-42287-9dafac11-e0d0-4cb8-959a-143bd0201041

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-12-09*

Here is a sample of Event ID 37 I am talking about.  

The Key Distribution Center (KDC) encountered a ticket that did not contain information about the account that requested the ticket while processing a request for another ticket. This prevented security checks from running and could open security vulnerabilities. See https://go.microsoft.com/fwlink/?linkid=2173051 to learn more.  

  Ticket PAC constructed by: <domaincontroller>  

  Client: domain.local\<username>  

  Ticket for: krbtgt  

Thanks

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-08*

They all stopped for me about two weeks ago.  

One log indicates a users username  

can you post it?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-12-08*

Hi, thank you for this confirmation. I manually ran updates on couple of systems but still appears to show up in the domain controller event logs. One log indicates a users username and not the system computer. Do you have an explanation for this?  

Thank you
