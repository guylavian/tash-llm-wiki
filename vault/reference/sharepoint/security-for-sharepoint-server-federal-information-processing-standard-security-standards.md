---
title: "Federal Information Processing Standard security standards and SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: security-for-sharepoint-server-federal-information-processing-standard-security-standards
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/security-for-sharepoint-server/federal-information-processing-standard-security-standards
family: security-for-sharepoint-server
documentKind: "reference"
abstract: "Learn about the Federal Information Processing Standard (FIPS) with SharePoint Server 2016 and SharePoint Server 2013."
---

# Federal Information Processing Standard security standards and SharePoint Server - SharePoint Server

Note

Federal Information Processing Standard security standards and SharePoint Server

# Federal Information Processing Standard security standards and SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint Server uses several Windows encryption algorithms for computing hash values that don't comply with Federal Information Processing Standard (FIPS) 140-2,  *Security Requirements for Cryptographic Modules*. These algorithms aren't used for security purposes; they're used for internal processing. For example, SharePoint Server uses MD5 to create hash values that are used as unique identifiers.

Because SharePoint Server uses these algorithms, it doesn't support the Windows security policy setting that requires FIPS compliant algorithms for encryption and hashing. This Windows security policy is managed through the **FIPSAlgorithmPolicy** registry key in Windows, which is described in the "Configure FIPS policy for a mixed environment" section of the following article:

- Additional System Countermeasures

FIPS 140-2 defines security standards that the United States and Canadian governments use to validate security levels for products that implement cryptography. For more information about FIPS 140-2, see the following references:

FIPS 140 Evaluation

FIPS Publications

The goal of FIPS is to provide a standardized way to ensure the security and privacy of sensitive information in computer systems of the United States and Canadian governments. Using a FIPS compliant algorithm for encryption of data over an open network is a key requirement for FISMA certification. The Windows FIPSAlgorithmPolicy registry key is not necessary or sufficient for FISMA certification, it's a useful enforcement tool for many solutions, but not SharePoint Server.

The FIPS contribution to FISMA certification is the strength of encryption used for security purposes. Security-related encryption within SharePoint Server is performed by using FIPS-compliant cipher suites.

For additional information about FISMA, see,Federal Information Security Management Act (FISMA) Implementation Project.

Additional resources

## Additional resources

- Last updated on 
		2024-05-30
