---
title: "ADFS SSL Renewal"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/40375/adfs-ssl-renewal
question_id: 40375
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS SSL Renewal

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/40375/adfs-ssl-renewal (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So I am very new to AD FS and have been dropped in it.

I have an SSL Cert that is going to expire in 7 days time.

The production System has 2 AD server with FS on and 2 Proxy Server.

I have created a test plaform that mimics the production as best I can and I purchased a test SSL, however I have installed and I get a few errors, which mention certauth.adfs.mytestdomain.com

The Production enviornment does not show those errors.

The production Cert also has adfs and mfa in it (as does the test System)

So here are my Questions

-   Does anyone know exactly what type of Certifcate should be purchased?

-   To perform the update of the SSL I think I need to do the following?  

    Import the new SSL and make it exportable,  

    Import that on all other Servers  

    Run a powershell script, it should then update all the other servers to use the new Cert?  

    I have to also update the Service Communications, Token-Decrytping and Token Signing Certs using the AD FS Tool (which looks at the moment to use the same SSL cert still active? Is that correct?)

-   What about the Relaying Parties, Do I need to do something with them?

-   Thanks

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2020-06-29*

Hi Plaudonn,  

I am only using the public certs are that is currently what is set at the moment.  

I am happy to go to self-signed if that is the best option.  But at the moment the Current Cert expires on the 4th July.  

The company and the previous IT person has purchased a new SSL certs and have installed that on the two AD FS servers and the Proxies Servers.  

So I am guessing that my process to update now should be;  

Add the new SSL Cert to the Token Signing and Token Decryption as secondary.  Do this, I guess will allow the relaying parties to update their information automatically if they are pulling the Metadata?  

Wait a could of days and change the Service Certicate in the AD FS Admin tool over to the new Cert.  

Run the Powershell Script on the Master ADFS box and update the thumbprint to point to that new Certificate.  I read that this then updates all other Proxies and ADFS servers using remote powershell, but I can I run the same powershell on the other AD FS and Proxy Boxes?  

Update the Binding on IIS as that also use the Certicate for the mfa.domain.com website?  

One further question.  I added the Public SSL Certificates as secondary on Token Signing and Decryption, I assume that that should not impact anything? Just we are now having reports that when users try to access O365 and they get redirected to the ADFS page to signin, they are getting an error?  

Thanks  

Chris

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2020-06-26*

Thanks once again for the super quick response.    

Sorry to be a little slow on the uptake here and after reading the Guide on Secondary Certificates    

I guess I will need to use a public signed certificate as it is currently set at the moment.    

In that case using a new Public Cert,  I guess I just follow those steps in the link above .    

I then have a secondary for both the Token-Signing and Token-Decrypting, as the current SSL expires on the 4th July I could make them Primary on the 3rd July.    

So I'm hoping these will be the last few questions, I hope!    

So If I make them secondary, what do I need to do for the relaying Parties?    

So, before my time, it appears that a new SSL Certificate for adfs.domain.com has already been purchased and looks like it has been installed on all ADFS and Proxy Servers, although, on the Primary ADFS, the account running running ADFS service was not set to read, so I have set that and will need to do the others.    

On the New Cert, I noticed that the Friendly name is not adfs.domain.com, like the previous one, will that matter?     

Thanks    

Chris

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2020-06-26*

certauth.adfs.mytestdomain.com is the URL used when you do certificate based authentication on port 443 (like user certificates). It is called alternate hostname binding. Historically certificate based authentication is using a different port: 49443. But because this port is often blocked in public network, starting Windows Server 2016 we introduce the ability to do the certificate based authentication over 443 but it has to use a different name.    

So you can ignore this error message if you are not using certificate based authentication. If you need it and want to use it, you need to add the Subject Alternate Name certauth.adfs.mytestdomain.com to your TLS/SSL certificate. This is explained here.    

Regarding the "type" certificate it is a TLS certificate It is described here. It must be a X509 v3 certificate (CNG keys are not supported) . To update the certificate, import it on the local store of each ADFS nodes, then you need two commands on the ADFS primary server.    

```
Set-AdfsCertificate -CertificateType "Service-Communications" -Thumbprint ''  
Set-AdfsSslCertificate -Thumbprint ''
```

This is also explained here. You also need to make sure the ADFS service account has the permissions to read the private key of the certificate. If you are using the same certificate on the WAPs (recommended), you also need to run the following on your WAP servers:    

```
Set-WebApplicationProxySslCertificate -Thumbprint ''
```

There is nothing to do on the relying party trusts when you update this certificate.    

Token-Signing and Token-Decrypting certificates should not be TLS certificates (they could but there is no value of paying for these two). You can use the default self-signed certificates for these two. Updating those two certificates will break the trust with the relying party trusts and external claim provider trusts (not the Active Directory one though). So if you change them, tell the admins of the parties to update their configuration. This is documented here. By default we use self-signed certificates and they renew automatically.     

Have a look and let us know if you need more clarity!
