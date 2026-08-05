---
title: "How to get all users of ADFS with all attributes (eg. name, email, phone etc.)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/566015/how-to-get-all-users-of-adfs-with-all-attributes-e
question_id: 566015
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# How to get all users of ADFS with all attributes (eg. name, email, phone etc.)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/566015/how-to-get-all-users-of-adfs-with-all-attributes-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi I created the custom claim for that so please check the below claim which is created by me:  

c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]  

 => issue(store = "Active Directory", types = ("http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress", "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname", "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/password"), query = "(&(objectClass=user)(objectCategory=person));mail,givenName,sn;{0}", param = c.Value);  

using that claim I can log in successfully. you can check the below SS when clicking on the below link:  

https://drive.google.com/file/d/1lV2zb6uV8PWzqk4qsgwVb6iFu-15O4bN/view?usp=sharing  

but a problem like I get total email =500 but name=200 so I can not be mapping this, so I want this data with any particular one claim/rule  

I already create below claim but this is not working:  

c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]  

 && c1:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/surname"]  

 && c2:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/name"]  

 => issue(Type = "http://Mydomainname.com/members", Value = c1.Value + "  " + c2.Value);  

So I want something like the above in one type of link and get all the details of all users.  

please click on the below link the check hows my code for that getting outgoing claims:  

https://drive.google.com/file/d/1Mwo7-ai0v1503dIr_37SkFhXZJYF-a4F/view?usp=sharing  

Please guide me on what I can do for that my main concern is I want all users of ADFS using the ADFS authentication, So I have already done Authentication but I can not get all user's details in a single claim/rule.  

Thanks & regards  

Bhavdip Talaviya

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2021-10-13*

You can use the following rules.

-   Extract the email and the given name and add it to the pipeline:    c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]  

    => add(store = "Active Directory", types = ("http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress", "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname"), query = ";mail,givenName;{0}", param = c.Value);

-   Then you can concatenate the two into a new claim (here claim:/custom/emailname as an example but you can use whatever):    c1:[Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"]  

    && c2:[Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname"]  

    => issue(Type = "claim:/custom/emailname", Value = "email=" + c1.Value + ", Givenname=" + c2.Value);

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-11-22*

Hi @Pierre Audonnet - MSFT   where is the access token in this below response:    

    

suppose I got an access token then After getting an access token how to get all user's details using that access token?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-11-21*

hi @Pierre Audonnet - MSFT   I am not asking for the access token,    

But it is about access token. The only point of the issuance rules is to "issue" claims that go into the access token.    

The query you are doing are returning things for all users. Why would an access token have the list of all users and and all email addresses?    

@Pierre Audonnet - MSFT   when I am using the below query in custom claim it will return all uses so basically I need all users so I use the below query: (&(objectClass=user)(objectCategory=person))    

You should not query info about other accounts than the one you are authenticating unless that information is then used for authorization by the relying party trust. But why would an application want all users info to authorize 1 user? There is very likely a misconception somewhere.    

In the first rule I suggested:    

```
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]  
=> add(store = "Active Directory", types = ("http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress", "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname"), query = ";mail,givenName;{0}", param = c.Value);
```

There is no LDAP filter. So we just get the attributes mail and givenName from the user. A bit like if you were doing a "base" LDAP search on the current user. For we can concatenate them like I suggested without worrying about multi-values.     

For the sake of the exerice of thought, if you retrieve a multi-value attribute from the AD attribute store, you won't be able to map it 1:1 with another attribute. You are essentially creating two distinct arrays. If "array1" = value1, value2 and "array2" = valueA, valueB doing the concatenation of "array1" and "array2" into a new claim called "stringConcat" will effectivly create a multi-values claim with all possibilities.    

"stringConcat" = value1valueA, value2valueA, value1valueB, value2valueB    

In certain cases we can use "dynamic" claim types and make it work. But the AD attribute doesn't support those. With this one, you can only add/issue claims by specifying their claim type with a string (no dynamic values).    

So, let's step back and restate... What do you need? and why (what does the application need to do with the data)?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-07*

hi, @Pierre Audonnet - MSFT   Can you please check below :    

hi I got the given name & Email from the below custom claim rule:    

c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]    

=> issue(store = "Active Directory", types = ("http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress", "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname"), query = "(&(objectClass=user)(objectCategory=person));mail,givenName;{0}", param = c.Value);    

but in this case, I got all emails in this (http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress )claim like below    

    

But I want both values in single outgoing claim like email= anon@USER   , Givenname=abc    

Can you please help me to get the user's details like above?    

Please help me.    

Thanks & regards.    

Bhavdip talaviya

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-10-01*

I am not sure I understand the request.  

You can create a rule to extract all the attributes you want. You need to know what attributes you want first and then you can send them as claims in the token.  

Note please, share images directly on the post (you can just copy/paste them) as opposend at links this way.
