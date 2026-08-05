---
title: "Exchange Powershell Showing a Calendar Reviewer as a Delegate. Why??"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/401231/exchange-powershell-showing-a-calendar-reviewer-as
question_id: 401231
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange Powershell Showing a Calendar Reviewer as a Delegate. Why??

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/401231/exchange-powershell-showing-a-calendar-reviewer-as (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am setting some Exchange permissions for PA's and their charges.    

I had a user who WAS a  calendar Editor - Delegate for a charge.    

During some housekeeping, I had to remove the user from the charge's calendar.    

I was then asked to re-add them, but as a Reviewer    

Now, the user is showing as a Reviewer with Delegate rights????    

    

How is this. I thought ONLY Editors can be Delegates?    

I have done the same with other users, and when re-added as a Reviewer, they are NOT a Delegate!!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-20*

Hi @Lee, Roly   ,    

By default the Remove-MailboxFolderPermission cmdlet will also remove the SharingPermissionFlags:    

    

So as michev said, you could use the parameter to reset the flags.    

    

```
Remove-MailboxFolderPermission -Identity "User:\Calendar" -ResetDelegateUserCollection
```

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-19*

Probably something got borked on the backend, you can run the Remove-MailboxFolderPermission cmdlet with the -ResetDelegateUserCollection flag to reset this.
