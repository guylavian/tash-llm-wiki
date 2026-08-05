---
title: "ADFS changepassword portal with MFA"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/358706/adfs-changepassword-portal-with-mfa
question_id: 358706
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS changepassword portal with MFA

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/358706/adfs-changepassword-portal-with-mfa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

I've seen other questions regarding using MFA on the Update Password page (https://adfs.xxx.com/adfs/portal/updatepassword), but none of the answers seemed to understand why there would be need of MFA on this page, as MFA only works if the users is authenticated which would require a valid password and "if the users password was elapsed, they could not use the page anyway, so why use MFA"?  

Well... Where I want the MFA part is directly in the middle of the process of the password change, AFTER the user has authenticated themselves with their current password, but BEFORE the password is actually changed; thereby requiring an MFA authentication in order to change the password.  

So when they click Submit on the updatepassword portal, it should initiate MFA to complete the process.  

How do we set that up?  

If that is not currently possible, how do we set up MFA on the ADFS changepassword website itself, so the page is not even accessible without MFA?   

-  That would also be an acceptable alternative as any use case would require the user knowing their current (or resetted by support) password and it must not have expired.   

-  However this could present a problem when support marks the "must change password" field in AD. That would prevent the users from logging in to the website, if the MFA is positioned in front of the website.  

-  "Must change password" is a usual marking to prevent misuse of a temporary default password.  

The danger with a password change website (whether internal or external) is always that the password can be changed if you just know the login and password. And regardless of having the portal only accessible internally, it would still allow another user (or hacker with network access) to change a users password, if they got wind of that users password and had malicious intent.  

That is why I want MFA active on this portal in order to change a password, even though the portal is only internally accessible.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-04-21*

But therein lies the rub... some legacy applications or portals may not (have built) support for MFA or may be networked internally and simply not set up with MFA, thus only using "simple" AD-login/password.  

Optimally any application/portal should be protected by MFA..  

Also simply by allowing any person to attempt to change passwords can cause users to be locked out of their accounts.  

That is some of the reasons for why it would be nice to have the ADFS change-password page protected by MFA, so you cannot even attempt to change a password without properly authenticating yourself.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2021-04-20*

Unfortunanly I side with your detractors on this topic.  

The password update page cannot be conditionned to pre-authentication in any supported way.  

And even if we could, I don't agree that it would bring a significant value. I am not saying there are no risks, but those risks should be addressed by triggering MFA for the applications the user can access to using ADFS. That way, even if a malcious user would do what you described (which by the way is really a corner case scenario as it generates a ton of logs - granted not everyone looks a the logs), it would not give the attacker an advantage as MFA will have to be performed to access applications.    

Your problem is not the password update page. Your problem is passwords.  

And for that we have alternative solutions (which are not using passwords...). Such as Windows Hello for Business, Azure MFA as a first factor for authentication or certificate based authentication (for the built-in one, but that's extendable with third party MFA that could also be used as a first logon for authentication with ADFS on Windows Server 2019).
