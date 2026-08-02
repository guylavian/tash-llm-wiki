---
title: "ADFS Group DN filter not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/276136/adfs-group-dn-filter-not-working
question_id: 276136
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS Group DN filter not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/276136/adfs-group-dn-filter-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all  

We have an  ADFS 3.0 farm, and need to include the group DN into the claim.  

I have the following 2 rules, the first one successfully pulls the DNs of all the user's groups. Worried about token bloat since some users have 100s of group memberships.  

The second one (Role) is meant to filter based on DNs starting with "CN=xyz*", but its not working.  

Any ideas?  

GroupSID  

c1:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]  

 && c2:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/groupsid"]  

 => issue(store = "Active Directory", types = ("http://group/DN"), query = "(&(objectClass=group)(objectSID={1}));distinguishedName;{0}", param = c1.Value, param = c2.Value);  

RoleSID  

c:[Type == "http://group/DN", Value =~ "^CN=XYZ*"]  

 => issue(claim = c);

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-24*

So being a techie and not a dev at all, plus no readily info on those matter, I have had to "figure out" how this stuff works. So I assume "issue" statement is like a closure on the command stating that nothing else needs to be done, issue that part of the token, and "add" takes that dataset into the next rule as per sequential order?  

I amended my rule and tested, got the exact expected result so thank you for the assistance. (and teaching me something!)  

PS i think the extra characters were copy paste errors
