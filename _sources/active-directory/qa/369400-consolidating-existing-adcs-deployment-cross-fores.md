---
title: "Consolidating Existing ADCS Deployment - cross-forest certificate enrollment (Windows Server 2016/2019)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/369400/consolidating-existing-adcs-deployment-cross-fores
question_id: 369400
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Consolidating Existing ADCS Deployment - cross-forest certificate enrollment (Windows Server 2016/2019)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/369400/consolidating-existing-adcs-deployment-cross-fores (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, currently we have 3 production forests completely isolated from one another with each production forest having 1-Tier PKI with Enterprise Issuing CA only so there is no Standalone Offline Root CA other CAs are its subordinates. I am thinking of creating a brand new management forest where I would like to implement 2-Tier PKI capable of enrolling certificates to users/computers in all 3 production forests - InfoSec team will allow two-way trust between production forests and management forest with selective authentication in direction production forest --> management forest.    

I was following article and scenario covered is when there is Standalone Offline Root CA with its Enterprise Subordinate Issuing CA in each forest. Does it mean I can not perform consolidation and have 2-Tier PKI only in management forest enrolling certificates to users/computers in all 3 production forests? If answer is that I can not what options are left?    

Thank you very much in advance!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-29*

Hello @Bojan Zivkovic  ,    

Thank you for your update.    

Q: I do not know if same procedure can be used in my scenario where in each production forest there is only Enterprise Issuing Root CA (1-Tier PKI).    

A: I think it does not matter with PKI tier.    

Tip: Please test the PKI consolidating in the test environment first, if there is no any problem, then operate it in the production environment if needed.     

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-26*

Two things to point out here.  

First, I would like to have certificate autoenrollment functionality as well hence I think two-way forest trust is a must (with selective authentication if InfoSec do not allow forest-wide authentication). For instance having CM client certificate auto-enrolled to all CM clients in all forests.  

Second, in article I was referring to, consolidation of PKI was depicted in details but with Sub CA in each forest having "the same" Standalone Offline Root CA as its CA - I do not know if same procedure can be used in my scenario where in each production forest there is only Enterprise Issuing Root CA (1-Tier PKI).

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-26*

Hello @Bojan Zivkovic  ,    

Based on the description above, I understand you have 3 production forests and management forest, and you want to deploy 2-Tier PKI with Standalone Offline Root CA and Enterprise Subordinate Issuing CA in management forest.    

production forest1 <==> two way forest trust with management forest    

production forest2 <==> two way forest trust with management forest    

production forest3 <==> two way forest trust with management forest    

And you want 2-Tier PKI in management forest to enroll certificates for 3 production forests.    

From the link you provided, I think that your understanding is right. I mean if you have multiple PKIs in multiple forests, you can consolidate to one central PKI in one Active Directory Domain Services (AD DS) forest.    

For your requirements, you can consider the article below, but there is no need to have a forest trust between the forests.    

Test Lab Guide Mini-Module: Cross-Forest Certificate Enrollment using Certificate Enrollment Web Services    

https://social.technet.microsoft.com/wiki/contents/articles/14715.test-lab-guide-mini-module-cross-forest-certificate-enrollment-using-certificate-enrollment-web-services.aspx    

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
