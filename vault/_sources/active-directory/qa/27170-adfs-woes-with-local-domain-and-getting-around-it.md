---
title: "ADFS woes with .local domain and getting around it on 2016 servers."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/27170/adfs-woes-with-local-domain-and-getting-around-it
question_id: 27170
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS woes with .local domain and getting around it on 2016 servers.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/27170/adfs-woes-with-local-domain-and-getting-around-it (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Ive inherited a domain set up as abc.local  

Within the domain are many, many services and applications.  

The exchange is onsite and very few but growing cloud presence.  

Changing the domain from abc.local to an outside domain such as abc.com  

isnt going to happen.   

Ive been tasked to create an ADFS portal to the outside world for single sign on  

that will allow outside services to be routed inwards and to be able to get our inside   

applications to the outside more easily.  

This is where all the fun begins.  Since it is currently an abc.local domain, there is no SSL certificate services that will or can verify the domain information.  So that meant that I had to use an outside registerable domain name such as abc.net  

 Ive got my WAP server setup on the outside DMZ as a stand alone server.  It has my SSL wildcard certificate for the new abc.net domain.  I can get said WAP server to see through DNS my internal domain with NO issue.    

The part that I get tripped up on is getting the WAP to tie correctly to the ADFS server.  It too has the SSL wildcard certificate used on the WAP server set up.  However I constantly when trying to tie them together get errors about not being able to communicate correctly.  

Second Scenario -  Same issue with the above abc.local domain, decided to put in a pristine domain forest all together, abc.net  to act as a bypass domain.  Set up domain controller, and all associated GPs, Sites & Services, etc.  Setup the Trust Relationship with the abc.local domain, complete two way transitive to ensure that this domain would be able to authenticate users from the associated abc.local domain.   WAP server will be again setup on the DMZ with associated SSL wildcard certificate, and be able to see the entire forests.  The ADFS server will be registered into the new abc.net domain as well as a MSSQL2017 server for the database.    

Has anyone got an Idea of what may or may not be causing issues on first setup, and be able to guide my fixing it?  

On the second scenario - Is this a common method of getting around the issues of the abc.local domains or is there a simpler way to deal with it?  If it's a common method, am I missing anything?  

ALL help is greatly appreciated.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-05-28*

The internal name of the domain does not matter. What matter will be the FQDN you will use for your ADFS farm.  

You can be domain.abc in ADDS and have the FQDN of your ADFS farm something line domain.com as long as internal client resolves it to the right IP address (you will need a split brain DNS to ensure that local clients will resolve the FQDN to the local IP address and the external clients will use an Internet DNS and resolve the FQDN to the public IP address of your WAP servers.  

You don't need a SQL Server instance for ADFS either, you can just use the local WID.
