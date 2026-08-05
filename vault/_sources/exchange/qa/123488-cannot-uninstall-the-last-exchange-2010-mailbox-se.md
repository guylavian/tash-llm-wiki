---
title: "Cannot uninstall the last Exchange 2010 mailbox server (public folder replicas left)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/123488/cannot-uninstall-the-last-exchange-2010-mailbox-se
question_id: 123488
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Cannot uninstall the last Exchange 2010 mailbox server (public folder replicas left)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/123488/cannot-uninstall-the-last-exchange-2010-mailbox-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

after we moved our mail infrastructure to another organization, I am trying to uninstall my remaining Exchange 2010 servers (one CAS/HT, one mailbox). I am stuck with the message that there are still public folder replicas left in the public folder database.In fact, there are still remnants from more than 20 years with Exchange which I cannot delete ("modification... isn't allowed"):

Get-PublicFolder \NON_IPM_SUBTREE -Recurse

Name Parent Path

NON_IPM_SUBTREE  

EFORMS REGISTRY \NON_IPM_SUBTREE  

Events Root \NON_IPM_SUBTREE  

OFFLINE ADDRESS BOOK \NON_IPM_SUBTREE  

/o=****/cn=addrlists/cn=oabs/cn=Default Offline Address ... \NON_IPM_SUBTREE\OFFLINE ADDRESS BOOK  

OAB Version 2 \NON_IPM_SUBTREE\OFFLINE ADDRESS BOOK/o=MPAe/cn=addrlis...  

OAB Version 3a \NON_IPM_SUBTREE\OFFLINE ADDRESS BOOK/o=MPAe/cn=addrlis...  

OAB Version 4 \NON_IPM_SUBTREE\OFFLINE ADDRESS BOOK/o=MPAe/cn=addrlis...  

EX:/o=****/ou=Exchange Administrative Group (************.. \NON_IPM_SUBTREE\OFFLINE ADDRESS BOOK  

EX:/o=****/ou=******* \NON_IPM_SUBTREE\OFFLINE ADDRESS BOOK  

SCHEDULE+ FREE BUSY \NON_IPM_SUBTREE  

EX:/o=****/ou=Exchange Administrative Group (************.. \NON_IPM_SUBTREE\SCHEDULE+ FREE BUSY  

EX:/o=****/ou=******* \NON_IPM_SUBTREE\SCHEDULE+ FREE BUSY

Is there a supported way to get rid of them? Or do I really have to use ADSIedit to delete the public folder database? There are also still some recipients listed corresponding to the above folders. Where can I find them in ADSIedit

Thanks a lot

Georg.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2020-10-12*

You can  try this to remove the system folders if they are unneeded:    

```
Get-PublicFolder -Server  "\Non_Ipm_Subtree" -Recurse -ResultSize:Unlimited | Remove-PublicFolder -Server  -Recurse -ErrorAction:SilentlyContinue
```

https://learn.microsoft.com/en-us/previous-versions/office/exchange-server-2010/bb201664(v=exchg.141)#use-the-shell-to-delete-system-public-folders    

If that doesnt work... Honestly? I would just use adsiedit to delete the pf database - assuming you do not need public folders any longer.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-13*

Hello,  

I renamed the PF files, and with a new PF database, the uninstall worked.  

Thanks, Georg.
