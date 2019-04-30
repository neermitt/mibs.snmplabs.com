#
# PySNMP MIB module CISCO-RTTMON-RTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RTTMON-RTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:54:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rttMonCtrlAdminIndex, rttMonStats, rttMonLatestOper = mibBuilder.importSymbols("CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex", "rttMonStats", "rttMonLatestOper")
RttResponseSense, = mibBuilder.importSymbols("CISCO-RTTMON-TC-MIB", "RttResponseSense")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, MibIdentifier, Integer32, ObjectIdentity, ModuleIdentity, Counter32, NotificationType, Bits, Unsigned32, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "Integer32", "ObjectIdentity", "ModuleIdentity", "Counter32", "NotificationType", "Bits", "Unsigned32", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64")
TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp")
ciscoRttMonRtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 487))
ciscoRttMonRtpMIB.setRevisions(('2005-08-09 00:00',))
if mibBuilder.loadTexts: ciscoRttMonRtpMIB.setLastUpdated('200508090000Z')
if mibBuilder.loadTexts: ciscoRttMonRtpMIB.setOrganization('Cisco Systems, Inc.')
ciscoRttMonRtpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 487, 0))
ciscoRttMonRtpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 487, 1))
rttMonLatestRtpOperTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3), )
if mibBuilder.loadTexts: rttMonLatestRtpOperTable.setStatus('current')
rttMonLatestRtpOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1), ).setIndexNames((0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"))
if mibBuilder.loadTexts: rttMonLatestRtpOperEntry.setStatus('current')
rttMonLatestRtpOperRTT = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperRTT.setStatus('current')
rttMonLatestRtpOperIAJitterDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperIAJitterDS.setStatus('current')
rttMonLatestRtpOperPacketLossDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperPacketLossDS.setStatus('current')
rttMonLatestRtpOperPacketLateDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperPacketLateDS.setStatus('current')
rttMonLatestRtpOperPacketEarlyDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperPacketEarlyDS.setStatus('current')
rttMonLatestRtpOperPacketOOSDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperPacketOOSDS.setStatus('current')
rttMonLatestRtpOperFrameLossDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperFrameLossDS.setStatus('current')
rttMonLatestRtpOperRFactorDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperRFactorDS.setStatus('current')
rttMonLatestRtpOperMOSCQDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperMOSCQDS.setStatus('current')
rttMonLatestRtpOperMOSLQDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperMOSLQDS.setStatus('current')
rttMonLatestRtpOperSense = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 11), RttResponseSense()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperSense.setStatus('current')
rttMonLatestRtpErrorSenseDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpErrorSenseDescription.setStatus('current')
rttMonLatestRtpOperIAJitterSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 13), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperIAJitterSD.setStatus('current')
rttMonLatestRtpOperPacketLossSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 14), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperPacketLossSD.setStatus('current')
rttMonLatestRtpOperPacketsMIA = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 15), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperPacketsMIA.setStatus('current')
rttMonLatestRtpOperRFactorSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperRFactorSD.setStatus('current')
rttMonLatestRtpOperMOSCQSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 17), Gauge32()).setUnits('voice quality').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperMOSCQSD.setStatus('current')
rttMonLatestRtpOperMinOWSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 18), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperMinOWSD.setStatus('current')
rttMonLatestRtpOperMaxOWSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 19), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperMaxOWSD.setStatus('current')
rttMonLatestRtpOperAvgOWSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 20), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperAvgOWSD.setStatus('current')
rttMonLatestRtpOperMinOWDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 21), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperMinOWDS.setStatus('current')
rttMonLatestRtpOperMaxOWDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 22), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperMaxOWDS.setStatus('current')
rttMonLatestRtpOperAvgOWDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 23), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperAvgOWDS.setStatus('current')
rttMonLatestRtpOperTotalPaksSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 24), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperTotalPaksSD.setStatus('current')
rttMonLatestRtpOperTotalPaksDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 25), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperTotalPaksDS.setStatus('current')
rttMonRtpStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6), )
if mibBuilder.loadTexts: rttMonRtpStatsTable.setStatus('current')
rttMonRtpStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1), ).setIndexNames((0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"), (0, "CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsStartTimeIndex"))
if mibBuilder.loadTexts: rttMonRtpStatsEntry.setStatus('current')
rttMonRtpStatsStartTimeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 1), TimeStamp())
if mibBuilder.loadTexts: rttMonRtpStatsStartTimeIndex.setStatus('current')
rttMonRtpStatsRTTAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 2), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsRTTAvg.setStatus('current')
rttMonRtpStatsRTTMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 3), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsRTTMin.setStatus('current')
rttMonRtpStatsRTTMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 4), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsRTTMax.setStatus('current')
rttMonRtpStatsIAJitterDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 5), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsIAJitterDSAvg.setStatus('current')
rttMonRtpStatsIAJitterDSMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 6), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsIAJitterDSMin.setStatus('current')
rttMonRtpStatsIAJitterDSMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 7), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsIAJitterDSMax.setStatus('current')
rttMonRtpStatsPacketLossDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 8), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketLossDSAvg.setStatus('current')
rttMonRtpStatsPacketLossDSMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 9), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketLossDSMin.setStatus('current')
rttMonRtpStatsPacketLossDSMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 10), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketLossDSMax.setStatus('current')
rttMonRtpStatsPacketLateDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 11), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketLateDSAvg.setStatus('current')
rttMonRtpStatsPacketEarlyDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 12), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketEarlyDSAvg.setStatus('current')
rttMonRtpStatsPacketOOSDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 13), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketOOSDSAvg.setStatus('current')
rttMonRtpStatsFrameLossDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 14), Gauge32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsFrameLossDSAvg.setStatus('current')
rttMonRtpStatsFrameLossDSMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 15), Gauge32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsFrameLossDSMin.setStatus('current')
rttMonRtpStatsFrameLossDSMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 16), Gauge32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsFrameLossDSMax.setStatus('current')
rttMonRtpStatsRFactorDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 17), Gauge32()).setUnits('voice quality').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsRFactorDSAvg.setStatus('current')
rttMonRtpStatsRFactorDSMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 18), Gauge32()).setUnits('voice quality').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsRFactorDSMin.setStatus('current')
rttMonRtpStatsRFactorDSMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 19), Gauge32()).setUnits('voice quality').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsRFactorDSMax.setStatus('current')
rttMonRtpStatsMOSCQDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 20), Gauge32()).setUnits('voice quality').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsMOSCQDSAvg.setStatus('current')
rttMonRtpStatsMOSCQDSMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 21), Gauge32()).setUnits('voice quality').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsMOSCQDSMin.setStatus('current')
rttMonRtpStatsMOSCQDSMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 22), Gauge32()).setUnits('voice quality').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsMOSCQDSMax.setStatus('current')
rttMonRtpStatsMOSLQDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 23), Gauge32()).setUnits('voice quality').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsMOSLQDSAvg.setStatus('current')
rttMonRtpStatsMOSLQDSMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 24), Gauge32()).setUnits('voice quality').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsMOSLQDSMin.setStatus('current')
rttMonRtpStatsMOSLQDSMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 25), Gauge32()).setUnits('voice quality').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsMOSLQDSMax.setStatus('current')
rttMonRtpStatsIAJitterSDAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 26), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsIAJitterSDAvg.setStatus('current')
rttMonRtpStatsIAJitterSDMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 27), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsIAJitterSDMin.setStatus('current')
rttMonRtpStatsIAJitterSDMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 28), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsIAJitterSDMax.setStatus('current')
rttMonRtpStatsPacketLossSDAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 29), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketLossSDAvg.setStatus('current')
rttMonRtpStatsPacketLossSDMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 30), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketLossSDMin.setStatus('current')
rttMonRtpStatsPacketLossSDMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 31), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketLossSDMax.setStatus('current')
rttMonRtpStatsPacketsMIAAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 32), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketsMIAAvg.setStatus('current')
rttMonRtpStatsRFactorSDAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 33), Gauge32()).setUnits('voice quality').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsRFactorSDAvg.setStatus('current')
rttMonRtpStatsRFactorSDMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 34), Gauge32()).setUnits('voice quality').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsRFactorSDMin.setStatus('current')
rttMonRtpStatsRFactorSDMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 35), Gauge32()).setUnits('voice quality').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsRFactorSDMax.setStatus('current')
rttMonRtpStatsMOSCQSDAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 36), Gauge32()).setUnits('voice quality').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsMOSCQSDAvg.setStatus('current')
rttMonRtpStatsMOSCQSDMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 37), Gauge32()).setUnits('voice quality').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsMOSCQSDMin.setStatus('current')
rttMonRtpStatsMOSCQSDMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 39), Gauge32()).setUnits('voice quality').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsMOSCQSDMax.setStatus('current')
rttMonRtpStatsOperAvgOWSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 40), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsOperAvgOWSD.setStatus('current')
rttMonRtpStatsOperMinOWSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 41), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsOperMinOWSD.setStatus('current')
rttMonRtpStatsOperMaxOWSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 42), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsOperMaxOWSD.setStatus('current')
rttMonRtpStatsOperAvgOWDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 43), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsOperAvgOWDS.setStatus('current')
rttMonRtpStatsOperMinOWDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 44), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsOperMinOWDS.setStatus('current')
rttMonRtpStatsOperMaxOWDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 45), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsOperMaxOWDS.setStatus('current')
rttMonRtpStatsTotalPacketsSDAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 46), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsTotalPacketsSDAvg.setStatus('current')
rttMonRtpStatsTotalPacketsSDMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 47), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsTotalPacketsSDMin.setStatus('current')
rttMonRtpStatsTotalPacketsSDMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 48), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsTotalPacketsSDMax.setStatus('current')
rttMonRtpStatsTotalPacketsDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 49), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsTotalPacketsDSAvg.setStatus('current')
rttMonRtpStatsTotalPacketsDSMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 50), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsTotalPacketsDSMax.setStatus('current')
rttMonRtpStatsTotalPacketsDSMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 51), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsTotalPacketsDSMin.setStatus('current')
ciscoRttMonRtpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 487, 2))
ciscoRttMonRtpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 487, 2, 1))
ciscoRttMonRtpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 487, 2, 2))
ciscoRttMonRtpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 487, 2, 1, 1)).setObjects(("CISCO-RTTMON-RTP-MIB", "ciscoRttMonRtpGroup"), ("CISCO-RTTMON-RTP-MIB", "ciscoRttMonRtpGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonRtpMIBCompliance = ciscoRttMonRtpMIBCompliance.setStatus('current')
ciscoRttMonRtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 487, 2, 2, 1)).setObjects(("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperRTT"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperIAJitterDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperPacketLossDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperPacketLateDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperPacketEarlyDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperPacketOOSDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperFrameLossDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperRFactorDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMOSCQDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMOSLQDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperSense"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpErrorSenseDescription"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRTTAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRTTMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRTTMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsIAJitterDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsIAJitterDSMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsIAJitterDSMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLossDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLossDSMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLossDSMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLateDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketEarlyDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketOOSDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsFrameLossDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsFrameLossDSMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsFrameLossDSMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRFactorDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRFactorDSMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRFactorDSMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSCQDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSCQDSMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSCQDSMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSLQDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSLQDSMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSLQDSMax"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonRtpGroup = ciscoRttMonRtpGroup.setStatus('current')
ciscoRttMonRtpGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 487, 2, 2, 2)).setObjects(("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperIAJitterSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperPacketLossSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperPacketsMIA"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperRFactorSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMOSCQSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMinOWSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMaxOWSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperAvgOWSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMinOWDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMaxOWDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperAvgOWDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperTotalPaksSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperTotalPaksDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsIAJitterSDAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsIAJitterSDMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsIAJitterSDMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLossSDAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLossSDMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLossSDMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketsMIAAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRFactorSDAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRFactorSDMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRFactorSDMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSCQSDAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSCQSDMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSCQSDMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsOperAvgOWSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsOperMinOWSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsOperMaxOWSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsOperAvgOWDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsOperMinOWDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsOperMaxOWDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsTotalPacketsSDAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsTotalPacketsSDMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsTotalPacketsSDMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsTotalPacketsDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsTotalPacketsDSMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsTotalPacketsDSMax"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonRtpGroupRev1 = ciscoRttMonRtpGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-RTTMON-RTP-MIB", rttMonRtpStatsPacketLossDSMin=rttMonRtpStatsPacketLossDSMin, rttMonRtpStatsPacketLossDSAvg=rttMonRtpStatsPacketLossDSAvg, rttMonRtpStatsPacketLossDSMax=rttMonRtpStatsPacketLossDSMax, rttMonLatestRtpOperMinOWDS=rttMonLatestRtpOperMinOWDS, rttMonRtpStatsRFactorSDAvg=rttMonRtpStatsRFactorSDAvg, rttMonLatestRtpOperRFactorSD=rttMonLatestRtpOperRFactorSD, rttMonRtpStatsPacketLossSDMax=rttMonRtpStatsPacketLossSDMax, rttMonRtpStatsRFactorDSMin=rttMonRtpStatsRFactorDSMin, rttMonRtpStatsRFactorDSAvg=rttMonRtpStatsRFactorDSAvg, rttMonLatestRtpOperPacketLossDS=rttMonLatestRtpOperPacketLossDS, rttMonRtpStatsMOSCQSDAvg=rttMonRtpStatsMOSCQSDAvg, rttMonLatestRtpOperIAJitterDS=rttMonLatestRtpOperIAJitterDS, rttMonRtpStatsOperAvgOWSD=rttMonRtpStatsOperAvgOWSD, rttMonRtpStatsTotalPacketsDSMin=rttMonRtpStatsTotalPacketsDSMin, rttMonRtpStatsEntry=rttMonRtpStatsEntry, rttMonRtpStatsStartTimeIndex=rttMonRtpStatsStartTimeIndex, rttMonRtpStatsIAJitterDSMin=rttMonRtpStatsIAJitterDSMin, rttMonLatestRtpOperPacketsMIA=rttMonLatestRtpOperPacketsMIA, rttMonRtpStatsOperAvgOWDS=rttMonRtpStatsOperAvgOWDS, rttMonRtpStatsOperMaxOWDS=rttMonRtpStatsOperMaxOWDS, rttMonRtpStatsMOSCQDSMin=rttMonRtpStatsMOSCQDSMin, rttMonRtpStatsIAJitterDSMax=rttMonRtpStatsIAJitterDSMax, rttMonRtpStatsPacketOOSDSAvg=rttMonRtpStatsPacketOOSDSAvg, rttMonLatestRtpOperMaxOWDS=rttMonLatestRtpOperMaxOWDS, rttMonRtpStatsPacketLossSDMin=rttMonRtpStatsPacketLossSDMin, rttMonRtpStatsRFactorDSMax=rttMonRtpStatsRFactorDSMax, rttMonRtpStatsIAJitterSDMax=rttMonRtpStatsIAJitterSDMax, rttMonRtpStatsPacketEarlyDSAvg=rttMonRtpStatsPacketEarlyDSAvg, rttMonRtpStatsTable=rttMonRtpStatsTable, rttMonRtpStatsTotalPacketsDSMax=rttMonRtpStatsTotalPacketsDSMax, rttMonLatestRtpOperMOSLQDS=rttMonLatestRtpOperMOSLQDS, rttMonRtpStatsOperMinOWSD=rttMonRtpStatsOperMinOWSD, rttMonRtpStatsMOSCQSDMax=rttMonRtpStatsMOSCQSDMax, rttMonRtpStatsIAJitterSDAvg=rttMonRtpStatsIAJitterSDAvg, ciscoRttMonRtpGroup=ciscoRttMonRtpGroup, rttMonLatestRtpOperEntry=rttMonLatestRtpOperEntry, rttMonRtpStatsTotalPacketsSDMin=rttMonRtpStatsTotalPacketsSDMin, rttMonLatestRtpOperRTT=rttMonLatestRtpOperRTT, ciscoRttMonRtpMIBGroups=ciscoRttMonRtpMIBGroups, rttMonRtpStatsRTTMin=rttMonRtpStatsRTTMin, rttMonLatestRtpOperSense=rttMonLatestRtpOperSense, ciscoRttMonRtpMIBCompliances=ciscoRttMonRtpMIBCompliances, rttMonLatestRtpOperPacketLateDS=rttMonLatestRtpOperPacketLateDS, rttMonRtpStatsRTTMax=rttMonRtpStatsRTTMax, rttMonRtpStatsFrameLossDSAvg=rttMonRtpStatsFrameLossDSAvg, rttMonLatestRtpOperAvgOWSD=rttMonLatestRtpOperAvgOWSD, ciscoRttMonRtpGroupRev1=ciscoRttMonRtpGroupRev1, rttMonRtpStatsRFactorSDMax=rttMonRtpStatsRFactorSDMax, rttMonRtpStatsOperMaxOWSD=rttMonRtpStatsOperMaxOWSD, rttMonRtpStatsPacketsMIAAvg=rttMonRtpStatsPacketsMIAAvg, rttMonRtpStatsMOSCQSDMin=rttMonRtpStatsMOSCQSDMin, rttMonLatestRtpOperMinOWSD=rttMonLatestRtpOperMinOWSD, rttMonRtpStatsMOSCQDSMax=rttMonRtpStatsMOSCQDSMax, rttMonLatestRtpOperFrameLossDS=rttMonLatestRtpOperFrameLossDS, rttMonLatestRtpOperTotalPaksDS=rttMonLatestRtpOperTotalPaksDS, rttMonLatestRtpErrorSenseDescription=rttMonLatestRtpErrorSenseDescription, ciscoRttMonRtpMIBNotifs=ciscoRttMonRtpMIBNotifs, rttMonRtpStatsMOSLQDSMax=rttMonRtpStatsMOSLQDSMax, rttMonLatestRtpOperTotalPaksSD=rttMonLatestRtpOperTotalPaksSD, rttMonRtpStatsFrameLossDSMax=rttMonRtpStatsFrameLossDSMax, rttMonLatestRtpOperRFactorDS=rttMonLatestRtpOperRFactorDS, rttMonRtpStatsPacketLossSDAvg=rttMonRtpStatsPacketLossSDAvg, PYSNMP_MODULE_ID=ciscoRttMonRtpMIB, ciscoRttMonRtpMIBConformance=ciscoRttMonRtpMIBConformance, rttMonRtpStatsPacketLateDSAvg=rttMonRtpStatsPacketLateDSAvg, rttMonRtpStatsFrameLossDSMin=rttMonRtpStatsFrameLossDSMin, rttMonRtpStatsTotalPacketsDSAvg=rttMonRtpStatsTotalPacketsDSAvg, rttMonLatestRtpOperMOSCQDS=rttMonLatestRtpOperMOSCQDS, rttMonRtpStatsTotalPacketsSDMax=rttMonRtpStatsTotalPacketsSDMax, rttMonLatestRtpOperTable=rttMonLatestRtpOperTable, rttMonRtpStatsMOSCQDSAvg=rttMonRtpStatsMOSCQDSAvg, rttMonLatestRtpOperMOSCQSD=rttMonLatestRtpOperMOSCQSD, rttMonRtpStatsRTTAvg=rttMonRtpStatsRTTAvg, rttMonRtpStatsMOSLQDSMin=rttMonRtpStatsMOSLQDSMin, rttMonRtpStatsIAJitterSDMin=rttMonRtpStatsIAJitterSDMin, ciscoRttMonRtpMIB=ciscoRttMonRtpMIB, rttMonLatestRtpOperPacketOOSDS=rttMonLatestRtpOperPacketOOSDS, rttMonRtpStatsTotalPacketsSDAvg=rttMonRtpStatsTotalPacketsSDAvg, rttMonRtpStatsIAJitterDSAvg=rttMonRtpStatsIAJitterDSAvg, ciscoRttMonRtpMIBCompliance=ciscoRttMonRtpMIBCompliance, rttMonRtpStatsOperMinOWDS=rttMonRtpStatsOperMinOWDS, ciscoRttMonRtpMIBObjects=ciscoRttMonRtpMIBObjects, rttMonLatestRtpOperMaxOWSD=rttMonLatestRtpOperMaxOWSD, rttMonLatestRtpOperAvgOWDS=rttMonLatestRtpOperAvgOWDS, rttMonLatestRtpOperPacketLossSD=rttMonLatestRtpOperPacketLossSD, rttMonRtpStatsRFactorSDMin=rttMonRtpStatsRFactorSDMin, rttMonLatestRtpOperPacketEarlyDS=rttMonLatestRtpOperPacketEarlyDS, rttMonRtpStatsMOSLQDSAvg=rttMonRtpStatsMOSLQDSAvg, rttMonLatestRtpOperIAJitterSD=rttMonLatestRtpOperIAJitterSD)