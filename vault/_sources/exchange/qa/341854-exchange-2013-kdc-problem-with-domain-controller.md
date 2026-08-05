---
title: "Exchange 2013 - KDC problem with domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/341854/exchange-2013-kdc-problem-with-domain-controller
question_id: 341854
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 - KDC problem with domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/341854/exchange-2013-kdc-problem-with-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

First, I'm sorry about confusing question title, here my environment:

3 sites/locations :

Default-First-Site-Name (Data center) :  

2 domain controllers : dc1 (Windows Server 2016 Standard) holds 5 FSMO roles , dc2 (Windows Server 2012 R2 Standard) , Forest/Domain function level : Windows Server 2008 R2.  

3 Exchange server 2013 CU23 (CAS + Mailbox roles) in 1 DAG , all are Windows server 2008 R2

South site : 1 domain controller dc-south (Windows Server 2016 Standard)

North site : 1 domain controller dc-north (Windows Server 2012 R2 Standard)

Yesterday , suddenly , mail service is down , I cannot connect to OWA , ECP , MS Outlook disconnected , it seems DAG and all mailbox databases are down too .  

I cannot even remote login (remote desktop) or direct login (console) into 3 Ex servers (error: username / pass incorrect) , but I can login to DCs and other joined domain servers (at 3 sites) normally  

Because it is urgent (in working hours) , I have no choice but hard reboot 1 Ex server, after restarting , I can login to Exchange server, of course , DAG and all mailbox databases are still down , so I restart other 2 Ex servers also.  

And everything back to normal, DAG on , all mailbox databases are mounted and healthy.

At that time, I look into event log at 3 Ex servers and see that there are errors (Event id 4) appear on 3 of them:

```
The Kerberos client received a KRB_AP_ERR_MODIFIED error from the server dc2$. The target name used was cifs/dc02.mydomain.com. This indicates that the target server failed to decrypt the ticket provided by the client. This can occur when the target server principal name (SPN) is registered on an account other than the account the target service is using. Please ensure that the target SPN is registered on, and only registered on, the account used by the server. This error can also happen when the target service is using a different password for the target service account than what the Kerberos Key Distribution Center (KDC) has for the target service account. Please ensure that the service on the server and the KDC are both updated to use the current password. If the server name is not fully qualified, and the target domain (mydomain.COM) is different from the client domain (mydomain.COM), check if there are identically named server accounts in these two domains, or use the fully-qualified name to identify the server.
```

So, something went wrong with KDC on dc02 at Default-First-Site-Name (Data center).  

Other servers switch to use KDC on other DCs automatically , so I still can remote login to them , right ?  

3 Ex servers didn't switch to use dc1 automatically , or they would do but it takes time (according to theory/doc , I asked about it before https://social.technet.microsoft.com/Forums/en-US/5e014747-ac63-465c-8716-c5a3f399553a/change-domain-controller-for-exchange-server-2013?forum=exchangesvrdeploy#5e014747-ac63-465c-8716-c5a3f399553a) , but because it's urgent, I force reboot 3 Ex servers and they switched to dc01 after reboot.  

Result are same on 3 Ex servers:

```
Get-ExchangeServer -Identity ex01 -status | Select-Object Name,StaticDomainControllers,StaticGlobalCatalogs,StaticConfigDomainController,StaticExcludedDomainControllers,CurrentDomainControllers,CurrentGlobalCatalogs,CurrentConfigDomainController,OriginatingServer

Name                            : ex01
StaticDomainControllers         : {}
StaticGlobalCatalogs            : {}
StaticConfigDomainController    :
StaticExcludedDomainControllers : {}
CurrentDomainControllers        : {dc1.mydomain.com}
CurrentGlobalCatalogs           : {dc1.mydomain.com}
CurrentConfigDomainController   : dc1.mydomain.com
OriginatingServer               : dc1.mydomain.com
```

They used to point to dc2.mydomain.com before reboot.  

At the same time:  

I cannot UNC \dc2  

I can UNC \dc1 , \dc-south , \dc-north and see NETLOGON , SYSVOL folder shared.  

At Active Directory Sites and Services , when I try to manual replicate from dc1 --> dc2 I get error "The target principal name is incorrect" , testing with Repadmin or dcdiag has similar result.

While looking for solutions to this KDC problem, I notice that Event ID 4 still happens on 3 Ex servers at the rate 1/2 times per hour*.

Several hours later**, it happened again (cannot connect to OWA , ECP , MS Outlook disconnected , ... ) , I cannot remote login to 1 Ex server , so I reset dc2 account password by this command on dc2:

```
netdom resetpwd /server:dc1 /userd:mydomain\administrator /passwordd:*
    The machine account password for the local machine has been successfully reset.

    The command completed successfully.
```

Then restart dc2 , Event ID 4 has gone, everything back to normal. (owa , ecp , mailbox databases , DAG , I can UNC \dc2 , manual replicate dc1 --> dc2 successfully)

"*" & "**" Why it happened again and why Ex servers still want to try KDC at dc2 ? If dc2 KDC had problem and all Ex servers switched to dc1 KDC (as I said above) , they should work ok without even consider dc2 ?

Now when dc2 KDC is fixed , this is same result on 3 Ex servers:

```
Get-ExchangeServer -Identity ex01 -status | Select-Object Name,StaticDomainControllers,StaticGlobalCatalogs,StaticConfigDomainController,StaticExcludedDomainControllers,CurrentDomainControllers,CurrentGlobalCatalogs,CurrentConfigDomainController,OriginatingServer

    Name                            : ex01
    StaticDomainControllers         : {}
    StaticGlobalCatalogs            : {}
    StaticConfigDomainController    :
    StaticExcludedDomainControllers : {}
    CurrentDomainControllers        : {dc1.mydomainl.com, dc2.mydomain.com}
    CurrentGlobalCatalogs           : {dc1.mydomainl.com, dc2.mydomain.com}
    CurrentConfigDomainController   : dc2.mydomain.com
    OriginatingServer               : dc2.mydomain.com
```

Will it happen again ? How can I configure my Ex servers to switch KDC automatically ? It's too bad that the service downtime still occurs even though 2 DCs exist at same site.  

Somehow, 3 Ex servers still prefers to use KDC on dc2 ? How to change it ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-05*

Hi joyceshen, thanks for your reply  

This is my Get-ADServerSettings | fl  

    Get-ADServerSettings | fl

```
RunspaceId                                         : 06ac569d-d6a1-49c1-8c1c-652386c15029
DefaultGlobalCatalog                               : dc2.mydomain.com
PreferredDomainControllerForDomain                 : {}
DefaultConfigurationDomainController               : dc2.mydomain.com
DefaultPreferredDomainControllers                  : {dc2.mydomain.com}
UserPreferredGlobalCatalog                         :
UserPreferredConfigurationDomainController         :
UserPreferredDomainControllers                     : {}
DefaultConfigurationDomainControllersForAllForests : {}
DefaultGlobalCatalogsForAllForests                 : {}
RecipientViewRoot                                  : mydomain.com
ViewEntireForest                                   : False
WriteOriginatingChangeTimestamp                    : False
WriteShadowProperties                              : False
Identity                                           :
IsValid                                            : True
ObjectState                                        : New
```

What I'm worried about is : even if I use "Set-ADServerSettings" to configure my Ex servers point to dc1.mydomain.com , KDC problem may occur with dc1 also , and Ex servers will be down again.  

About fixing KDC problem, I don't care about it before because I don't do anything to mess up/twist with dns records recently , I have checked that there is no SPN/service/A duplicate record relating to dc2.mydomain.com.  

But now, I think I figure out why Kerberos client error 4 happens : I made a basic mistake , my internal domain same name as an external domain which I don't own .  

I have I looked into event log at 4 DC servers and see that there are errors (Event id 4) appear on 3 of them:  

```
The Kerberos client received a KRB_AP_ERR_MODIFIED error from the server workstation1$. The target name used was RPCSS/workstation1.mydomain.com
```

I can post another question adding AD and windows server related tags to ask about fixing it but I just want to consult your opinion one more time : can I fix it temporarily by adding into 4 DC and 3 Ex servers host file A records of 4 DC and 3 Ex servers ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-05*

Hi @Jack Chuong      

From Exchange server side, we could use Get-ADServerSettings | fl  to view the Active Directory Domain Services (AD DS) environment settings in the current Exchange Management Shell session.     

Using the -PreferredServer parameter which specifies the FQDN of the domain controller to be used for this session in Set-ADServerSettings    

Like this article introduces: How to Use a Specific Domain Controller in Exchange 2010 Management Shell , applies to Exchange 2013 as well.    

And the KDC switch seems to be more related to Active Directory and Windows server, I searched below links discussed about such error:    

Fixing the Security-Kerberos / 4 error    

Servers getting Security-Kerberos client error 4    

Replication Errors (The target principal name is incorrect )    

I would suggest you post your question adding AD and windows server related tags to get more professional support there, thanks for your understanding!    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
