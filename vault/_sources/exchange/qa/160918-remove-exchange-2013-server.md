---
title: "Remove Exchange 2013 server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/160918/remove-exchange-2013-server
question_id: 160918
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Remove Exchange 2013 server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/160918/remove-exchange-2013-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to remove an Exchange 2013 server from our setup.  

We had a single Exchange 2013 CU23 server in a hybrid config, all mailboxes are Exchange online, the server was simply a transport server used to allow our scan to email service and a few systems to email alerts/reports etc.  

I recently added an Exchange 2016 CU18 server to this with the intention of removing the Exchange 2013 server.  

However, despite following the setup instructions it looks like if I remove the 2013 server we lose access to autodiscover and the Exchange ECP console because they default to the 2013 box.  

When I say lose access, I mean the ECP page loads but it then refuses to allow anyone to log on, says user ID or password are wrong despite the same person being able to log on when the 2013 machine is still online.  

Looking at the ECP console both servers have their own entry for each of the virtual directory urls but as soon as the 2013 box is taken offline we lose access though the email flow from the scan to email and the alerts/reports still works, if a little slowly.  

What am I missing here?  

Again, there are no mailboxes on the on premises Exchange servers though each of them has a database. The database on the 2013 machine was originally used to store mailboxes while the one on the 2016 was set up by default when I installed Exchange on the server, the database on the 2013 box is dismounted.   

The servers are not in a DAG  

Both servers are multi role (mailbox and CAS)  

The 2016 server has been set as the hybrid server by rerunning the hybrid setup wizard.  

Both machines are Hyper-V guests, the 2013 server is on Server 2012 R2, the 2016 one is running on Server 2016  

Update:  

After checking the certificate settings I now get a slightly different error when trying to log into the ECP console. If I just use my samaccountname I get the ID/password error, if I use domain\samaccountname and password it does the same. If I use my UPN it gives me a 500 error saying the page cannot handle the request.  

As soon as the old server is brought back online it lets me log in.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-11-12*

Did you move the arbitration mailboxes on the 2013 server to the 2016 server?  

```
Set-ADServerSettings -ViewEntireForest:$true
 get-mailbox -arbitration | new-moverequest -targetdatabase 
```

You will need to mount the 2013 DB to move these of course.
