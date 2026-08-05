---
title: "Cached Exchange Mode GPO won't set to 1 month"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/744844/cached-exchange-mode-gpo-wont-set-to-1-month
question_id: 744844
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
---
# Cached Exchange Mode GPO won't set to 1 month

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/744844/cached-exchange-mode-gpo-wont-set-to-1-month (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are on Exchange Online and working on efficiency, so are trying to implement Exchange Cached Mode. We need to set the cached sync settings to 1 month, but when we try it sets to "All" instead.    

Is this an error in the admx? Is there another way to get it to actually get it to cache for 1 month?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-19*

You can try setting the cached sync settings to 1 month by editing the registry key. To do this, open the registry editor (regedit) and navigate to the following registry key:

HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Outlook\Cached Mode

Once you are in the registry key, create a new DWORD (32-bit) value and name it “SyncWindow”. Set the value to 1 to enable a one-month sync window. After making the changes, restart Outlook and the sync window should now be set to one month.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-22*

Hi @Mark R      

Did you select the One month for cached exchange mode sync settings for profiles?    

    

Then you can see this:    

    

And the following registry data is used by Outlook:    

Key: HKEY_CURRENT_USER\Software\Policies\Microsoft\Office\16.0\Outlook\Cached Mode    

DWORD: SyncWindowSetting    

Value: integer value (Decimal) specifying the number of months (use only the following values)    

0 = All (whole mailbox)    

1 = 1 month of email items    

3 = 3 months of email items    

6 = 6 months of email items    

12 = 12 months of email items    

24 = 24 months of email items    

Details: https://learn.microsoft.com/en-US/outlook/troubleshoot/user-interface/only-subset-items-synchronized#feature-administration-through-group-policy    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
