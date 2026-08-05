---
title: "Windows Server 2019 ADCS on Azure VMs as global PKI service"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/212172/windows-server-2019-adcs-on-azure-vms-as-global-pk
question_id: 212172
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
---
# Windows Server 2019 ADCS on Azure VMs as global PKI service

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/212172/windows-server-2019-adcs-on-azure-vms-as-global-pk (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have been asked to plan, design, and deploy a Microsoft Windows Server 2019 ADCS PKI deployed on Azure Windows VMs.  It will be a two-tier architecture with an offline standalone rootCA and six Enterprise issuing subCAs deployed in six Azure regions to include three paired regions with each region having a primary and secondary region i.e. US, EU, ad APAC paired regions.  AD DS domain controller global catalog servers and ADCS issuing subCAs will be deployed in each Azure region.  ASR will not be used for failover AD DS domain controllers and AD CS server in the primary regions to the secondary regions due to some risk when using ASR for failover of AD DS domain controllers and its dependent ADCS subCAs.  

The rootCA will be stood up then brought offline per best practices during the deployment of the subCAs and all other components.  Before the the rootCA is taken offline all recommended security measures per guidance will be followed for securing the rootCA.  All recommended security measures per guidance will taken with all other components comprising the global PKI.  

The PKI will need to support both AD DS joined computers with autoenrollment and for non AD DS aware devices.  The same certificate templates will be created and deployed on all subordinate CAs so that each subordinate issuing CA will have the same certificate templates.  The encryption algorithm will use ECC p384. The PKI will need to support both NDES (used for SCEP with Intune/Endpoint Manager) and NPS for integration with Azure MFA using the NPS extension.  

The CDP and AIA will use both CRL and OSCP and will be deployed on separate web servers.  This takes into account older systems that are not OCSP aware.  Those web servers will be geo load balanced using Citrix ADC LBs and a CNAME record will be configured for the LB VIP which clients will use to access the CDP and AIA.   

What I am not clear about is how best to configure the Certificate Web Enrollment Service (CES) and the Certificate Web Enrollment Policy (CEP) so it is globally accessible and resilient to any outages for systems that are not AD DS aware and cannot use autoenrollment thus requiring manual enrollment.  Should the CES and CEP be deployed on separate web servers and load balanced?  If these services are deployed on separate web servers and load balanced would it randomly select an issuing subCA?  What impact would this have on BC/DR?  What if the issuing CA is no longer available?  Since each issuing subCA will contain the same certificate templates, would it even matter if the certificate needs to be renewed or revoked and renewed?  Please advise.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-01-08*

Here is an example Two-Tier PKI solution developed to provide services for OSX, Windows, and Linux clients globally. The solution is based on ADCS and an external HSM/Root CA.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-13*

Shawn,  

For my design, I have separated the AIA, CRL, and OSCP onto separate web servers.  NDES is also on a separate group of web servers.  Both are load balanced.  Since The NDES servers must be publicly available, they will be load balanced either with Azure Front Door w/ WAF or an internal LB that is front ended by a AppGW w/WAF.  Ultimately NetScalars will replaced the native Azure LBs.  The Certification Authority Web, Certificate Enrollment Web, and Certificate Enrollment Policy Web services will be installed on all Enterprise Subordinate Issuing CAs.  Azure AD MFA with the NPS extension will be configured on the domain controllers since putting both first and second authentication in the same place is a best practice.  The ECC encryption algorithm will be used for everything.  Not absolutely sure that iOS and Android will support ECC or if NDES can be configured with ECC but will vet in my lab.  Certificate templates will be configured to use ECC by changing compatibility to Windows 7/Windows Server 2008 R2.  Will published common set of certificate templates to AD where applicable for autoenrollment and create common set of certificate templates not published to AD for those services and servers that require manual enrollment.  Must carefully see how AD site topology and GPOs are configured when using autoenrollment and create special AD OUs to organize where GPOs are applied.  After all this is working, will look to tackle Windows Hello for Business configuration.  Have documented everything from planning, design, deployment step-by-step, and operations and security operations in a 250 page document.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-08*

Shawn,  

I had planned to use separate web servers for the CDP and AIA, OCSP.  No revocation lists will be published in the rootCA per best practices and only configured and published in the Enterprise Subordinate Issuing CAs  I had already considered using separate and additional web servers for the CES and CEP.  Yep, an two different Azure internal LB VIPs would be used as the DNS RR for both the CRL and Web Enrollment i.e. crl.contoso.com and pki.contoso.com for example.    

I plan to use the exact same certificate templates for all issuing CAs globally.  Both manual and auto enrollment will be configure for non AD aware or joined servers and for AD aware and joined servers, respectively.  Yes, I am aware auto enrollment is configured for user and server certificates through GPOs.  When using multiple globally disperse Enterprise issuing subCAs, I am determining if I need to publish the CDP and AIA for every subCA to the share on the web servers intended for revocation lists.  Simple enough to do but cannot find much documentation about this topic when using multiple subCAs.  As you mentioned, if load balancing the CES, CEP, and NDES, which subCA it picks for certificate enrollment is based upon AD DS sites for AD joined servers but it seems that servers not joined to AD using manual enrollment randomly select the closest subCA from what I've been able to determine.  I am testing in a lab and will see if that is the case.  

Thanks,  

Gary

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-08*

I deployed a global PKI solution providing these capabilities. My recommendation is to utilize a VIP in front of the exposed web services load balanced to the different servers providing the web services in each region. One caveat to this approach is that Microsoft's IIS is not suitable as a transparent proxy. We had to rely on a separate solution to provide the required transparent proxying. The other recommendation I would make is that I'd separate the web services to different IIS servers. You can stack all of the different (NDES, CES, CEP) onto a single box, however, you will find that management and troubleshooting complexity is greatly increased if you do.  

Let me try to address your other concern regarding which CA will provide the PKI services. A certificate issued by a Windows CA will always try to utilize the issuing CA for any certificate services. With this in mind, we developed a process to provide initial enrollment utilizing scripts to request on behalf of the recipient. The certificates were then delivered via a one time use Google code. Once initial enrollment was performed any subsequent certificate services would be performed at the initial issuing CA. We need to keep in mind that CEP/CES are secure gateways to the internal ADCS services, any logic is performed through GPO's and certificate policies defined on published templates within the issuing CA.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-29*

Hello,    

Thank you so much for posting here.    

We mainly focus on the problems or issue about on-premises Active Directory. To deploy the two-tier architecture PKI, we could refer to the below document.    

https://social.technet.microsoft.com/wiki/contents/articles/15037.ad-cs-step-by-step-guide-two-tier-pki-hierarchy-deployment.aspx    

But according to our description, we will make the deployment of PKI on Azure Windows VMs with an offline standalone root CA and six Enterprise issuing subCAs deployed in six Azure regions. So sorry that we are not professional with Azure. If we have any concerns, we could turn to Azure-Active-Directory forum to see whether they could provide further assistance (Select the tag of Azure-Active-Directory).    

As for the CES and CEP, we could check whether the below document could help.     

https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/certificate-enrollment-web-services/ba-p/397385#:~:text=CES%20is%20another%20web%20service,not%20connected%20to%20the%20domain.    

https://social.technet.microsoft.com/wiki/contents/articles/7734.certificate-enrollment-web-services-in-active-directory-certificate-services.aspx    

Thank you so much for your understanding and support.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
