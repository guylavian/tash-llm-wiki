---
title: "why ADFS requires two way trust"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/61001/why-adfs-requires-two-way-trust
question_id: 61001
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# why ADFS requires two way trust

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/61001/why-adfs-requires-two-way-trust (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am curious to know why do I need to have 2-way trust in following flow where    

My ADFS server is with  contoso.com forest.    

Per me,  the meaning of above statement is,  I have kick off ADFS on Windows 2016 box  with a service-account which is in contoso.com.   Am I correct ?    

When ADFS  receives a request for authentication and when user feeds in for eg.,   ******@constoso.com/password  ,  what exactly happens ?    

 (the user is not in the network.  So no IWA from that point of view)    

My understanding is ADFS service-account  will  internally use  IWA   OR  it would be simple  LDAPS call to AD   ?    

If ADFS takes kerbeors route for password checking then  logically following will be performed    

		Determine the user's Kerberos principal name: netid@Adrian Seni  .NORTHWESTERN.EDU  

		Use the principal name and password to obtain a ticket-granting ticket (TGT)  

		Use the TGT to obtain a service ticket, verifying the authenticity of the KDC  

If fabrikam.com  trust constoso.com (one-way trust),  won’t it be sufficient for ADFS to authenticate user for eg.,   ******@farikam.com    

Meaning,  ADFS service-account   will obtain the proper ST (service-ticket) and use it authenticate and collect all the necessary attributes of Mary  to pack in the SAML-claim.    

Appreciate your help.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-08-08*

Yes, you are right and we indeed see that in context of azure-ad app proxy architecture where the on-prem proxy connector gets the ticket on behalf of the user.  

Coming back to our point,   

The first part is validating the  end-user's password.  ADFS performs this with the help of Kerberos.  

As long as   domain-controller of the user's  AD  is in line-of-sight ,  ADFS can send the  TGT  request and validate that user's password is correct.  

To accomplish this,  there is NO need of any kind of inter-forest trust  required.    Am I correct ?  

Now in the second part,  ADFS needs to pull up all the necessary claims.  

For that you said that,  

ADFS is making LDAP calls (not to authenticate the user, but to enrich the token depending on your claim issuance rules). If the user is from a different domain, the ADFS service still need to do LDAP queries to this domain.  

If it is literally LDAP call on ldap protocol, then I believe the service-account of ADFS should have permission in all the domains where the end-user is residing.  

Would you help me understanding this ?  

Thanks.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-08-07*

First of all, I'd like to make clear that ADFS is not a requirement to have SSO with Azure AD workloads (eg. Office 365). You can use Azure Active Directory Seamless Single Sign-On and even other options for Windows 10.    

When you are using Form Based Authentication, the user is doing an explicit credential logon. Meaning that the password is sent to the ADFS server for logon but not the domain controller. From the ADFS server, the service asks for a Kerberos ticket for the user. So the Windows logon really starts from the ADFS server. As a result, if you look at the DC's logs, the Kerberos ticket request events will show the IP address of the ADFS server, and if the password is wrong and the account has to be locked out, the source workstation will show the ADFS server name.    

ADFS is making LDAP calls (not to authenticate the user, but to enrich the token depending on your claim issuance rules). If the user is from a different domain, the ADFS service still need to do LDAP queries to this domain. The service also uses the Kerberos S4ULogin feature (Service for User to Self) to check group membership and build tokens.
