---
title: "Can't add exchange on prem account to Outlook Mobile App"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1655421/cant-add-exchange-on-prem-account-to-outlook-mobil
question_id: 1655421
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 4
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Can't add exchange on prem account to Outlook Mobile App

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1655421/cant-add-exchange-on-prem-account-to-outlook-mobil (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Are there any known issues with adding an on prem exchange account to the Outlook mobile app? Keep getting error unable to log in. Check username and password. Password is not the issue. I've tried domain\username and username both for the username but neither work.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2024-04-30*

Today 30 April 2024, I random tried to add mail in Outllook Mobile (iOS) , Now it's added successful.  

I think Microsoft had something change in Mobile App and they fixed 

Finally!!!  Yeah!!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-27*

Anyone find a solution to this? I have stopped my android users from updating their phone apps but a few of us updated and boom no mail.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-23*

Hi @Anonymous  ,

Based on your description, I suggest you check whether the user's email address/SMTP and login address/UPN match. Many users have experienced similar problems recently. According to my experience, if the two do not match, it will cause login problems. It is recommended that you follow the following steps to check the user's email address/SMTP and login address/UPN:

-  Check email address/SMTP:

· In the Exchange Admin Center, navigate to Mailbox under Recipient Configuration.

· Find and select the corresponding user mailbox,select "edit".

· In the "Email Address" tab, you can see a list of all the user's email addresses, including the primary SMTP address, which is usually shown in bold and preceded by the "SMTP:" prefix.

-  Check the user login address/UPN:

· In Active Directory Users and Computers (ADUC), find the corresponding user account, right-click and select "Properties".

· In the "Account" tab, you can see the user's login name and domain, which is the user's UPN. A UPN is usually in a format similar to an email address, such as "******@domain.com".

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-20*

Hello everyone,

As an institution, we have been experiencing the same problem since April 15th. 

We have a very large number of Mobile users. Suddenly all users started having problems. We have internal Exchange system. We have done many tests. I want to summarize to help you;

-  Our ActiveSync system is working. We did our tests with Microsoft Remote Connectivity Analyzer site and the results are successful.

-  In general, we use Microsoft Outlook Mobile for all users. Everyone was affected because the problem occurred.

-  The programs currently used do not receive and send mail. Sometimes it works but very rarely. So it is not stable.

-  On some phones I uninstalled the outlook software and reinstalled it. We tried to set up the account, but the user or password is incorrect message comes up. I even see the same error on the Exchange server, even though the user information is correct. 

-  We can set up using the ActiveSync protocol in the built-in mail program on Samsung phones. Mail works without any problems.

Whatever happened, the problem occurred for about 5 days. We ask for help.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-04-19*

Neither do i, Last successfully added Exchange Server mail account  in Outlook Mobile (both IOS, Android) was 12 April 2024. Today I tried to add but it's always authentication failed.
