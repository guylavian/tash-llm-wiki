---
title: "ADFS 3.0: Custom Outgoing Claim Type?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/338796/adfs-3-0-custom-outgoing-claim-type
question_id: 338796
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS 3.0: Custom Outgoing Claim Type?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/338796/adfs-3-0-custom-outgoing-claim-type (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

So our ADFS guy left a while ago leaving me to hold the fort with zero previous ADFS experience. Mostly ok, however very basic setups or Vendors who know exactly what they need to integrate. I currently have a vendor who is insisting I return the user group membership as an array called "Groups". I told them I could do this using role or group as published in our metadata, however they are insisting it be called "Groups".  

I thought I might be able to do this by doing a transform of incoming claim type to outgoing claim type, I'm just ending up with errors though. I'm completely unfamiliar with doing anything like this, is it even possible using ADFS 3.0 On-Prem infrastructure? Would be very grateful if someone could lend assistance as the vendor neither has documentation or a willingness to help.  

Might help if I add what I've tried so far to get a custom attribute name to work. Found a similar issue elsewhere on the web whose solution was to create two seperate rules like this;  

1st Rule gets the users group membership and assigns it to a temporary store  

```
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]
 => add(store = "Active Directory", types = ("memberOf"), query = ";memberOf;{0}", param = c.Value);
```

2nd rule issues these results to the custom attribute name.  

```
c:[Type == "memberOf"]
 => issue(Type = "Groups", Value = c.Value);
```

I put each of these in their own custom rule in the order listed above which generates and error for me.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-04-03*

You can call your claim as you wish.    

SAML2 is fine with whatever format. When the application is using WS-Federation, the claim has to be in a URI format (like for example: namespace:item/stuff). They do not need to exist in your metadata not even in your list of claim definition.    

Note that memberof just gives you the direct memebership (no nested groups). And the format is a distinguishedName (like CN=group,OU=Apps,DC=contoso,DC=com). You might consider checking the building rules: Create a Rule to Send Group Membership as a Claim.
