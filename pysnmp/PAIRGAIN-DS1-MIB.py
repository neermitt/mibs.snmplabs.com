#
# PySNMP MIB module PAIRGAIN-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PAIRGAIN-DS1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:27:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
pgainDSLAM, = mibBuilder.importSymbols("PAIRGAIN-COMMON-HD-MIB", "pgainDSLAM")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, Gauge32, Counter32, Counter64, NotificationType, IpAddress, Unsigned32, ModuleIdentity, ObjectIdentity, Integer32, Bits, MibIdentifier, TimeTicks, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "Counter32", "Counter64", "NotificationType", "IpAddress", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "Integer32", "Bits", "MibIdentifier", "TimeTicks", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DateAndTime, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "RowStatus", "DisplayString")
pgds1Mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 927, 1, 9, 17))
if mibBuilder.loadTexts: pgds1Mib.setLastUpdated('0003030000Z')
if mibBuilder.loadTexts: pgds1Mib.setOrganization('Pairgain Technologies Inc.')
pgds1MibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 9, 17, 1))
pgds1ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 9, 17, 1, 1), )
if mibBuilder.loadTexts: pgds1ConfigTable.setStatus('current')
pgds1ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 9, 17, 1, 1, 1), ).setIndexNames((0, "PAIRGAIN-DS1-MIB", "pgds1LineIndex"))
if mibBuilder.loadTexts: pgds1ConfigEntry.setStatus('current')
pgds1LineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 17, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgds1LineIndex.setStatus('current')
pgds1IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 17, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgds1IfIndex.setStatus('deprecated')
pgds1LineBuildout = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 17, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgds1LineBuildout.setStatus('current')
mibBuilder.exportSymbols("PAIRGAIN-DS1-MIB", pgds1MibObjects=pgds1MibObjects, pgds1ConfigTable=pgds1ConfigTable, pgds1LineIndex=pgds1LineIndex, pgds1LineBuildout=pgds1LineBuildout, pgds1Mib=pgds1Mib, pgds1IfIndex=pgds1IfIndex, pgds1ConfigEntry=pgds1ConfigEntry, PYSNMP_MODULE_ID=pgds1Mib)