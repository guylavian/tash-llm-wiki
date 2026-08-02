---
title: "Replacement Characters Displayed When Exchange Disclaimer Rule Enabled"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/148652/replacement-characters-displayed-when-exchange-dis
question_id: 148652
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Replacement Characters Displayed When Exchange Disclaimer Rule Enabled

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/148652/replacement-characters-displayed-when-exchange-dis (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

All,    

We have an odd issue that started happening about a month ago, where many Emails coming from O365 to our on-prem Exchange 2016 get re-encoded and ?? appear in line breaks and nbsp; characters. (Example below). Note, this only happens when the Disclaimer - Append mail rule is enabled. It does not happen when this rule is disabled. Are there any configuration options in Exchange I can make so this doesn't happen?  NOTE: I am aware of language options in Outlook, that isn't the issue, as Email is being rewritten with unknown replacement characters (they show up in OWA, Thunderbird, forwards etc.) only when the disclaimer is enabled/being written.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-18*

I never came up with a definitive solution. I think there is a bug in the Exchange transport agent that rewrites the message with an incorrect character set in very specific circumstances. In our case, the mail flow looked like this:  

Message sent from Office 365 -> Hornet (our Email security provider) -> Exchange -> Prepend message compliance rule -> Message rewritten with unknown characters inserted into message.  

Our workaround was to add [EXTERNAL] to the subject, which didn't produce the unknown characters. I actually like this better because you can see where the message originated in the subject without actually opening it.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-14*

Same here.  

Not a single post on this page till the date of my post is really helpful.  

Better Microsoft advice something ...  

Tried new rule creation, tried remotedomain encoding change, tried other exchange installation on separate environment, all same with Exchange 2016 CU19 ... CU20.  

Anyone ?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-03*

I am seeing the same thing with a similar rule...

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-03*

Thanks for the reply---    

I've attached the rule, redacted a few exceptions for privacy, but basically yes all incoming messages are tagged with our phishing warning banner to alert users to be careful before clicking. Also, does not matter if the banner is html or plain text.    

Sent items look OK.  The top example was sent from my Outlook.com address. Happens every time.  We have seen this from other senders (sendgrid, but have only seen 1 example of this) but primarily it has been from O365/Microsoft servers.    

UTF-8 is clicked. If I change to another encoding, the characters are represented in a different way, but still displaying garbage.    

Interesting thing here -- If I change to another mail rule that tags the subject and leaves the body alone, the characters do not appear.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-03*

How does your rule look like? You make it applied to all inbound messages？Post a snapshot of it if possible.    

Have you contacted the senders and checked the messages in his Sent Items, looking correct?    

You said "many messages" rather than "all messages", does this issue happen randomly?    

Open those messages and click Actions-other Actions-Encoding , is UTF-8 ticked?    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
