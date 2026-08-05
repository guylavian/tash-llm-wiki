---
title: "Exchange Online Non-Spam Emails Going Directly to Quarantine"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/351977/exchange-online-non-spam-emails-going-directly-to
question_id: 351977
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Online Non-Spam Emails Going Directly to Quarantine

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/351977/exchange-online-non-spam-emails-going-directly-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have emails from one customer where every email received by my Exchange Online (Office 365) account are going to Quarantine. I have other emails from other domains that are not spam also going to Quarantine, too. I had my customer send me an email saying "This is a test", and it was Quarantined. In addition, my customer's domain is not only any spam list. Something is horrible broken on Exchange Online. I can't add every domain to an allow list and I can't predict which domains I will receive emails from. Nor can my customer's go ask every company they email to contact their IT department ahead of time to put the domain on an Allow List. In other words, Microsoft's spam filtering is a business killer. I can pinpoint when this started to the day, March 27th.

So the questions are:

1) What happened to the spam filtering on March 27th where it is now 100% inaccurate?  

2) How does a company get their domain off Microsoft's inaccurate spam block list?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-14*

I appreciate you guys getting back to me.  I am a bit slow getting back, but I did do quite a bit of research based on your suggestions.    

At one point, I did find multiple SPF records.  I got that fixed, but it did not clear the problem.  I waited a few days, and still no improvement.  

We are sending these emails through a third party SMTP service.  They require two DKIM records, which we have.  

We do not have a DMARC record.  I will create one.  Any tips on keeping the spammers from blasting the mailto addresses for rua and ruf tags?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-12*

Hi @Michael Adams      

What's the quarantine reason for these emails? Like Andy suggest above, please check the configuration of their SPF and DMARC records.     

Like the issue in this thread: Emails getting stuck in quarantine, multiple SPFs, etc...    

Here is the official document introduces about How EOP works, you could check the configuration for your connection filter and anti-malware as well.    

If you have checked all the configurations properly, the issue still exists, we could consider feedback this issue to the o365 support.    

Ways to contact support for business products - Admin Help    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-09*

Usually messages are categorized as junk or phish if they fail to pass to necessary auth tests.  

If an org was on a block list, the message would be rejected, not simply quarantined.  

So for the customer that set you a test message,  

Can you post the headers of the message with the personal information removed?  

Look up their domain here:  

https://mxtoolbox.com/  

What does it show for DMARC?  

How about for SPF?  

https://mxtoolbox.com/spf.aspx
