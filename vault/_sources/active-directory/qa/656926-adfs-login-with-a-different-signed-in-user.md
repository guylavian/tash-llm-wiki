---
title: "ADFS Login with a different signed in user"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/656926/adfs-login-with-a-different-signed-in-user
question_id: 656926
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Login with a different signed in user

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/656926/adfs-login-with-a-different-signed-in-user (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We installed ADFS on-premise and Active Directory and successfully configured it on Auth0 and log in.  

However, we faced a strange behavior as the following:  

```
Log in with a user enabled ADFS ex: ******@xxx.com
Logout from the application ‘not federated logout to keep user signed in for other application he uses’
Attempt to login from the application with a new ADFS user from the same domain ex: ******@xxx.com or even a user that doesn’t exist on ADFS AD.
Auth0 doesn’t ask the user for a password and directly sign in the user but the Id token is for the user1, not 2.
```

The above scenario doesn’t happen with other enterprise connections we tried it with Azure Active Directory. with Azure AD second user is prompted to enter the password and Auth0 replied with the right Id token.  

Did anyone face that with ADFS?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-12-09*

I think there is a confusion here. There's no such a thing as a multi user SSO from the user's perspective. SSO as in Single Sign On is the principle that we are going to use the user's credentials of the current OS session to authenticate to other applications. In other words it allows the user to access multiple application without typing her/his/their credentials. And the OS only has one user per session.  

What you are describing has nothing to do with SSO. It kinda is the opposite. You want to prompt users. In that context, it is going to conflict with the fact that ADFS will try (and often will manage to perform) SSO if conditions are met. Now you can create the condition for SSO to fail (incorrect configuration or by disabling Windows Integrated Authentication).  

Also, if the issue is specific to an application triggering the Single Log Out flow, it will depends on whether or not the endpoint was 1. set properly in the ADFS relying party trust and 2. implemented by the application.   

It might also work differently if you involve another claim provider trust. You mention Auth0 here but you don't tell if that's a claim provider trust or another type of integration.   

A diagram of your setup might help us to see clearer.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-09*

As we faced that unexpected behavior. We managed the solution by editing the Authentication Policies, Per Relying Party Trust for (Auth0 rely only) to force users to provide their credentials every login.  

-  On the multi-level nested list under Authentication Policies, click Per Relying Party Trust.  

-  Right-click the relying party you’ve just created (e.g., Talentlms) and click Edit Custom Primary Authentication.  

-  Go to the Primary tab, check Users are required to provide credentials each time at sign in, and click OK.  

It seems that ADFS doesn't manage multi SSO users.
