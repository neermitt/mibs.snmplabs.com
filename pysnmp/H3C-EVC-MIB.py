#
# PySNMP MIB module H3C-EVC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-EVC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:09:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, Unsigned32, ModuleIdentity, Counter32, IpAddress, Integer32, iso, TimeTicks, Counter64, MibIdentifier, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "Unsigned32", "ModuleIdentity", "Counter32", "IpAddress", "Integer32", "iso", "TimeTicks", "Counter64", "MibIdentifier", "Gauge32", "ObjectIdentity")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
h3cEvc = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 106))
h3cEvc.setRevisions(('2009-08-08 10:00',))
if mibBuilder.loadTexts: h3cEvc.setLastUpdated('200908081000Z')
if mibBuilder.loadTexts: h3cEvc.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cEvcObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1))
h3cEvcScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 1))
h3cEvcSrvInstEncapCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 1, 1), Bits().clone(namedValues=NamedValues(("encapPortBased", 0), ("encapUntagged", 1), ("encapTagged", 2), ("encapSvlanId", 3), ("encapSvlanIdList", 4), ("encapSvlanIdOnlyTagged", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cEvcSrvInstEncapCapabilities.setStatus('current')
h3cEvcPortMaxSrvInstNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cEvcPortMaxSrvInstNum.setStatus('current')
h3cEvcSrvInstTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 2), )
if mibBuilder.loadTexts: h3cEvcSrvInstTable.setStatus('current')
h3cEvcSrvInstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "H3C-EVC-MIB", "h3cEvcSrvInstId"))
if mibBuilder.loadTexts: h3cEvcSrvInstEntry.setStatus('current')
h3cEvcSrvInstId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cEvcSrvInstId.setStatus('current')
h3cEvcSrvInstEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 0), ("portBased", 1), ("untagged", 2), ("tagged", 3), ("svlanIdList", 4), ("svlanIdListOnlyTagged", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cEvcSrvInstEncap.setStatus('current')
h3cEvcSrvInstSvlanIdListLow = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cEvcSrvInstSvlanIdListLow.setStatus('current')
h3cEvcSrvInstSvlanIdListHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cEvcSrvInstSvlanIdListHigh.setStatus('current')
h3cEvcSrvInstRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cEvcSrvInstRowStatus.setStatus('current')
mibBuilder.exportSymbols("H3C-EVC-MIB", h3cEvc=h3cEvc, h3cEvcSrvInstEncap=h3cEvcSrvInstEncap, h3cEvcSrvInstEncapCapabilities=h3cEvcSrvInstEncapCapabilities, h3cEvcSrvInstTable=h3cEvcSrvInstTable, PYSNMP_MODULE_ID=h3cEvc, h3cEvcPortMaxSrvInstNum=h3cEvcPortMaxSrvInstNum, h3cEvcSrvInstEntry=h3cEvcSrvInstEntry, h3cEvcSrvInstRowStatus=h3cEvcSrvInstRowStatus, h3cEvcSrvInstId=h3cEvcSrvInstId, h3cEvcObjects=h3cEvcObjects, h3cEvcScalarGroup=h3cEvcScalarGroup, h3cEvcSrvInstSvlanIdListLow=h3cEvcSrvInstSvlanIdListLow, h3cEvcSrvInstSvlanIdListHigh=h3cEvcSrvInstSvlanIdListHigh)