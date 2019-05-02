#
# PySNMP MIB module SONUS-SIP-SIGNALLING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONUS-SIP-SIGNALLING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:10:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, NotificationType, iso, TimeTicks, Counter64, ModuleIdentity, Unsigned32, Counter32, Integer32, MibIdentifier, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "NotificationType", "iso", "TimeTicks", "Counter64", "ModuleIdentity", "Unsigned32", "Counter32", "Integer32", "MibIdentifier", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
sonusEventLevel, sonusEventDescription, sonusEventClass = mibBuilder.importSymbols("SONUS-COMMON-MIB", "sonusEventLevel", "sonusEventDescription", "sonusEventClass")
sonusSignallingMIBs, = mibBuilder.importSymbols("SONUS-SMI", "sonusSignallingMIBs")
SonusServiceState, SonusAdminState, SonusName = mibBuilder.importSymbols("SONUS-TC", "SonusServiceState", "SonusAdminState", "SonusName")
sonusSipSignallingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7))
if mibBuilder.loadTexts: sonusSipSignallingMIB.setLastUpdated('200107310000Z')
if mibBuilder.loadTexts: sonusSipSignallingMIB.setOrganization('Sonus Networks, Inc.')
if mibBuilder.loadTexts: sonusSipSignallingMIB.setContactInfo(' Customer Support Sonus Networks, Inc, 5 carlisle Road Westford, MA 01886 USA Tel: 978-692-8999 Fax: 978-392-9118 E-mail: cs.snmp@sonusnet.com')
if mibBuilder.loadTexts: sonusSipSignallingMIB.setDescription('The MIB Module for SIP IP Call Signal Port Management.')
sonusSipSignallingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1))
sonusSipSigTimerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 1))
sonusSipSigTimerT1 = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)).clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSipSigTimerT1.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigTimerT1.setDescription('This is the SIP protocol retransmission timer T1 (in milliseconds). This value applies to all future SIP calls.')
sonusSipSigTimerT2 = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(4000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSipSigTimerT2.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigTimerT2.setDescription('This is the SIP protocol retransmission timer T2 (in milliseconds). This value applies to all future SIP calls.')
sonusSipSigTimerSessionKeepalive = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000)).clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSipSigTimerSessionKeepalive.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigTimerSessionKeepalive.setDescription('This is the SIP protocol session keep-alive timer (in seconds). This value applies to all future SIP calls. when it is set to 0 keepalive is turned off')
sonusSipSigRetryObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 2))
sonusSipSigNumOfRetry = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 12)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSipSigNumOfRetry.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigNumOfRetry.setDescription('This is the number of retransmission for SIP message. This value applies to all future SIP calls.')
sonusSipSigInviteRetry = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 12)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSipSigInviteRetry.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigInviteRetry.setDescription('This is the number of retransmission for INVITE. This value applies to all future SIP calls.')
sonusSipSigPortTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3), )
if mibBuilder.loadTexts: sonusSipSigPortTable.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortTable.setDescription('Table of SIP Signalling Port configurations. Limit of two ports.')
sonusSipSigPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1), ).setIndexNames((0, "SONUS-SIP-SIGNALLING-MIB", "sonusSipSigPortIndex"))
if mibBuilder.loadTexts: sonusSipSigPortEntry.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortEntry.setDescription('SIP Signalling Port configuration.')
sonusSipSigPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipSigPortIndex.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortIndex.setDescription('Identifies the Signal Listen Port entry.')
sonusSipSigPortIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSipSigPortIpAddress.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortIpAddress.setDescription('IP Address of the Sip Signalling Port - mandatory parameter')
sonusSipSigPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(5060)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSipSigPortNum.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortNum.setDescription('UDP port number of SIP Signalling Port (default is 5060).')
sonusSipSigPortInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mgtNif", 1), ("nif", 2))).clone('mgtNif')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSipSigPortInterface.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortInterface.setDescription("The interface type of SIP Call Signal Port. 'mgtnif' routes traffic over the gateway Managment ports. 'nif' routes traffic over one of the gateway PNS ports.")
sonusSipSigPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2))).clone('primary')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSipSigPortRole.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortRole.setDescription('Role of the Sip Call Siganlling Port.')
sonusSipSigPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1, 6), SonusServiceState().clone('inService')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSipSigPortMode.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortMode.setDescription('Mode of the SIP Signalling Port.')
sonusSipSigPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1, 7), SonusAdminState().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSipSigPortState.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortState.setDescription('State of the SIP Signalling Port.')
sonusSipSigPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSipSigPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortRowStatus.setDescription('This is for SNMP use.')
sonusSipSigPortAclState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1, 9), SonusAdminState().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSipSigPortAclState.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortAclState.setDescription('ACL checking state of the SIP Signalling port')
sonusSipSigPortStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 4), )
if mibBuilder.loadTexts: sonusSipSigPortStatusTable.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatusTable.setDescription('Table of SIP Signalling Port status.')
sonusSipSigPortStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 4, 1), ).setIndexNames((0, "SONUS-SIP-SIGNALLING-MIB", "sonusSipSigPortStatusIndex"))
if mibBuilder.loadTexts: sonusSipSigPortStatusEntry.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatusEntry.setDescription('SIP Signalling Port Status.')
sonusSipSigPortStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipSigPortStatusIndex.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatusIndex.setDescription('Identifies the Signal Listen Port entry.')
sonusSipSigPortStatusIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipSigPortStatusIpAddress.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatusIpAddress.setDescription('IP Address of the Sip Signalling Port')
sonusSipSigPortStatusNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipSigPortStatusNum.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatusNum.setDescription('UDP port number of SIP Signalling Port.')
sonusSipSigPortStatusInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mgtNif", 1), ("nif", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipSigPortStatusInterface.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatusInterface.setDescription("The interface type of SIP Call Signal Port. 'mgtnif' routes traffic over the gateway Managment ports. 'nif' routes traffic over one of the gateway PNS ports.")
sonusSipSigPortStatusRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipSigPortStatusRole.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatusRole.setDescription('Role of the Sip Call Siganlling Port.')
sonusSipSigPortStatusNif = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipSigPortStatusNif.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatusNif.setDescription('The network interface index of the port.')
sonusSipSigPortStatusState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 4, 1, 7), SonusServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipSigPortStatusState.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatusState.setDescription('State of the SIP Signalling Port.')
sonusSipSigPortStatTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5), )
if mibBuilder.loadTexts: sonusSipSigPortStatTable.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatTable.setDescription('Table of SIP Signalling Port statistics data.')
sonusSipSigPortStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1), ).setIndexNames((0, "SONUS-SIP-SIGNALLING-MIB", "sonusSipSigPortStatIndex"))
if mibBuilder.loadTexts: sonusSipSigPortStatEntry.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatEntry.setDescription('SIP Signalling Port Statistics.')
sonusSipSigPortStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipSigPortStatIndex.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatIndex.setDescription('Identifies the Signal Listen Port entry.')
sonusSipSigPortStatIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipSigPortStatIpAddress.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatIpAddress.setDescription('IP Address of the Sip Signalling Port')
sonusSipSigPortStatPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipSigPortStatPortNum.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatPortNum.setDescription('UDP port number of SIP Signalling Port.')
sonusSipSigPortStatCountReset = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unknown", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSipSigPortStatCountReset.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatCountReset.setDescription('set opertion on this object resets all the statistics counts to zero')
sonusSipSigPortStatCallRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipSigPortStatCallRate.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatCallRate.setDescription('number of SIP calls per second during the last minute')
sonusSipSigPortStatNumOrigCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipSigPortStatNumOrigCalls.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatNumOrigCalls.setDescription('Total number of outgoing calls sent out from this signaling port')
sonusSipSigPortStatNumTermCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipSigPortStatNumTermCalls.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatNumTermCalls.setDescription('Total number of incoming calls received on this signaling port')
sonusSipSigPortStatNumTxPdus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipSigPortStatNumTxPdus.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatNumTxPdus.setDescription('The total number of signalling PDUS sent out on this port')
sonusSipSigPortStatNumRxPdus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipSigPortStatNumRxPdus.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatNumRxPdus.setDescription('The total number of signalling PDUS received on this port')
sonusSipSigPortStatNumTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipSigPortStatNumTxBytes.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatNumTxBytes.setDescription('The total number of signalling BYTES sent out from this port')
sonusSipSigPortStatNumRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipSigPortStatNumRxBytes.setStatus('current')
if mibBuilder.loadTexts: sonusSipSigPortStatNumRxBytes.setDescription('The total number of signalling BYTES received by this port')
sonusSipAcl = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 6))
sonusSipAclNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipAclNextIndex.setStatus('current')
if mibBuilder.loadTexts: sonusSipAclNextIndex.setDescription('the next valid index to use when creating a new sonusSipAclEntry')
sonusSipAclTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 6, 2), )
if mibBuilder.loadTexts: sonusSipAclTable.setStatus('current')
if mibBuilder.loadTexts: sonusSipAclTable.setDescription('This is the Application Server List')
sonusSipAclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 6, 2, 1), ).setIndexNames((0, "SONUS-SIP-SIGNALLING-MIB", "sonusSipRemoteAppSvrIndex"))
if mibBuilder.loadTexts: sonusSipAclEntry.setStatus('current')
if mibBuilder.loadTexts: sonusSipAclEntry.setDescription('An Application Server')
sonusSipRemoteAppSvrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 6, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSipRemoteAppSvrIndex.setStatus('current')
if mibBuilder.loadTexts: sonusSipRemoteAppSvrIndex.setDescription('Identifies a remote application server entry.')
sonusSipRemoteAppSvrName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 6, 2, 1, 2), SonusName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSipRemoteAppSvrName.setStatus('current')
if mibBuilder.loadTexts: sonusSipRemoteAppSvrName.setDescription('Name of the application server.')
sonusSipRemoteAppSvrIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 6, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSipRemoteAppSvrIpAddress.setStatus('current')
if mibBuilder.loadTexts: sonusSipRemoteAppSvrIpAddress.setDescription('IP Address of the application server.')
sonusSipRemoteAppSvrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 6, 2, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSipRemoteAppSvrRowStatus.setStatus('current')
if mibBuilder.loadTexts: sonusSipRemoteAppSvrRowStatus.setDescription('row status of the application server.')
sonusSipSignallingMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 2))
sonusSipSignallingMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 2, 0))
sonusSipSignallingMIBNotificationsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 2, 1))
sonusSipCallSigPortOpenNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 2, 0, 1)).setObjects(("SONUS-SIP-SIGNALLING-MIB", "sonusSipSigPortIpAddress"), ("SONUS-SIP-SIGNALLING-MIB", "sonusSipSigPortNum"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusSipCallSigPortOpenNotification.setStatus('current')
if mibBuilder.loadTexts: sonusSipCallSigPortOpenNotification.setDescription('This trap indicates that a call signaling port is opened.')
sonusSipCallSigPortCloseNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 2, 0, 2)).setObjects(("SONUS-SIP-SIGNALLING-MIB", "sonusSipSigPortIpAddress"), ("SONUS-SIP-SIGNALLING-MIB", "sonusSipSigPortNum"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusSipCallSigPortCloseNotification.setStatus('current')
if mibBuilder.loadTexts: sonusSipCallSigPortCloseNotification.setDescription('This trap indicates that a call signaling port is closed.')
mibBuilder.exportSymbols("SONUS-SIP-SIGNALLING-MIB", PYSNMP_MODULE_ID=sonusSipSignallingMIB, sonusSipSignallingMIBNotifications=sonusSipSignallingMIBNotifications, sonusSipSigPortState=sonusSipSigPortState, sonusSipSigPortStatTable=sonusSipSigPortStatTable, sonusSipSigPortStatNumRxPdus=sonusSipSigPortStatNumRxPdus, sonusSipRemoteAppSvrIpAddress=sonusSipRemoteAppSvrIpAddress, sonusSipRemoteAppSvrName=sonusSipRemoteAppSvrName, sonusSipSigTimerT1=sonusSipSigTimerT1, sonusSipSigTimerObjects=sonusSipSigTimerObjects, sonusSipRemoteAppSvrRowStatus=sonusSipRemoteAppSvrRowStatus, sonusSipSigPortStatusIndex=sonusSipSigPortStatusIndex, sonusSipSigPortRowStatus=sonusSipSigPortRowStatus, sonusSipSigPortStatusEntry=sonusSipSigPortStatusEntry, sonusSipSigRetryObjects=sonusSipSigRetryObjects, sonusSipSigPortStatusNif=sonusSipSigPortStatusNif, sonusSipCallSigPortOpenNotification=sonusSipCallSigPortOpenNotification, sonusSipSigPortStatusState=sonusSipSigPortStatusState, sonusSipSigPortStatNumOrigCalls=sonusSipSigPortStatNumOrigCalls, sonusSipSigPortEntry=sonusSipSigPortEntry, sonusSipSigPortStatusRole=sonusSipSigPortStatusRole, sonusSipSigPortStatNumRxBytes=sonusSipSigPortStatNumRxBytes, sonusSipSigPortStatEntry=sonusSipSigPortStatEntry, sonusSipSigPortNum=sonusSipSigPortNum, sonusSipSigNumOfRetry=sonusSipSigNumOfRetry, sonusSipSignallingMIBNotificationsObjects=sonusSipSignallingMIBNotificationsObjects, sonusSipAclNextIndex=sonusSipAclNextIndex, sonusSipSigTimerT2=sonusSipSigTimerT2, sonusSipSigInviteRetry=sonusSipSigInviteRetry, sonusSipSigPortStatNumTxPdus=sonusSipSigPortStatNumTxPdus, sonusSipSigPortIpAddress=sonusSipSigPortIpAddress, sonusSipRemoteAppSvrIndex=sonusSipRemoteAppSvrIndex, sonusSipSigTimerSessionKeepalive=sonusSipSigTimerSessionKeepalive, sonusSipSigPortStatCallRate=sonusSipSigPortStatCallRate, sonusSipSigPortStatNumTermCalls=sonusSipSigPortStatNumTermCalls, sonusSipSigPortStatusNum=sonusSipSigPortStatusNum, sonusSipSigPortStatPortNum=sonusSipSigPortStatPortNum, sonusSipSigPortInterface=sonusSipSigPortInterface, sonusSipSigPortStatusTable=sonusSipSigPortStatusTable, sonusSipSignallingMIBNotificationsPrefix=sonusSipSignallingMIBNotificationsPrefix, sonusSipSigPortMode=sonusSipSigPortMode, sonusSipSigPortTable=sonusSipSigPortTable, sonusSipSigPortStatIpAddress=sonusSipSigPortStatIpAddress, sonusSipSignallingMIBObjects=sonusSipSignallingMIBObjects, sonusSipSigPortIndex=sonusSipSigPortIndex, sonusSipAclEntry=sonusSipAclEntry, sonusSipSigPortStatusIpAddress=sonusSipSigPortStatusIpAddress, sonusSipSigPortRole=sonusSipSigPortRole, sonusSipSigPortAclState=sonusSipSigPortAclState, sonusSipCallSigPortCloseNotification=sonusSipCallSigPortCloseNotification, sonusSipSigPortStatusInterface=sonusSipSigPortStatusInterface, sonusSipSigPortStatNumTxBytes=sonusSipSigPortStatNumTxBytes, sonusSipSigPortStatIndex=sonusSipSigPortStatIndex, sonusSipSignallingMIB=sonusSipSignallingMIB, sonusSipAcl=sonusSipAcl, sonusSipSigPortStatCountReset=sonusSipSigPortStatCountReset, sonusSipAclTable=sonusSipAclTable)