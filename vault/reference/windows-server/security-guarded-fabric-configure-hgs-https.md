---
title: "Configure HGS for HTTPS communications"
type: reference
domain: windows-server
slug: security-guarded-fabric-configure-hgs-https
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/security/guarded-fabric-shielded-vm/guarded-fabric-configure-hgs-https
family: security
documentKind: "how-to"
abstract: "Learn more about: Configure HGS for HTTPS communications"
---

# Configure HGS for HTTPS communications

# Configure HGS for HTTPS communications

By default, when you initialize the HGS server it will configure the IIS web sites for HTTP-only communications.
All sensitive material being transmitted to and from HGS are always encrypted using message-level encryption, however if you desire a higher level of security you can also enable HTTPS by configuring HGS with an SSL certificate.

[!INCLUDE [Configure HTTPS](../../../includes/configure-hgs-for-https.md)]
