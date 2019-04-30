#
# PySNMP MIB module DTI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DTI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:39:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
clabProjDocsis, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabProjDocsis")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, Unsigned32, ModuleIdentity, Integer32, Counter32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, iso, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "Unsigned32", "ModuleIdentity", "Integer32", "Counter32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "iso", "ObjectIdentity", "IpAddress")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
dtiMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7))
dtiMib.setRevisions(('2006-06-28 00:00', '2005-08-05 00:00',))
if mibBuilder.loadTexts: dtiMib.setLastUpdated('200606280000Z')
if mibBuilder.loadTexts: dtiMib.setOrganization('CableLabs Cable Television Laboratories, Inc')
class DtiCableAdvance(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

dtiNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 0))
dtiMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1))
dtiProtocolObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1))
dtiServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2))
dtiClientObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 3))
dtiServerProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 1))
dtiServerGlobalParameters = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 2))
dtiProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1), )
if mibBuilder.loadTexts: dtiProtocolTable.setStatus('current')
dtiProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dtiProtocolEntry.setStatus('current')
dtiProtocolEntityType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("root", 1), ("server", 2), ("client", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolEntityType.setStatus('current')
dtiProtocolClientClockType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ituI", 1), ("ituII", 2), ("ituIII", 3), ("st3", 4), ("dtiClock", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolClientClockType.setStatus('current')
dtiProtocolServerStatusFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("warmup", 1), ("freerun", 2), ("fastTrackingMode", 3), ("normalMode", 4), ("holdoverMode", 5), ("clientStable", 6), ("testMode", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolServerStatusFlag.setStatus('current')
dtiProtocolClientStatusFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("warmup", 1), ("freerun", 2), ("fastTrackingMode", 3), ("normalMode", 4), ("holdoverMode", 5), ("bridgingMode", 6), ("testMode", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolClientStatusFlag.setStatus('current')
dtiProtocolServerToDState = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolServerToDState.setStatus('current')
dtiProtocolServerToDType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("default", 1), ("userTime", 2), ("ntpv4", 3), ("gps", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolServerToDType.setStatus('current')
dtiProtocolServerToDValue = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(33, 33), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolServerToDValue.setStatus('current')
dtiProtocolServerCableAdvanceFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2), ("manual", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolServerCableAdvanceFlag.setStatus('current')
dtiProtocolServerCableAdvanceValue = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 9), DtiCableAdvance()).setUnits('clockSamples').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtiProtocolServerCableAdvanceValue.setStatus('current')
dtiProtocolClientPhaseError = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-32767, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolClientPhaseError.setStatus('current')
dtiProtocolClientVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolClientVersion.setStatus('current')
dtiProtocolClientPathTraceability = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolClientPathTraceability.setStatus('current')
dtiProtocolServerClientStableFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolServerClientStableFlag.setStatus('current')
dtiProtocolControlTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 2), )
if mibBuilder.loadTexts: dtiProtocolControlTable.setStatus('current')
dtiProtocolControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dtiProtocolControlEntry.setStatus('current')
dtiProtocolControlTimeInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtiProtocolControlTimeInterval.setStatus('current')
dtiProtocolControlErrorRateInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtiProtocolControlErrorRateInterval.setStatus('current')
dtiProtocolControlJitterTimeInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtiProtocolControlJitterTimeInterval.setStatus('current')
dtiProtocolControlTestMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 2, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtiProtocolControlTestMode.setStatus('current')
dtiProtocolControlToDValue = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 2, 1, 5), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(33, 33), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtiProtocolControlToDValue.setStatus('current')
dtiProtocolPerformanceTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 3), )
if mibBuilder.loadTexts: dtiProtocolPerformanceTable.setStatus('current')
dtiProtocolPerformanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dtiProtocolPerformanceEntry.setStatus('current')
dtiProtocolPerformanceDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 3, 1, 1), Unsigned32()).setUnits('nanoseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolPerformanceDelay.setStatus('current')
dtiProtocolPerformanceFrameErrorRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 3, 1, 2), Unsigned32()).setUnits('FER').setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolPerformanceFrameErrorRate.setStatus('current')
dtiProtocolPerformancePeakToPeakJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-10000, 10000))).setUnits('picoseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolPerformancePeakToPeakJitter.setStatus('current')
dtiProtocolPerformanceWander35Second = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setUnits('picoseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolPerformanceWander35Second.setStatus('current')
dtiProtocolPerformanceWanderTSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 3, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setUnits('picoseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolPerformanceWanderTSeconds.setStatus('current')
dtiProtocolClientFsmStatsTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 6), )
if mibBuilder.loadTexts: dtiProtocolClientFsmStatsTable.setStatus('current')
dtiProtocolClientFsmStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dtiProtocolClientFsmStatsEntry.setStatus('current')
dtiProtocolClientFsmStatsT3Count = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 6, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolClientFsmStatsT3Count.setStatus('current')
dtiProtocolClientFsmStatsT4Count = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolClientFsmStatsT4Count.setStatus('current')
dtiProtocolClientFsmStatsT6Count = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolClientFsmStatsT6Count.setStatus('current')
dtiProtocolClientFsmStatsT7Count = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolClientFsmStatsT7Count.setStatus('current')
dtiProtocolClientFsmStatsNormalActiveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 6, 1, 5), Counter32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolClientFsmStatsNormalActiveTime.setStatus('current')
dtiProtocolClientFsmStatsHoldoverActiveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 6, 1, 6), Counter32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiProtocolClientFsmStatsHoldoverActiveTime.setStatus('current')
dtiPathTraceabilityTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4), )
if mibBuilder.loadTexts: dtiPathTraceabilityTable.setStatus('current')
dtiPathTraceabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1), ).setIndexNames((0, "DTI-MIB", "dtiPathTraceabilityIndex"))
if mibBuilder.loadTexts: dtiPathTraceabilityEntry.setStatus('current')
dtiPathTraceabilityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: dtiPathTraceabilityIndex.setStatus('current')
dtiPathTraceabilityRootServerInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiPathTraceabilityRootServerInetAddrType.setStatus('current')
dtiPathTraceabilityRootServerInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiPathTraceabilityRootServerInetAddr.setStatus('current')
dtiPathTraceabilityRootServerOutPhyIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1, 4), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiPathTraceabilityRootServerOutPhyIdx.setStatus('current')
dtiPathTraceabilityServerInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiPathTraceabilityServerInetAddrType.setStatus('current')
dtiPathTraceabilityServerInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiPathTraceabilityServerInetAddr.setStatus('current')
dtiPathTraceabilityServerOutPhyIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1, 7), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiPathTraceabilityServerOutPhyIdx.setStatus('current')
dtiPathTraceabilityRootServerProtVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiPathTraceabilityRootServerProtVersion.setStatus('current')
dtiPathTraceabilityServerProtVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiPathTraceabilityServerProtVersion.setStatus('current')
dtiServerRootClockType = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ituI", 1), ("ituII", 2), ("ituIII", 3), ("st3", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiServerRootClockType.setStatus('current')
dtiServerHopCount = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("root", 1), ("proxy", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiServerHopCount.setStatus('current')
dtiServerExternalTimingSource = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noExternal", 1), ("gps", 2), ("network", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiServerExternalTimingSource.setStatus('current')
dtiServerToDSources = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 1, 4), Bits().clone(namedValues=NamedValues(("default", 0), ("userTime", 1), ("ntpv4", 2), ("gps", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtiServerToDSources.setStatus('current')
dtiServerGlobalTimeInterval = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtiServerGlobalTimeInterval.setStatus('current')
dtiServerGlobalErrorRateInterval = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 2, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtiServerGlobalErrorRateInterval.setStatus('current')
dtiServerGlobalJitterTimeInterval = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtiServerGlobalJitterTimeInterval.setStatus('current')
dtiServerGlobalToDMethod = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("default", 1), ("userTime", 2), ("ntpv4", 3), ("gps", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtiServerGlobalToDMethod.setStatus('current')
dtiServerGlobalToDValue = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 2, 5), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(33, 33), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtiServerGlobalToDValue.setStatus('current')
dtiMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 2))
dtiMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 2, 1))
dtiMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 2, 2))
dtiMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 2, 1, 1)).setObjects(("DTI-MIB", "dtiBaseGroup"), ("DTI-MIB", "dtiServerGroup"), ("DTI-MIB", "dtiClientGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dtiMibCompliance = dtiMibCompliance.setStatus('current')
dtiBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 2, 2, 1)).setObjects(("DTI-MIB", "dtiProtocolServerToDState"), ("DTI-MIB", "dtiProtocolEntityType"), ("DTI-MIB", "dtiProtocolClientClockType"), ("DTI-MIB", "dtiProtocolServerStatusFlag"), ("DTI-MIB", "dtiProtocolClientStatusFlag"), ("DTI-MIB", "dtiProtocolServerToDType"), ("DTI-MIB", "dtiProtocolServerToDValue"), ("DTI-MIB", "dtiProtocolServerCableAdvanceFlag"), ("DTI-MIB", "dtiProtocolServerCableAdvanceValue"), ("DTI-MIB", "dtiProtocolClientPhaseError"), ("DTI-MIB", "dtiProtocolClientVersion"), ("DTI-MIB", "dtiProtocolClientPathTraceability"), ("DTI-MIB", "dtiPathTraceabilityRootServerInetAddrType"), ("DTI-MIB", "dtiPathTraceabilityRootServerInetAddr"), ("DTI-MIB", "dtiPathTraceabilityRootServerOutPhyIdx"), ("DTI-MIB", "dtiPathTraceabilityServerInetAddrType"), ("DTI-MIB", "dtiPathTraceabilityServerInetAddr"), ("DTI-MIB", "dtiPathTraceabilityServerOutPhyIdx"), ("DTI-MIB", "dtiPathTraceabilityRootServerProtVersion"), ("DTI-MIB", "dtiPathTraceabilityServerProtVersion"), ("DTI-MIB", "dtiProtocolPerformanceDelay"), ("DTI-MIB", "dtiProtocolPerformanceFrameErrorRate"), ("DTI-MIB", "dtiProtocolPerformancePeakToPeakJitter"), ("DTI-MIB", "dtiProtocolPerformanceWander35Second"), ("DTI-MIB", "dtiProtocolPerformanceWanderTSeconds"), ("DTI-MIB", "dtiProtocolServerClientStableFlag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dtiBaseGroup = dtiBaseGroup.setStatus('current')
dtiServerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 2, 2, 2)).setObjects(("DTI-MIB", "dtiProtocolControlTimeInterval"), ("DTI-MIB", "dtiProtocolControlErrorRateInterval"), ("DTI-MIB", "dtiProtocolControlJitterTimeInterval"), ("DTI-MIB", "dtiProtocolControlTestMode"), ("DTI-MIB", "dtiProtocolControlToDValue"), ("DTI-MIB", "dtiServerRootClockType"), ("DTI-MIB", "dtiServerHopCount"), ("DTI-MIB", "dtiServerExternalTimingSource"), ("DTI-MIB", "dtiServerToDSources"), ("DTI-MIB", "dtiServerGlobalTimeInterval"), ("DTI-MIB", "dtiServerGlobalErrorRateInterval"), ("DTI-MIB", "dtiServerGlobalJitterTimeInterval"), ("DTI-MIB", "dtiServerGlobalToDMethod"), ("DTI-MIB", "dtiServerGlobalToDValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dtiServerGroup = dtiServerGroup.setStatus('current')
dtiClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 2, 2, 3)).setObjects(("DTI-MIB", "dtiProtocolClientFsmStatsT3Count"), ("DTI-MIB", "dtiProtocolClientFsmStatsT4Count"), ("DTI-MIB", "dtiProtocolClientFsmStatsT6Count"), ("DTI-MIB", "dtiProtocolClientFsmStatsT7Count"), ("DTI-MIB", "dtiProtocolClientFsmStatsNormalActiveTime"), ("DTI-MIB", "dtiProtocolClientFsmStatsHoldoverActiveTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dtiClientGroup = dtiClientGroup.setStatus('current')
mibBuilder.exportSymbols("DTI-MIB", dtiProtocolServerToDValue=dtiProtocolServerToDValue, dtiProtocolServerClientStableFlag=dtiProtocolServerClientStableFlag, dtiProtocolControlTestMode=dtiProtocolControlTestMode, dtiProtocolClientFsmStatsT4Count=dtiProtocolClientFsmStatsT4Count, dtiPathTraceabilityRootServerInetAddr=dtiPathTraceabilityRootServerInetAddr, dtiProtocolControlTimeInterval=dtiProtocolControlTimeInterval, dtiProtocolClientFsmStatsT7Count=dtiProtocolClientFsmStatsT7Count, dtiProtocolControlEntry=dtiProtocolControlEntry, dtiServerGroup=dtiServerGroup, dtiProtocolClientVersion=dtiProtocolClientVersion, dtiServerGlobalToDMethod=dtiServerGlobalToDMethod, PYSNMP_MODULE_ID=dtiMib, dtiProtocolEntityType=dtiProtocolEntityType, dtiMib=dtiMib, dtiProtocolClientStatusFlag=dtiProtocolClientStatusFlag, dtiProtocolPerformancePeakToPeakJitter=dtiProtocolPerformancePeakToPeakJitter, dtiNotifications=dtiNotifications, dtiProtocolServerCableAdvanceFlag=dtiProtocolServerCableAdvanceFlag, dtiPathTraceabilityRootServerOutPhyIdx=dtiPathTraceabilityRootServerOutPhyIdx, dtiPathTraceabilityServerInetAddrType=dtiPathTraceabilityServerInetAddrType, dtiProtocolPerformanceWanderTSeconds=dtiProtocolPerformanceWanderTSeconds, dtiPathTraceabilityIndex=dtiPathTraceabilityIndex, dtiProtocolPerformanceFrameErrorRate=dtiProtocolPerformanceFrameErrorRate, dtiServerExternalTimingSource=dtiServerExternalTimingSource, dtiProtocolControlErrorRateInterval=dtiProtocolControlErrorRateInterval, dtiServerGlobalErrorRateInterval=dtiServerGlobalErrorRateInterval, dtiProtocolControlJitterTimeInterval=dtiProtocolControlJitterTimeInterval, dtiProtocolPerformanceTable=dtiProtocolPerformanceTable, dtiServerHopCount=dtiServerHopCount, dtiMibGroups=dtiMibGroups, dtiProtocolPerformanceDelay=dtiProtocolPerformanceDelay, dtiClientGroup=dtiClientGroup, dtiPathTraceabilityServerOutPhyIdx=dtiPathTraceabilityServerOutPhyIdx, dtiServerToDSources=dtiServerToDSources, dtiServerRootClockType=dtiServerRootClockType, dtiPathTraceabilityEntry=dtiPathTraceabilityEntry, dtiProtocolPerformanceEntry=dtiProtocolPerformanceEntry, dtiMibCompliance=dtiMibCompliance, dtiPathTraceabilityServerInetAddr=dtiPathTraceabilityServerInetAddr, dtiServerProperties=dtiServerProperties, dtiPathTraceabilityTable=dtiPathTraceabilityTable, dtiProtocolClientFsmStatsT3Count=dtiProtocolClientFsmStatsT3Count, dtiProtocolClientClockType=dtiProtocolClientClockType, dtiMibConformance=dtiMibConformance, dtiProtocolClientPhaseError=dtiProtocolClientPhaseError, DtiCableAdvance=DtiCableAdvance, dtiServerGlobalParameters=dtiServerGlobalParameters, dtiProtocolServerStatusFlag=dtiProtocolServerStatusFlag, dtiProtocolPerformanceWander35Second=dtiProtocolPerformanceWander35Second, dtiPathTraceabilityRootServerInetAddrType=dtiPathTraceabilityRootServerInetAddrType, dtiProtocolClientFsmStatsEntry=dtiProtocolClientFsmStatsEntry, dtiProtocolClientFsmStatsTable=dtiProtocolClientFsmStatsTable, dtiProtocolClientFsmStatsHoldoverActiveTime=dtiProtocolClientFsmStatsHoldoverActiveTime, dtiServerGlobalTimeInterval=dtiServerGlobalTimeInterval, dtiPathTraceabilityRootServerProtVersion=dtiPathTraceabilityRootServerProtVersion, dtiPathTraceabilityServerProtVersion=dtiPathTraceabilityServerProtVersion, dtiBaseGroup=dtiBaseGroup, dtiProtocolServerToDType=dtiProtocolServerToDType, dtiProtocolClientFsmStatsT6Count=dtiProtocolClientFsmStatsT6Count, dtiProtocolServerCableAdvanceValue=dtiProtocolServerCableAdvanceValue, dtiProtocolClientFsmStatsNormalActiveTime=dtiProtocolClientFsmStatsNormalActiveTime, dtiServerObjects=dtiServerObjects, dtiClientObjects=dtiClientObjects, dtiProtocolServerToDState=dtiProtocolServerToDState, dtiServerGlobalJitterTimeInterval=dtiServerGlobalJitterTimeInterval, dtiProtocolTable=dtiProtocolTable, dtiProtocolEntry=dtiProtocolEntry, dtiServerGlobalToDValue=dtiServerGlobalToDValue, dtiMibObjects=dtiMibObjects, dtiProtocolClientPathTraceability=dtiProtocolClientPathTraceability, dtiProtocolObjects=dtiProtocolObjects, dtiProtocolControlTable=dtiProtocolControlTable, dtiProtocolControlToDValue=dtiProtocolControlToDValue, dtiMibCompliances=dtiMibCompliances)