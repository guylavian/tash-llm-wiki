---
title: "exchange address policies - edit the default policy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/222168/exchange-address-policies-edit-the-default-policy
question_id: 222168
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# exchange address policies - edit the default policy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/222168/exchange-address-policies-edit-the-default-policy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I would like to either configure a new address policy for migrated users or edit the default policy - any assistance much appreciated.  

Our exchange 2013 address policies use a custom policy with priority 3 for our domain, and that applies to local users with exchange mailboxes, resource mailboxes and mail-enabled groups.  

When a user is migrated to office 365 however, they appear in Exchange 2013 (full-hybrid) as "office 365" mailbox type and that is no longer matched to that policy above and instead, the "Default Policy" applies. The problem is that policy is no in use or accurate and contains invalid domain etc.  

How can I edit the default policy? Is this a good practice?  

Set-EmailAddressPolicy -Identity “Default Policy” -EnabledEmailAddressTemplates SMTP:%******@ourcorrectdomain.com  

Alternatively, how can I create a new policy with narrow scope to apply only to migrated users to office 365? I cannot use OU :(

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-07*

Thanks for that,

I tried creating a separate policy, but could not get the syntax right - any idea what I am doing wrong?

New-EmailAddressPolicy -Name "MigratedUsers to o365" –RecipientFilter "(RecipientType –eq 'MailUser') -and (ExternalEmailAddress -like '*ourcorrectdomain.mail.onmicrosoft.com')" -EnabledEmailAddressTemplates "SMTP:%******@ourcorrectdomain.com" -Priority 1

Cannot bind parameter 'RecipientFilter' to the target. Exception setting "RecipientFilter": "Invalid filter syntax.  

For a description of the filter parameter syntax see the command help.  

"(RecipientType -eq 'MailUser') -and (ExternalEmailAddress -like '*ourcorrectdomain.mail.onmicrosoft.com')" at position 17."  

-  CategoryInfo : WriteError: (:) [New-EmailAddressPolicy], ParameterBindingException  

-  FullyQualifiedErrorId : ParameterBindingFailed,Microsoft.Exchange.Management.SystemConfigurationTasks.NewEmailAd  

dressPolicy

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-07*

it would have been ideal to be able to create a policy that only applies to migrated users (mailbox type Office 365) - the default policy applies to all so that will change all to .com primary and we appear to have users with .co.uk primary etc.  

Is that at all possible?
