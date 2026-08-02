---
title: "How to merge 2 Domain Controllers of the same Domain that has been separated for a long period?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1600459/how-to-merge-2-domain-controllers-of-the-same-doma
question_id: 1600459
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# How to merge 2 Domain Controllers of the same Domain that has been separated for a long period?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1600459/how-to-merge-2-domain-controllers-of-the-same-doma (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,
I have a setup with 2 domain controllers for the same domain (PriDC and SecDC).
PriDC was installed and had users and computers added to it. PriDC is located in SiteA.
I will install SecDC, a few months after PriDC, in a different location, SiteB.
My idea is to take an image from PriDC and load it in a temp server in SiteB. After that, I will install SecDC and join as Domain Controller to this Domain.
Consider that I have to create other users and join other computers to this Domain Controller (SecDC) in SiteB.
I need to have both Domain Controllers running on the same site (SiteA).
My question is: Is it possible to merge both Domain Controllers (PriDC and SecDC) whitout loose any information or object? Will they synchronize?
Thanks.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-02-28*

Hello Daniel Dias,
Thank you for posting in Q&A forum.
Based on your description, you want to clone the PriDC, load it on the temporary server of sitB, and then do a clean install of the SecDC on sitB and join it to the temporary server. Regarding your question, my advice is not to clone PriDC. Here are my recommendations:

-  It is not recommended to clone PriDC: It is not recommended to clone domain controllers as duplicate SIDs, USNs, and other issues may occur.

-  Install SecDC directly on PlantB: Perform a clean install of Windows sever on the server that will be the SecDC. Then add the ADDS role and promote the server to a domain controller. During the upgrade process, select the option to add domain controllers to an existing domain.
3.AD Data Replication: Once a SecDC is promoted to a domain controller, it automatically replicates data from the PriDC. Make sure that the two domain controllers can communicate with each other and that the necessary ports are open.

-  Create a user and join a domain: You can create a new user account and join the computer to a domain in PlantB. These changes will also be replicated to PlantA's PriDC.

-  Transfer of all nodes of Plant B to Plant A: When you are ready to transfer everything to PlantA, make sure that the domain controllers are already synchronized. You can use repadmin /showrepl >C:rep1.txt to check the AD replication status and DCDIAG /v to check the running status of the DC.

Tip: By default, all the Domain Controllers in the same domain (even if they are in different site) will replicate with each other).
I hope the information above is helpful.
If you have any question or concern, please feel free to let us know.
Best Regards,
Daisy Zhou

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2024-02-27*

Hi Daniel,

Thanks for your question here on Q&A.

Why take a clone of PriDC to SecDC, as when if you install DC services on SecDC (clean) and join that DC to the domain/install DC services - all the data from PriDC (the primary DC in the domin) is cloned over to SecDC in the process?

I will recommend that ay :)

See here: https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-#BKMK_GUI

"On the Deployment Configuration page, choose one of the following options:

-  If you are installing an additional domain controller in an existing domain, click Add a domain controller to an existing domain, and type the name of the domain (for example, emea.corp.contoso.com) or click Select... to choose a domain, and credentials (for example, specify an account that is a member of the Domain Admins group) and then click Next."

Else let me hear
