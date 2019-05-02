#
# PySNMP MIB module CISCO-VPDN-MGMT-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VPDN-MGMT-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:19:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
cvpdnTunnelAttrEntry, cvpdnSessionAttrEntry = mibBuilder.importSymbols("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrEntry", "cvpdnSessionAttrEntry")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter64, MibIdentifier, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, Integer32, IpAddress, NotificationType, Counter32, ObjectIdentity, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "Integer32", "IpAddress", "NotificationType", "Counter32", "ObjectIdentity", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoVpdnMgmtExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 51))
ciscoVpdnMgmtExtMIB.setRevisions(('2011-12-01 00:00', '2007-06-04 00:00', '1999-04-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVpdnMgmtExtMIB.setRevisionsDescriptions(('This revision involves the following changes to table cvpdnTunnelExtTable. 1] Deprecated cvpdnTunnelBytesIn, cvpdnTunnelBytesOut 32-bit counters. 2] Added new OIDs cvpdnTunnelBytesIn64, cvpdnTunnelBytesOut64 64-bit counters.', 'Corrected the format of LAST-UPDATED and REVISION fields.', 'Original version of this MIB.',))
if mibBuilder.loadTexts: ciscoVpdnMgmtExtMIB.setLastUpdated('201112010000Z')
if mibBuilder.loadTexts: ciscoVpdnMgmtExtMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVpdnMgmtExtMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-vpdn@cisco.com')
if mibBuilder.loadTexts: ciscoVpdnMgmtExtMIB.setDescription('Cisco VPDN management MIB extension Module. This MIB is a supplement to CISCO-VPDN-MGMT-MIB.my. The main enhancements are: 1. Added cvpdnTunnelExtTable for more tunnel information. 2. Added cvpdnSessionExtTable for more session information. Please notice that objects in CvpdnTunnelEntry and CvpdnTunnelSessionEntry are still applicable to the corresponding tunnels and sessions.')
ciscoVpdnMgmtExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 51, 1))
cvpdnTunnelExtInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1))
cvpdnSessionExtInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2))
cvpdnTunnelExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1), )
if mibBuilder.loadTexts: cvpdnTunnelExtTable.setStatus('current')
if mibBuilder.loadTexts: cvpdnTunnelExtTable.setDescription('Vpn Tunnel table includes all tunnels configured.')
cvpdnTunnelExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1), )
cvpdnTunnelAttrEntry.registerAugmentions(("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelExtEntry"))
cvpdnTunnelExtEntry.setIndexNames(*cvpdnTunnelAttrEntry.getIndexNames())
if mibBuilder.loadTexts: cvpdnTunnelExtEntry.setStatus('current')
if mibBuilder.loadTexts: cvpdnTunnelExtEntry.setDescription('Please notice that this entry is a supplement to CvpdnTunnelEntry in CISCO-VPDN-MGMT-MIB for the L2TP tunnels. Here more objects are used to reflect tunnel parameters. Included are tunnel statistics, UDP port numbers and the time of last state (cvpdnTunnelState) change.')
cvpdnTunnelLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnTunnelLocalPort.setStatus('current')
if mibBuilder.loadTexts: cvpdnTunnelLocalPort.setDescription('The local port number of the tunnel. This is the UDP port of the interface at the local end of the tunnel.')
cvpdnTunnelRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnTunnelRemotePort.setStatus('current')
if mibBuilder.loadTexts: cvpdnTunnelRemotePort.setDescription('The remote port number of the tunnel. This is the UDP port of the interface at the remote end of the tunnel.')
cvpdnTunnelLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnTunnelLastChange.setStatus('current')
if mibBuilder.loadTexts: cvpdnTunnelLastChange.setDescription('The time of last state change reflected in cvpdnTunnelState.')
cvpdnTunnelPacketsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnTunnelPacketsOut.setStatus('current')
if mibBuilder.loadTexts: cvpdnTunnelPacketsOut.setDescription('The total number of output packets through the tunnel.')
cvpdnTunnelBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 5), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnTunnelBytesOut.setStatus('deprecated')
if mibBuilder.loadTexts: cvpdnTunnelBytesOut.setDescription('The total number of output bytes through the tunnel. cvpdnTunnelBytesOut object is superseded by cvpdnTunnelBytesOut64.')
cvpdnTunnelPacketsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnTunnelPacketsIn.setStatus('current')
if mibBuilder.loadTexts: cvpdnTunnelPacketsIn.setDescription('The total number of input packets through the tunnel.')
cvpdnTunnelBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 7), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnTunnelBytesIn.setStatus('deprecated')
if mibBuilder.loadTexts: cvpdnTunnelBytesIn.setDescription('The total number of input bytes through the tunnel. cvpdnTunnelBytesIn object is superseded by cvpdnTunnelBytesIn64.')
cvpdnTunnelBytesIn64 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnTunnelBytesIn64.setStatus('current')
if mibBuilder.loadTexts: cvpdnTunnelBytesIn64.setDescription('The total number of input bytes through the tunnel.')
cvpdnTunnelBytesOut64 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnTunnelBytesOut64.setStatus('current')
if mibBuilder.loadTexts: cvpdnTunnelBytesOut64.setDescription('The total number of output bytes through the tunnel.')
cvpdnSessionExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1), )
if mibBuilder.loadTexts: cvpdnSessionExtTable.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionExtTable.setDescription('Session table includes all Sessions currently active.')
cvpdnSessionExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1), )
cvpdnSessionAttrEntry.registerAugmentions(("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionExtEntry"))
cvpdnSessionExtEntry.setIndexNames(*cvpdnSessionAttrEntry.getIndexNames())
if mibBuilder.loadTexts: cvpdnSessionExtEntry.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionExtEntry.setDescription('Please notice that this entry is a supplement to CvpdnTunnelSessionEntry in CISCO-VPDN-MGMT-MIB for the L2TP sessions. Here more objects are used to reflect session parameters.')
cvpdnSessionRemoteId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionRemoteId.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionRemoteId.setDescription('The remote end ID of an active VPN tunnel user session.')
cvpdnSessionInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionInterfaceName.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionInterfaceName.setDescription('The interface name (description) of the user session.')
cvpdnSessionLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionLastChange.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionLastChange.setDescription('The time stamp of last change in cvpdnTunnelSessionState.')
cvpdnSessionOutOfOrderPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionOutOfOrderPackets.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionOutOfOrderPackets.setDescription('The total number of out of order packets through this active user session.')
cvpdnSessionSequencing = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionSequencing.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionSequencing.setDescription('The object indicates whether sequencing is on or not.')
cvpdnSessionSendSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionSendSequence.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionSendSequence.setDescription('This object contains the next send sequence number for for this session.')
cvpdnSessionRecvSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionRecvSequence.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionRecvSequence.setDescription('This object contains the next receive sequence number expected to be received on this session.')
cvpdnSessionRemoteSendSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionRemoteSendSequence.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionRemoteSendSequence.setDescription('This object contains the next send sequence number for for this session.')
cvpdnSessionRemoteRecvSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionRemoteRecvSequence.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionRemoteRecvSequence.setDescription('This object contains the next receive sequence number expected to be received on this session.')
cvpdnSessionSentZLB = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionSentZLB.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionSentZLB.setDescription('This object returns the total number of Zero Length Body acknowledgement packets transmitted on this session.')
cvpdnSessionRecvZLB = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionRecvZLB.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionRecvZLB.setDescription('This object returns the total number of Zero Length Body acknowlegement payload packets received for this session.')
cvpdnSessionSentRBits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionSentRBits.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionSentRBits.setDescription('This object contains the total number of sequence number resets (payload packets with the R-bit set) received on this session.')
cvpdnSessionRecvRBits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionRecvRBits.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionRecvRBits.setDescription('This object contains the total number of sequence number resets (payload packets with the R-bit set) received on this session.')
cvpdnSessionLocalWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionLocalWindowSize.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionLocalWindowSize.setDescription('This object returns the local send window size for this session. If the value of the object cvpdnSessionSequencing is false, then this object should return value zero.')
cvpdnSessionRemoteWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionRemoteWindowSize.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionRemoteWindowSize.setDescription('This object returns the initial remote send window size for this session. If the value of the object cvpdnSessionSequencingState is none(1) then this object should not be interpreted.')
cvpdnSessionCurrentWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionCurrentWindowSize.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionCurrentWindowSize.setDescription('This object returns the local send window size for this session. If the value of the object cvpdnSessionSequencingState is none(1) then this object should not be interpreted.')
cvpdnSessionMinimumWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionMinimumWindowSize.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionMinimumWindowSize.setDescription('This object returns the initial remote send window size for this session. If the value of the object cvpdnSessionSequencingState is none(1) then this object should not be interpreted.')
cvpdnSessionATOTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('msecs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionATOTimeouts.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionATOTimeouts.setDescription('The object reflects the current adaptive timeout the system is using.')
cvpdnSessionOutGoingQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionOutGoingQueueSize.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionOutGoingQueueSize.setDescription('The object reflects the queue size of out going queue.')
cvpdnSessionCalculationType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("adaptive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionCalculationType.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionCalculationType.setDescription('The object reflects the round trip time calculation type.')
cvpdnSessionAdaptiveTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('msecs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionAdaptiveTimeOut.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionAdaptiveTimeOut.setDescription('The object reflects the configured session adaptive timeout.')
cvpdnSessionRoundTripTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('msecs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionRoundTripTime.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionRoundTripTime.setDescription('The object reflects the round trip time.')
cvpdnSessionPktProcessingDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionPktProcessingDelay.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionPktProcessingDelay.setDescription('The object reflects the number of packets in processing delay for this session.')
cvpdnSessionZLBTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('msecs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionZLBTime.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionZLBTime.setDescription('The object reflects the zero length body time interval.')
ciscoVpdnMgtExtMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 51, 2))
ciscoVpdnMgmtExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 51, 3))
ciscoVpdnMgmtExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 1))
ciscoVpdnMgmtExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 2))
ciscoVpdnMgmtExtMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 1, 1)).setObjects(("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelExtGroup"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVpdnMgmtExtMIBBasicCompliance = ciscoVpdnMgmtExtMIBBasicCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoVpdnMgmtExtMIBBasicCompliance.setDescription('The compliance statement for entities which implement the Cisco VPN Management MIB. ciscoVpdnMgmtExtMIBBasicCompliance is superseded by ciscoVpdnMgmtExtMIBBasicComplianceV2.')
ciscoVpdnMgmtExtMIBBasicComplianceV2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 1, 2)).setObjects(("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionExtGroup"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelExtGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVpdnMgmtExtMIBBasicComplianceV2 = ciscoVpdnMgmtExtMIBBasicComplianceV2.setStatus('current')
if mibBuilder.loadTexts: ciscoVpdnMgmtExtMIBBasicComplianceV2.setDescription('The compliance statement for entities which implement the Cisco VPN Management MIB Version 2.')
cvpdnTunnelExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 2, 1)).setObjects(("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelLocalPort"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelRemotePort"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelLastChange"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelPacketsIn"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelPacketsOut"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelBytesIn"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelBytesOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvpdnTunnelExtGroup = cvpdnTunnelExtGroup.setStatus('deprecated')
if mibBuilder.loadTexts: cvpdnTunnelExtGroup.setDescription('VPN Tunnel Group. cvpdnTunnelExtGroup is superseded by cvpdnTunnelExtGroupV2')
cvpdnSessionExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 2, 2)).setObjects(("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRemoteId"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionInterfaceName"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionLastChange"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionSequencing"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionSendSequence"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRecvSequence"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRemoteSendSequence"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRemoteRecvSequence"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionOutOfOrderPackets"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionSentZLB"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRecvZLB"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionSentRBits"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRecvRBits"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionLocalWindowSize"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRemoteWindowSize"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionCurrentWindowSize"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionMinimumWindowSize"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionATOTimeouts"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionOutGoingQueueSize"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionCalculationType"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionAdaptiveTimeOut"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRoundTripTime"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionPktProcessingDelay"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionZLBTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvpdnSessionExtGroup = cvpdnSessionExtGroup.setStatus('current')
if mibBuilder.loadTexts: cvpdnSessionExtGroup.setDescription('VPDP Session Group.')
cvpdnTunnelExtGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 2, 3)).setObjects(("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelLocalPort"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelRemotePort"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelLastChange"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelPacketsOut"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelPacketsIn"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelBytesIn64"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelBytesOut64"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvpdnTunnelExtGroupV2 = cvpdnTunnelExtGroupV2.setStatus('current')
if mibBuilder.loadTexts: cvpdnTunnelExtGroupV2.setDescription('VPN Tunnel Group Version 2.')
mibBuilder.exportSymbols("CISCO-VPDN-MGMT-EXT-MIB", cvpdnTunnelLocalPort=cvpdnTunnelLocalPort, ciscoVpdnMgmtExtMIBBasicCompliance=ciscoVpdnMgmtExtMIBBasicCompliance, cvpdnSessionRecvZLB=cvpdnSessionRecvZLB, cvpdnTunnelPacketsIn=cvpdnTunnelPacketsIn, cvpdnSessionRemoteId=cvpdnSessionRemoteId, cvpdnSessionExtInfo=cvpdnSessionExtInfo, cvpdnTunnelExtEntry=cvpdnTunnelExtEntry, cvpdnTunnelExtTable=cvpdnTunnelExtTable, cvpdnSessionZLBTime=cvpdnSessionZLBTime, cvpdnTunnelBytesIn=cvpdnTunnelBytesIn, cvpdnSessionSendSequence=cvpdnSessionSendSequence, cvpdnTunnelPacketsOut=cvpdnTunnelPacketsOut, cvpdnSessionLastChange=cvpdnSessionLastChange, cvpdnTunnelExtGroup=cvpdnTunnelExtGroup, cvpdnSessionRemoteRecvSequence=cvpdnSessionRemoteRecvSequence, cvpdnSessionSentZLB=cvpdnSessionSentZLB, cvpdnSessionExtEntry=cvpdnSessionExtEntry, cvpdnSessionPktProcessingDelay=cvpdnSessionPktProcessingDelay, ciscoVpdnMgmtExtMIBGroups=ciscoVpdnMgmtExtMIBGroups, cvpdnTunnelBytesOut64=cvpdnTunnelBytesOut64, cvpdnSessionInterfaceName=cvpdnSessionInterfaceName, cvpdnSessionATOTimeouts=cvpdnSessionATOTimeouts, ciscoVpdnMgmtExtMIBObjects=ciscoVpdnMgmtExtMIBObjects, cvpdnSessionMinimumWindowSize=cvpdnSessionMinimumWindowSize, cvpdnSessionCurrentWindowSize=cvpdnSessionCurrentWindowSize, cvpdnTunnelBytesIn64=cvpdnTunnelBytesIn64, ciscoVpdnMgmtExtMIB=ciscoVpdnMgmtExtMIB, cvpdnSessionSequencing=cvpdnSessionSequencing, cvpdnTunnelLastChange=cvpdnTunnelLastChange, cvpdnSessionRemoteSendSequence=cvpdnSessionRemoteSendSequence, cvpdnTunnelBytesOut=cvpdnTunnelBytesOut, ciscoVpdnMgmtExtMIBConformance=ciscoVpdnMgmtExtMIBConformance, cvpdnSessionRemoteWindowSize=cvpdnSessionRemoteWindowSize, ciscoVpdnMgmtExtMIBCompliances=ciscoVpdnMgmtExtMIBCompliances, cvpdnSessionRoundTripTime=cvpdnSessionRoundTripTime, cvpdnSessionAdaptiveTimeOut=cvpdnSessionAdaptiveTimeOut, cvpdnSessionExtGroup=cvpdnSessionExtGroup, cvpdnSessionOutOfOrderPackets=cvpdnSessionOutOfOrderPackets, cvpdnTunnelExtInfo=cvpdnTunnelExtInfo, cvpdnSessionExtTable=cvpdnSessionExtTable, cvpdnSessionRecvSequence=cvpdnSessionRecvSequence, cvpdnSessionSentRBits=cvpdnSessionSentRBits, cvpdnTunnelRemotePort=cvpdnTunnelRemotePort, PYSNMP_MODULE_ID=ciscoVpdnMgmtExtMIB, cvpdnSessionOutGoingQueueSize=cvpdnSessionOutGoingQueueSize, ciscoVpdnMgtExtMIBNotificationPrefix=ciscoVpdnMgtExtMIBNotificationPrefix, cvpdnSessionRecvRBits=cvpdnSessionRecvRBits, ciscoVpdnMgmtExtMIBBasicComplianceV2=ciscoVpdnMgmtExtMIBBasicComplianceV2, cvpdnTunnelExtGroupV2=cvpdnTunnelExtGroupV2, cvpdnSessionCalculationType=cvpdnSessionCalculationType, cvpdnSessionLocalWindowSize=cvpdnSessionLocalWindowSize)