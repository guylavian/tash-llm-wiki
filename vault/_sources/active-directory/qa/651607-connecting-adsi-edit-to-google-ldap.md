---
title: "Connecting ADSI Edit to Google LDAP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/651607/connecting-adsi-edit-to-google-ldap
question_id: 651607
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Connecting ADSI Edit to Google LDAP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/651607/connecting-adsi-edit-to-google-ldap (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to connect ADSI Edit to Google LDAP.  From what I found, the steps below need to be taken:  

-  Login to G-Suite Admin Console  

-  Apps  

-  LDAP  

-  Add Client -- (ADSI EDIT -- Windows Server 2019)  

-  Specify what the LDAP client can see -- (Entire Domain, Selected OUs, No Access)   

-  Specify clients access level for reading user information..  

-  After adding the LDAP Client in Gsuite, connect the client to the LDAP Service.  

At this point Gsuite generates a Certificate that you can download for use with the LDAP Client.  

This is where I get a little Hazy on the details.  

I believe you can generate credentials to use with the LDAP Client (ADSI Edit) to use to Authenticate to the LDAP Directory.  

Does anyone have any details on the setup through ADSI Edit, or can you provide any additional details that I may have missed in the steps above?   

Thanks in advance for any feedback!  

-NoobEngineer

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-12-04*

Hi @NoobSysEngineer      

Here is a link to the instruction on how to setup LDAP clients to connect to g-suite:     

https://support.google.com/a/answer/9089736    

Gary.
