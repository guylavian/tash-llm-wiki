---
title: "DFSR Sysvol replication issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2187271/dfsr-sysvol-replication-issue
question_id: 2187271
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# DFSR Sysvol replication issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2187271/dfsr-sysvol-replication-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This is a test environment and has been raked over the coals, just to put that out there.

Two domain controllers both 2019.  The PDCe has been up and running a long time, DC1, and does contain all the FSMO roles.  

The second one DC2 has been added and removed from the domain several times, but currently is a DC but has no FSMO roles.

DFSR issues go back in excess of a year.  Umm Yes, no joke.

AD is healthy, repadmin /syncall /force /AdeP finishes no errors, no errors in DCDIAG......

SYSVOL on DC1 is complete and up to date.  It should be "authoritative."

SYSVOL on DC2 is incomplete.  DFSR is not replicating.  DFS Manager GUI, when you add replication groups the only server you see is DC2.

DFSRMIG /getmigrationstate on both servers shows eliminated so yes SYSVOL should be using DFSR, also msDFSR-Flags=48 in ADUC\Domain\System\DFSR-GlobalSettings.  But if you drill further down to Topology there's only an object for DC2.  

Using on DC1 WMIC /namespace:\root\microsoftdfs path dfsrreplicatedfolderinfo WHERE replicatedfoldername='SYSVOL share' get replicationgroupname,replicatedfoldername,state (off the top of my head excuse any typos) but the result is No Instance Available.

Since DC1 is the correct copy of Sysvol it makes sense to follow the Perform an AUthoritative Synch from the following:

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization#how-to-perform-an-authoritative-synchronization-of-dfsr-replicated-sysvol-replication-like-d4-for-frs

the problem is, with no DC1 instance I can't complete the following:

CN=SYSVOL Subscription,CN=Domain System Volume,CN=DFSR-LocalSettings,CN=<the server name>,OU=Domain Controllers,DC=<domain> msDFSR-Enabled=FALSE 

msDFSR-options=1

There is no CN=SYSVOL Subscription,CN=Domain System Volume,CN=DFSR-LocalSettings for DC1.  There is for DC2.

I'm at the point now I believe this to be the thing that needs to be fixed first.  

Is there a way to get these attributes recreated?

DC1 obviously has to remain a DC and holder of the roles, but I can essentially do whatever is needed to on DC2.

I have a ton of info on this and a lot of logs, but that's probably enough to start the conversation.  Thanks in advance...

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-29*

Hello   

Good day!  

Please run net share on each Domain Controller and check if the two folders are shared.  

  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-29*

also forgot to mention, this does not exist either:

-  Under the default naming context, browse to DC=domain > OU=Domain Controllers > CN=servername > CN=DFSR-LocalSettings > CN=Domain System Volume. In this step, servernamerepresents the name of the target DC.

From the non-auth synch directions.....in other words the DC itself is missing a bunch of attributes :)

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-29*

There's no AD replication issues.

And yes I was trying to do the non-authoritative synch....issue is:

CN=SYSVOL Subscription,CN=Domain System Volume,CN=DFSR-LocalSettings...and so on

does NOT exist for the DC1 server, which is the one that has a correct up to date version of SYSVOL...

DC2 has the completed path with all the attributes, but that's the one with the incomplete copy of sysvol.

Took a lot of digging into but that right there is unequivocally the first hurdle that needs to be resolved, and it's been troublesome finding some info on how to recreate the SYSVOL tree.  But I found this How to rebuild the SYSVOL tree using DFSR | TechTarget which is the road I'm going down now.  Fingers crossed.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-29*

Hello willmeister,  

Thank you for posting in Microsoft Community forum.

Firstly, please check the AD replication again on PDC using the commands below.  

repadmin /showrepl >C:\rep1.txt  

repadmin /replsum >C:\rep2.txt  

repadmin /showrepl * /csv >c:\repsum.csv

If there is no any error of these result, it seems AD replication works fine.  

Secondly, if AD replication works fine, you can try the steps of part "How to perform a non-authoritative synchronization of DFSR-replicated sysvol replication (like D2 for FRS)" for DC2 (non-authoritative DC).  

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-28*

Im thinking i might need to copy the valid sysvol folder from DC1 to DC2 and then do an authoritative synch from there...but still again, don't have a msDFRS-Enabled flag on the DC1 object so can't set that to false....
