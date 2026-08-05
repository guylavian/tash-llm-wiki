---
title: "ACTIVE DIRECTORY After create PSO the password expired and i cant renew the password"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1284935/active-directory-after-create-pso-the-password-exp
question_id: 1284935
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# ACTIVE DIRECTORY After create PSO the password expired and i cant renew the password

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1284935/active-directory-after-create-pso-the-password-exp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

As part of password security for certain services, I opted to set up a PSO.

After having created a PSO this one is well functional at the level of a group.

But as soon as the password expires, it is impossible for me to register a new one each time it tells me that the password expires and it is renewed.

I have to go through the active directory to change the user password.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-02*

Good morning

I add in addition that it does not come from the PSO.

When I create a user by checking the option, the user must change the password on the first connection, it gives me the same problem.

Impossible to modify it, it keeps coming back, do you have an idea?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-19*

Hello,

Thank you for your reply.

Clearly, the user cannot change his password from his client.

I have provided you with screenshots.

The first we see that we have to change the password so the pso applies correctly, the second I change the password then I go to confirm and that's where the error appears (3rd screenshot afterchangepassword) logon failur the specified account password has expired.

I have to go to the ADUC to reset the password, which is extremely restrictive.

Thanks

Error.png

afterchangepassword.png

before.png

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-05-16*

Hello StarlRW,

Thank you for posting in our Q&A forum.  

As my understanding, one PSO is Password Setting Object, we can create one or more PSOs in AD domain, then set different password policy within PSO than domain password policy.  

If you want to set different password policy than domain password policy to user or user group, we can use Password Settings Object (PSO) which is an Active Directory object which contains a password strategy.  

https://rdr-it.com/en/active-directory-password-policy-pso/  

https://www.windows-active-directory.com/pso-ad-administrative-center.html  

If user applies password policy within PSO and the user password is expired, the user should change his/her password on his/her client, or his/her administrator can reset password for him or her in ADUC.  

Based on "it is impossible for me to register a new one each time it tells me that the password expires and it is renewed.",   

would you please tell us how you did it? You can change user password this way,right?  

Hope the information above is helpful. If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
