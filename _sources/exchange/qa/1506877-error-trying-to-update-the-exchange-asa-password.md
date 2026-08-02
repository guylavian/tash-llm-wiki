---
title: "Error trying to update the Exchange ASA password"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1506877/error-trying-to-update-the-exchange-asa-password
question_id: 1506877
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-user-experience-powershell"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Error trying to update the Exchange ASA password

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1506877/error-trying-to-update-the-exchange-asa-password (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Running 2 servers with Exchange 19 and when adding another one and doing the configurations I ran into a problem changing the ASA password. (It has been a few months since a built the first 2)
Using the rollalternateserviceaccountpassword.ps1 i first tried to use the copy from one of the original servers to the new one and when that failed I thought 
I would create the password again and then copy to the other servers.
.\RollAlternateServiceAccountPassword.ps1 -ToSpecificServers Exch03 -GenerateNewPasswordFor “DOMAIN\EXCHASA19” -Verbose
produces the following error.
RecordErrors : Cannot convert value "EXCH03" to type "Microsoft.Exchange.Data.Directory.Management.ClientAccessServer". Error: "Cannot convert the "EXCH03" value of type "Deserialized.Microsoft.Exchange.Data.Directory.Management.ClientAccessServer" to type
"Microsoft.Exchange.Data.Directory.Management.ClientAccessServer"."
I get the same error on all 3 exchange servers. The script worked perfectly when i built the first 2 Exchange servers so at a loss as to whats happened.
I have spent 3 days solid trying to diagnose and the 3 servers look very healthy.
Anyone know what might be going on?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-11*

So others dont have to go through the hours of torture i just did went through, it was cause when Microsoft did the enablement of PowerShell serialization payload signing. 
So you 2 choices, get the certificate done which i will do but i turned it off for the moment so i could quickly get my ASA problem sorted (which is now working yay).
If you want to turn it off like i did to get your problem fixed run this 
New-SettingOverride -Name "DisableSigningVerification" -Component Data -Section EnableSerializationDataSigning -Parameters @("Enabled=false") -Reason "Disable Signing Verification"
And DONT do it to an individual server for testing like I did by adding "-server Servername" cause youll regret it, cause then it wont let you do the others.
Please Microsoft do a better job of advertising when you make changes like this

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-22*

Hello Daryl  

Is there coexistence in your environment? The same error seems to be happening here.  

https://www.reddit.com/r/exchangeserver/comments/12fyfre/exchange_2013_2019_migration_autodiscover_errors/  

https://farkhadm.blogspot.com/2016/12/

(Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.)  

Kind Regards
