---
title: "OWA timeout (5 mins instead 6 hours by default)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1155380/owa-timeout-5-mins-instead-6-hours-by-default
question_id: 1155380
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# OWA timeout (5 mins instead 6 hours by default)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1155380/owa-timeout-5-mins-instead-6-hours-by-default (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everybody! :-) Need some help with OWA timeout - I changed the settings but still no effect:    
------before changes----------    
C:\Windows\system32>Get-OrganizationConfig |Fl Activity*    
ActivityBasedAuthenticationTimeoutEnabled                 : True    
ActivityBasedAuthenticationTimeoutInterval                : 06:00:00    
ActivityBasedAuthenticationTimeoutWithSingleSignOnEnabled : True    

Set-OrganizationConfig -ActivityBasedAuthenticationTimeoutInterval 00:05:00    

after changes-------------------    

Get-OrganizationConfig |Fl Activity*    

ActivityBasedAuthenticationTimeoutEnabled                 : True    

ActivityBasedAuthenticationTimeoutInterval                : 00:05:00    

ActivityBasedAuthenticationTimeoutWithSingleSignOnEnabled : True    

But after all of these changes if I go to the mailbox through OWA, after 5 minutes I am not thrown out of the session (as it should be). Tel me please, what else shoud I check? Thank you.

## Answers

_No answers on this thread._
