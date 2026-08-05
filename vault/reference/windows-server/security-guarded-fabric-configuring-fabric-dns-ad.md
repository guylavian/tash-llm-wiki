---
title: "Configure the fabric DNS for guarded hosts (AD)"
type: reference
domain: windows-server
slug: security-guarded-fabric-configuring-fabric-dns-ad
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/security/guarded-fabric-shielded-vm/guarded-fabric-configuring-fabric-dns-ad
family: security
documentKind: "how-to"
abstract: "Learn more about: Configure the fabric DNS for guarded hosts (AD)"
---

# Configure the fabric DNS for guarded hosts (AD)

# Configure the fabric DNS for guarded hosts (AD)


>[!IMPORTANT]
>AD mode is deprecated beginning with Windows Server 2019. For environments where TPM attestation is not possible, configure [host key attestation](guarded-fabric-initialize-hgs-key-mode.md). Host key attestation provides similar assurance to AD mode and is simpler to set up.

A fabric administrator needs to configure the fabric DNS takes to allow guarded hosts to resolve the HGS cluster.
The HGS cluster must already be set up by the [HGS administrator](/windows-server/security/guarded-fabric-shielded-vm/guarded-fabric-initialize-hgs).



[!INCLUDE [Configure fabric DNS](../../../includes/guarded-fabric-configure-fabric-dns.md)]


## Next step

> [!div class="nextstepaction"]
> [Configure HGS DNS and a one-way trust](guarded-fabric-configure-dns-forwarding-and-trust.md)
