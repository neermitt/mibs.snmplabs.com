#
# PySNMP MIB module RTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:50:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, TimeTicks, iso, ObjectIdentity, Unsigned32, Bits, Counter32, IpAddress, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, NotificationType, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "iso", "ObjectIdentity", "Unsigned32", "Bits", "Counter32", "IpAddress", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "NotificationType", "Gauge32", "ModuleIdentity")
TDomain, TestAndIncr, TimeStamp, TAddress, TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TDomain", "TestAndIncr", "TimeStamp", "TAddress", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
Utf8String, = mibBuilder.importSymbols("SYSAPPL-MIB", "Utf8String")
rtpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 87))
rtpMIB.setRevisions(('2000-10-02 00:00',))
if mibBuilder.loadTexts: rtpMIB.setLastUpdated('200010020000Z')
if mibBuilder.loadTexts: rtpMIB.setOrganization('IETF AVT Working Group Email: rem-conf@es.net')
rtpMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 87, 1))
rtpConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 87, 2))
rtpSessionNewIndex = MibScalar((1, 3, 6, 1, 2, 1, 87, 1, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtpSessionNewIndex.setStatus('current')
rtpSessionInverseTable = MibTable((1, 3, 6, 1, 2, 1, 87, 1, 2), )
if mibBuilder.loadTexts: rtpSessionInverseTable.setStatus('current')
rtpSessionInverseEntry = MibTableRow((1, 3, 6, 1, 2, 1, 87, 1, 2, 1), ).setIndexNames((0, "RTP-MIB", "rtpSessionDomain"), (0, "RTP-MIB", "rtpSessionRemAddr"), (0, "RTP-MIB", "rtpSessionLocAddr"), (0, "RTP-MIB", "rtpSessionIndex"))
if mibBuilder.loadTexts: rtpSessionInverseEntry.setStatus('current')
rtpSessionInverseStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 2, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSessionInverseStartTime.setStatus('current')
rtpSessionTable = MibTable((1, 3, 6, 1, 2, 1, 87, 1, 3), )
if mibBuilder.loadTexts: rtpSessionTable.setStatus('current')
rtpSessionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 87, 1, 3, 1), ).setIndexNames((0, "RTP-MIB", "rtpSessionIndex"))
if mibBuilder.loadTexts: rtpSessionEntry.setStatus('current')
rtpSessionIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: rtpSessionIndex.setStatus('current')
rtpSessionDomain = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 2), TDomain()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rtpSessionDomain.setStatus('current')
rtpSessionRemAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 3), TAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rtpSessionRemAddr.setStatus('current')
rtpSessionLocAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 4), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSessionLocAddr.setStatus('current')
rtpSessionIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 5), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rtpSessionIfIndex.setStatus('current')
rtpSessionSenderJoins = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSessionSenderJoins.setStatus('current')
rtpSessionReceiverJoins = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSessionReceiverJoins.setStatus('current')
rtpSessionByes = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSessionByes.setStatus('current')
rtpSessionStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSessionStartTime.setStatus('current')
rtpSessionMonitor = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSessionMonitor.setStatus('current')
rtpSessionRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rtpSessionRowStatus.setStatus('current')
rtpSenderInverseTable = MibTable((1, 3, 6, 1, 2, 1, 87, 1, 4), )
if mibBuilder.loadTexts: rtpSenderInverseTable.setStatus('current')
rtpSenderInverseEntry = MibTableRow((1, 3, 6, 1, 2, 1, 87, 1, 4, 1), ).setIndexNames((0, "RTP-MIB", "rtpSessionDomain"), (0, "RTP-MIB", "rtpSenderAddr"), (0, "RTP-MIB", "rtpSessionIndex"), (0, "RTP-MIB", "rtpSenderSSRC"))
if mibBuilder.loadTexts: rtpSenderInverseEntry.setStatus('current')
rtpSenderInverseStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 4, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderInverseStartTime.setStatus('current')
rtpSenderTable = MibTable((1, 3, 6, 1, 2, 1, 87, 1, 5), )
if mibBuilder.loadTexts: rtpSenderTable.setStatus('current')
rtpSenderEntry = MibTableRow((1, 3, 6, 1, 2, 1, 87, 1, 5, 1), ).setIndexNames((0, "RTP-MIB", "rtpSessionIndex"), (0, "RTP-MIB", "rtpSenderSSRC"))
if mibBuilder.loadTexts: rtpSenderEntry.setStatus('current')
rtpSenderSSRC = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: rtpSenderSSRC.setStatus('current')
rtpSenderCNAME = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 2), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderCNAME.setStatus('current')
rtpSenderAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 3), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderAddr.setStatus('current')
rtpSenderPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderPackets.setStatus('current')
rtpSenderOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderOctets.setStatus('current')
rtpSenderTool = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 6), Utf8String().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderTool.setStatus('current')
rtpSenderSRs = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderSRs.setStatus('current')
rtpSenderSRTime = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderSRTime.setStatus('current')
rtpSenderPT = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderPT.setStatus('current')
rtpSenderStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderStartTime.setStatus('current')
rtpRcvrInverseTable = MibTable((1, 3, 6, 1, 2, 1, 87, 1, 6), )
if mibBuilder.loadTexts: rtpRcvrInverseTable.setStatus('current')
rtpRcvrInverseEntry = MibTableRow((1, 3, 6, 1, 2, 1, 87, 1, 6, 1), ).setIndexNames((0, "RTP-MIB", "rtpSessionDomain"), (0, "RTP-MIB", "rtpRcvrAddr"), (0, "RTP-MIB", "rtpSessionIndex"), (0, "RTP-MIB", "rtpRcvrSRCSSRC"), (0, "RTP-MIB", "rtpRcvrSSRC"))
if mibBuilder.loadTexts: rtpRcvrInverseEntry.setStatus('current')
rtpRcvrInverseStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 6, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrInverseStartTime.setStatus('current')
rtpRcvrTable = MibTable((1, 3, 6, 1, 2, 1, 87, 1, 7), )
if mibBuilder.loadTexts: rtpRcvrTable.setStatus('current')
rtpRcvrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 87, 1, 7, 1), ).setIndexNames((0, "RTP-MIB", "rtpSessionIndex"), (0, "RTP-MIB", "rtpRcvrSRCSSRC"), (0, "RTP-MIB", "rtpRcvrSSRC"))
if mibBuilder.loadTexts: rtpRcvrEntry.setStatus('current')
rtpRcvrSRCSSRC = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 1), Unsigned32())
if mibBuilder.loadTexts: rtpRcvrSRCSSRC.setStatus('current')
rtpRcvrSSRC = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 2), Unsigned32())
if mibBuilder.loadTexts: rtpRcvrSSRC.setStatus('current')
rtpRcvrCNAME = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 3), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrCNAME.setStatus('current')
rtpRcvrAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 4), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrAddr.setStatus('current')
rtpRcvrRTT = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrRTT.setStatus('current')
rtpRcvrLostPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrLostPackets.setStatus('current')
rtpRcvrJitter = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrJitter.setStatus('current')
rtpRcvrTool = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 8), Utf8String().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrTool.setStatus('current')
rtpRcvrRRs = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrRRs.setStatus('current')
rtpRcvrRRTime = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrRRTime.setStatus('current')
rtpRcvrPT = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrPT.setStatus('current')
rtpRcvrPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrPackets.setStatus('current')
rtpRcvrOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrOctets.setStatus('current')
rtpRcvrStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 14), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrStartTime.setStatus('current')
rtpGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 87, 2, 1))
rtpSystemGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 87, 2, 1, 1)).setObjects(("RTP-MIB", "rtpSessionDomain"), ("RTP-MIB", "rtpSessionRemAddr"), ("RTP-MIB", "rtpSessionIfIndex"), ("RTP-MIB", "rtpSessionSenderJoins"), ("RTP-MIB", "rtpSessionReceiverJoins"), ("RTP-MIB", "rtpSessionStartTime"), ("RTP-MIB", "rtpSessionByes"), ("RTP-MIB", "rtpSessionMonitor"), ("RTP-MIB", "rtpSenderCNAME"), ("RTP-MIB", "rtpSenderAddr"), ("RTP-MIB", "rtpSenderPackets"), ("RTP-MIB", "rtpSenderOctets"), ("RTP-MIB", "rtpSenderTool"), ("RTP-MIB", "rtpSenderSRs"), ("RTP-MIB", "rtpSenderSRTime"), ("RTP-MIB", "rtpSenderStartTime"), ("RTP-MIB", "rtpRcvrCNAME"), ("RTP-MIB", "rtpRcvrAddr"), ("RTP-MIB", "rtpRcvrLostPackets"), ("RTP-MIB", "rtpRcvrJitter"), ("RTP-MIB", "rtpRcvrTool"), ("RTP-MIB", "rtpRcvrRRs"), ("RTP-MIB", "rtpRcvrRRTime"), ("RTP-MIB", "rtpRcvrStartTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rtpSystemGroup = rtpSystemGroup.setStatus('current')
rtpHostGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 87, 2, 1, 2)).setObjects(("RTP-MIB", "rtpSessionLocAddr"), ("RTP-MIB", "rtpSenderPT"), ("RTP-MIB", "rtpRcvrPT"), ("RTP-MIB", "rtpRcvrRTT"), ("RTP-MIB", "rtpRcvrOctets"), ("RTP-MIB", "rtpRcvrPackets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rtpHostGroup = rtpHostGroup.setStatus('current')
rtpMonitorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 87, 2, 1, 3)).setObjects(("RTP-MIB", "rtpSessionNewIndex"), ("RTP-MIB", "rtpSessionRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rtpMonitorGroup = rtpMonitorGroup.setStatus('current')
rtpInverseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 87, 2, 1, 4)).setObjects(("RTP-MIB", "rtpSessionInverseStartTime"), ("RTP-MIB", "rtpSenderInverseStartTime"), ("RTP-MIB", "rtpRcvrInverseStartTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rtpInverseGroup = rtpInverseGroup.setStatus('current')
rtpCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 87, 2, 2))
rtpHostCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 87, 2, 2, 1)).setObjects(("RTP-MIB", "rtpSystemGroup"), ("RTP-MIB", "rtpHostGroup"), ("RTP-MIB", "rtpMonitorGroup"), ("RTP-MIB", "rtpInverseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rtpHostCompliance = rtpHostCompliance.setStatus('current')
rtpMonitorCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 87, 2, 2, 2)).setObjects(("RTP-MIB", "rtpSystemGroup"), ("RTP-MIB", "rtpMonitorGroup"), ("RTP-MIB", "rtpHostGroup"), ("RTP-MIB", "rtpInverseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rtpMonitorCompliance = rtpMonitorCompliance.setStatus('current')
mibBuilder.exportSymbols("RTP-MIB", rtpRcvrTable=rtpRcvrTable, rtpRcvrInverseTable=rtpRcvrInverseTable, rtpRcvrRTT=rtpRcvrRTT, rtpRcvrStartTime=rtpRcvrStartTime, rtpMIBObjects=rtpMIBObjects, rtpMonitorCompliance=rtpMonitorCompliance, rtpSessionEntry=rtpSessionEntry, rtpRcvrRRs=rtpRcvrRRs, rtpSenderInverseEntry=rtpSenderInverseEntry, rtpSenderEntry=rtpSenderEntry, rtpRcvrSSRC=rtpRcvrSSRC, rtpInverseGroup=rtpInverseGroup, rtpSenderInverseStartTime=rtpSenderInverseStartTime, rtpHostCompliance=rtpHostCompliance, rtpSenderPT=rtpSenderPT, rtpSessionDomain=rtpSessionDomain, rtpSenderSRTime=rtpSenderSRTime, rtpRcvrInverseEntry=rtpRcvrInverseEntry, rtpHostGroup=rtpHostGroup, rtpSessionLocAddr=rtpSessionLocAddr, rtpSessionStartTime=rtpSessionStartTime, rtpSenderPackets=rtpSenderPackets, rtpRcvrPackets=rtpRcvrPackets, rtpSenderInverseTable=rtpSenderInverseTable, rtpSessionInverseEntry=rtpSessionInverseEntry, rtpRcvrAddr=rtpRcvrAddr, rtpSenderSSRC=rtpSenderSSRC, rtpSessionIndex=rtpSessionIndex, rtpSessionRemAddr=rtpSessionRemAddr, rtpSessionSenderJoins=rtpSessionSenderJoins, rtpRcvrInverseStartTime=rtpRcvrInverseStartTime, rtpSessionByes=rtpSessionByes, rtpSenderSRs=rtpSenderSRs, rtpSenderOctets=rtpSenderOctets, rtpSessionInverseTable=rtpSessionInverseTable, rtpSenderStartTime=rtpSenderStartTime, rtpRcvrPT=rtpRcvrPT, rtpMIB=rtpMIB, rtpSenderTool=rtpSenderTool, rtpRcvrRRTime=rtpRcvrRRTime, rtpSessionRowStatus=rtpSessionRowStatus, rtpRcvrTool=rtpRcvrTool, rtpSessionTable=rtpSessionTable, rtpRcvrSRCSSRC=rtpRcvrSRCSSRC, rtpRcvrCNAME=rtpRcvrCNAME, rtpRcvrOctets=rtpRcvrOctets, rtpSessionReceiverJoins=rtpSessionReceiverJoins, rtpSystemGroup=rtpSystemGroup, PYSNMP_MODULE_ID=rtpMIB, rtpSenderCNAME=rtpSenderCNAME, rtpSenderTable=rtpSenderTable, rtpRcvrEntry=rtpRcvrEntry, rtpSessionNewIndex=rtpSessionNewIndex, rtpRcvrLostPackets=rtpRcvrLostPackets, rtpGroups=rtpGroups, rtpMonitorGroup=rtpMonitorGroup, rtpSessionMonitor=rtpSessionMonitor, rtpConformance=rtpConformance, rtpSessionInverseStartTime=rtpSessionInverseStartTime, rtpRcvrJitter=rtpRcvrJitter, rtpSenderAddr=rtpSenderAddr, rtpCompliances=rtpCompliances, rtpSessionIfIndex=rtpSessionIfIndex)