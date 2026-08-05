---
title: "AD CS: Deploying Cross-forest Certificate Enrollment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/357894/ad-cs-deploying-cross-forest-certificate-enrollmen
question_id: 357894
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# AD CS: Deploying Cross-forest Certificate Enrollment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/357894/ad-cs-deploying-cross-forest-certificate-enrollmen (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I’m having trouble with AD CS: Deploying Cross-forest Certificate Enrollment.  I’ve followed the article’s for 2012 r2.  Things just don’t seem to work.    

Right now I can see certificates assigned to a user.  I am getting an error about the certificate chain.    

I had used dspublish to put my ROOTCA’s and intermediate ca’s crt and Crl in.      

Can anyone verify what dspublish commands to use and which certs and crls would be required?  Maybe I didn’t publish the certs everywhere or used a wrong switch.   A working example would be amazing.    

Also in lab I have everything deployed and it works for workstation certs.  It is failing for user certs.  The error says it cannot find the directory object.  It seems like maybe I need to do something with referrals but I don’t know what to do.    

    

Some extra details:         

We have two forests with a full trust relationship        

I have one cert server in one forest.  I install the addition roles all on the same server.  When I installed I didn’t use a service account and opted for machine account.   Delegation is setup.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-16*

Okay I resolved my issues. It was difficult since the 2012 doc is incomplete and you have to borrow from the 2008 doc to figure it out.

The missing part from the 2012 doc is the adding of the certs. The best way to get the certs is to login to the CA Web Service and download the certificate chain. Save each certificate in the chain. Copy over to the other Forest and install. LDAP Referrals do need to be enabled.

```
REM Enable LDAP referral support on enterprise CAs.
REM certutil -setreg Policy\EditFlags +EDITF_ENABLELDAPREFERRALS

REM RUN ON DC in remote domain
REM Verify CA is working
certutil -config "offlineROOTCA\Cert Root PKI" -ca.cert C:\Scripts\rootcapki.cer 

REM Install certs
certutil -dspublish -f C:\Scripts\rootcapki.cer RootCA

REM Publish enterprise CA certificates from the resource forest into the NTAuthCertificates and AIA containers in each account forest.
REM Verify CA is working
certutil -config "certsrv03.domain.com\Cert Issuing PKI" -ca.cert C:\Scripts\issuingpki.cer

REM Install certs
certutil -dspublish -f C:\Scripts\issuingpki.cer NTAuthCA
certutil -dspublish -f C:\Scripts\issuingpki.cer SubCA
```

Also for my other error that was hard to figure out. The issue came up because we have a Forest that shares the same name space as another Forest. Basically we have overlapping forest names. Full trust and all that.

Ex:  

Forest1.com  

Forest2.Forest1.com

With this I had to learn about creating LDAP referrals in AD. The article below was so helpful because Microsoft just gave you a vb script.

To use ADSI Edit to create a cross-reference object  

-  In ADSI Edit, expand the Configuration container.  

-  Right-click the CN=Partitions container, click New , and then click Object .  

-  For Select a class , you can create objects of only class crossRef , which is already selected. Click Next .  

-  For the cn attribute, in the Value box, type a name that describes the location, and then click Next .  

-  For the nCName attribute, in the Value box, type the distinguished name for the external domain, and then click Next .  

-  For the dnsHostname attribute, in the Value box, type a DNS name for the server that hosts the domain directory partition, or type the domain name.  

-  When you are sure that your entries are correct, click Finish.

From <http://cloud365.in/unable-to-create-crossref-object-in-active-directory/>
