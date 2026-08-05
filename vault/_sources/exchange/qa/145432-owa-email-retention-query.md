---
title: "OWA email retention query"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/145432/owa-email-retention-query
question_id: 145432
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# OWA email retention query

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/145432/owa-email-retention-query (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

About 2 years ago I converted an inbox to a shared mailbox.  If I log into that account using the Open another Mailbox feature in OWA I can see back as far as 2013.  However in my own inbox in OWA I can only see 2 years.  I have been searching around and getting many different answers so I am hoping someone can point me to something definitive on how long emails are kept for in Office365.    

I am not even talking about deleted files at this point, thats a whole different world I need to look into at some point.  

Thank you,

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-02*

Hi @Wayne Singh  ,    

However in my own inbox in OWA I can only see 2 years.    

According to the following official document, there is a default retention policy named "Default 2 years move to archive" in the Default MRM Policy, and this policy is automatically applied to new users in Exchange Online:    

Default Retention Policy in Exchange Online and Exchange Server    

    

That being said, agree with michev that probably your mailbox is having online archive enabled.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-30*

You most likely have an Online Archive enabled for your own mailbox, look at the bottom of the left nav pane.
