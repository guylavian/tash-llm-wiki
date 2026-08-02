---
title: "Exchange hybrid - autodiscover not working for several accepted domains + teams calendar button not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/353951/exchange-hybrid-autodiscover-not-working-for-sever
question_id: 353951
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Exchange hybrid - autodiscover not working for several accepted domains + teams calendar button not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/353951/exchange-hybrid-autodiscover-not-working-for-sever (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We're having a problem with the external autodiscover of our accepted domains in our hybrid deployment (and therefor the teams calendar button not working).    

On-prem we have two DAG's with exchange 2016 CU19 installed. The hybrid setup is a full modern deployment.    

Internally autodiscover works fine because the devices are domain-joined and use SCP lookup. But externally autodiscover only works for our primary domain (we use a wildcard certificate for our on-prem exchange).    

The autodiscover A-record (autodiscover.contoso.com) points to our on-prem exchange, which works fine externally.    

From what I'm gathering (correct me if I'm wrong), you just rerun the hybrid wizard and when you get to the autodiscover step, you just tick off the accepted domains to enable autodiscover for these additional domains.    

This will also setup the necessary OAuth configuration for the Teams calendar button to show up properly.    

(Or alternatively you can add the accepted domains through EMS with the following command: Set-HybridConfiguration -Domains secondarydomain1.com, secondarydomain2.com, autod:primarydomain.com)    

I checked with "Get-HybridConfiguration" and the accepted domains do show up there.    

After doing this I waited two days (due to o365 retention), but autodiscover still didn't work. (testconnectivity analyzer still gave me errors, see attach)    

Afterwards I saw that there were no HCW TXT verification records defined to the external DNS for the primary and all additional domains. From searching the web, you need these for autodiscover to work properly    

(source: https://exitcodezero.wordpress.com/2014/03/31/using-the-autodiscover-domain-feature-to-enable-multiple-smtp-domains-in-your-hybrid-configuration/)    

So I created those and were validated succesfully. Waited two days and again nothing. (testconnectivity analyzer gave me the same errors)    

So I suppose the problem isn't DNS related anymore but something else... Because hybrid deployments don't support SRV, we removed the SRV records for these accepted domains.    

(source: https://learn.microsoft.com/en-us/previous-versions/technet-magazine/dn249970(v=msdn.10)?redirectedfrom=MSDN)    

It's not exactly clear to me but if you do the above steps (re-running the hybrid wizard and adding the HCW TXT verification records) you don't need the external CNAME record (autodiscover.outlook.com) as well anymore?    

Since autodiscover will use the HCW TXT records to resolve the autodiscover process? Searching the web I don't find a definitive answer for this...    

(source: https://community.spiceworks.com/topic/1990666-autodiscover-cname-hybrid-exchange)    

Can someone clarify on this? Because adding or removing the CNAME and SRV records didn't make any difference anyway.    

I'm not sure but I assume it's a federation trust issue. At first, when I checked the federation trust wasn't even enabled. When I did "Get-FederatedOrganizationIdentifier | fl" on my on-prem server it was disabled ("enabled" was set to False).    

Also the account namespace was blank and the value for domains was blank. In the attach you'll see before and after I enabled the FederationTrust...    

And from here autodiscover still doesn't work... Rerunning the hybrid wizard doesn't make any difference (reran the hybrid wizard countless times). In the attach you'll find the values for the FederationTrust on our Exchange Online tenant.    

Any advice from where to look now?    

Kind regards.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-14*

Hi,    

autodiscover is pointing to on-prem for our main domain. MX is pointing to Exchange Online, we can't change this because we use EOP (exchange online protection) as our spamfilter. Before the hybrid setup we used SRV records for all our other accepted domains. This worked without problems.    

But since the hybrid setup we are unable to get autodiscover to work for the other domains. And I don't know if this is indeed "normal" behavior. Like mentioned before, this microsoft article states SRV is not supported in a Hybrid setup: https://learn.microsoft.com/en-us/previous-versions/technet-magazine/dn249970(v=msdn.10)?redirectedfrom=MSDN    

Unless this changed since the article was written in 2016?    

Kind regards.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-13*

Thanks for anserwing.  

Yes it's indeed correct that some mailboxes may be migrated to Exchange Online (and some stay on-prem). AD accounts are hosted on local AD.  

The accepted domains are already configured on the onprem exchange. (as well as on the exchange online)  

Is autodiscover in this scenario (******@samedomain.com hosted on EXO, ******@samedomain.com hosted ONPREM) supported?  

Or is the only way to achieve this, to create a certificate that contains all the domain names?  

Because I thought the alternative, if you had 1 certificate with only 1 domainname (*.domain.com) you could achieve autodiscover for the other domains with "Set-HybridConfiguration -Domains secondarydomain1.com, secondarydomain2.com, autod:primarydomain.com"? Or is this a wrong assumption?  

Thank you for your time.  

Kind regards

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-13*

@Miba      

Internally autodiscover works fine because the devices are domain-joined and use SCP lookup.     

From above information, I think you also used those domain name on Exchange on-premises. (AD account hosted on local AD, some mailboxes may be migrated to Exchange online)    

You need to add those domain as accepted domain on your Exchange on-premises first.    

Then, you will need to create Autodiscover record on public DNS provider for those domains, then point those DNS record to Exchange on-premises. You also need to create a certificate contains all the domain name that you need to used(such as "*.domain.com","*.domain1.com","*.domain2.com").    

After that, you also need to create DNS lookup zone for those additional domain name on your DC's DNS manager. In this way, autodiscover request will could find your Exchange on-premises, then redirected to Exchange online if mailboxes hosted on Exchange online.    

About the teams issue, I would suggest you confirm with the Teams side.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
