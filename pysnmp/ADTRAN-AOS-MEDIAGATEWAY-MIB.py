#
# PySNMP MIB module ADTRAN-AOS-MEDIAGATEWAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTRAN-AOS-MEDIAGATEWAY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:58:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
adGenAOSVoice, = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSVoice")
adShared, adIdentity = mibBuilder.importSymbols("ADTRAN-MIB", "adShared", "adIdentity")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, Integer32, NotificationType, Gauge32, ModuleIdentity, Bits, TimeTicks, Unsigned32, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "NotificationType", "Gauge32", "ModuleIdentity", "Bits", "TimeTicks", "Unsigned32", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenAOSMediaGatewayMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 5, 2))
adGenAOSMediaGatewayMIB.setRevisions(('2012-08-22 00:00',))
if mibBuilder.loadTexts: adGenAOSMediaGatewayMIB.setLastUpdated('200504190000Z')
if mibBuilder.loadTexts: adGenAOSMediaGatewayMIB.setOrganization('ADTRAN, Inc.')
adGenAOSMediaGateway = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2))
adGenAOSMediaGatewayObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1))
adGenAOSMediaGatewayConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 99))
adGenAOSMediaGatewayCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 99, 1))
adGenAOSMediaGatewayMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 99, 2))
adGenAOSRtpSessionTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1), )
if mibBuilder.loadTexts: adGenAOSRtpSessionTable.setStatus('current')
adGenAOSRtpSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1), ).setIndexNames((0, "ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionChannelId"))
if mibBuilder.loadTexts: adGenAOSRtpSessionEntry.setStatus('current')
adGenAOSRtpSessionChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionChannelId.setStatus('current')
adGenAOSRtpSessionChannelIdName = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionChannelIdName.setStatus('current')
adGenAOSRtpSessionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unavailable", 0), ("available", 1), ("allocated", 2), ("active", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionStatus.setStatus('current')
adGenAOSRtpSessionStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionStartTime.setStatus('current')
adGenAOSRtpSessionDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionDuration.setStatus('current')
adGenAOSRtpSessionVocoder = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39))).clone(namedValues=NamedValues(("none", 0), ("g711ulaw", 1), ("gsm", 2), ("g723", 3), ("g711alaw", 4), ("g722", 5), ("g728", 6), ("g729a", 7), ("dynamic96", 8), ("dynamic97", 9), ("dynamic98", 10), ("dynamic99", 11), ("dynamic100", 12), ("dynamic101", 13), ("dynamic102", 14), ("dynamic103", 15), ("dynamic104", 16), ("dynamic105", 17), ("dynamic106", 18), ("dynamic107", 19), ("dynamic108", 20), ("dynamic109", 21), ("dynamic110", 22), ("dynamic111", 23), ("dynamic112", 24), ("dynamic113", 25), ("dynamic114", 26), ("dynamic115", 27), ("dynamic116", 28), ("dynamic117", 29), ("dynamic118", 30), ("dynamic119", 31), ("dynamic120", 32), ("dynamic121", 33), ("dynamic122", 34), ("dynamic123", 35), ("dynamic124", 36), ("dynamic125", 37), ("dynamic126", 38), ("dynamic127", 39)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionVocoder.setStatus('current')
adGenAOSRtpSessionVAD = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionVAD.setStatus('current')
adGenAOSRtpSessionTdmPortDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionTdmPortDescription.setStatus('current')
adGenAOSRtpSessionLocalIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionLocalIPAddress.setStatus('current')
adGenAOSRtpSessionLocalUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionLocalUdpPort.setStatus('current')
adGenAOSRtpSessionSIPPortDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionSIPPortDescription.setStatus('current')
adGenAOSRtpSessionRemoteIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 12), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionRemoteIPAddress.setStatus('current')
adGenAOSRtpSessionRemoteUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionRemoteUdpPort.setStatus('current')
adGenAOSRtpSessionTxFramesPerPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionTxFramesPerPacket.setStatus('current')
adGenAOSRtpSessionEchoCancellerEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionEchoCancellerEnabled.setStatus('current')
adGenAOSRtpSessionRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionRxPackets.setStatus('current')
adGenAOSRtpSessionRxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionRxOctets.setStatus('current')
adGenAOSRtpSessionRxPacketsLost = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionRxPacketsLost.setStatus('obsolete')
adGenAOSRtpSessionRxPacketsUnknown = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionRxPacketsUnknown.setStatus('current')
adGenAOSRtpSessionRxJitterBufferDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionRxJitterBufferDepth.setStatus('current')
adGenAOSRtpSessionRxMaxJitterBufferDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionRxMaxJitterBufferDepth.setStatus('current')
adGenAOSRtpSessionRxFrameLateDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionRxFrameLateDiscards.setStatus('obsolete')
adGenAOSRtpSessionRxFrameOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionRxFrameOverflows.setStatus('obsolete')
adGenAOSRtpSessionRxFrameOutOfOrders = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionRxFrameOutOfOrders.setStatus('current')
adGenAOSRtpSessionRxSyncSource = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionRxSyncSource.setStatus('current')
adGenAOSRtpSessionTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 35), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionTxPackets.setStatus('current')
adGenAOSRtpSessionTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 36), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionTxOctets.setStatus('current')
adGenAOSRtpSessionTxSyncSource = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 37), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionTxSyncSource.setStatus('current')
adGenAOSRtpSessionTotalsTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2), )
if mibBuilder.loadTexts: adGenAOSRtpSessionTotalsTable.setStatus('current')
adGenAOSRtpSessionTotalsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1), ).setIndexNames((0, "ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsSessions"))
if mibBuilder.loadTexts: adGenAOSRtpSessionTotalsEntry.setStatus('current')
adGenAOSRtpSessionTotalsSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionTotalsSessions.setStatus('current')
adGenAOSRtpSessionTotalsSessionDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionTotalsSessionDuration.setStatus('current')
adGenAOSRtpSessionTotalsRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionTotalsRxPackets.setStatus('current')
adGenAOSRtpSessionTotalsRxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionTotalsRxOctets.setStatus('current')
adGenAOSRtpSessionTotalsRxPacketsLost = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionTotalsRxPacketsLost.setStatus('obsolete')
adGenAOSRtpSessionTotalsRxPacketsUnknown = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionTotalsRxPacketsUnknown.setStatus('current')
adGenAOSRtpSessionTotalsTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionTotalsTxPackets.setStatus('current')
adGenAOSRtpSessionTotalsTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionTotalsTxOctets.setStatus('current')
adGenAOSRtpSessionTotalsRxFrameLateDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionTotalsRxFrameLateDiscards.setStatus('obsolete')
adGenAOSRtpSessionTotalsRxFrameOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionTotalsRxFrameOverflows.setStatus('obsolete')
adGenAOSRtpSessionTotalsRxFrameOutOfOrders = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionTotalsRxFrameOutOfOrders.setStatus('current')
adGenAOSRtpSessionTotalsClearCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSRtpSessionTotalsClearCounters.setStatus('current')
adGenAOSRtpSessionTotalsTimeSinceLastClearCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpSessionTotalsTimeSinceLastClearCounters.setStatus('current')
adGenAOSMediaGatewayInfoTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 3), )
if mibBuilder.loadTexts: adGenAOSMediaGatewayInfoTable.setStatus('current')
adGenAOSMediaGatewayInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 3, 1), ).setIndexNames((0, "ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSMediaGatewayInfoIdentifier"))
if mibBuilder.loadTexts: adGenAOSMediaGatewayInfoEntry.setStatus('current')
adGenAOSMediaGatewayInfoIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSMediaGatewayInfoIdentifier.setStatus('current')
adGenAOSMediaGatewayInfoSoftwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSMediaGatewayInfoSoftwareVersion.setStatus('current')
adGenAOSMediaGatewayInfoUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSMediaGatewayInfoUtilization.setStatus('current')
adGenAOSMediaGatewayInfoUtilizationMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSMediaGatewayInfoUtilizationMaximum.setStatus('current')
adGenAOSMediaGatewayInfoFreePacketBuffers = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSMediaGatewayInfoFreePacketBuffers.setStatus('current')
adGenAOSMediaGatewayInfoUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSMediaGatewayInfoUptime.setStatus('current')
adGenAOSRtpChannelTotalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4), )
if mibBuilder.loadTexts: adGenAOSRtpChannelTotalTable.setStatus('current')
adGenAOSRtpChannelTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1), ).setIndexNames((0, "ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalId"))
if mibBuilder.loadTexts: adGenAOSRtpChannelTotalEntry.setStatus('current')
adGenAOSRtpChannelTotalId = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpChannelTotalId.setStatus('current')
adGenAOSRtpChannelTotalIdName = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpChannelTotalIdName.setStatus('current')
adGenAOSRtpChannelTotalSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpChannelTotalSessions.setStatus('current')
adGenAOSRtpChannelTotalSessionDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpChannelTotalSessionDuration.setStatus('current')
adGenAOSRtpChannelTotalRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpChannelTotalRxPackets.setStatus('current')
adGenAOSRtpChannelTotalRxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpChannelTotalRxOctets.setStatus('current')
adGenAOSRtpChannelTotalRxPacketsLost = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpChannelTotalRxPacketsLost.setStatus('obsolete')
adGenAOSRtpChannelTotalRxPacketsUnknown = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpChannelTotalRxPacketsUnknown.setStatus('current')
adGenAOSRtpChannelTotalTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpChannelTotalTxPackets.setStatus('current')
adGenAOSRtpChannelTotalTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpChannelTotalTxOctets.setStatus('current')
adGenAOSRtpChannelTotalRxMaxDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpChannelTotalRxMaxDepth.setStatus('obsolete')
adGenAOSRtpChannelTotalRxFrameLateDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpChannelTotalRxFrameLateDiscards.setStatus('obsolete')
adGenAOSRtpChannelTotalRxFrameOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpChannelTotalRxFrameOverflows.setStatus('obsolete')
adGenAOSRtpChannelTotalRxFrameOutOfOrders = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpChannelTotalRxFrameOutOfOrders.setStatus('current')
adGenAOSRtpChannelClearCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSRtpChannelClearCounters.setStatus('current')
adGenAOSRtpChannelTimeSinceLastClearCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSRtpChannelTimeSinceLastClearCounters.setStatus('current')
adGenAOSMediaGatewayCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 99, 1, 1)).setObjects(("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSMediaGatewayRtpSessionGroup"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSMediaGatewayRtpSessionTotalsGroup"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSMediaGatewayInfoGroup"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSMediaGatewayRtpChannelTotalsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSMediaGatewayCompliance = adGenAOSMediaGatewayCompliance.setStatus('current')
adGenAOSMediaGatewayRtpSessionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 99, 2, 1)).setObjects(("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionChannelId"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionChannelIdName"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionStatus"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionStartTime"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionDuration"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionVocoder"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionVAD"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTdmPortDescription"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionLocalIPAddress"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionLocalUdpPort"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionSIPPortDescription"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRemoteIPAddress"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRemoteUdpPort"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTxFramesPerPacket"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionEchoCancellerEnabled"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxPackets"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxOctets"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxPacketsLost"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxPacketsUnknown"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxJitterBufferDepth"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxMaxJitterBufferDepth"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxFrameLateDiscards"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxFrameOverflows"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxFrameOutOfOrders"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxSyncSource"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTxPackets"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTxOctets"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTxSyncSource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSMediaGatewayRtpSessionGroup = adGenAOSMediaGatewayRtpSessionGroup.setStatus('current')
adGenAOSMediaGatewayRtpSessionTotalsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 99, 2, 2)).setObjects(("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsSessions"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsSessionDuration"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsRxPackets"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsRxOctets"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsRxPacketsLost"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsRxPacketsUnknown"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsTxPackets"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsTxOctets"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsRxFrameLateDiscards"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsRxFrameOverflows"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsRxFrameOutOfOrders"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsClearCounters"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsTimeSinceLastClearCounters"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSMediaGatewayRtpSessionTotalsGroup = adGenAOSMediaGatewayRtpSessionTotalsGroup.setStatus('current')
adGenAOSMediaGatewayInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 99, 2, 3)).setObjects(("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSMediaGatewayInfoIdentifier"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSMediaGatewayInfoSoftwareVersion"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSMediaGatewayInfoUtilization"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSMediaGatewayInfoUtilizationMaximum"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSMediaGatewayInfoFreePacketBuffers"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSMediaGatewayInfoUptime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSMediaGatewayInfoGroup = adGenAOSMediaGatewayInfoGroup.setStatus('current')
adGenAOSMediaGatewayRtpChannelTotalsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 99, 2, 4)).setObjects(("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalId"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalIdName"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalSessions"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalSessionDuration"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalRxPackets"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalRxOctets"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalRxPacketsLost"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalRxPacketsUnknown"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalTxPackets"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalTxOctets"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalRxMaxDepth"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalRxFrameLateDiscards"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalRxFrameOverflows"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalRxFrameOutOfOrders"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelClearCounters"), ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTimeSinceLastClearCounters"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSMediaGatewayRtpChannelTotalsGroup = adGenAOSMediaGatewayRtpChannelTotalsGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-MEDIAGATEWAY-MIB", adGenAOSRtpChannelTotalTable=adGenAOSRtpChannelTotalTable, adGenAOSRtpSessionTotalsRxOctets=adGenAOSRtpSessionTotalsRxOctets, adGenAOSRtpSessionRemoteUdpPort=adGenAOSRtpSessionRemoteUdpPort, adGenAOSRtpSessionTotalsSessionDuration=adGenAOSRtpSessionTotalsSessionDuration, adGenAOSRtpChannelTotalSessions=adGenAOSRtpChannelTotalSessions, adGenAOSRtpSessionVAD=adGenAOSRtpSessionVAD, adGenAOSRtpChannelTotalRxFrameOutOfOrders=adGenAOSRtpChannelTotalRxFrameOutOfOrders, adGenAOSRtpSessionSIPPortDescription=adGenAOSRtpSessionSIPPortDescription, adGenAOSRtpSessionTotalsTxPackets=adGenAOSRtpSessionTotalsTxPackets, adGenAOSRtpChannelTotalIdName=adGenAOSRtpChannelTotalIdName, adGenAOSRtpSessionLocalUdpPort=adGenAOSRtpSessionLocalUdpPort, adGenAOSRtpSessionTxFramesPerPacket=adGenAOSRtpSessionTxFramesPerPacket, adGenAOSRtpSessionTable=adGenAOSRtpSessionTable, adGenAOSMediaGatewayRtpSessionTotalsGroup=adGenAOSMediaGatewayRtpSessionTotalsGroup, adGenAOSMediaGatewayRtpChannelTotalsGroup=adGenAOSMediaGatewayRtpChannelTotalsGroup, adGenAOSMediaGatewayInfoGroup=adGenAOSMediaGatewayInfoGroup, adGenAOSRtpSessionTotalsRxFrameOverflows=adGenAOSRtpSessionTotalsRxFrameOverflows, adGenAOSMediaGatewayCompliances=adGenAOSMediaGatewayCompliances, adGenAOSRtpSessionStatus=adGenAOSRtpSessionStatus, adGenAOSRtpSessionStartTime=adGenAOSRtpSessionStartTime, adGenAOSRtpChannelTimeSinceLastClearCounters=adGenAOSRtpChannelTimeSinceLastClearCounters, adGenAOSMediaGatewayConformance=adGenAOSMediaGatewayConformance, adGenAOSMediaGatewayInfoUtilization=adGenAOSMediaGatewayInfoUtilization, adGenAOSRtpSessionTotalsRxFrameOutOfOrders=adGenAOSRtpSessionTotalsRxFrameOutOfOrders, adGenAOSRtpSessionTotalsRxPacketsUnknown=adGenAOSRtpSessionTotalsRxPacketsUnknown, adGenAOSRtpSessionTotalsEntry=adGenAOSRtpSessionTotalsEntry, adGenAOSMediaGateway=adGenAOSMediaGateway, adGenAOSRtpChannelTotalTxOctets=adGenAOSRtpChannelTotalTxOctets, adGenAOSRtpSessionRxFrameLateDiscards=adGenAOSRtpSessionRxFrameLateDiscards, adGenAOSRtpChannelTotalRxMaxDepth=adGenAOSRtpChannelTotalRxMaxDepth, adGenAOSRtpChannelTotalTxPackets=adGenAOSRtpChannelTotalTxPackets, adGenAOSMediaGatewayInfoFreePacketBuffers=adGenAOSMediaGatewayInfoFreePacketBuffers, adGenAOSMediaGatewayObjects=adGenAOSMediaGatewayObjects, adGenAOSRtpChannelClearCounters=adGenAOSRtpChannelClearCounters, adGenAOSRtpSessionRxSyncSource=adGenAOSRtpSessionRxSyncSource, adGenAOSRtpSessionEchoCancellerEnabled=adGenAOSRtpSessionEchoCancellerEnabled, adGenAOSRtpSessionTotalsTable=adGenAOSRtpSessionTotalsTable, adGenAOSRtpSessionLocalIPAddress=adGenAOSRtpSessionLocalIPAddress, adGenAOSMediaGatewayRtpSessionGroup=adGenAOSMediaGatewayRtpSessionGroup, adGenAOSRtpChannelTotalEntry=adGenAOSRtpChannelTotalEntry, adGenAOSRtpSessionTxSyncSource=adGenAOSRtpSessionTxSyncSource, adGenAOSRtpSessionTxOctets=adGenAOSRtpSessionTxOctets, adGenAOSMediaGatewayInfoSoftwareVersion=adGenAOSMediaGatewayInfoSoftwareVersion, adGenAOSRtpChannelTotalRxOctets=adGenAOSRtpChannelTotalRxOctets, adGenAOSRtpSessionTotalsSessions=adGenAOSRtpSessionTotalsSessions, adGenAOSRtpSessionRxJitterBufferDepth=adGenAOSRtpSessionRxJitterBufferDepth, adGenAOSRtpChannelTotalId=adGenAOSRtpChannelTotalId, adGenAOSRtpSessionRxPacketsLost=adGenAOSRtpSessionRxPacketsLost, adGenAOSRtpChannelTotalRxFrameLateDiscards=adGenAOSRtpChannelTotalRxFrameLateDiscards, adGenAOSRtpSessionTotalsRxPacketsLost=adGenAOSRtpSessionTotalsRxPacketsLost, PYSNMP_MODULE_ID=adGenAOSMediaGatewayMIB, adGenAOSRtpSessionRxFrameOverflows=adGenAOSRtpSessionRxFrameOverflows, adGenAOSRtpSessionTotalsTimeSinceLastClearCounters=adGenAOSRtpSessionTotalsTimeSinceLastClearCounters, adGenAOSRtpSessionRxPacketsUnknown=adGenAOSRtpSessionRxPacketsUnknown, adGenAOSRtpChannelTotalSessionDuration=adGenAOSRtpChannelTotalSessionDuration, adGenAOSRtpSessionChannelIdName=adGenAOSRtpSessionChannelIdName, adGenAOSRtpSessionRemoteIPAddress=adGenAOSRtpSessionRemoteIPAddress, adGenAOSRtpSessionRxFrameOutOfOrders=adGenAOSRtpSessionRxFrameOutOfOrders, adGenAOSRtpSessionDuration=adGenAOSRtpSessionDuration, adGenAOSRtpSessionTotalsRxFrameLateDiscards=adGenAOSRtpSessionTotalsRxFrameLateDiscards, adGenAOSRtpSessionEntry=adGenAOSRtpSessionEntry, adGenAOSMediaGatewayMIBGroups=adGenAOSMediaGatewayMIBGroups, adGenAOSRtpSessionRxMaxJitterBufferDepth=adGenAOSRtpSessionRxMaxJitterBufferDepth, adGenAOSRtpChannelTotalRxFrameOverflows=adGenAOSRtpChannelTotalRxFrameOverflows, adGenAOSRtpSessionVocoder=adGenAOSRtpSessionVocoder, adGenAOSMediaGatewayInfoEntry=adGenAOSMediaGatewayInfoEntry, adGenAOSMediaGatewayInfoUptime=adGenAOSMediaGatewayInfoUptime, adGenAOSRtpChannelTotalRxPacketsUnknown=adGenAOSRtpChannelTotalRxPacketsUnknown, adGenAOSMediaGatewayMIB=adGenAOSMediaGatewayMIB, adGenAOSRtpSessionChannelId=adGenAOSRtpSessionChannelId, adGenAOSMediaGatewayInfoUtilizationMaximum=adGenAOSMediaGatewayInfoUtilizationMaximum, adGenAOSRtpSessionTdmPortDescription=adGenAOSRtpSessionTdmPortDescription, adGenAOSRtpSessionRxOctets=adGenAOSRtpSessionRxOctets, adGenAOSMediaGatewayInfoTable=adGenAOSMediaGatewayInfoTable, adGenAOSMediaGatewayInfoIdentifier=adGenAOSMediaGatewayInfoIdentifier, adGenAOSRtpChannelTotalRxPacketsLost=adGenAOSRtpChannelTotalRxPacketsLost, adGenAOSRtpSessionTotalsTxOctets=adGenAOSRtpSessionTotalsTxOctets, adGenAOSRtpSessionTotalsRxPackets=adGenAOSRtpSessionTotalsRxPackets, adGenAOSRtpChannelTotalRxPackets=adGenAOSRtpChannelTotalRxPackets, adGenAOSRtpSessionRxPackets=adGenAOSRtpSessionRxPackets, adGenAOSMediaGatewayCompliance=adGenAOSMediaGatewayCompliance, adGenAOSRtpSessionTxPackets=adGenAOSRtpSessionTxPackets, adGenAOSRtpSessionTotalsClearCounters=adGenAOSRtpSessionTotalsClearCounters)
