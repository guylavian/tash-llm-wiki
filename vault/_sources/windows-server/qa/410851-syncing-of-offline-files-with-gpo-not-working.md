---
title: "syncing of offline files with GPO not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/410851/syncing-of-offline-files-with-gpo-not-working
question_id: 410851
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# syncing of offline files with GPO not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/410851/syncing-of-offline-files-with-gpo-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a Windows server 2012R2 domain with a GPO configured for Folder redirection. Syncing of offline files appears to be configured as well but cannot find the Group Policy that contains this configuration. Is there a way to determine which GPO contains this configuration and how can I disable it? Thank you

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-26*

Hi,  

To collect all the user settings:  

on the computer which the user logon to, run command: gpresult /h report1.html  

To collect the computer settings, run the cmd as administrator and run command: gpresult /h c:\report2.html  

And check the offline file settings on the output of the command.  

You can see the winning GPO for the setting in the output.  

Then go to the GPO and disable the setting.  

Best Regards,
