---
title: "User on exchange online did not send an email but somene received an email - is it hacked ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2132592/user-on-exchange-online-did-not-send-an-email-but
question_id: 2132592
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# User on exchange online did not send an email but somene received an email - is it hacked ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2132592/user-on-exchange-online-did-not-send-an-email-but (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

In an enterprise exchange online environment, user A received an email from user B.

User B says never sent it and i system admin checked user B's sent box in outlook and i do not see that email in sent 

I also did a message trace on exchange admin centre , i see a trace of user B sending email to User A.

I also have mail filtering tool and i dont see a trace there either.

Is it a spam or phish or a genuine hack ?  how do i find out ?  I have changed password of user B for now.  what other steps should i take to make sure environment is safe

Thanks in advance 

Alex

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-08*

user do not have send as permission, I logged a support call with Microsoft and they said it is safe to ignore

Thanks for response

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-08*

Hello,

To confirm if the email was hacked, you can check for the ip address of the users sign in.

Go to the identity admin center.

Go to users > All users> select the affected user account.

Then click on sign in logs, this gives you the information of the location where the users account has been signed in from.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-18*

Hello, @Alex Rabbi,

Welcome to the Microsoft Q&A platform!

According to your description , User A receives an email from User B without User B's knowledge, and email tracking finds the email but it is not visible in User B's sent mailbox. 

After my test, it is probably because a user has the “Send As” permission of user B, so it can send emails to user A with user B's email address. 

The following figure shows the description of the “Send As” permission for your reference.

Therefore, before suspecting whether the email is spam, phishing or a real hacker attack, please check whether other users have the “Send As” privilege of user B in the following two ways.

1.Use the EAC to manage permissions according to the screenshot below. If other users do have “Send As” or higher privileges for user B, you can remove them as needed.

2.Use Exchange Online PowerShell to check or remove users who you do not want to assign "Send As" permission.

```
Get-RecipientPermission -Identity ******@domain.com | Where-Object {$_.AccessRights -contains "SendAs"}
```

```
Remove-RecipientPermission -Identity user1@example.com -Trustee user2@example.com -AccessRights SendAs
```

For more guidance, please click on https://learn.microsoft.com/en-us/exchange/recipients-in-exchange-online/manage-permissions-for-recipients#use-the-eac-to-assign-permissions-to-individual-mailboxes for reference.

Please try to check as above, if you can rule out the possibility of “Send As” privilege or if there is something else you don't understand, feel free to post back. 

If the answer is helpful please click on ACCEPT ANSWER as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.

Best Wishes,

Alex Zhang
