---
title: "ADFS endpoint configurations"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/645614/adfs-endpoint-configurations
question_id: 645614
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS endpoint configurations

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/645614/adfs-endpoint-configurations (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,  

I would like to check, there is ADFS server being setup in our development environment for testing purpose.  

currently the endpoint is being used as https://serverhostname.testdomain.com/adfs/ls   

There is a requirements from development team that the URL should be visible as https://adfs.testdomain.com/adfs/ls   

Where should i make the changes so the ADFS url is accesible using as https://adfs.testdomain.com/adfs/ls   

Please advise. TQ.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-01*

Hi there,    

Open the ADFS Management application, on the right, is the "Edit Federation Service Properties" and change the Federation service name and identifier with the new domain name. In your case, it will be https://adfs.testdomain.com/adfs/ls. Update the ADFS certificate that it uses.     

You can use this article to get the detailed steps behind the process https://social.technet.microsoft.com/wiki/contents/articles/37530.adfs-how-to-change-the-adfs-server-fqdn-from-one-domain-to-another.aspx    

AD FS user sign-in customization    

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/ad-fs-user-sign-in-customization    

-------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-11-30*

AD FS is leveraging SNI from TLS.  The hostname used to established the TLS tunnel has to match the ADFS farm name that you can see in the administrative console and in the output of `Get-ADFSProperties` (it is the name you pick at the installation).  

To have the server listen on another hostname, you need to add that name to the HTTP bindings. You can use the following command on the ADFS server:  

```
netsh http add sslcert ipport=adfs.testdomain.com:443 certhash= appid={5d89a20c-beab-4389-9447-324788eb944a}
```

You need to replace <hash of the TLS cert> with the actual hash.  

{5d89a20c-beab-4389-9447-324788eb944a} is the App Id of ADFS.  

If you are also using a WAP, the following command can be ran on the WAP:  

```
netsh http add sslcert ipport=adfs.testdomain.com:443 certhash= appid={f955c070-e044-456c-ac00-e9e4275b3f04}
```

{f955c070-e044-456c-ac00-e9e4275b3f04} is the APp Id of WAP.
