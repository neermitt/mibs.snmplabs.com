#
# PySNMP MIB module H3C-PBR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-PBR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:10:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, TimeTicks, Unsigned32, MibIdentifier, iso, Counter64, Integer32, Gauge32, ObjectIdentity, ModuleIdentity, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "TimeTicks", "Unsigned32", "MibIdentifier", "iso", "Counter64", "Integer32", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Counter32", "NotificationType")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
h3cPBR = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 113))
h3cPBR.setRevisions(('2010-12-10 15:58',))
if mibBuilder.loadTexts: h3cPBR.setLastUpdated('201012101558Z')
if mibBuilder.loadTexts: h3cPBR.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cPBRObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 113, 1))
h3cPBRGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 113, 1, 1))
h3cPBRMibTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 113, 1, 2))
h3cPBRNexthopTrapEnabled = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 113, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPBRNexthopTrapEnabled.setStatus('current')
h3cPBRTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 113, 1, 2, 1))
h3cPBRNexthopAddrType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 113, 1, 2, 1, 1), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cPBRNexthopAddrType.setStatus('current')
h3cPBRNexthopAddr = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 113, 1, 2, 1, 2), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cPBRNexthopAddr.setStatus('current')
h3cPBRTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 113, 1, 2, 2))
h3cPBRTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 113, 1, 2, 2, 0))
h3cPBRNexthopFailedTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 113, 1, 2, 2, 0, 1)).setObjects(("H3C-PBR-MIB", "h3cPBRNexthopAddrType"), ("H3C-PBR-MIB", "h3cPBRNexthopAddr"))
if mibBuilder.loadTexts: h3cPBRNexthopFailedTrap.setStatus('current')
mibBuilder.exportSymbols("H3C-PBR-MIB", h3cPBRTraps=h3cPBRTraps, h3cPBRTrapsPrefix=h3cPBRTrapsPrefix, h3cPBRMibTrap=h3cPBRMibTrap, h3cPBRNexthopAddrType=h3cPBRNexthopAddrType, h3cPBRObjects=h3cPBRObjects, h3cPBRTrapObjects=h3cPBRTrapObjects, h3cPBRNexthopAddr=h3cPBRNexthopAddr, PYSNMP_MODULE_ID=h3cPBR, h3cPBRGlobal=h3cPBRGlobal, h3cPBR=h3cPBR, h3cPBRNexthopTrapEnabled=h3cPBRNexthopTrapEnabled, h3cPBRNexthopFailedTrap=h3cPBRNexthopFailedTrap)