---
title: "Exchange 2016: after installation of CU 18 attachments from shared mailbox can't be opened in OWA"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/112628/exchange-2016-after-installation-of-cu-18-attachme
question_id: 112628
fetched: 2026-07-25
answer_count: 20
has_accepted_answer: false
upvotes: 4
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016: after installation of CU 18 attachments from shared mailbox can't be opened in OWA

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/112628/exchange-2016-after-installation-of-cu-18-attachme (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

we installed last Thursday CU 18 on a single Exchange 2016. After that we recognized that attachment from shared mailboxes can't be opened anymore. This affects all attachments, download and preview. The problem seems to be that the URL for the attachment ist wrong. When we try to download an attchment a new windows is opened and we're redircted to a url in this format (original domain name is replaced):  

"https://outlook.office365.com/owa/******@domain-name.de/service.svc/s/GetAttachmentDownloadToken?redirect=%2fowa%2ftemp-test%40domain-name.de%2fservice.svc%2fs%2fGetFileAttachment%3fid%3dAAMkADVjYTJlNmVhLWU5YWUtNDExNC04YmI5LTNkNDI1NzU0YTRhZQBGAAAAAACFeKz%252b7LiwTJTGaiFKmoEUBwDgWBbEnQXzT5ipyGwAVbfZAAAAAAEMAADgWBbEnQXzT5ipyGwAVbfZAAAAAAk3AAABEgAQAHTIfMMNYkBEk%252bb%252f1UJcNZo%253d%26X-OWA-CANARY%3dji4zp9VACUGzxzvHkAjNH0AOjQZUZNgIt7lknLLRBv1JieCvW96de5oLgPWmV6rJSNOZafAG8fU.%26isDocumentPreview%3dFalse  

I do not understand why this request is getting redirected to office365.com. We do not have an hybrid enviroment or anything like that. "Normal" user accounts does not have any problems. if we forward the affected e-mail from the shared mailbox to a real person, attachment can be opened. Event logs or similar do not show any related anomalies. Any ideas whats going on or how to fix this?  

btw, problem exists only in OWA, the same attachment can be opened in Outlook without any problems. The problem also exists with a new shared mailbox.  

kind regards Christoph

## Answer (community) — community member

*upvotes: 1 · updated: 2020-10-15*

btw, I got a nearly final anwser from the MS support that the real bugfix will be only available in the next CU.

## Answer (community) — community member

*upvotes: 1 · updated: 2020-10-09*

Hi everyone,    

The engineering team is working on the issue and fix would be release in the coming updates.    

Please wait for the next CU released then test if the issue persists.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-01*

It seems a bug with Exchange 2016 CU18, not heard such issues before and it's working well in my Lab(2013&2016).    

Let's see how Microsoft would explain about this.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-09-30*

Hi @Christoph  ,    

Microsoft support is aware of a similar issue and asks that you open a support ticket with them so they can track it down.  So please do that to get some resolution. It's not something that can be solved here.     

Thanks!
