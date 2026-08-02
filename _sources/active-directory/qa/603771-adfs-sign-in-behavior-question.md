---
title: "ADFS sign-in behavior question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/603771/adfs-sign-in-behavior-question
question_id: 603771
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Volunteer Moderator"]
---
# ADFS sign-in behavior question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/603771/adfs-sign-in-behavior-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have some question about sign-in behavior on ADFS and would like to know someone can clarify me here.  

I understand that ADFS web applications shares the same session cookie and allows SSO under the same browser session. We have few applications in our ADFS farms, some with MFA requirement and some don't. When signing-in on one application without MFA requirement, if I launch other applications (without MFA requirement) in the same browser, authentication will not be needed and that is what is expected. If I sign-in on one applications with MFA requirement, other applications without MFA requirement will be signing in automatically due to the same reason. Applications with MFA requirement will need to be sign-in. I guess this is also normal because of the extra MFA requirement. However, one particular application with MFA requirement will sign-in automatically (unlike the other). I guessed there is some special setting control that behavior. Does anyone know what is it?  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-26*

Thanks for the feedback.  

The things that I am not certain is how some ADFS applications (with MFA requirement) can share the sign-in credential from the previously login-in but not the others. Here is a example.  

3 ADFS applications all require MFA in the access policy. A, B and C  

When users sign-in to application A successfully, launching application B will automatically sign-in in the same browser.  

When users sing-in to application B successfully, launching application C will not sign-in automatically in the same browser. Users will need to enter their credential and MFA.  

So what settings control these behavior. It looks to me is from the application sides as I compared the ADFS settings for both application (relying party trust) B and C and didn't see anything too obvious.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2021-10-26*

Hello @HK G  ,    

Thanks for reaching out.    

AD FS when it receives an authentication request regardless of SSO configuration. First determines whether or not there is an SSO context (such as a cookie) and then, if MFA is required (such as if the request is coming in from outside) it will assess whether or not the SSO context contains MFA. If not, MFA is prompted.    

Multi-factor authentication can be enabled at an AD FS server, at a relying party, or specified in an authentication request parameter. Check the configurations to see if they are correctly set. If multi-factor authentication is expected but not prompted for it, check if the claim rules in the relying party are correctly set for multi-factor authentication.    

Multi-factor authentication prompt and check the configuration on the AD FS server and the relying party: https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/troubleshoot-ad-fs-sso-issue#check-the-configuration-on-the-ad-fs-server-and-the-relying-party    

For more information about multi-factor authentication in AD FS, see the following articles:    

Under the hood tour on Multi-Factor Authentication in ADFS – Part 1: Policy    

Under the hood tour on Multi-Factor Authentication in ADFS – Part 2: MFA aware Relying Parties    

Multi-factor authentication (MFA) behavior: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/ad-fs-single-sign-on-settings    

Hope this helps.    

------    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
