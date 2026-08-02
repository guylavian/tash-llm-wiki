---
title: "SCCM Active directory discovery full not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/181739/sccm-active-directory-discovery-full-not-working
question_id: 181739
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
---
# SCCM Active directory discovery full not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/181739/sccm-active-directory-discovery-full-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have a problem when I launched a full system discovery.  

I don't retrieve the new attributes informations, and the full scan runs during few minutes(3-4) instead of 2 hours usually.  

Does somebody can help me or has any idea of my issue?  

Thank you by advance  

Mohamed SAKHO

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-01*

This is not really a CM issue, it is an AD issue. I would look at those object in AD.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-01*

No I didn't clone the AD neither the CM environment.  

I just tried to discover others OU but it's the same things...  

I also set the system discovery directly to the domain level but it the same.  

I don't know how to troubleshoot this issue.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-01*

So what exactly have you done to troubleshoot these errors?   

Did you clone you AD or CM environments?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-01*

Hello @Garth Jones   ,    

Thank you for your answer.    

On the at the time when launched the full discovery, it shows the following lines:    

WARN: Failed in LookupAccountSidW. LastError: 0x534	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

ERROR: Failed to resolve a full AD path for the member entry (CN=S-1-5-21-254631761-919945742-1819828000-3157,CN=ForeignSecurityPrincipals,DC=vincic-fr,DC=grpsc,DC=net), continuing to next value	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

WARN: Failed in LookupAccountSidW. LastError: 0x534	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

ERROR: Failed to resolve a full AD path for the member entry (CN=S-1-5-21-254631761-919945742-1819828000-2980,CN=ForeignSecurityPrincipals,DC=vincic-fr,DC=grpsc,DC=net), continuing to next value	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

WARN: Failed in LookupAccountSidW. LastError: 0x534	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

ERROR: Failed to resolve a full AD path for the member entry (CN=S-1-5-21-71844251-1705847533-83388525-1795,CN=ForeignSecurityPrincipals,DC=vincic-fr,DC=grpsc,DC=net), continuing to next value	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

WARN: Failed in LookupAccountSidW. LastError: 0x534	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

ERROR: Failed to resolve a full AD path for the member entry (CN=S-1-5-21-254631761-919945742-1819828000-2910,CN=ForeignSecurityPrincipals,DC=vincic-fr,DC=grpsc,DC=net), continuing to next value	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

WARN: Failed in LookupAccountSidW. LastError: 0x534	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

ERROR: Failed to resolve a full AD path for the member entry (CN=S-1-5-21-71844251-1705847533-83388525-1292,CN=ForeignSecurityPrincipals,DC=vincic-fr,DC=grpsc,DC=net), continuing to next value	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

WARN: Failed in LookupAccountSidW. LastError: 0x534	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

ERROR: Failed to resolve a full AD path for the member entry (CN=S-1-5-21-71844251-1705847533-83388525-1894,CN=ForeignSecurityPrincipals,DC=vincic-fr,DC=grpsc,DC=net), continuing to next value	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

WARN: Failed in LookupAccountSidW. LastError: 0x534	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

ERROR: Failed to resolve a full AD path for the member entry (CN=S-1-5-21-71844251-1705847533-83388525-1989,CN=ForeignSecurityPrincipals,DC=vincic-fr,DC=grpsc,DC=net), continuing to next value	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

WARN: Failed in LookupAccountSidW. LastError: 0x534	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

ERROR: Failed to resolve a full AD path for the member entry (CN=S-1-5-21-254631761-919945742-1819828000-1792,CN=ForeignSecurityPrincipals,DC=vincic-fr,DC=grpsc,DC=net), continuing to next value	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

WARN: Failed in LookupAccountSidW. LastError: 0x534	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

ERROR: Failed to resolve a full AD path for the member entry (CN=S-1-5-21-254631761-919945742-1819828000-1271,CN=ForeignSecurityPrincipals,DC=vincic-fr,DC=grpsc,DC=net), continuing to next value	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

WARN: Failed in LookupAccountSidW. LastError: 0x534	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

ERROR: Failed to resolve a full AD path for the member entry (CN=S-1-5-21-254631761-919945742-1819828000-1963,CN=ForeignSecurityPrincipals,DC=vincic-fr,DC=grpsc,DC=net), continuing to next value	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

WARN: Failed in LookupAccountSidW. LastError: 0x534	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)    

ERROR: Failed to resolve a full AD path for the member entry (CN=S-1-5-21-71844251-1705847533-83388525-1324,CN=ForeignSecurityPrincipals,DC=vincic-fr,DC=grpsc,DC=net), continuing to next value	SMS_AD_SYSTEM_DISCOVERY_AGENT	01/12/2020 10:11:23	7512 (0x1D58)

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-01*

What exact does the log file show is happening?
