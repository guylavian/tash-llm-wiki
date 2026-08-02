---
title: "Exchange 2016 CU20 Schema Update setup.exe /preparead fail because of case sensitivity of OWA APP Policy DEFAULT"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/365522/exchange-2016-cu20-schema-update-setup-exe-prepare
question_id: 365522
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 CU20 Schema Update setup.exe /preparead fail because of case sensitivity of OWA APP Policy DEFAULT

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/365522/exchange-2016-cu20-schema-update-setup-exe-prepare (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2016 CU20 Schema Update setup.exe /preparead fail because of case sensitivity of OWA APP Policy    

Hello,    

During the last few weeks we had to update several 2013/2016 to latest CU several times. Thanks to the NSA and their backdoor which they had to fix with help of the FBI which kept us quite busy. The problem was the amount of customers we had to patch and that the work had to be delegated to non Exchange Engineers. For people who do no handle such upgraded regularly it's important that they understand that the fully exchange get's de-installed and afterwards re-installed based in some backup and XML files. From 28 customers we updated we have seen one bluescreen during the CU20 install. All other where fine because we informed the people on how to do it: a) Elevated, b) Check Certificate Revocation OFF in Load Balancer VLAN's d) With commandline and /LVE setup Logfile so we could help afterwards.    

However we have seen one larger customer where we had problems with the CU20:    

We had a case in a Mother / Child Domain setup where we had to update Active Directory of the Mother domain of the company with commandline to a new Schema Version. This was related to the second Exchange 2016 Breach/Hotfix and we wanted to uplift Exchange 2016 from CUMU 19 to 20 urgently.    

Problem we have seen with CU20 Update ( We are unsure if this may be related to a Mother-Child Domain setup or simply a bug in the MSP included PowerShell)    

Exchange 2016 CU 20 need and fails to update Active Directory Schema to newer Version (setup.exe /prepareschema works setup.exe /Preparead fails) if you have renamed Outlook Web App Policy anything else than "Default" (As example default or DEFAULT)    

    

```
The following error was generated when "$error.Clear();  
$policyDefault =   
Get-OwaMailboxPolicy -DomainController $RoleDomainController | where  
{$_.Identity -eq "Default"};  
if($policyDefault -eq $null)  
{  
New-OwaMailboxPolicy -Name "Default" -DomainController $RoleDomainController  
}  
"Microsoft.Exchange.Data.Directory.ADObjectAlreadyExistsException: Active   
Directory operation failed on server.contoso.com. The object   
'CN=Default,CN=OWA Mailbox Policies,CN=NSA,CN=Microsoft   
Exchange,CN=Services,CN=Configuration,DC=usa,DC=net' already exists. --->   
System.DirectoryServices.Protocols.DirectoryOperationException: The object   
exists. at System.DirectoryServices.Protocols.LdapConnection.ConstructResponse(Int32 messageId, LdapOperation operation, ResultAll resultType, TimeSpan
```

Workaround:    

Rename the OWA APP Policy from whatever you have to Default (Large D and small chars rest)    

    

comment: We have seen several other such related issues with 2016/2019 Exchange. Something does not update or install simply because something is case sensitive or some argument is missing or there where it should not be. Mainly in long history customer which where over 15 years on Exchange in several version.     

We know how to fix but always say "And then? Next Update or when it runs same? Does it run?" And sometimes Tier 3 from Microsoft does nothing else. They compare what's different with the customer to their reference and then change the Attribute with ADSIEDIT and close the case. That's it, no explanation.    

Still the above mentioned gives me some bad feeling. The patch was released asap and it was the second patch. If the tested the patch to death someone else would have come again and said why do they keep the patch back so long? (For IT > It was because they had to discuss so long with NSA on how to turn things back).    

If you read the story about the FBI who could change your Exchange settings by court you know what happened if you are not a naiv IT-world geek...    

Office 365 was not affected because their NSA backdoor works in another way (Read more on google...)    

Hope this may help some people stuck in a server room at night ;-)    

Greetings from switzerland    

a on-premise lover    

Details:    

http://www.butsch.ch/post/Exchange-2016-CU20-Schema-Update-setupexe-preparead-fail-because-of-case-sensitivity-of-OWA-APP-Policy.aspx

## Answers

_No answers on this thread._
