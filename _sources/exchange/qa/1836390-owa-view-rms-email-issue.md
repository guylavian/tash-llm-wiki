---
title: "OWA view RMS email issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1836390/owa-view-rms-email-issue
question_id: 1836390
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# OWA view RMS email issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1836390/owa-view-rms-email-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The envirome is Exchange 2013 and local RMS server enviroment.

here is the test steps to reproduce issue:

-  create a new test message from outlook 2016, email add rms permission, such as "not allow forwared"

-  send this rms message to another internal user

-  recipient can read this message well from outlook client, however, it cannot view email content from OWA client.

Is there any special configuration for OWA?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-24*

Hi,

Thanks for posting your question on Microsoft Q&A forum!

Based on your description, it sounds like there might be an issue with the configuration of Rights Management Services (RMS) in relation to Outlook Web App (OWA). You can do the following to troubleshoot:

-  run the following command to check the RMS configuration: 

```
Get-IRMConfiguration
```

-  Make sure that OWA IRM (Information Rights Management) is enabled.

```
Set-OWAMailboxPolicy -Identity "OWA Mailbox Policy Name" -IRMEnabled $true
```

-  Verify that your OWA virtual directory is configured correctly. You can do this by running: 

```
Get-OWAVirtualDirectory | FL
```

Please be free to contact us if any updates. And if this helps, don't forget to mark it as an answer.
