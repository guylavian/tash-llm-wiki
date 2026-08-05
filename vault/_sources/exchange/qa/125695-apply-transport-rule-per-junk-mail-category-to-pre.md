---
title: "Apply transport rule per Junk mail category to prepend subject line"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/125695/apply-transport-rule-per-junk-mail-category-to-pre
question_id: 125695
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Apply transport rule per Junk mail category to prepend subject line

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/125695/apply-transport-rule-per-junk-mail-category-to-pre (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange Online Protection adds anti-spam message headers as described here: https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spam-message-headers?view=o365-worldwide    

I tried to create transport rules to prepend subject lines accordingly. So if a mail was filtered as category SPM or HSPM, subject should be prepended with "[SPAM]"; if it was filtered as category "SPOOF" it should be prepended with "[SPOOF]" etc.    

My test message contains "CAT:HSPM" in "X-Forefront-Antispam-Report" header:    

    

Accordingly this transport rule should apply to it:    

    

But this is not the case. The transport rule is not applied. But other transport rules (with "higher" priority, so more down in the list) are correctly applied.    

Is the Forefront header added at a later stage? What am I doing wrong?

## Answer (community) — community member

*upvotes: 1 · updated: 2020-10-15*

@Stephan van Helden      

This picture below may be useful to you(From this article: Exchange Online Protection overview):    

    

The mail flow rule works before content filtering (also known as Anti-spam)    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2020-10-14*

I tested this and see the same results as you. This is expected from what I can tell. The rules are applied before the anti-spam checks.  

This doc confirms this:

****If you want to mark specific messages as spam before they're even scanned by spam filtering,** or mark messages so they'll skip spam filtering, you can create mail flow rules (also known as transport rules)** to identify the messages and set the spam confidence level (SCL). For more information about the SCL, see Spam confidence level (SCL) in EOP.

https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/use-mail-flow-rules-to-set-the-spam-confidence-level-scl-in-messages?view=o365-worldwide

So I think you will have to use the anti-spam to set this as I mentioned above.  

https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/configure-your-spam-filter-policies?view=o365-worldwide#use-the-security--compliance-center-to-create-anti-spam-policies

Hope this helps!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2020-10-14*

Instead of creating a new transport rule, why not set this up in the anti-spam policy itself:    

https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/configure-your-spam-filter-policies?view=o365-worldwide#use-the-security--compliance-center-to-create-anti-spam-policies

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-15*

anonymous userDavid  Thanks, but if I understand this article correctly, this doesn't help:    

https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/how-policies-and-protections-are-combined?view=o365-worldwide    

    

The anti-spam policy has only one field for the text to prepend. But I wanted to preprend text depending on the spam category.    

I could define multiple policies (one for Spam, one for Phishing, one for Bulk), but per this article, only the first of these would be applied.
