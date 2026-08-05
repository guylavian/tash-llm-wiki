---
title: "Active Directory account password expiry email notification to end users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/434255/active-directory-account-password-expiry-email-not
question_id: 434255
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory account password expiry email notification to end users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/434255/active-directory-account-password-expiry-email-not (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Friends,  

Please help me to configure Windows Active Directory account password expiry email notification to end users.  

Regards  

Amit Kumar

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-15*

You can use the below powershell script and schedule it via windows task scheduler, this script will find the users whose password is going to expire in next 15 days and send them a notification email to change the password.    

https://www.magicpowershell.com/2022/10/password-expiry-reminder-email-alert.html

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-14*

Hi,  

Welcome to share here!  

To configure Windows Active Directory account password expiry email notification to end users, we need to run a script.  

Below is a script that can identify Active Directory accounts that are about to expire and sends a mail notification to the end users. It optionally allows sending the applied Password Policy settings which make easier for users to choose a new password that meets the company requirements.  

If you don't want to run the script manually, you may consider running it regularly by configure a schedule task.  

For more details, you can refer to the following links:  

Notify Active Directory Users about Password Expiry using PowerShell  

How to Setup a Password Expiration Notification Email Solution
