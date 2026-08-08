---
title: "Fetch attributes from Active Directory when ADFS is used as SAML Broker/Proxy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1427462/fetch-attributes-from-active-directory-when-adfs-i
question_id: 1427462
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Fetch attributes from Active Directory when ADFS is used as SAML Broker/Proxy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1427462/fetch-attributes-from-active-directory-when-adfs-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!  

Is it possible to fetch attributes from Active Directory when ADFS is used as a SAML Broker/SAML Proxy and the authentication takes place at an external 3rd party Claims Provider?  

So the setup are something like the following:  

Application (Replying Party Trust) <-> ADFS <-> External IDP (Claims Provider Trust)  

The external IDP in this case just authenticates the user and returns one single SAML Attribute in the SAML Response called "uid".   

I want to use the value in that claim/attribute and match that towards the "employeeID" in local Active Directory that ADFS is using and then fetch some additional attributes from that user in local AD, for example mail.  

I have tried a lot different claim rules for testing this out but none seems to be working because ADFS wants {0} to be formatted as 'domain\user' in the query towards Active Directory.  

So here is an example of claim rule that I've been playing with  

c:[Type == "uid"]

 => issue(store = "Active Directory", types = ("mail"), query = ";(&(objectClass=user)(employeeID={0}));mail;{0}", param = c.Value);

Let's assume the uid in the SAML Response from the external Claims Provider is "123456"  

If "uid" is present in the SAML Response from the external Claims Provider then I want ADFS to search in AD for users with objectClass=user and employeeID=123456, fetch the mail attribute from that user and then release a SAML Response containing that attribute value.   

But ADFS always complains about the third part in the claim rule, the last {0}, as it expect that to be in format 'domain\user'. And I have not yet find a way to get around that issue..  

c:[Type == "uid"]

 => issue(store = "Active Directory", types = ("mail"), query = ";(&(objectClass=user)(employeeID={0}));mail;{0}", param = c.Value);

Can I solve this somehow? Or am I forced to use another attribute store than Active Directory?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-17*

The solution was very simple for this.  

Just add 'domain\random' to your claim, something like this:  

c:[Type == "uid"]

=> issue(store = "Active Directory", types = ("mail"), query = ";(&(objectClass=user)(employeeID={0}));mail;DOMAIN\random", param = c.Value);
