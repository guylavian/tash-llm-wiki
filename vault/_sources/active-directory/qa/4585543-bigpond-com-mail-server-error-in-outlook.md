---
title: "Bigpond.com Mail Server Error in Outlook"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4585543/bigpond-com-mail-server-error-in-outlook
question_id: 4585543
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 59
qa_tags: []
---
# Bigpond.com Mail Server Error in Outlook

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4585543/bigpond-com-mail-server-error-in-outlook (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

Based in Australia, using a bigpond.com email address. 

Having issues sending mail. Can receive without issue. 

Error is 0x800CCC6F "Sending reported error (0x800CCC6F) ; "Your outgoing (SMTP) email server has reported an internal error. If you continue to receive this message, contact your service administrator or Internet service provider (ISP). The server responded: 554 5.7.1 Connection Refused. 206.xx.xxx.xxx is blacklisted in Spamhaus RBL List. See: <spamhaus URL> "

IP has been hashed for security purposes. 

What's more, I can't even change the mailbox settings/server settings in Outlook. I get the "Something went wrong" error when trying to save. 

Telstra being Telstra, wiped their hands of it and said it's a Microsoft problem. Sends without issue in their web-based system. 

Any ideas?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-04*

Hello Josh,

Good day! Thanks for posting in Microsoft Community. We are happy to help you.

I understand you are getting an error message “0x800CCC6F” “Your outgoing (SMTP) email server has reported an internal error. The server responded: 554 5.7.1 Connection Refused.”

Please note this is a known issue an a permanent fix is being developed. This issue can occur if your machine was updated to have TLS 1.3 configured.  To work around the issue, remove the TLS 1.3 settings by doing the following:

-  Click Start, search for Regedit and open the application

-  Navigate to this path in the registry:

Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols

-  Review if you see TLS 1.3 under Protocols.  If you do, right click on Protocols and click Export to save out a registry export of the configuration in case you need to revert back for any reason.

-  If under Protocols you see TLS 1.3 delete that key and its sub keys.

-  Restart Outlook.  If you still don’t see sync start working, restart Windows.

After making the change the registry should appear similar to below not showing any TLS 1.3 keys.

For your reference please see Outlook IMAP or POP server unexpectedly terminated the connection, and the server was interrupted (microsoft.com)

We are looking forward to your reply. Thank you for your cooperation.

 Sincerely,

Simbarashe | Microsoft Community Moderator
