---
title: "Transport Rule BCCs email to external address but converts email from HTML to Plain Text"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1039930/transport-rule-bccs-email-to-external-address-but
question_id: 1039930
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Transport Rule BCCs email to external address but converts email from HTML to Plain Text

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1039930/transport-rule-bccs-email-to-external-address-but (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, we are using Office 365 Exchange Online and I have a transport rule setup to BCC any email received in a specific mailbox to an MDaemon server we host onpremises. When this transport rule kicks off, it appears to be converting the emails from HTML to Plain text, which is breaking one of our 3rd party importing tools. Is there any way to force emails to HTML in the transport rule, or by other means?     

I've looked over the Mdaemon settings and I believe I have all the settings correct there, which leads me ot believe that the transport rule may be at fault.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-07*

Yep, setting the contact conversion type is something else i was thinking. Thats always been a good work-around!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-07*

Thanks for the reply! I don't have remote domain setup so I can talk to my systems engineer about that.     

I was incorrect in my first statement. that it was converting from HTML to plain. It's actually a 'multipart/alternative' content type message. I pulled a copy of an email from the MDaemon server and saw that it's a MultiPart content type, starting with the Plain version and then the HTML version.    

the original email that it BCCs to MDaemon is Content-Type: application/ms-tnef; name="winmail.dat".     

I might try setting up these email addresses as a 'contact' and applying the TNEF conversion policy.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-07*

Is there a remote domain defined for that MDaemon server?    

You could set the remote domain content type to  MimeHtml and see if that helps.    

otherwise, I tend to blame the receiving server or client for these issues, not a transport rule.    

If you were to BCC another remote contact  in that rule, I would wonder what format it is for that receiving client.    

https://learn.microsoft.com/en-us/powershell/module/exchange/set-remotedomain?view=exchange-ps
