---
title: "Exchange Online Modern Authentication and Outlook"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/380509/exchange-online-modern-authentication-and-outlook
question_id: 380509
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Online Modern Authentication and Outlook

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/380509/exchange-online-modern-authentication-and-outlook (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

In our hybrid configuration UPN is not equal to Primary SMTP address. Alternate Login ID is not used. Outlook for Microsoft 365 installed on workstations. All users are synced, and mailboxes migrated (except for some shared mailboxes) to EXO.  

I need to enable Modern Authentication for Exchange Online. Hybrid Modern Authentication is not needed.  

Does anyone know how process of switching from Basic to Modern authentication will look like for end-users when UPN differs from Email? Will they have to enter “Email -> UPN -> password” sequence or just “UPN -> password” when the Modern Auth pop-up window shows in Outlook?  

Thanks!

## Answer (community) — community member

*upvotes: 1 · updated: 2021-05-05*

Hi @Anatoliy A   ,    

Even if a pop-up window prompts the user to enter the UPN and password, if the user can successfully log in to the mailbox and use it after entering the credentials only once, then I don't think you need to worry about this behavior.    

But as Andy mentioned, alternate login ID is also an option. And if the environment permits in the future, UPN and primary email address are the same will be the best choice.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-04*

Hi anonymous userDavid , @Lucas Liu-MSFT      

Thank you for your replies!    

Yes, I know that in the end it should be UPN -> password. My main concern here is when I turn on Modern Authentication, Outlook will ask users for credentials, and I thought that it may want to re-discover user’s mailbox again. For this purpose Outlook will ask for Email first and when mailbox is discovered, user will need to enter UPN -> password for authentication. So this re-authentication flow is unclear for me.    

Unfortunately, organization has lots of dependencies on-prem and UPN change was rejected from the start.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-04*

Hi @Anatoliy A   ,    

I agree with what Andy said. We should log in to the mailbox in the "UPN -> Password".    

We could view the UPN of Exchange online mailbox in Microsoft 365 admin center. You can check the "Username" attribute in Active user.     

According to my test, the UPN and email address of a test mailbox both are ******@domian.onmicrosoft.com, when I changed the UserName of the mailbox from ******@domian.onmicrosoft.com to "AAA1-1@keyman  .onmicrosoft.com", and keep email address unchanged. Then I log in to mailbox by using "AAA@keyman  .onmicrosoft.com" will get an error.This also shows that we logged in through UPN, not an email address.    

In addtion, Microsoft's recommended best practices are to match UPN to primary SMTP address. This will better manage user mailboxes and will not cause user confusion.    

    

    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-03*

For any authentication, it will always be UPN > Password.
