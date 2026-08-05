---
title: "I am trying to add my partner's bigpond email account to Outlook but I get a message saying it can't add a work or school account. It is not a work or school account. It is a bigpond.net.au account."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4695212/i-am-trying-to-add-my-partners-bigpond-email-accou
question_id: 4695212
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 2
qa_tags: []
---
# I am trying to add my partner's bigpond email account to Outlook but I get a message saying it can't add a work or school account. It is not a work or school account. It is a bigpond.net.au account.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4695212/i-am-trying-to-add-my-partners-bigpond-email-accou (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to add my partner's bigpond email account to Outlook because Telstra say they are moving to Outlook, but I get a message saying it can't add a work or school account. It is not a work or school account. It is a bigpond.net.au account.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-10*

Hi Yvonne Deering，

Welcome to the Microsoft Community.

I understand your question about adding accounts. If this is truly not a work or school account, please see the suggestions below.

Whether you are using Outlook Classic or Outlook(new), I suggest you manually configure your bigpond mailbox.

I am providing you with the configuration parameters of the bigpond mail server here for reference, you can consult their service provider for details as this may be variable.

Adding an account

Select a configuration method:

       Select "Manual Setup or Other Server Type", and then click Next.

Select the account type:

       Select "POP" or "IMAP", IMAP is recommended so that emails can be synchronized to multiple devices.

Mail Server Settings

The following provides the mail server configuration parameters for BigPond:

IMAP Server Settings (recommended)

-  Incoming Mail Server (IMAP)

o Server Address: imap.telstra.com

o Port: 993

o Encryption method: SSL/TLS

-  Sending Mail Server (SMTP)

o Server address: smtp.telstra.com

o Port: 465

o Encryption: SSL/TLS

POP3 Server Settings

-  Incoming mail server (POP3)

o Server Address: pop.telstra.com

o Port: 995

o Encryption method: SSL/TLS

-  Sending Mail Server (SMTP)

o Server address: smtp.telstra.com

o Port: 465

o Encryption: SSL/TTLS

Please try the suggestions above and feel free to contact me if you have further questions.

Best Regards,

Jimmy Wang |Microsoft Community Support Specialist
