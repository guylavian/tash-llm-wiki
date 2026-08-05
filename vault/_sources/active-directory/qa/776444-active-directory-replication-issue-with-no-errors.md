---
title: "Active Directory - Replication issue with no errors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/776444/active-directory-replication-issue-with-no-errors
question_id: 776444
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory - Replication issue with no errors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/776444/active-directory-replication-issue-with-no-errors (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Everyone!  

We are having this weird replication behaviour in Active Directory and since we are struggling to get help even from Microsoft Support, I think to start a discussion to get some fresh ideas.  

This Active Directory is a single forest with no trusts and up to 60k user objects. All DCs are Windows Server 2012 R2 on a 2008 R2 Domain and Forest Functional Level. Also, this domain has born one year ago and most of the objects were created by using ADMT Tool, migrating data from another legacy domain that is already deactivated.  

It happens like this:  

We have a internal LDAP tool that run advanced LDAP queries, the tool can list all the users and attributes in ldif format and compare its results. That tool told us that in the latest months several discrepancy in attribute information for user objects troughout Active Directory, where there are certain objects that does not have the same value in its attributes on all Domain Controllers.  

With his output, we made the same queries and comparisons by using PowerShell Get-Aduser functions and really by checking directly in Active Directory console to found out that his inference was in fact true, and some users may present different values on said attribute depending on which Domain Controller is being queried at the moment. Unfortunately, we didn't see a clear pattern on this behaviour, as it happens randomly on all of the 29 DCs, sometimes the discrepancy happen and different values are found on DCs in the same site, it happens on builtin and custom attributes alike.  

We had in the beginning of the report, that was like a month ago, about 400 users in this scenario, that we took as a punctual event and manually correct the values of attributes by using Set-ADUser functions. The number was reduced, but we observe that when attributes are changed throughout the organization for any reason, and we do these LDAP queries again, those numbers start to pump up again.  More then once we observe a pattern of certain users being affected, some know names, so maybe the question is what can cause objects in Active Directory to show this behaviour?  

Another pattern that we observe recently is, that the recent events of this reocurrence happens in DCs that has an especific DC as a replication partner (lets call it 03), but that recently, when we first face the issue, all the DCs were being affected.  

By using repadmin /showobjmeta, we saw that the attributes of the object affected in the DC affect is on a sort of "sleep" state that does not replicate, by following the natural intra or intersite cycle or even using repadmin /syncall and Replicate Now options. The USN of the attribute as well as the  version value and date time stays freezed on a DC, and others got a more updated version.  

Something that in fact helped us and was provided by Microsoft Support was the use of: repadmin /replicate AFFECTEDDC HEALTHYDC  “DC=contoso,DC=com” /full in fact helped us as it forces the write of the content from a partition of a health DC to a affected DC, but that is the workaround used right now. After using that command we have a brief solution, however after another Change where a bunch of users got their attributes modified for the needs of an Application, we noticed the same behaviour returning. The method of modification was done by us, Sysadmins, using normal powershell set-aduser -replace functions.  

Its also worthy mentioning that everyday we receive Health Check information (dcdiag and repadmin) in a html form and no errors are being show on Active Directory at all, for replication summary and dcdiag tests. If we were to create new users, or even update users, most of the time the replication will work fine, except for some said cases.  

Right now, we are investigating the root cause and any help is appreciated.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-03-17*

Hi @ALostAdmin      

Thanks for sharing your interesting problem, which I'm sure its also frustrating for you.    

A couple of question to help clarify the issue, I do have a couple suggestion but just want to make sure I understand the issue correctly.    

Are only user objects affected by this issue?    

Once you have completed the repladmin /full sync, on average how long does it take for the issue to happen again?    

Are there any domain controllers that haven't exhibited the issue?    

For a user object that has stopped replicating, if you force a full replication using repadmin /full, does the same user have the issue again?    

For an attribute on a user that has stopped replicating, if you change the attribute again, on a single DC, does the new value replicate the affected DC?    

When the replication stops, do all the affected dc have the same old value for the attributes?    

When the replication stops on an affected DC, if you change the value of an object that is non affected does the attribute change get replicated to the affected DC?    

When the replication stops, on user object that has a frozen attribute, if you change a different, non-frozen attribute, does the change get replicated to an affected DC?    

Is the HighestCommittedUSN in the RootDSE on the affected DC changing when attribute are?    

Can you provide the specification of the hardware or virtual platform used for the DCs?    

Other than the repladmin /full sync workaround, did Microsoft support provide any other insight into the cause of the problem?    

Gary.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-03-17*

Hi! Have you checked the events related to replication issues? Check this out: https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/common-active-directory-replication-errors    

I'd say that the first step you should do is to check the events, this is the starting point to troubleshoot your issue, once there's a lot of types of replication issues that could be caused due different types of problems in your infrastructure.    

Once you get the events, you can start troubleshooting according to those events.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-17*

Hi,    

Yep this is going to be difficult issue to identify as it does appear to be a drop of individual replication transactions and you will probably need Microsoft Support to complete the analysis and provide the solution.  However we can look at a few things to see if we can help with the troubleshooting.    

So a quick recap, please correct if this summary is incorrect:    

The scope of the issue is currently unknown, you only have visibility of the impact on user objects, but could be impacting other object types.    

Intermittently a random number of DC are not receiving or are ignoring replication updates    

If the same attribute is changed the affected DC will receive the attribute change and update the attribute, but this can be intermittent    

The lost of replication seems to isolated to the specific attribute changes, and does appear to be impacting the normal replication of the server    

DCDiags, Repladmin /summaryrepl, repladmin /showreps don't show any errors    

The affected DC don't shows any errors in the event logs    

a couple of extra questions,     

Do you see this problem if you change multiple attributes or only with single attribute change?    

When you change the stuck attribute on a user object, on the affected DC does the meta data version number increment by one or more?    

So a couple of things to check first off, most of which, I'm sure you have already done.    

Check that the DC are getting their time source from the PDC and that the VM DC are not set to use physical host for time sync    

Check the time is sync'd between all the DC - using w32tm /stripchart from the PDC to all the DCs    

Create a diagram with your understanding of the AD replication topology    

Check the network for any packet drops or excessive retries, or inconsistency in traffic delivery or rerouting    

As it appears that the affected DCs are missing or ignoring replication traffic, it's a difficult one to troubleshoot as you have to be monitoring the DC when the replication is fails, post failure it too late.  In which case it might be useful to enable the field engineering diagnostic event logs for replication, to see if there are any internal errors being reported.  I would do this on a DC that experience the issue the most, and not the PDC.      

I do have a few options on testing and monitor the replication, let me know if you want me to share these.    

Gary.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-17*

@Gary Reynolds       

Are only user objects affected by this issue?    

tbh, we are not quite sure as the mentioned tool only query users, attributes were usually handled by users object so is the context that we see most impact.     

Once you have completed the repladmin /full sync, on average how long does it take for the issue to happen again?    

As soon as a new modification is made on the user object, and from there, the issue may or may not happen again, value is replicated to some DCs and some does not seem to receive the new value, they got stuck with the old value, with USN stuck on previous version and previous modification data. A user that was previously affect may or may not show the behavior again.    

Are there any domain controllers that haven't exhibited the issue?    

Yes, there are some domain controllers that weren't listed so far, a few.     

For a user object that has stopped replicating, if you force a full replication using repadmin /full, does the same user have the issue again?    

Yes, that happens. The object that we are studying and testing right now is a user that was mitigated on the workaround but showed up later as inconsistent after a change request with his "userprincipalname" in this scenario.     

For an attribute on a user that has stopped replicating, if you change the attribute again, on a single DC, does the new value replicate the affected DC?    

Before the "repadmin /full" provided by Microsoft, that was exactly what we were doing. We get info of attributes and we send a script (set-aduser -clear and set-aduser -replace) to really elevate USN and force replication. The results were mixed, most of the users when the new value was set (we wrote it on PDC) it sucessfully replicated to all other DCs and numbers decreased considerable, but unfortunately, we also face some cases that users that replication didn't happen in all DCs, when the DC affected were the bridgehead of a branch site, fatally the whole site didn't receive the new value. It was a very morose workaround and took a while to handle, before Microsoft show us the repadmin /full solution.     

When the replication stops, do all the affected dc have the same old value for the attributes?    

As show in repadmin /showobjmeta, the affected DC will have the previous value according to version, 1 version behind.     

When the replication stops on an affected DC, if you change the value of an object that is non affected does the attribute change get replicated to the affected DC?    

It does, we create some fresh users (one in a DC without issues and one in a DC that experienced the frozen atribute problem) and observe its creation being replicated throughout the whole forest. After that we change its description and no issues were found, replication went ok throughout the forest.    

When the replication stops, on user object that has a frozen attribute, if you change a different, non-frozen attribute, does the change get replicated to an affected DC?    

It does, we tested that a few hours ago, a user with "userprincipalname" on this stuck behavior didn't have issues when we changed, for instance his description, the replication went sucessfully in all DCs in this case.    

Is the HighestCommittedUSN in the RootDSE on the affected DC changing when attribute are?    

It seems so:    

```
PS C:\Users\MYUSER> Get-ADRootDSE -server DC04 -properties * | select highestCommittedUSN  
  
                                                                                                    highestCommittedUSN  
                                                                                                    -------------------  
                                                                                                               50047835  
  
  
PS C:\Users\MYUSER> Set-ADUser -Identity testrep2022 -Description "170320221851"  
PS C:\Users\MYUSER> Get-ADRootDSE -server DC04 -properties * | select highestCommittedUSN  
  
                                                                                                    highestCommittedUSN  
                                                                                                    -------------------  
                                                                                                               50047854
```

Can you provide the specification of the hardware or virtual platform used for the DCs?    

Sure, right now for the Head Office (which is the main channel of replication, Hub Spoke), we have 6 DCs:    

4 virtual running on ESXI 6.7 - 2 physical that are HP Gen 10, those 2 are the FSMO, seized for forest and domain according to best practices. Furthermore, we took the liberty of gathering performance reports for latest 3 months this week, we noticed that in our main site, the Head Office, those 6 DCs never got even close to threeshold for CPU usage, disk usage and RAM, one or two peaks observed in the VMs, but even those were like 60%.    

Other than the repladmin /full sync workaround, did Microsoft support provide any other insight into the cause of the problem?    

Not really so far, we did things like, update the VMWare Tools of all DCs to the same version, which weren't. We ran a offline defrag on a DC that was showing the behavior, those two showed no results whatsoever. And we collect tons and tons of logs which are now being escalated for their Engineers and we are awaiting feedback.     

Many thanks for your support, actually your questions alone let me gather very important information that I would like to keep tabs when discussing the issue with vendor.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-03-17*

Simplest solution may be to demote, reboot, promo the problematic one again. This assumes it has not tombstoned in which case it would need to be rebuilt from scratch.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
