---
title: "ADFS SQL WID Errors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/549869/adfs-sql-wid-errors
question_id: 549869
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS SQL WID Errors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/549869/adfs-sql-wid-errors (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I just built two new ADFS servers on 2016 using the WID database as our two old ones were giving us issues.  This went really well, moved the primary from the older server to a new server, no issues.   

Now I'm seeing the following show up in the logs of the two new servers:   

The query notification dialog on conversation handle '{3EC7D52A-9514-EC11-8B7F-00505685271D}.' closed due to the following error: '<?xml version="1.0"?><Error xmlns="http://schemas.microsoft.com/SQL/ServiceBroker/Error"><Code>-8494</Code><Description>You do not have permission to access the service 'IdentityServerNotificationsService'.</Description></Error>'.   

And the following log repeated periodically:   

Starting up database 'AdfsArtifactStore'.   

In the ADFS event logs, I see the following periodically as well:  

An error occurred when communcating with the account store endpoint on server hq-2padfs01.internal.ieeeglobalspec.com.   

Additional Data   

%Exception Message:   

Microsoft.IdentityServer.WebHost.Rest.RestExceptionDataContract   

See https://go.microsoft.com/fwlink/?linkid=849965 for more information.  

Everything seems to be working fine though - except for my OTP MFA Identity Provider, which doesn't seem to work on the second ADFS server.  (I have two load balanced WAPs, pointing to a load balancer that has the two new ADFS servers in it).   

This was working perfectly fine on the two old servers though.   

Any idea about the SQL error?

## Answers

_No answers on this thread._
