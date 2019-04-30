#
# PySNMP MIB module A3COM-HUAWEI-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-DNS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:49:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, Integer32, Gauge32, IpAddress, Counter32, Bits, Unsigned32, ModuleIdentity, iso, MibIdentifier, ObjectIdentity, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Gauge32", "IpAddress", "Counter32", "Bits", "Unsigned32", "ModuleIdentity", "iso", "MibIdentifier", "ObjectIdentity", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
h3cDns = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97))
h3cDns.setRevisions(('2009-02-12 00:00',))
if mibBuilder.loadTexts: h3cDns.setLastUpdated('200902120000Z')
if mibBuilder.loadTexts: h3cDns.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cDnsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1))
h3cDnsStaticSrvIpTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 1), )
if mibBuilder.loadTexts: h3cDnsStaticSrvIpTable.setStatus('current')
h3cDnsStaticSrvIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-DNS-MIB", "h3cDnsStaticSrvIpType"), (0, "A3COM-HUAWEI-DNS-MIB", "h3cDnsStaticSrvIpAddr"))
if mibBuilder.loadTexts: h3cDnsStaticSrvIpEntry.setStatus('current')
h3cDnsStaticSrvIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: h3cDnsStaticSrvIpType.setStatus('current')
h3cDnsStaticSrvIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 1, 1, 2), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: h3cDnsStaticSrvIpAddr.setStatus('current')
h3cDnsStaticSrvIpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDnsStaticSrvIpPriority.setStatus('current')
h3cDnsStaticSrvIpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDnsStaticSrvIpRowStatus.setStatus('current')
h3cDnsDynamicSrvIpTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 2), )
if mibBuilder.loadTexts: h3cDnsDynamicSrvIpTable.setStatus('current')
h3cDnsDynamicSrvIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-DNS-MIB", "h3cDnsDynamicSrvIpType"), (0, "A3COM-HUAWEI-DNS-MIB", "h3cDnsDynamicSrvIpAddr"))
if mibBuilder.loadTexts: h3cDnsDynamicSrvIpEntry.setStatus('current')
h3cDnsDynamicSrvIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: h3cDnsDynamicSrvIpType.setStatus('current')
h3cDnsDynamicSrvIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 2, 1, 2), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: h3cDnsDynamicSrvIpAddr.setStatus('current')
h3cDnsDynamicSrvIpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDnsDynamicSrvIpPriority.setStatus('current')
h3cDnsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 2))
h3cDnsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 2, 1))
h3cDnsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 2, 1, 1)).setObjects(("A3COM-HUAWEI-DNS-MIB", "h3cDnsStaticSrvIpGroup"), ("A3COM-HUAWEI-DNS-MIB", "h3cDnsDynamicSrvIpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cDnsMIBCompliance = h3cDnsMIBCompliance.setStatus('current')
h3cDnsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 2, 2))
h3cDnsStaticSrvIpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 2, 2, 1)).setObjects(("A3COM-HUAWEI-DNS-MIB", "h3cDnsStaticSrvIpPriority"), ("A3COM-HUAWEI-DNS-MIB", "h3cDnsStaticSrvIpRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cDnsStaticSrvIpGroup = h3cDnsStaticSrvIpGroup.setStatus('current')
h3cDnsDynamicSrvIpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 2, 2, 2)).setObjects(("A3COM-HUAWEI-DNS-MIB", "h3cDnsDynamicSrvIpPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cDnsDynamicSrvIpGroup = h3cDnsDynamicSrvIpGroup.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-DNS-MIB", h3cDnsStaticSrvIpPriority=h3cDnsStaticSrvIpPriority, h3cDnsStaticSrvIpAddr=h3cDnsStaticSrvIpAddr, h3cDnsDynamicSrvIpPriority=h3cDnsDynamicSrvIpPriority, h3cDnsDynamicSrvIpGroup=h3cDnsDynamicSrvIpGroup, h3cDns=h3cDns, h3cDnsDynamicSrvIpType=h3cDnsDynamicSrvIpType, h3cDnsStaticSrvIpType=h3cDnsStaticSrvIpType, h3cDnsStaticSrvIpEntry=h3cDnsStaticSrvIpEntry, h3cDnsDynamicSrvIpEntry=h3cDnsDynamicSrvIpEntry, h3cDnsMIBConformance=h3cDnsMIBConformance, h3cDnsStaticSrvIpRowStatus=h3cDnsStaticSrvIpRowStatus, h3cDnsDynamicSrvIpTable=h3cDnsDynamicSrvIpTable, h3cDnsMIBCompliance=h3cDnsMIBCompliance, h3cDnsObjects=h3cDnsObjects, PYSNMP_MODULE_ID=h3cDns, h3cDnsStaticSrvIpTable=h3cDnsStaticSrvIpTable, h3cDnsStaticSrvIpGroup=h3cDnsStaticSrvIpGroup, h3cDnsMIBGroups=h3cDnsMIBGroups, h3cDnsDynamicSrvIpAddr=h3cDnsDynamicSrvIpAddr, h3cDnsMIBCompliances=h3cDnsMIBCompliances)