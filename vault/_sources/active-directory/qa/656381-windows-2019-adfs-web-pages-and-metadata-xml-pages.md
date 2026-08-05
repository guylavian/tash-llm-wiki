---
title: "Windows 2019 ADFS Web pages and metadata.xml pages missing - no web access after install"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/656381/windows-2019-adfs-web-pages-and-metadata-xml-pages
question_id: 656381
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Windows 2019 ADFS Web pages and metadata.xml pages missing - no web access after install

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/656381/windows-2019-adfs-web-pages-and-metadata-xml-pages (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Windows Server  2019 ADFS Web pages and metadata.xml pages missing   

unable to get ADFS working with claim based apps as web access URLs not working and unable to verify webpages or metadata.xml   

No IIS virtual directory created for ADFS too.  

help!

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-12-08*

ADFS doesn't use IIS since Windows Server 2012 R2. It is built directly on the top on the HTTP.sys.  

The federation metadata file is always available without authentication by default. You need to use the following URL:  https://ADFSFARMURL/FederationMetadata/2007-06/FederationMetadata.xml  

Where `ADFSFARMURL` is the FQDN of your farm not the FQDN of the server where the farm is. It has to be the right FQDN (not the IP address either) because of TLS/SNI (which in a nutshell will allow the TLS tunnel only if the FQDN that the client is sending is matching the FQDN registered in the HTTPs endpoint).
