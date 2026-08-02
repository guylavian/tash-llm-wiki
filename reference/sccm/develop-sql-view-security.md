---
title: "SQL View Security"
type: reference
domain: sccm
slug: develop-sql-view-security
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/core/understand/sql-view-security
family: develop
documentKind: "article"
abstract: "Facilitate instance (or row) level security on core object classes. Using the Configuration Manager schema views, an application or user is operating outside of this security mechanism."
---

# SQL View Security

# Configuration Manager SQL View Security
The Configuration Manager object security mechanism, implemented in the SMS Provider, facilitates instance (or row) level security on core object classes. By using the Configuration Manager schema views, an application or user is operating outside of this security mechanism. This doesn't mean that the views can't be secured from unauthorized data access; however, security must be configured separately and is less precise than standard Configuration Manager object security. You can give a user read-only permission to access only the views and deny access to any internal Configuration Manager tables. The main security functionality that is lost in the view approach is the ability to secure specific object instances (such as packages and collections) separately for members of groups.

## See Also
 [Configuration Manager Schema View Mapping](../../../develop/core/understand/configuration-manager-schema-view-mapping.md)
 [Configuration Manager Schema SQL Views](../../../develop/core/understand/configuration-manager-schema-sql-views.md)
