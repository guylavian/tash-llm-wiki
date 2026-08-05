---
title: "Error configuring WAP for ADFS: event ID 395 (Trust Established) followed by 276 (Unable to Authenticate)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/301595/error-configuring-wap-for-adfs-event-id-395-trust
question_id: 301595
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Error configuring WAP for ADFS: event ID 395 (Trust Established) followed by 276 (Unable to Authenticate)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/301595/error-configuring-wap-for-adfs-event-id-395-trust (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When I launch the Install-WebApplicationProxy command, I can see the proxy's certificate being added to both the adfs servers (active/active with SQL backend) and even the record added in the SQL table [AdfsConfigurationV4].[IdentityServerPolicy].[ProxyTrusts]. The process however fails, with errors 276 logged after the iniziatl 395 on the ADFS servers. I tried everything I could find on the web but nothing worked for me...   

ADFS servers are 2019 and wap are 2016 and 2019 (tried to upgrade one of them to check if the error was about different windows versions).  

bye, Dario

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 2 · updated: 2022-04-22*

I was helping the customer exact same error  

Here is the env   

ADFS farm level : 3 (Server 2016 level, Mixed mode)  

ADFS servers :4   

2016 ADFS servers :2  

2019 ADFS servers: 2 (recently added)  

WAP servers  

2016 WAP servers :2  

2019 WAP servers: 2 (recently added)  

Recent change was happened 3/20  

Proxy trust was known working condition was 3/31 and it renewed new cert for next 20 days   

(you can see this cert in WAP local computer store with 20 days validity, every time you stablish WAP trust )  

Exactly 4/20 - it failed , then customer rebooted other WAPs and all failed too  

We saw 395 (trust established) and even id 276 not able to authenticate (401 unauthorized)   

Validated account used local administrators across all ADFS servers  

Then mean time, we removed 2019 ADFS recently added to see if that fix the problem  

Removed 2019 nodes and cleaned up via (set-adfsfarminformation).RemoveNodes Server2019xyz.domain.com  

However error stay as it is , no change   

We spot the cert comes from WAP local machine store to ADFS server "ADFS Trusted device" store on both the ADFS servers  

Difference is after few min one of the ADFS server remove that cert and logs 276 error message (why?!)  

Then discussed with my colleague (Amit), who is also expert in ADFS side.  

What's scenario does ADFS accept WAP trust and reject after few min ?.. delete the cert .. log 276  

 Amit thinked and looked at it, Then its spark him to check binding via "netsh http show sslcert"  

We spot the difference between "CTLStoreName" the bad server is empty (There you go!.. fix is just cutting a  cake)  

Once we delete and re-add below bindings with correct CTL store on the faulty ADFS server   

"netsh http add sslcert hostnameport=sts.domain.com:443 certhash=<certhash> appid={guid} certstorename=MY sslctlstorename=AdfsTrustedDevices "  

The WAP trust which was hanging on "Waiting for proxy trust relationship to be synchronized across farm."  

Message disappeared and its finished smoothly   

Then we added remaining WAP as well  

Next day customer informed, He re-added back all 2019 ADFS and validated binding are okay post adding back as well  

Then how it was working till 3/31. then customer informed few more info  

Before adding the server 2019 , they did change SSL cert and trust was fine post change  

(because WAP uses exiting session until reboot ) -that's why they didnt see immediately any issues with WAP trust-My assumption here  

We never imagined, this would be the cause. spent 3hrs finding out.   

Sharing here. so it would be useful for someone in future
