---
title: "GPO Proxy Whitelist Blocking Windows OS Patches on Shop Floor"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5825959/gpo-proxy-whitelist-blocking-windows-os-patches-on
question_id: 5825959
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Independent Advisor"]
---
# GPO Proxy Whitelist Blocking Windows OS Patches on Shop Floor

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5825959/gpo-proxy-whitelist-blocking-windows-os-patches-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey everyone, I manage the IT for a busy manufacturing floor. The guys on the line use a shared profile on the terminals, which I've locked down tight using Group Policy so they cant surf the web during shifts. They only have permission to hit our internal servers, databases, and a couple of essential external pages, which I handled through the proxy override list without a hitch. However, I absolutely cant get Windows Updates to pull through this restrictive setup. I pasted alot of Microsoft domains into the whitelist, but the OS still flat out refuses to download any patches. The production managers are breathing down my neck because these unpatched rigs are starting to lag and throw weird security alerts. Does anyone know what I'm missing here?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-03-17*

Hello,

This problem is directly tied to how Windows Update communicates through restrictive proxy and firewall configurations. It’s not related to Windows 365 Enterprise or Windows for Business—it’s a pure infrastructure and networking issue. The reason your updates are failing is that Windows Update requires access to a specific set of Microsoft endpoints, and unlike normal web browsing, it uses multiple domains, CDNs, and sometimes hard‑coded IP ranges. Simply whitelisting a handful of Microsoft URLs in the proxy override list is not sufficient.

For Windows 10/11 and Server 2022/2025, the required endpoints include windowsupdate.microsoft.com, update.microsoft.com, download.windowsupdate.com, *.update.microsoft.com, *.windowsupdate.com, *.delivery.mp.microsoft.com, and *.dl.delivery.mp.microsoft.com. Additionally, the Windows Update client uses the Delivery Optimization service, which requires access to *.do.dsp.mp.microsoft.com. If those are blocked or only partially whitelisted, the update agent will connect but fail to download payloads.

Another common oversight is SSL inspection. If your proxy or firewall is performing TLS interception, the Windows Update agent will reject the connection because it requires a direct trusted Microsoft certificate chain. You need to bypass SSL inspection for the update domains.

The most reliable way to handle this in a locked‑down environment is to configure Group Policy or MDM to point clients to Windows Update for Business or to an internal WSUS server. WSUS allows you to control patch distribution without opening broad internet access. If you must use direct Windows Update, you need to ensure that all the required domains and CDNs are whitelisted and excluded from proxy filtering. Microsoft maintains an official list of required endpoints in their documentation, and you should mirror that list exactly rather than trying to guess or paste domains piecemeal.

In short, your updates are failing because the restrictive proxy is blocking or inspecting traffic to required Microsoft update endpoints. Either configure WSUS internally or expand your proxy whitelist to include the full set of Windows Update and Delivery Optimization domains, with SSL inspection disabled for those. Once that’s in place, the VMs will patch normally without breaking your browsing restrictions.

I hope you've found something useful here. If it helps you get more insight into the issue, it's appreciated to accept the answer. Should you have more questions, feel free to leave a message. Have a nice day!

Domic Vo.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-03-17*

Windows Update traffic is more complex than a few single domains and also depends on how the proxy is configured (user vs system level, HTTP RANGE support, TLS, etc.). With a very restrictive proxy allowlist, several things must be in place or updates will fail even if some Microsoft URLs are whitelisted.

Key points to check and configure:

-  Configure the proxy for the system account (WinHTTP), not just the user

-  Windows Update uses WinHTTP, not the user’s browser proxy.

-  If the proxy is only set via user GPO/IE settings, Windows Update will fail.

-  Configure the proxy at system level using WinHTTP, for example:

```
netsh winhttp set proxy ProxyServerName:PortNumber
```

     or import from the (locked-down) IE settings:

```
netsh winhttp import proxy source=ie
```

-  This must be done on the terminals (or via a startup script/management tool) so the Windows Update service can reach the internet through the proxy.

-  Ensure the proxy supports HTTP RANGE requests

-  Windows Update uses WinHTTP with Partial Range requests (RFC 7233).

-  If the proxy blocks or breaks RANGE requests, downloads will fail or behave badly.

-  Adjust the proxy to allow HTTP RANGE requests, at least for Windows Update endpoints such as:

-  `*.download.windowsupdate.com`

-  `*.dl.delivery.mp.microsoft.com`

-  `*.delivery.mp.microsoft.com`

-  If RANGE requests cannot be allowed, updates may still work but will download more data (no delta patching), so bandwidth usage increases.

-  Allow the correct Microsoft endpoints through the proxy/firewall

-  Windows Update and related services use multiple endpoints. In locked-down environments, Microsoft recommends explicitly allowing the documented Windows and Microsoft 365 endpoints.

-  For Windows clients and Windows Update, review and allow the endpoints documented under:

-  Windows Update client policies firewall and proxy requirements

-  Manage connection endpoints for Windows 10/11 Enterprise (per OS version)

-  If using Windows Autopatch or Intune/Windows Update for Business, also ensure the listed Autopatch and Intune endpoints are allowed (for example `mmdcustomer.microsoft.com`, `mmdls.microsoft.com`, `*.webpubsub.azure.com`, and the Microsoft 365 URL/IP ranges if applicable).

-  If using WSUS, configure WSUS/proxy behavior correctly

-  If updates are offered from an on-premises WSUS server, ensure:

-  The clients can reach WSUS directly or via the system proxy.

-  If WSUS is HTTP-only and a system proxy is not configured, scanning may fail by default.

-  There is an MDM policy `./Device/Vendor/MSFT/Policy/Config/Update/SetProxyBehaviorForUpdateDetection` that allows using the user proxy as a fallback for WSUS scan when only an HTTP WSUS is available. This is less secure but can be used in tightly controlled environments.

-  Avoid conflicting or overly restrictive GPOs on Windows Update

-  Misconfigured or conflicting Windows Update policies can cause unexpected behavior. If you have many GPOs touching Windows Update, review them against Microsoft’s guidance for configuring automatic updates.

In practice, to get your shop-floor machines patching again while keeping users locked down:

-  Set the proxy at system level via `netsh winhttp` (or equivalent) so Windows Update can reach the internet.

-  Update the proxy allowlist to:

-  Permit HTTP RANGE requests for the key Windows Update download endpoints.

-  Include the documented Windows 10/11 and Microsoft 365/Intune/Autopatch endpoints relevant to your environment.

-  If using WSUS, verify WSUS connectivity and consider the `SetProxyBehaviorForUpdateDetection` policy if you rely on an HTTP WSUS behind a proxy.

Once these are in place, Windows Update should be able to download patches even though interactive web browsing remains blocked for the shared shop-floor profile.

References:

-  Windows Update issues troubleshooting

-  Policy CSP - Update

-  Configure your network
