---
title: "Error install exchange 2016 coexistence with exchange 2010"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1337562/error-install-exchange-2016-coexistence-with-excha
question_id: 1337562
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Error install exchange 2016 coexistence with exchange 2010

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1337562/error-install-exchange-2016-coexistence-with-excha (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When installing exchange 2016.

 Error: step 7 of 14 mailbox role: Transport service

```
The following error was generated when "$error.Clear(); 

          if ( ($server -eq $null) -and ($RoleIsDatacenter -ne $true) )

          {

            Update-RmsSharedIdentity -ServerName $RoleNetBIOSName

          }

        ": "Microsoft.Exchange.Data.DataValidationException: Database is mandatory in UserMailbox.

   in Microsoft.Exchange.Data.Directory.ADDataSession.Save(ADObject instanceToSave, IEnumerable`1 properties, Boolean bypassValidation)

   )".
```

Checking in exchange 2010. I have the following error, in the following Blog FederateMailbox comment on the problem. Also in this other  Blog SystemMailbox and Blog DiscoverySearchMailbox

```
Get-Mailbox -Arbitration | Format-Table Name, ServerName, Database -Auto
```

```
Get-Mailbox
```

Shows error of objects with server name that does not exist (mail-ex01 server that currently exists)

WARNING: The object contoso.com/Users/SystemMailbox  

WARNING: The object contoso.com/Users/FederateMailbox  

WARNING: The object contoso.com/Users/DiscoverySearchMailbox  

has been corrupted and is in an incoherent state. The following validation errors have occurred:

NAME
Server Name

SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}
mail-ex02

SystemMailbox{1f05a927-43f2-4459-9ea1-31ee79fcf789}
mail-ex02

FederatedEmail.4c1f4d8b-8179-4148-93bf-00a95fa1e042
mail-ex02

DiscoverySearchMailbox{D919BA05-46A6-415f-80AD-7E09334BB852}
mail-ex02

My query is, delete and recreate does not affect anything. Or fix registry attributes, which would be the most recommended.

Exchange 2010 (Mail-EX01) shows log of an old mail server with the name Mail-EX02.

Exchange 2010 (Mail-EX01 server that currently exists) is running smoothly with 100 users.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-23*

Thank you very much everyone for the help.

I can now install exchange server 2016. Following the next steps

-  On the domain server I delete the arbitration accounts of the following tutorial.

-  Uninstall exchange 2016 CU23

```
Setup.exe /Mode:Uninstall /IAcceptExchangeServerLicenseTerms_DiagnosticDataON
```

-  Check in IIS on Server for Exchange Server 2016, When uninstalling there is a temporary website, I delete the duplicate because it generates an error when reinstalling.

-  Restart the exchange server 2016 server.

-  Recreate the arbitration accounts, on the exchange server 2016 server

```
setup.exe /PrepareAD /IAcceptExchangeServerLicenseTerms_DiagnosticDataON
```

```
Check on the domain server that the accounts are created.
```

-  I just installed the Exchange server 2016 CU23

-  Restart and test connection exchange 2016, Shell, Toolbox, ECP

Now I have a curiosity, the exchange 2016 installs without problem When configuring for the migration I realize that only the mailbox role is installed.

```
Get-ExchangeServer
```

Exchange 2010 (Roles)-> MailBox, ClientAccess, HubTransport

Exchange 2016 (Roles)-> Mailbox

I don't know if it is enabled later or if any problem occurred when installing exchange 2016

The idea is to migrate from Exchange 2010 to 2016 and then delete exchange 2010

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-07-28*

Check this similar thread for help - https://learn.microsoft.com/en-us/answers/questions/870977/(exchange-2016)-database-is-mandatory-on-usermailb

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-07-27*

Hi @Luis Alberto,

<<My query is, delete and recreate does not affect anything. Or fix registry attributes, which would be the most recommended.

Answer: I checked the three blogs you shared, and I see that they all end up with the same link and don't seem to have the same issue as yours. Or you could re-share. So, I could not answer your query.

Also, for your error I found out: Generally, if it is corrupt, it means that the value of the HomeMDB attribute for this account is empty. The solution to this issue is to add the correct value to the HomeMDB attribute of the corrupted account.

Here’s the steps:

Refer links: Exchange 2016: “Database is mandatory on UserMailbox” – Sabrina Kay's Blog (sabrinaksy.com)

(Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.)

Regards

Shaofan

*****************************************************  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
