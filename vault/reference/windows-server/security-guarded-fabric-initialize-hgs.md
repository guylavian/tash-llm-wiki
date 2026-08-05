---
title: "Initialize HGS"
type: reference
domain: windows-server
slug: security-guarded-fabric-initialize-hgs
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/security/guarded-fabric-shielded-vm/guarded-fabric-initialize-hgs
family: security
documentKind: "how-to"
abstract: "Learn more about: Initialize the Host Guardian Service (HGS)"
---

# Initialize HGS

# Initialize the Host Guardian Service (HGS)

When you initialize HGS, you specify the mode that HGS will use to measure the health of guarded hosts. There are two mutually exclusive options. For background information about which mode to choose, see [Guarded Fabric and Shielded VM Planning Guide for Hosters](guarded-fabric-planning-for-hosters.md).

The following topics cover deployment steps for each mode:

- [TPM-trusted attestation (TPM mode)](guarded-fabric-initialize-hgs-tpm-mode.md)
- [Host key attestation (Key mode)](guarded-fabric-initialize-hgs-key-mode.md)
- [Admin-trusted attestation (AD mode)](guarded-fabric-initialize-hgs-ad-mode.md)

You should perform these steps on a physical server.
