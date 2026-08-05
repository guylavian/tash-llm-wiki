---
title: "Best Practice to prevent Active Directory Enumeration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/929688/best-practice-to-prevent-active-directory-enumerat
question_id: 929688
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Best Practice to prevent Active Directory Enumeration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/929688/best-practice-to-prevent-active-directory-enumerat (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I trying to prevent AD enumeration via LDAP calls and net commands (any other method if possible).    

Every user in an AD environment can view all sensitive groups like "Domain Admins" via net group command.    

I've searched the network for a suitable solution to prevent it. I came across "https://www.adamcouch.co.uk/disable-domain-user-enumeration/". & "https://social.technet.microsoft.com/wiki/contents/articles/28241.controlling-object-visibility-deny-list-content.aspx"    

For testing purposes, I've created a group named "Denied-Enumeration", from ADUC, in the domain root security ACL I ticked the deny "List contents", after few tests I ticked the deny on the "Read" permission for the group.    

The 3 Methods to enumerate domain Admins were:    

Dsquery: dsquery * -filter “(&(objectclass=group)(samaccountname=Domain Admins))” -attr name samaccountname member    

PowerShell: ([ADSISearcher]”(distinguishedname=CN=domain admins,OU=Groups,DC=mic,DC=com)”).FindOne().Properties.member    

net.exe: net group “domain admins” /domain    

(All ran from PowerShell)    

Denying "List Contents" only prevented enumeration from "net group" but the denying "Full control" or "Read" prevented all 3 commands from producing results.    

My questions are:    

-  Could any issues arise from denying "Full Control" or "Read" permissions to the majority of users (No built-in & no admins) on the domain root ACL (mic.com) tree from ADUC? if yes, what are the issues?    

-  Why Microsoft default permissions are enabling AD objects enumeration?    

-  Is there another best practice to prevent user enumeration in AD environment?

## Answer (community) — Q&A User [Mvp]

*upvotes: 2 · updated: 2022-07-17*

Hi MicComMan,      

I would say that read all permissions for users is a bad idea.      

This may entice users to look around areas of your server than they should be.      

If you’re planning on moving more of your resources to the cloud/Azure then you would be provided some big advantages.      

Moving away from your on-prem servers and depending more on Azure Active Directory, deploying 100% Multi Factor Authentication, and deploying Defender for Identity to track anomalous user activity would be recommended.    

Also if you think beyond just user access, if you’re deploying Defender for endpoint on all your workstations you’ll have much better insight and control over user activities.    

I would also strongly encourage you to create ‘honeytoken user accounts’ and alert on any access to these accounts. The use of ‘active defences’ or ‘deception’ tactics are a great way to catch enumeration related activity.    

In addition you can use Azure Arc to extend the reach of Azure policy controls over all of your servers, and use Azure Purview to control access to sensitive data.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-07-16*

Could any issues arise from denying "Full Control" or "Read" permissions to the majority of users (No built-in & no admins) on the domain root ACL (mic.com) tree from ADUC? if yes, what are the issues?    

Maybe, if you are assigning the permissions to a group, then you have the ability to remove\change permissions if any issues are found, just make sure that you don't add any of your admins or service account to the group.  By using Deny Full Control, rather than blocking specific attributes, you are preventing a user from reading the attributes on their own user object, which could cause problems.  As to what the issues will be it's difficult to tell, as it will depend on what applications and services you are running in your environment and what access they require to the AD.  As always you will need to test if these changes cause any issues.    

Why Microsoft default permissions are enabling AD objects enumeration?    

One of the original intents for AD was to provide an open directory service which could be used to store and share information within organizations, unfortunately 20+ years later this openness can be used by bad actors to compromise the environment.  The other possible reason, by providing a more open permission set, it simplified the adoption of Active Directory, back in the day when NetWare was king but more complicated to implement.    

Is there another best practice to prevent user enumeration in AD environment?    

I don't believe Microsoft have published anything specifically, their security models are based around delegation and tiering of roles, rather than preventing users from reading objects or attributes.    

One thing to bear in mind with this approach, it may not work as you expects, as the deny permissions set at the root of the domain, maybe not be enforced lower down the OU structure.  As an explicit allow will take precedence over an inherited deny permission.  The default permissions for an OU has authenticated user List and Read.    

    

Also with groups and users protected by the SDProp process, permissions set on root will not be applied to these objects, you will need to set these permissions on the AdminSDHolder, but update these permissions with caution, as there is potential to lock yourself out of the AD.    

    

With AD you have the ability to change the permissions to whatever your want and define your own access model, however, MS will only test new features and updates based on the default permissions.  As with any changes, document the changes, so the next person to manage the environment know what has been changed.     

Gary.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-07-16*

You can follow along here.    

https://social.technet.microsoft.com/wiki/contents/articles/6130.how-to-hide-objects-in-active-directory-from-specific-users.aspx    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
