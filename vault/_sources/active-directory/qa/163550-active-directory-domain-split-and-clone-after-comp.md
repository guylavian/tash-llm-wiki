---
title: "Active Directory domain split and clone after company demerger"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/163550/active-directory-domain-split-and-clone-after-comp
question_id: 163550
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory domain split and clone after company demerger

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/163550/active-directory-domain-split-and-clone-after-comp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day.  

We used to be part of one big company, let’s call it Company-A. Then a subsection of Company-A demerged (split-up) to form Company-B. Company-A continues to exist entirely separate from the newly created Company-B.   

So a new Active Directory domain Company-B.com was created for Company-B, and an AD trust was setup between Company-A.com domain and Company-B.com. We are currently busy migrating the users and computers demerging from Company-A to the new Company-B.com domain using ADMT. This is all working well.  

The idea was to migrate all Company-B AD objects from Company-A.com to Company-B.com, then “cut” the network between the two companies forever. The network cut will obviously mean we need to break the trust between the two AD domains, as they won’t be connected by network anymore. For an unknown reason the network “cut” date has been moved up by senior management, leaving inadequate time to migrate thousands of AD objects from Company-A.com to Company-B.com before the network cut (COVID lockdown and staff layoffs is playing a part). We thus need to keep the Company-A.com domain running and accessible on the Company-B side after the network cut, alongside the Company-B.com domain in a trust, which will allow us to migrate all remaining AD objects to the Company-B.com domain at our own pace. We at Company-B thus need to continue using the Company-A.com domain which is disconnected by network from the existing Company-A.com domain.   

So currently the primary domain controller is on Company-A.com on the Company-A side of the network (which we will lose network access to after the network cut), but we have several Company-A.com domain controllers on our property on Company-B side of the network.  

So I was thinking before the network cut, creating a new Company-A.com domain controller on our Company-B side of the network, promote to it Primary Domain Controller with the relevant FSMO roles, and then cut the network. The Company-A.com domain will keep functioning (internal to the network only, not externally) in a trust with the Company-B domain completely separate from the original Company-A.com domain, and we can migrate computers at our own pace, and decommission the Company-A.com domain once that is done.  

I hope I explained the situation well enough.  

So the question, will it be that simple (or even possible), or is there more to it that I’m not considering?

## Answer (community) — community member

*upvotes: 1 · updated: 2021-11-15*

Hi, okay so a lot has happened in the last year.  

To double check this I approached a reputable 3rd party that offers Active Directory consulting services, where I have a contact. And the answer from them was that yes, this is possible to do assuming it's done correctly (the ordering is very important).  

We planned it in a fair amount of detail, but this was the action plan at a high-level:  

- 	Make sure there are no required outstanding DFS replications (not likely, but good to check)  

- 	Make sure Company-B DNS forwarders point to local servers (not Company-A servers)  

- 	Backup domain controllers that hold FSMO roles.  

- 	Cut network between Company-A and Company-B, and test to verify no network communication can be possible between these two company networks  

- 	On Company-A side, break the AD trust between Company-A and Company-B domain. On Company-B side, keep AD trust in place  

- 	Verify again no network communication (especially AD related) are possible between the two companies before proceeding  

- 	Seize Company-A FSMO roles to local Company-B Domain Controllers  

- 	Validate Company-A to Company-B trust on Company-B side (no longer setup on Company-A side)  

- 	Cleanup AD sites and services (subnets of Company-A sites no longer applicable, as well as servers and also the sites)  

- 	Enable AD recycle bin (or confirm it is enabled)  

- 	Delete (or disable) all Company-A users from Company-A domain (on Company-B side)  

- 	Delete DNS zones not in use anymore  

- 	Cleanup DFS  

Unfortunately Company-A decided that it's "too much of a risk" to them for us at Company-B to keep their domain live at Company-B for a few more months to complete migrations, and that we had to complete by the original moved-up target date. Thus we were forced to bring in a team of contractors to come and do the migrations for us (our small internal team was already over capacity).   

It's all politics, there was no real risk to Company-A by us keeping their domain live for 3 more months, since the demerger was amicable and a level of trust still exists between the two companies as we signed contracts to do a lot of work together. In the end the trust break / network break didn't happen on schedule due to some lose ends on Company-A side because of a joint project which required the AD trust to remain in place for more than 3 months beyond schedule. Ended up us having to needlessly spend that money on the contractors to come and do our migrations, and the migrations ended up being finished about 3 months before the belated trust break...  

Thus we didn't get to actually keep the trust alive on our side, so I can't say how well it would have worked, but in theory it is sound and I see no reason why it wouldn't work.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-12*

I know this was a year ago, but wondering if this was successful. We are looking at solving a nearly identical problem.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-25*

Thanks, I'm busy setting up a simple test environment to test this, will respond with the results.  

Cheers  

Jimmy

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-11-17*

Hi,  

Theoretically, there should be no problem.  

Be careful not to disconnect the network while the migration is in progress.  

Before disconnecting from the network, make sure that the new DC has no problems and all replications have been completed; the fsmo role transfer is successful, and there is no problem with trust.  

I still recommend that you perform the operation after testing in the experimental environment.  

Best Regards,
