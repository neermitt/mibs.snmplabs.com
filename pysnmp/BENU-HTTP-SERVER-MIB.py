#
# PySNMP MIB module BENU-HTTP-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BENU-HTTP-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:20:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
benuWAG, = mibBuilder.importSymbols("BENU-WAG-MIB", "benuWAG")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, Counter64, NotificationType, Counter32, iso, ModuleIdentity, Bits, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Counter64", "NotificationType", "Counter32", "iso", "ModuleIdentity", "Bits", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
benuHttpServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10))
benuHttpServerMIB.setRevisions(('2015-10-21 00:00',))
if mibBuilder.loadTexts: benuHttpServerMIB.setLastUpdated('201510210000Z')
if mibBuilder.loadTexts: benuHttpServerMIB.setOrganization('Benu Networks,Inc')
bHttpServerObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1))
if mibBuilder.loadTexts: bHttpServerObjects.setStatus('current')
bHttpServerLatencyTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1), )
if mibBuilder.loadTexts: bHttpServerLatencyTable.setStatus('current')
bHttpServerLatencyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1), ).setIndexNames((0, "BENU-HTTP-SERVER-MIB", "bHttpServLatencyStatsInterval"))
if mibBuilder.loadTexts: bHttpServerLatencyEntry.setStatus('current')
bHttpServLatencyStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: bHttpServLatencyStatsInterval.setStatus('current')
bHttpServLatencyStatsIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyStatsIntervalDuration.setStatus('current')
bHttpServLatencyTotalPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyTotalPktCount.setStatus('current')
bHttpServLatencyMaxProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyMaxProcessingTime.setStatus('current')
bHttpServLatencyMinProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyMinProcessingTime.setStatus('current')
bHttpServLatencyAvgProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyAvgProcessingTime.setStatus('current')
bHttpServLatencyProcessTimeMorethan1MSPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyProcessTimeMorethan1MSPktCount.setStatus('current')
bHttpServLatencyGetTotalPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyGetTotalPktCount.setStatus('current')
bHttpServLatencyGetMaxProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyGetMaxProcessingTime.setStatus('current')
bHttpServLatencyGetMinProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyGetMinProcessingTime.setStatus('current')
bHttpServLatencyGetAvgProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyGetAvgProcessingTime.setStatus('current')
bHttpServLatencyGetProcessTimeMorethan1MSPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyGetProcessTimeMorethan1MSPktCount.setStatus('current')
bHttpServLatencyPostTotalPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyPostTotalPktCount.setStatus('current')
bHttpServLatencyPostMaxProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyPostMaxProcessingTime.setStatus('current')
bHttpServLatencyPostMinProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyPostMinProcessingTime.setStatus('current')
bHttpServLatencyPostAvgProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyPostAvgProcessingTime.setStatus('current')
bHttpServLatencyPostProcessTimeMorethan1MSPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyPostProcessTimeMorethan1MSPktCount.setStatus('current')
bHttpServLatencyDeleteTotalPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyDeleteTotalPktCount.setStatus('current')
bHttpServLatencyDeleteMaxProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyDeleteMaxProcessingTime.setStatus('current')
bHttpServLatencyDeleteMinProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyDeleteMinProcessingTime.setStatus('current')
bHttpServLatencyDeleteAvgProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyDeleteAvgProcessingTime.setStatus('current')
bHttpServLatencyDeleteProcessTimeMorethan1MSPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyDeleteProcessTimeMorethan1MSPktCount.setStatus('current')
mibBuilder.exportSymbols("BENU-HTTP-SERVER-MIB", bHttpServLatencyPostProcessTimeMorethan1MSPktCount=bHttpServLatencyPostProcessTimeMorethan1MSPktCount, bHttpServLatencyGetAvgProcessingTime=bHttpServLatencyGetAvgProcessingTime, bHttpServLatencyProcessTimeMorethan1MSPktCount=bHttpServLatencyProcessTimeMorethan1MSPktCount, bHttpServLatencyGetTotalPktCount=bHttpServLatencyGetTotalPktCount, bHttpServLatencyDeleteAvgProcessingTime=bHttpServLatencyDeleteAvgProcessingTime, bHttpServLatencyPostMinProcessingTime=bHttpServLatencyPostMinProcessingTime, bHttpServerObjects=bHttpServerObjects, bHttpServLatencyMinProcessingTime=bHttpServLatencyMinProcessingTime, bHttpServLatencyStatsIntervalDuration=bHttpServLatencyStatsIntervalDuration, bHttpServLatencyAvgProcessingTime=bHttpServLatencyAvgProcessingTime, bHttpServLatencyPostTotalPktCount=bHttpServLatencyPostTotalPktCount, bHttpServLatencyTotalPktCount=bHttpServLatencyTotalPktCount, bHttpServLatencyMaxProcessingTime=bHttpServLatencyMaxProcessingTime, bHttpServLatencyGetMinProcessingTime=bHttpServLatencyGetMinProcessingTime, bHttpServLatencyGetMaxProcessingTime=bHttpServLatencyGetMaxProcessingTime, bHttpServLatencyGetProcessTimeMorethan1MSPktCount=bHttpServLatencyGetProcessTimeMorethan1MSPktCount, bHttpServLatencyDeleteProcessTimeMorethan1MSPktCount=bHttpServLatencyDeleteProcessTimeMorethan1MSPktCount, bHttpServLatencyPostAvgProcessingTime=bHttpServLatencyPostAvgProcessingTime, bHttpServLatencyDeleteMinProcessingTime=bHttpServLatencyDeleteMinProcessingTime, bHttpServLatencyStatsInterval=bHttpServLatencyStatsInterval, bHttpServLatencyDeleteTotalPktCount=bHttpServLatencyDeleteTotalPktCount, bHttpServerLatencyTable=bHttpServerLatencyTable, PYSNMP_MODULE_ID=benuHttpServerMIB, bHttpServLatencyPostMaxProcessingTime=bHttpServLatencyPostMaxProcessingTime, benuHttpServerMIB=benuHttpServerMIB, bHttpServLatencyDeleteMaxProcessingTime=bHttpServLatencyDeleteMaxProcessingTime, bHttpServerLatencyEntry=bHttpServerLatencyEntry)
