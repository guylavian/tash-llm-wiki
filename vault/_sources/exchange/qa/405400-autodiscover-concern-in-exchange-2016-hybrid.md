---
title: "Autodiscover Concern in Exchange 2016 Hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/405400/autodiscover-concern-in-exchange-2016-hybrid
question_id: 405400
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 2
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Autodiscover Concern in Exchange 2016 Hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/405400/autodiscover-concern-in-exchange-2016-hybrid (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team   

i looking for the correct auto discover setup on my current exchnage 2016 hybrid environment.   

In my external DNS (godaddy) Auto Discover is pointing to Autodiscover.outlook.com  

i dont have any any other records in internal DNS with respect to Auto Discover  

is this correct setup?  

when ever i am connecting my outlook(On-prem) both domain joined machine and non domain joined machine (Open network) and getting security alert   

exchangeservername. mytestdomain.xyz   

information you exchange with this site cannot be viewed or changed by others.however there is a prolem with site's security certficate.  

blaha.....  

looks there is is something issue related to on-prem autodiscover?  

how do i setup correct auto discover in my hybrid environment?

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2021-05-23*

Hi @Ramki   ,    

Usually, we will also create internal DNS record with autodiscover.domain.com and point to the load balancer if there are multiple servers for high availability. This autodiscover.domain.com should be set on the AutoDiscoverServiceInternalUri value on the Get-ClientAccessServer which is the Autodiscover SCP for internal clients.     

For the certificate prompt while connecting through outlook, please share the screenshot by covering your personal information to provide the suggestions as this can be of various reasons like certificate is not binded correctly in IIS, virtual directories are not configured with the URL matching the certificate, certificate validity, etc. Also, for external client prompt, possibility could be that the certificate can be fetched from any of the network devices in between like load balancer, etc    

In Exchange hybrid environment, we need point autodiscover record to On-premise Exchange server.    

For On-premise mailbox, it remain use previous autodiscover lookup behavior to find endpoint and access to Exchange.    

For migrated mailbox, autodiscover service will redirect On-premise autodiscover record to Office 365 (autodiscover-s.outlook.com), and access to Office 365.    

If the above suggestion helps, please click on "Accept Answer" and upvote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-24*

Thanks @Ashok M   anonymous userDavid @Lucas Liu-MSFT    - All    

Yes. as i told  currently my autodiscover is pointing to Exchange online in external DNS and Thanks for correcting me to have a autodiscover point to onprem exchange server in a hybrid environment. so Migrated mailbox will redirect the auto discover to exchange online     

Here is my current screens shot of the auto discover inernalURI    

    

AutodiscoverServiceinternaluri is HTTPS://cmex01.cloudmonkeys.xyz/autodiscover/autodiscover.xml    

so the next action is set the auto discover to the below link as Cloudmonkeys.xyz is certificate domain name pointing to my exchange server     

AutodiscoverServiceinternaluri :  is HTTPS://cloudmonkeys.xyz/autodiscover/autodiscover.xml    

Delete the Auto discover CNAME record in the go daddy and     

create a new autodiscover record point to Onprem exchange server server in godaddy    

is that correct Steps? ..Please correct me if anything am wrong

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-24*

Hi @Ramki   ,  

1.Agree with above. It depends on the location of your mailbox.

1)If all mailboxes has been migrated to Exchange online. You could set up the Autodiscover DNS records point to Exchange online instead of to on-premises. And run the following command to remove the Servcie Connection Point(SCP) values on your Exchange servers.

```
Get-ClientAccessService | Set-ClientAccessService -AutoDiscoverServiceInternalUri $Null
```

For more information, please refer to the scenario two in this article: How and when to decommission your on-premises Exchange servers in a hybrid deployment

2)If there are mailboxes located on the on-premises Exchange server. We need point autodiscover record to On-premise Exchange server. For On-premise mailbox, it remain use previous autodiscover lookup behavior to find endpoint and access to Exchange. For migrated mailbox, autodiscover service will redirect On-premise autodiscover record to Office 365 (autodiscover-s.outlook.com), and access to Office 365.

2.Regarding the certificate error. Generally, there are three types of certificate errors, and the reasons for each type of error are different. Please share the specific information of your certificate error. It should be noted that please cover your personal privacy information.  

In addition, you could refer to this article to check whether your certificate meets the requirements of hybrid environment: Certificate requirements for hybrid deployments

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
