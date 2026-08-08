---
title: "Exhange 2016 not proxying to Exchange 2010 CAS for Outlook"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/430193/exhange-2016-not-proxying-to-exchange-2010-cas-for
question_id: 430193
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exhange 2016 not proxying to Exchange 2010 CAS for Outlook

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/430193/exhange-2016-not-proxying-to-exchange-2010-cas-for (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all.  

In the same site I have an Exchange 2010 Server and an Exchange 2016 server.  

The target is to migrate all of the mailbox to Exchange 2016 and then dismiss Exchange 2010.  

audiscover in DNS is set to point to Exchange 2016.  

With OWA I have no problems and Exchange 2016 proxies to Exchange 2010.  

When I use Outlook to connect to a mailbox which resides on Exchange 2016, all is ok.  

BUT when I launch Outlook to connect to a mailbox which resides on Exchange 2010 I get this error:  

"Cannot start Microsoft Outlook. Cannot open the outlook window.The set of folders cannot be opened.You must connecto to Microsoft Exchange with the current profile before you can syncronize your folders with your Outlook Data File (.ost)"  

If I configure Outlook NOT to use cache the error becomes:  

""Cannot start Microsoft Outlook. Cannot open the outlook window. The set of folders cannot be opened. Microsoft Exchange is not available. Either there are network problems or the Exchange server is down for maintainance"  

If now run Microsoft Remote Connectivity Analyzer for Outlook it says everything is OK.  

On Exchange 2010 Outlook Anywhere is ON with basic authentication.  

On Exchange 2016 Outlook Anywhere is ON with NTLM authentication.  

Any suggestions?  

Thanks.

## Answers

_No answers on this thread._
