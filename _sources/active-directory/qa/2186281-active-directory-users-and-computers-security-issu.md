---
title: "Active Directory Users and Computers security issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2186281/active-directory-users-and-computers-security-issu
question_id: 2186281
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Active Directory Users and Computers security issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2186281/active-directory-users-and-computers-security-issu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When I go to the user properties in AD and I click on the security tab I see lots of unknown accounts followed by a bunch of numbers. 

For example: Account Unknown(S-1-5-21-17288237615-122927721-11772389

I understand that these may be permissions for services or applications that are no longer in use. But when I try to remove these unknown accounts. I get an error: You can't remove Account Unknown because this object is inheriting permissions from its parent.

I have 2 questions: 

How can I find out the parent for these objects?

Is it okay to remove inheritance so I can remove these unknown accounts and then enable inheritance again? 

Thanks in advance for you help.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-19*

Hi Karim Boroumand1,

Thank you for posting in the Microsoft Community Forums.

In Active Directory, you may encounter some unknown accounts with SIDs in the format "S-1-5-21-xxxxxxx-xxxxxxx-xxxxxxx" when you browse through user properties and click on the Security tab. These unknown accounts typically fall into one of the following categories:

-  Deleted or Moved Objects: You might see some unknown accounts that represent objects that have been deleted or moved. These objects' SIDs exist in permission assignments but do not correspond to existing users or groups. This could occur because the object was deleted but permissions were not updated or because the object was moved to another location, but permissions were not updated accordingly.

-  External Objects: Sometimes, you may encounter unknown accounts with SIDs from other domains or external systems that your current domain cannot resolve. These external accounts often appear in Active Directory as SID values.

-  System Built-in Accounts: Certain system built-in accounts might also appear as unknown accounts, especially in special circumstances such as domain controller upgrades or migrations.

It is not recommended that you make a deletion of this form of object, considering the circumstances of your environment, there are many unknown accounts, which may be followed by continued use.

Best regards

Neuvi Jiang
