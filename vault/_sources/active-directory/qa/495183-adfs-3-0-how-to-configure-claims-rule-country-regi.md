---
title: "ADFS 3.0 - how to configure claims rule - country/region"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/495183/adfs-3-0-how-to-configure-claims-rule-country-regi
question_id: 495183
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS 3.0 - how to configure claims rule - country/region

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/495183/adfs-3-0-how-to-configure-claims-rule-country-regi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am fairly new to ADFS configuration. I have been asked to set up a claim to send the SAML response to our vendor on country based on the field Country/Region in AD.  I can confirm that all our users have the Country/region populated with country New Zealand. I can also see the relevant fields populated in Attribute editor e.g  c = NZ, co = New Zealand, countryCode = 554.  

When I go into the Edit Claims rules in ADFS, I cant see how to configure this using the Claim rule templates. Do i need to use the "Send Claims using a custom rule"? If so, how to i do configure it? Ive tried google searches and cant find anything obvious...  

Your advice is much appreciated.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-07-30*

You can do that with the wizard. No need of a custom claim rule.    

You pick the template "Send LDAP Attributes as Claims". Then you can use something like this:    

    

The attributes on the LDAP Attribute column can be typed manually even if they are not in the dropdown. Yo can just double click on the fied and type the attribute you want (and don't let the auto complete mess with you, just type the letter "c" for example and if the autocomplete does "company" with it, just manually delete "ompany").     

On the Outgoing Claim Type column, you can also type something manually. Here is send the attribute "c" into a claim called "claim:country/c". But you can call that outgoing claim as you want. Usually the application will tell you what names they want. Here I used a URI format because if your application is using WS-Federation (they also use SAML tokens), the claim type has to be in a URI format. But if your application is SAML2 service provider, you can just type "c" if you'd like.
