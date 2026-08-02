---
title: "Access denied issue in Active directory Ldap"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/805459/access-denied-issue-in-active-directory-ldap
question_id: 805459
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-csharp", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Access denied issue in Active directory Ldap

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/805459/access-denied-issue-in-active-directory-ldap (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I am creating a user in an active directory with lap connection (c#)  from server 1 OU to another server OU with User (Domain user) having permission to create / set password , created through delegate wizard.   

e.g.  

  PrincipalContext newContext = new PrincipalContext(ContextType.Domain,  "LdapPath:389", oupath, ContextOptions.SimpleBind, username, password);  

UserPrincipal newUserPricipal = new UserPrincipal(newContext, Convert.ToString(result.Properties["SAMAccountName"][0]), "somerandompassword", true);       

                     newUserPricipal.Save();

User details with all properties get synced but set password throws Access denied exception.  

I cannot make user administrator or domain admin as per policy. This worked with windows server 2012 r2. But not in windows server 2016. Why?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-14*

Hi there,  

The specific privileges required by the user to connect to LDAP are "Bind" and "Read" which the user can obtain by being a member of the Active Directory's built-in administrators group. Try the same method with an Admin user and see if that sorts the issue.  

The other possible reason might be the credentials provided to access the Active Directory or LDAP tree might have included an expired password. To verify the account credentials, log on to the Domain Controller or LDAP server using the Remote Desktop Protocol (RDP) and verify your credentials.  

--If the reply is helpful, please Upvote and Accept it as an answer–
