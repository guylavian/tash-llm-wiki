---
title: "How do you switch users easily in active directory?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1573122/how-do-you-switch-users-easily-in-active-directory
question_id: 1573122
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How do you switch users easily in active directory?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1573122/how-do-you-switch-users-easily-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have two children trying to log into their school elearning page using the same computer and it automatically saves the first user in active directory.  When I try to log out so the 2nd user can log in to do their work, it automatically logs the first user back in.  How do I change this so that I can switch users easily?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-03-07*

Hello Tracy Mehling,

Thank you for posting in Q&A forum.

In the Windows operating system, when multiple users need to log in to their respective school e-learning pages on the same computer, and you encounter a situation where you cannot easily switch users, you can take the following steps to solve the problem:

Group Policy Settings:

You can use Administrator account login to manage user login settings through the Group Policy Editor to ensure that a specific user is not automatically logged in. In the Local Group Policy Editor, navigate to Computer Configuration -> Windows Settings -> Security Settings -> Local Policies -> Security Options, find Interactive Logon: Don't Show Last Logon Username and enable the policy so that you need to manually enter your username every time you log in.

Note that it is a good idea to make a backup before changing the Group Policy so that you can revert to the previous state in the event of a problem or adverse impact.

Clear your cache or cookies:

School e-learning pages may have cookies or cached information that causes the previous user's session to be automatically loaded even if the user is switched. Before each child logs in, make sure to clear the browser's cache and cookies, or use private browsing mode.

Multiple browser profiles:

If the school's e-learning page supports multi-user mode, different user profiles can be created and used in a browser (e.g. Chrome, Firefox, etc.), so that each child can have their own browser environment without affecting each other.

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-24*

Hi Tracy,  

If you want to use Edge for both your children then you can use the profile functionality in Edge. How to add an additional Profile is explained here:  

https://www.microsoft.com/en-us/edge/learning-center/how-to-add-new-profiles?form=MA13I2  

Using two different browsers would also work.  

If you want to fully switch the user including also separating applications you need to create an additional user account in Windows.   

Here is explained how that works:  

https://support.microsoft.com/en-us/windows/add-or-remove-accounts-on-your-pc-104dc19f-6430-4b49-6a2b-e4dbd1dcdf32#:~:text=Select%20Start%20%3E%20Settings%20%3E%20Accounts%20%3E,information%20and%20follow%20the%20prompts.
