---
title: "ADFS health check for connection between ADFS and SQL Database"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/609903/adfs-health-check-for-connection-between-adfs-and
question_id: 609903
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS health check for connection between ADFS and SQL Database

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/609903/adfs-health-check-for-connection-between-adfs-and (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Problem summary:    

HTTP probes towards ADFS & WAP is not enough if the ADFS service is still running but the connection between ADFS and SQL database is dead.    

Environment:    

    

Using HTTP probes in Environment:    

    

HTTP probes:    

The normal way of having health checks setup as HTTP probes     

that runs HTTP checks towards each WAP & ADFS server URL or IP.    

They run health checks over HTTP port 80. Gets a 200 (OK) returned.     

The response to these probe endpoints is an HTTP 200 OK and is only checking the server/service locally, with no dependence on back-end services(SQL cluster\Database)    

Conclusion:    

Using HTTP probes towards ADFS & WAP servers is not enough    

Problem description:    

The HTTP port is going directly to the WAP and ADFS servers respectively.    

This means that they only check if the servers & services themselves are OK.    

There's a known problem where the connection between the ADFS backend    

and the SQL server dies for 2-3 minutes. During this time,    

the ADFS backend server times out, if you're unlucky.    

The problem here is when the ADFS backend server times out,    

the ADFS service    

itself is still running.(so as far as the HTTP probe is concerned the ADFS is    

still upp and running.) The HTTP probe is signalling that the    

ADFS service is OK.     

So the load balancer is till sending end users to the    

ADFS service that has a dead connection towards the SQL database    

because its service is still running.    

End-users ends up getting error during authentication.    

Question:    

How can I setup a proper health check between ADFS --> SQL cluster/database?    

So that you can see that communication between ADFS --> SQL does not work    

as intended. As in the case when the service on the ADFS servers are still running, but the database connection between ADFS and SQL database is dead.    

I would want that health check to be used for monitoring as a first stop. Secondary, you could build some recovery steps that could be executed thanks to this health check.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-11-04*

There are different ways to do probing. If you use the FederationMetadata URL, the IDP Initiated Signin page URL or the MEX URL, this should only get an answer only if the DB works. If you use the http/probe over HTTP (not HTTPs) it just returns a 200 if the web service is listening. This HTTP probe was introduces to address situations where load balancers probes cannot use HTTPs. ADFS enforces SNI therefore some load balancers which couldn't do health probing using HTTPs + SNI would fail. The solution is to make sure 1 the load balancer probing supports SNI, and 2 use HTTPs URLs which check the service end-to-end.  

On a side note, you should try to get rid of SQL as a part of your ADFS deployment. It makes other things a bit more complex. Any reason why you use SQL instead of WID?
