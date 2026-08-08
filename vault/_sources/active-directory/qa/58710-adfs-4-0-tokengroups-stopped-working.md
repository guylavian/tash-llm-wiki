---
title: "ADFS 4.0 tokenGroups stopped working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/58710/adfs-4-0-tokengroups-stopped-working
question_id: 58710
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS 4.0 tokenGroups stopped working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/58710/adfs-4-0-tokengroups-stopped-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I am currently running ADFS 4.0 in a 2012 R2 Domain. My colleague is upgrading the domain to 2019 so we have a mix of 2012 R2 and 2019 servers, but the functional level is still 2012 R2. Recently ( I don't know exactly when) my ADFS server stopped providing the tokenGroups claim for some users. It DOES work for others. I have no idea what's functionally different between those that are OK and those that are not. ADFS is using a GMSA and it's been fine for a over a year.  

My query is:  

```
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]
 => issue(store = "Active Directory", types = ("memberOf"), query = ";tokenGroups;{0}", param = c.Value);
```

This works fine for some users and not at all for others. I've use Firefox SAML tracer and verified that the tokenGroups claim is never put into the SAML response, for those that are not working.  

Any help would be greatly appreciated.  

--tim

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-08-04*

Is it consistent for these users?  

Does this persist after a restart of the ADFS service?  

The only way I can repro is by playing with the permissions of the service account on the user. Can you compare the security descriptor (i.e. the security tab) of a working user versus a non-working user?
