---
title: "ADFS - possibility to determine to which application user has logged in"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/23405/adfs-possibility-to-determine-to-which-application
question_id: 23405
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS - possibility to determine to which application user has logged in

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/23405/adfs-possibility-to-determine-to-which-application (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

In our environment we use ADFS for authentication to various applications and we would like to have report about how many users logged in through ADFS to specific application.  

On basic logging level I was able to find only events 4624 and 4648 about that ADFS service account logon on User account.  

On verbose logging level I can see events like 1200 or 1202 where we have information about user ID, but there is still no information to which application user login. There is also IP address, but in our case it is address of load balancer.  

Is there any option to determine for which application user login through ADFS?  

Thanks, for any help

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-04-21*

urn:federation:MicrosoftOnline  

microsoft:identityserver:XXXX.coupahost.com  

are the identifiers of the relying parties. This is the information you are looking for (maybe not the format you want). You can see the identifiers from the ADFS admin console or in PowerShell in the output of Get-ADFSRelyingPartyTrust.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-04-21*

Hello @Pierre Audonnet - MSFT  ,    

Thanks for your quick answer.    

Yes we use WAP servers, but for question about doing NAT on load balancers I don't know answer.    

I quickly check logs and in <RelyingParty> I can find only 2 values:    

-  urn:federation:MicrosoftOnline    

-  microsoft:identityserver:XXXX.coupahost.com    

So unfortunately this is not what I'm looking for, because I can't determine if user authenticated to application ABC or DEF.    

Do you have any other idea how I could solve that problem?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-04-21*

This is an example of the event 1200:  

```
The Federation Service issued a valid token. See XML for details. 

Activity ID: 9d4acd9f-c9ee-495e-0e00-0080000000d5 

Additional Data 
XML: 

  AppToken
  Success
  None
  N/A
  
    
      urn:microsoft:adfs:claimsxray
      AD AUTHORITY
      V\piaudonnmsdn
    
    
      urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport
      false
      N/A
      false
      N/A
      true
      false
      TokenBoundAndValid
    
    
      N/A
      N/A
    
    
      http://sts.verenatex.com/adfs/services/trust
      WSFederation
      Intranet
      10.0.1.8
      
      N/A
      N/A
      N/A
      Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; Touch; .NET4.0C; .NET4.0E)
      /adfs/ls
    
  

```

You an see there is a relying trust section "<RelyingParty>urn:microsoft:adfs:claimsxray</RelyingParty>". Don't you have it in your events?  

For the load balancer IP, it depends on your implementation. Do you use WAP servers? Are your load balancer doing NAT?
