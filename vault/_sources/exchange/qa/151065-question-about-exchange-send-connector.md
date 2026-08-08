---
title: "question about exchange send connector ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/151065/question-about-exchange-send-connector
question_id: 151065
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# question about exchange send connector ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/151065/question-about-exchange-send-connector (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a little bit confuse about the "scoped send connector " and "source servers" setting on send connector.  

first of all, I think I know what they mean, okay ...may be I don't really know....haha  

lets take a example:  

if we have 2 AD site, one in China, and one in US, each site have 1 exchange 2016.  

Scenario A:  

create a send connector (no scoped) and add China exchange as source server. (address space is wildcard)  

create a send connector (no scoped) and add US exchange as source server. (address space is wildcard)  

Scenario B:   

create a send connect (scoped) and add 2 exchange servers as the source server.  

quesiton:  

what the different between scenario A and B ?  

I want the outbound server location to be the same as the mailbox database server location for the account, for example a China account will send from China server and a US account will send from the US server. which scenarios can do that ?  

sorry about my terrible english...and thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-05*

hi Andy and Ashok,  both answers are very clarity.  thanks!

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-05*

@Jerry Su       

Hi,    

The "Scope" controls whether the send connector is visible to other exchange servers.    

If a send connector is scoped,it can only be used by exchange servers in the same site.    

If it is not scoped,it can be used by all exchange servers in your environment.    

The "Source servers" determines the destination Exchange server for mail that needs to be routed through the Send connector.    

For example,if you configure a send connector to send mails to the internet and add only one server to the "Source servers",the other servers will route outbound mails to this server.    

And only through this server are outbound mails sent to the internet.    

In Scenario A,since the send connector are not scoped,the two servers can use both send connectors to send mails.    

For example, if "send connector A" is configured to send mails to domain "contoso.com" and its source server is the server in China.     

The server in US will route mails to the server in China if the mails are supposed to be sent to "contoso.com".    

Then the server in China will send the mails to "contoso.com".    

In Scenario B,I think it you may get a warning of adding servers in different sites to source servers of a scoped send connector,as server in a different site isn't able to see the send connector.    

I want the outbound server location to be the same as the mailbox database server location for the account, for example a China account will send from China server and a US account will send from the US server. which scenarios can do that ?    

You may need to configure two scoped send connectors and add the specific server in China or US as the only source server to each of them.    

So the mails won't be routed to the other server.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-11-04*

Ok, lets look at each case:  

Scenario A:  

create a send connector (no scoped) and add China exchange as source server. (address space is wildcard)  

create a send connector (no scoped) and add US exchange as source server. (address space is wildcard)  

In this scenario, each send connector can be seen and  used by any mailbox server in the org to route mail through. This is generally the recommended setting - to leave the default.  

So in other words, even though one send connector has just the US server as the source server, the server in China can still see it and send mail out through it using the US server as the source.   

Scenario B:  

create a send connect (scoped) and add 2 exchange servers as the source server.  

This configuration would not make sense in your case. With 2 servers and 2 sites , this is the same as having one unscoped send connector with both source servers.   

In fact, I suspect Exchange would throw an error if you tried to configure it this way.  

Bottom Line: If Scoped - only the servers in the same AD site as the source servers can see and use the send connector. Servers outside that AD site will NOT  be able to see it exists.  

Make sense?  

This may help as well:  

http://clintboessen.blogspot.com/2014/01/what-are-scoped-send-connectors.html
