---
title: "Active directory question begginer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1073112/active-directory-question-begginer
question_id: 1073112
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active directory question begginer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1073112/active-directory-question-begginer (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I am a beginner and I have some questions about the active directory  

-  Could you explain me what is a domain name in an Active directory. Is it the name of the base the active directory ? Why is it necessary to have a domain name and what is the use of it?  

Example  

Kira.net

2) what is the différence between CN and OU?  

I see two different examples on the internet  

Example 1 cn= patrick cn=users: DC=Kira DC=net  

Example 2 cn= patrick or=users: DC=Kira DC=net

3)  

An active directory database contains all the users, groups and computers of a company.  

My company is called X, in Paris.  

It will have an active directory database with a domain name.  

If I have the same company in New York, will it use the same active directory database and the same domain name for its users?

Thank you very much.

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2022-11-02*

Hi @Vinc Mouss       

1) A Domain by definition is:    

An Active Directory domain is a collection of objects within a Microsoft Active Directory network. An object can be a single user or a group or it can be a hardware component, such as a computer or printer. Each domain holds a database containing object identity information.    

Cited from https://www.techtarget.com/searchwindowsserver/definition/Active-Directory-domain-AD-domain#:~:text=An%20Active%20Directory%20domain%20is,database%20containing%20object%20identity%20information.    

2) The CN is:    

In Active Directory the acronym "cn" only stands for "Common Name". But there is a canonicalName attribute in Active Directory, which is different from the CNAME in DNS.    

Cited from https://social.technet.microsoft.com/Forums/ie/en-US/bacb9ca7-0c16-457d-85dc-439a6f9adb4d/what-does-quotcnquot-stand-for?forum=winserverDS#:~:text=In%20Active%20Directory%20the%20acronym,from%20the%20CNAME%20in%20DNS.    

Example 2 would be correct if you are using OU and not "or". If a user is located under kira.net (domain) > Users (OU) then their Distinguished Name (DN) would be:    

CN=Patrick,OU=Users,DC=Kira,DC=net    

3) You can have it all under the same domain (kira.net). You can separate this by having different OUs (Organizational Units) for the locations:    

kira.net (domain) > Users (OU) > Paris (OU)    

AND    

kira.net (domain) > Users (OU) > New York (OU)    

Note: OUs are not used in Azure AD (AAD/365/Cloud), so when you are architecting your environment be aware of this if you will be using Microsoft Azure (Cloud).    

-------------------------------------    

If this is helpful please accept answer.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-03*

Active Directory (AD) is a directory service that Microsoft developed for Windows domain networks. It is included in most Windows Server operating systems as a set of processes and services. Active Directory serves as a central location for network administration and security. Active Directory (AD) is a directory service that Microsoft developed for Windows domain networks. It is included in most Windows Server operating systems as a set of processes and services. Active Directory serves as a central location for network administration and security.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-02*

Something here could help.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/assigning-domain-names    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
