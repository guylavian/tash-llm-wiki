---
title: "Restored default domain controller policy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/483674/restored-default-domain-controller-policy
question_id: 483674
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Restored default domain controller policy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/483674/restored-default-domain-controller-policy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We applied some security setting on domain controllers and our application broke.  

These were many security GPOs added that it was difficult to figure out how to fix it.  

Next we decided to restore the "default domain controller policy" by creating a new domain with new DCs.  

The new default domain controller policy  GPO was restored on the original domain's domain controllers.  

See errors below:  

Running enterprise tests on : ds.domain.com  

Starting test: LocatorCheck  

Warning: DcGetDcName(GC_SERVER_REQUIRED) call failed, error 1722  

A Global Catalog Server could not be located - All GC's are down.  

Warning: DcGetDcName(PDC_REQUIRED) call failed, error 1722  

A Primary Domain Controller could not be located.  

The server holding the PDC role is down.  

Warning: DcGetDcName(TIME_SERVER) call failed, error 1722  

A Time Server could not be located.  

The server holding the PDC role is down.  

Warning: DcGetDcName(GOOD_TIME_SERVER_PREFERRED) call failed, error 1722  

A Good Time Server could not be located.  

Warning: DcGetDcName(KDC_REQUIRED) call failed, error 1722  

A KDC could not be located - All the KDCs are down.  

......................... ds.domain.com failed test LocatorCheck

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-21*

Hello @David Kim  ,    

Thank you for posting here.    

To better understand your question, please confirm the following information at your convenience.    

1-Based on the description "we decided to restore the "default domain controller policy" by creating a new domain with new DCs", I understand you have backed up the "default domain controller policy" on DC in the old domain as below, right?    

    

2-Based on the description "The new default domain controller policy GPO was restored on the original domain's domain controllers", how did you restore default domain controller policy GPO on new DC in the new domain from backed up default domain controller policy GPO on DC in the old domain?    

In my test lab, when I back up GPO named 111 （in domain a.local）, I can restore this GPO to only GPO named 111 in the same domain （in domain a.local）.    

    

If I restored GPO named 111（in domain a.local） to another GPO named 222 in the same domain （in domain a.local）, then I will see message "No backups found".    

Or if I copied backed up GPO named 111 （in domain a.local）to DC in domain named b.local and restored the backed up GPO named 111 to any GPO in b.local, then I will see message "No backups found".    

    

3-Where did you see the errors you mentioned above? Or the errors above appears after you run one command (what command)?    

Would you please check and view all GPO settings within Default Domain Controllers Policy on DC in the old domain? If so, I suggest you had better configure these GPO settings on Default Domain Controllers Policy on new DC in the new domain.    

Hope the information above is helpful to you.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
