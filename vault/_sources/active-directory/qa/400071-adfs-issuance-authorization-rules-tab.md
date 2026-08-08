---
title: "ADFS Issuance Authorization Rules tab"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/400071/adfs-issuance-authorization-rules-tab
question_id: 400071
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Issuance Authorization Rules tab

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/400071/adfs-issuance-authorization-rules-tab (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In ADFS 3 (2012 r2) when restricting a access via Issuance Authorization Rules through Group SID, the group with a prefix # does not work. The value gets stripped off in the rule dialog box and user who is a member of that group is unable to login. When attempting to restrict access to a group that bears simple name (no special characters) it works. Is this a known issue?   

Also, is there a way to customize the rule that permits access to #abcd group ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-20*

So, it wasn't the hash. The GUI strips it off but the underlying SID was the same. The problem was the group was a distribution group. When it was switched to a "security" group type, it worked.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-19*

@Pierre Audonnet - MSFT       

Thank you.     

the get-adgroup didn't work with # in group name. Looked up dn from adsi and it began with \ # in DN name. Used the dn and Get-ADgroup returned the output with (S-1-...-5537) . Then created a "permit or deny Users based on incoming claim" and viewed its rule language. It had the same SID in Value = "^(?i)S-1-....-5537$". But in the GUI of the rule box it shows the Incoming Claim Value "Domain\abcd" instead of "Domain\ #abcd". It picked up the pre-2000 name instead it looks like.     

Also, this is a distribution group. Does it need to be a security group?     

[using \ and # together in this form results in # being displayed instead of \ # together so multiple edits. aplogies]

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-05-18*

I don't have a 2012 R2 environment to repro. And 2016/2019 work differently as we have Access Control Policies now.    

But if we suspect the GUI to be the issue, you can always create the rule direcly in "claim rule language".     

-  Create a rule for a group without the #.    

-  Look at the language it uses. You can edit the rule and click on:    

    

-  Get the SID of your group with the # using Get-ADGroup    

-  Create a rule using the custom option in the wizard:    

    

Paste the value you got from step 2 and replace the SID with the one you got in step 3.    

That should do the trick.
