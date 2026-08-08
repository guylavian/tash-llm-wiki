---
title: "No database on the second Exchange Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1052929/no-database-on-the-second-exchange-server
question_id: 1052929
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# No database on the second Exchange Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1052929/no-database-on-the-second-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!    

After installing the second Exchange Server 2019 CU12 (no issues during installations) I was greatly surprised to see the newly-installed server does not have any mailbox database - I mean there always was a default database on each MB server installed and I remember I had posted the question here on MS forum regarding what is the best practice with this database on second (third..._ Exchange servers.    

    

Maybe I'm missing something here and this behaviour is now by design???    

Regards,    

Michael

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-28*

Hi LiLyLi2-MSFT,    

Thank you for the reply!    

Installation of EXCH1:    

.\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /Mode:Install /Roles:Mailbox /on:"TestENTERPRISE" /EnableErrorReporting /TargetDir:"C:\EXCHANGE" /MdbName:"DB01" /DbFilePath:"C:\EXCHANGE\DATABASES\DB01\DB01.edb" /LogFolderPath:"C:\EXCHANGE\DATABASES\DB01"    

Installation of EXCH2:    

.\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /Mode:Install /Roles:Mailbox /on:"TestENTERPRISE" /EnableErrorReporting /TargetDir:"C:\EXCHANGE" /MdbName:"DB01" /DbFilePath:"C:\EXCHANGE\DATABASES\DB01S\DB01S.edb" /LogFolderPath:"C:\EXCHANGE\DATABASES\DB01S"    

There's only one database on EXCH2 - DB01 - that's being replicated from EXCH1:    

    

By the way, there's one more strange thing in this installation: as you see from above commands I prefer placing DB and log files to C:\EXCHANGE\DATABASES[   ] folder and I have never had any problems with that (I had been using the exact same commands recently when I was installing CU11), but this time the location of log files hasn't changed:    

    

P.S. EXCH2 is up and running flawlessly!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-20*

Hi imamitsingh,    

Thank yor for the reply!    

Unfortunately these links don't have the answer to my question.    

Roughly six months earlier I deployed two Exchange Servers CU11 and there was a default database on the second CU11 server - now I've taken exactly the same steps with CU12 but there's no default db on the second server... ???

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-20*

Check these helpful links - https://community.spiceworks.com/topic/2278922-installing-new-exchange-server-2019-on-the-same-network-having-old-exchange-2016    

https://www.alitajran.com/install-second-exchange-server-in-domain/

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-19*

Hi LiLyLi2-MSFT,    

"It is recommended that you sign in to the EAC to check if this server has a default mailbox database":    

    

    

Both Exchange Servers are 2019 installed on Windows Server 2022.    

"what would be the result if you used Get-MailboxDatabase directly?" - sorry, didn't get it: what does mean "directly"? I've posted the result of the Get-MailboxDatabase -Server EXCH2 above and that command was issued on EXCH2. Ommiting "-Server EXCH2" leads to the single output - "DB01 on EXCH1", exactly as in EAC.    

Regards,    

Michael
