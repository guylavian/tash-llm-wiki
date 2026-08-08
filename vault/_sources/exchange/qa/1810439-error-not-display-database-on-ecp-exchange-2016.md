---
title: "error not display database on ecp exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1810439/error-not-display-database-on-ecp-exchange-2016
question_id: 1810439
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# error not display database on ecp exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1810439/error-not-display-database-on-ecp-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our system has 2 faulty Exchange servers. I have removed these 2 servers from AD and reinstalled Exchange 2016 on 2 other servers. After installation is complete, we proceed to create a DB for the system. When creating, there is an error message Multiple databases match "MBDB02". Specify a unique value. When I checked, the database was not displayed on ECP. We used Exchange Management Shell (EMS) and the results were as shown. Can anyone help me regarding this case?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-18*

Hi @Anonymous  

I discovered some more of these files, please help me see what they are? Is it dangerous?

C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\ecp\auth\getidtoken.aspx

 

C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\ecp\auth\logon.aspx

 

C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\Current\themes\resources\owafont.aspx

 

C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\ecp\auth\Logout.aspx

 

C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\15.1.2242\themes\resources\aria-down.css.aspx

 

C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\15.1.2242\themes\resources\owafont_es.aspx

 

/aspnet_client/system_web.aspx

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-07-15*

When you’re creating database with the name “MBDB02” its showing an error – multiple databases with similar name.

To resolve this, you can do it with the help of EMS.

1.       Check all the existing databases by running the command. Also verify there are no hidden and disconnected databases.

2.       If you find any database named “MBDB02” remove it.

3.       After that create the database “MBDB02” through EMS.

Refer this link for the same.

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.
