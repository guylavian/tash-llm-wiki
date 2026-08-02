---
title: "Unable to reset a User in Active Directory 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/299266/unable-to-reset-a-user-in-active-directory-2016
question_id: 299266
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Unable to reset a User in Active Directory 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/299266/unable-to-reset-a-user-in-active-directory-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Experts   

I am trying to reset the user account of a user in Active direcory 2016 and there is this error mesage for a particuler user :" The supplied user Buffer is not valid for the Operation"  

Any ideas?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-06*

Can I reset active directory admin password from a local account

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-16*

Hi,  

Yes, Based on my research ,we need to patch the 2016 servers with latest updates.  

Including the kb: KB 4034661  

https://support.microsoft.com/en-us/topic/august-16-2017-kb4034661-os-build-14393-1613-404023e0-df0b-1ceb-af08-7648804fc8ae  

Then check if it can solve the issue.  

Best Regards,

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-05*

Hi,  

Based on my understanding , when you tried to reset the password, the error displayed, right?  

Are there any events logged in the event viewer ?  

Similar case for your reference:  

https://social.technet.microsoft.com/Forums/en-US/dd73e48f-0aea-410e-972d-0748b124b795/unable-to-reset-users-password-supplied-user-buffer-is-not-valid?forum=winserverDS  

Best Regards,
