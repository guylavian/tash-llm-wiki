---
title: "Disable file sharing without breaking sysvol/netlogon"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/108819/disable-file-sharing-without-breaking-sysvol-netlo
question_id: 108819
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Disable file sharing without breaking sysvol/netlogon

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/108819/disable-file-sharing-without-breaking-sysvol-netlo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a server that has both the DC and File server roles running. I want to migrate my users over to a new file server on new hardware. I've robocopied all the files over to the new server and everything looks great. That being said, I want to shut off file sharing on the old server in case users have old shortcuts, etc to the old server. Is there an easy way of doing this, without changing all the share permissions? I thought about simply disabling file and print sharing in the nic, but I'm not sure if that stops sysvol from sharing as well?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-27*

File sharing is used by a domain controller for things like group policies - users need shared access to group policies in order to download them.  So I don't think your DC would operate if you tried to remove file sharing services.    

I would simply remove all user file share locations and inform the users that their location has been changed.  IF a user runs into a non-existent share which they have set up outside the controlled shares, it is their issue and they can fix it quickly enough
