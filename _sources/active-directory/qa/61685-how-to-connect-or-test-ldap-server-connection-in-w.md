---
title: "How to connect or test ldap server connection in windows through command prompt or Powershell cmdlet without GUI"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/61685/how-to-connect-or-test-ldap-server-connection-in-w
question_id: 61685
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# How to connect or test ldap server connection in windows through command prompt or Powershell cmdlet without GUI

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/61685/how-to-connect-or-test-ldap-server-connection-in-w (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In our company infrastructure we have an ldap directory service hosted. Currently I'm using Ldap tool  to connect to ldap directory service to search for the records.   

Now I have a task to modify few attributes for several users. Manually its taking lot of time to update the attributes. I'm looking to develop a script where i can connect to ldap server and traverse the directory tree  to modify attributes. I have searched in internet for any command in windows to test connectivity to server could not find any command in windows  

Kindly request anyone to help me with any available command in windows or any powershell module to use for ldap connection and search the records like Get-ADUser or Get-ADObject.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2020-08-13*

Hello,  

Try this module S.DS.P. Please test it before!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-10*

This forum aims to provide users with script modification assistance and answers to commands.  

Creating scripts is not within the scope of our technical support. Of course, I am also trying to search for the corresponding information for you.  

BTW we are also very happy to see that other users on the forum can answer your questions.  

Please be patient.
