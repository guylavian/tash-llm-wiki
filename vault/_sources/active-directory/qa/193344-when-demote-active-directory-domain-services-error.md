---
title: "When demote Active Directory Domain Services error \"DFS Replication: Access is Denied\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/193344/when-demote-active-directory-domain-services-error
question_id: 193344
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# When demote Active Directory Domain Services error "DFS Replication: Access is Denied"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/193344/when-demote-active-directory-domain-services-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a secondary AD DS, then I clone it to three secondary AD DS. All three AD DS have the same hostname. Two secondary AD DS I turned off the replication to the primary AD DS. One secondary AD DS wants me to demote to change the hostname and wants me to replicate it to the primary AD DS. But when I demote the AD DS an error appears:  

The operation failed because:  

DFS Replication: Access is denied.  

"Access is denied."  

Even though I use the administrator user and when I demote the AD DS, the two AD DSs whose replication died and I turned off the server, why did the error still appear?  

How do I fix it so that I can demote the AD DS and replicate it again?  

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-11*

From the active healthy domain controller, it can be deleted but the AD DS that will be deleted is still there and later on in active healthy domain controller the AD DS returns when replication is running

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-11*

From the top the the tree right-click and choose Change Domain Controller to another active healthy domain controller.    

    

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-11*

Thanks @Anonymous    for the answers given, but when I try to manually delete the domain controller an error appears like this :    

    

When I try to clean up AD DS like this :

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-12-11*

Hi,    

Thanks for sharing here!    

I would agree with @Anonymous   you can perform a forceful remove for the DCs if you can't demote it successfully.    

For steps you can refer to the links provided above.    

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-10*

The simplest solution may be to remove from network then perform cleanup.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

--please don't forget to Accept as answer if the reply is helpful--
