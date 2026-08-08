---
title: "ADFS in DR site V4.0 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/251242/adfs-in-dr-site-v4-0-2016
question_id: 251242
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS in DR site V4.0 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/251242/adfs-in-dr-site-v4-0-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have been looking at configuring a DR solution to our 2016 ADFS configuration.  

Currently 2x ADFS servers and 2x WAP Proxy servers in PROD site. Both of these are load balanced with Windows NLB.  

This is backed by the WID database.  

While I know we can simply add more servers in the DR site and make them part of the same farm. I also know that we should be able to control the failover with DNS, by pointing ADFS to the second site in the event of a failure at PROD (customer doesn't want to purchase geo load balancing and sites are physically quite close).  

My concern is really about failing over the database and failing back.  

Is this as simple as just setting one of the DR servers to be primary and telling the rest what the new primary is and that they are secondary now.   

Also, what will happen with the PROD site which is down - will we be able to set that to a secondary if it can't see the primary?  

Ultimately, is it possible to do this and anything I need to be aware of?  

I have done so much reading on this, but can't seem to find anything about doing this like mentioned above. But I also find nothing saying it will not be possible.  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-24*

I am going to piggy back on this thread as its something I'm looking into myself. We have similar setup 2x proxy servers NLB and 2xADFS servers but SQL instance holding the artefact database. This is all in one site and we want to add some DR to this setup.  

So we are building out a DR site with 1xproxy server and 1xadfs server and a SQL instance that is a mirror of the databases.   

In the case of the first site going down how do we move to the DR instance? I'm guessing that ADFS has a Database connection string somewhere more than likely encrypted.  

Is there documentation for this type of scenario anywhere ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-05*

Thanks for that, unfortunately this doesn't really answer my question for what happens when the link between PROD and DR sites is down.  

Under normal conditions as a test, we can easily move the primary server to DR and repoint the PROD servers to see that as primary.  

But assume that PROD lost all it's network for a couple of weeks. I can run the command to change the prod servers to look at DR as the primary, but it won't be able to talk to them.  

And when I promote the DR server to be primary in a real DR scenario (with PROD being totally down) it won't be able to see the original primary. Would that be a problem?  

Also, while PROD is offline, we won't be sending requests to it obviously - but what happens when the network is restored?  

I know with the PDC roll on a domain controller for example, we may need to seize that. If we seize it then we have to destroy the old DC. Does anything bad like that happen if you have two primary ADFS servers suddenly reconnect in the same farm?

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-02-01*

Hi @J Slack  , the process you outlined above is correct. The  prod site will know of the new primary server as well as long as they have network connectivity to the new primary server. The cmdlets for the same are documented at https://learn.microsoft.com/en-us/powershell/module/adfs/set-adfssyncproperties?view=win10-ps
