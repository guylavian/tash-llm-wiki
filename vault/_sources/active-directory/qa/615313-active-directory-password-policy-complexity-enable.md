---
title: "Active Directory Password Policy Complexity enable all 4 categories"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/615313/active-directory-password-policy-complexity-enable
question_id: 615313
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Active Directory Password Policy Complexity enable all 4 categories

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/615313/active-directory-password-policy-complexity-enable (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have a requirement from audit to enable all the 4 categories of the password complexity of the Password Policy. We already have complexity enabled so the criteria of the password complexity states that  you need to meet any of the 3 of the 4 categories, i.e Uppercase, lowercase (6 chars min), digits[0-9], special characters. Is there a way that all the 4 categories can be enabled so you can force the user to have all 4 character types in their passwords.  

Thanks.  

Regards,  

Ochen

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-11-04*

Hi @Ochen Ao       

AD only requires three of the complexity requirements to be meet when setting a password.  You will need to purchase a third party password filter\control solution if you want more control over what password can set.  Search for "windows ad password filter" for more options    

https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements    

Gary.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-04*

Hello @Ochen Ao       

In fact the ones you mention are the 4 complexity rules:    

1-Uppercase    

2-Lowercase    

3-Digit    

4-Special character    

Regarding the topic there is a very well explained discussion from different angles about setting and customizing additional complexities here: https://learn.microsoft.com/en-us/answers/questions/118459/custom-change-in-39password-must-meet-complexity-r.html    

Hope this helps with your query,    

---------    

--If the reply is helpful, please Upvote and Accept as answer--
