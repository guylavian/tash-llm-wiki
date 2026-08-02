---
title: "In active directory site and services\\public key services\\enrollement services entry was deleted"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/167683/in-active-directory-site-and-servicespublic-key-se
question_id: 167683
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# In active directory site and services\public key services\enrollement services entry was deleted

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/167683/in-active-directory-site-and-servicespublic-key-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How do I  recreate the entry under active directory site and services\services\public Key Services\enrollement services  

How to recreate the entry

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-11-19*

Hi,    

For the containers public Key Services\enrollment services you can recreate through ADSI:    

    

For the entries under the  enrollment services    

Firstly, i would suggest you backup the CA:    

In the Certification Authority snap-in, right-click on the CA name, go to All Tasks and click Backup CA    

Within the Backup wizard, backup both the CA database and the Public/Private Key Pair    

Backup the CA locally (C:\Backup, etc.)    

Then, in the Certification Authority snap-in, right-click on the CA name, go to All Tasks and click Renew CA Certificate    

Choose the same key (the No selection in the UI)    

Check for the pkiEnrollmentService object in CN=Enrollment Services,CN=Public Key Services,CN=Services,CN=Configuration,DC=Contoso,DC=com using ADSIEdit    

Confirm the object also was also created using site and services.
