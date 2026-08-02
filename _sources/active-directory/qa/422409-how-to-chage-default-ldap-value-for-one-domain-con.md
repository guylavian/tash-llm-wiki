---
title: "HOW TO CHAGE DEFAULT LDAP VALUE FOR ONE DOMAIN CONTROLLER IN FOREST"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/422409/how-to-chage-default-ldap-value-for-one-domain-con
question_id: 422409
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# HOW TO CHAGE DEFAULT LDAP VALUE FOR ONE DOMAIN CONTROLLER IN FOREST

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/422409/how-to-chage-default-ldap-value-for-one-domain-con (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi guys    

please help how to change the ldap default value from 120 sec for (InitrecvTimeout & MaxQueryDuration)only for one domain controller across the forest .I gone thorough the below article but  could not achieve as we required     

can anyone help on this pls    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/view-set-ldap-policy-using-ntdsutil    

    

regards

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-24*

Hi，  

Thank you for waiting and replying  

》》other dcs policy would be same as have currently am i correct ?  

This is ok  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-24*

Hi,  

Welcome to share your current situation if there are any updates.  

Please feel free to let us know if you need further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-15*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-11*

Hi，  

Thank you for your reply and waiting.  

Instructions for configuring per domain controller or per site policy  

Create a new query policy under CN=Query-Policies,CN=Directory Service,CN=Windows NT,CN=Services,CN=Configuration, forest root.  

Set the domain controller or site to point to the new policy by entering the distinguished name of the new policy in the Query-Policy-Object attribute. The location of the attribute is as follows:  

The location for the domain controller is CN=NTDS Settings, CN= DomainControllerName, CN=Servers,CN= site name,CN=Sites,CN=Configuration, forest root.  

The location for the site is CN=NTDS Site Settings,CN= site name,CN=Sites,CN=Configuration, forest root.  

After the policy is created, it needs to be configured on the DC that requires the new value to take effect  

Not after the policy is created, all DCs will be applied  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-07*

Open ADSI Edit.  

In the Configuration partition, browse to Services → Windows NT → Directory Service → Query Policies.  

In the left pane, click on the Query Policies container, then right-click on the Default Query Policy object in the right pane, and select Properties.  

Double-click on the lDAPAdminLimits attribute.  

Click on the attribute you want to modify and click Remove.  

Modify the value in the Value to add box and click Add.  

Click OK twice.  

Using a command-line interface  

To view the current settings, use the following command:  

reference： https://www.oreilly.com/library/view/active-directory-cookbook/0596004648/ch04s24.html  

Tip: This answer contains the content of a third-party website. Microsoft makes no representations about the content of these websites. We provide this content only for your convenience.  

Hope this information can help you  

Best wishes  

Vicky
