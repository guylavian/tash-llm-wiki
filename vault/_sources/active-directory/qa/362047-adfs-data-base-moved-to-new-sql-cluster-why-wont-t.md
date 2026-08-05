---
title: "adfs data base moved to new sql cluster why wont the  adfssrv service t start on the secondary adfs server?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/362047/adfs-data-base-moved-to-new-sql-cluster-why-wont-t
question_id: 362047
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# adfs data base moved to new sql cluster why wont the  adfssrv service t start on the secondary adfs server?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/362047/adfs-data-base-moved-to-new-sql-cluster-why-wont-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

ADFS data base moved to new SQL  2019 cluster and now the adfssrv service will not start on the second adfs server. I am using a gmsa to  run the service . My servers are all server 2019 . The adfsdata bases are in a SQL Availability Group. I was able to set the connection string on my primary ADFS server but the service wont start on the secondary to access the new location now. Any ideas?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-20*

ok ok Thank for the response -- server number 1 is ok and on server number 2 the service wont start. The errors from server number 2 are simply that the service cannot start:  

The Federation Service configuration could not be loaded correctly from the AD FS configuration database.   

Additional Data   

Error:    

ADMIN0012: OperationFault  

Which makes sense because the old database is offline / detached and server number 2 is still pointing in that direction.   

That being said I think I know what I did wrong, but I am not sure how to fix it. Looking at the following blog I think I did what his guy (https://www.joshyuhasey.com/?p=172) is saying not to do.   

Read the following and mainly the paragraph wrapped in asterisks:  

"IMPORTANT: Use the below commands to see what settings are currently in the ADFS servers.  

$adfsSecurityTokenService = Get-WmiObject -namespace root/ADFS -class SecurityTokenService  

$adfsSecurityTokenService.ConfigurationDatabaseConnectionString  

Example Output: Data Source=<sqlservername>;Initial Catalog=AdfsConfigurationV3;Integrated Security=True;Min Pool Size=20  

get-AdfsProperties | select artifactdbconnection  

Example Output: Data Source=<sqlservername>;Initial Catalog=AdfsArtifactStore;Integrated Security=True;Min Pool Size=20  

The trick here is that you need to run both command but the get/set-adfsproperties command only works when ADFS is running. The first WMI command will only work when ADFS is stopped. If you stop ADFS, run the first WMI command, and try to start ADFS it may fail to start. Then you can’t run the second command. So the order of these commands is very important.  

How to switch it:  

Run the below commands while everything is running.  

The temp put one will fail. Ignore this.  

The set-adfsprops command should work (it won’t if adfs is off)  

Stop adfs services  

Run temp put again (should work now)  

Rename DBs on old server (to ensure you are no longer using them)  

Start services.  

Do this on both ADFS servers.  

$adfsSecurityTokenService = Get-WmiObject -namespace root/ADFS -class SecurityTokenService  

$adfsSecurityTokenService.ConfigurationdatabaseConnectionstring=”Data Source=<sqlservername>;Initial Catalog=AdfsConfigurationV3;Integrated Security=True;Min Pool Size=20″  

$adfsSecurityTokenService.put()  

Set-AdfsProperties –artifactdbconnection “Data Source=<sqlservername>;Initial Catalog=AdfsArtifactStore;Integrated Security=True;Min Pool Size=20”  

"  

I am tempted to bring another server online and just kill this one.
