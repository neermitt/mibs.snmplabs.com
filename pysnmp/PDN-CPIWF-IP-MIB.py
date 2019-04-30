#
# PySNMP MIB module PDN-CPIWF-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-CPIWF-IP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:29:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
pdnCpIwfEntry, pdnCpIwfIndex = mibBuilder.importSymbols("PDN-CP-IWF-MIB", "pdnCpIwfEntry", "pdnCpIwfIndex")
pdn_common, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-common")
SwitchState, = mibBuilder.importSymbols("PDN-TC", "SwitchState")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, IpAddress, Integer32, NotificationType, Unsigned32, Counter32, ObjectIdentity, MibIdentifier, ModuleIdentity, Gauge32, TimeTicks, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "Integer32", "NotificationType", "Unsigned32", "Counter32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Gauge32", "TimeTicks", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pdnCpIwfIpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53))
pdnCpIwfIpMIB.setRevisions(('2005-03-24 11:00', '2005-01-05 11:00', '2004-12-03 11:00', '2004-10-07 11:00', '2004-09-30 11:00', '2004-08-24 00:00',))
if mibBuilder.loadTexts: pdnCpIwfIpMIB.setLastUpdated('200412031100Z')
if mibBuilder.loadTexts: pdnCpIwfIpMIB.setOrganization('Paradyne Networks MIB Working Group Other information about group editing the MIB')
pdnCpIwfIpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 0))
pdnCpIwfIpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1))
pdnCpIwfIpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2))
pdnCpIwfIpConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1))
pdnCpIwfIpTestObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 2))
pdnCpIwfIpStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 3))
pdnCpIwfIpApplObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4))
class VoiceChannelType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("bearer", 1), ("signaling", 2))

pdnCpIwfIpTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 1), )
if mibBuilder.loadTexts: pdnCpIwfIpTable.setStatus('current')
pdnCpIwfIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 1, 1), )
pdnCpIwfEntry.registerAugmentions(("PDN-CPIWF-IP-MIB", "pdnCpIwfIpEntry"))
pdnCpIwfIpEntry.setIndexNames(*pdnCpIwfEntry.getIndexNames())
if mibBuilder.loadTexts: pdnCpIwfIpEntry.setStatus('current')
pdnCpIwfIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpAddress.setStatus('current')
pdnCpIwfIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpNetMask.setStatus('current')
pdnCpIwfIpDefGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpDefGateway.setStatus('current')
pdnCpIwfIpActiveSoftswitch = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2), ("none", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnCpIwfIpActiveSoftswitch.setStatus('current')
pdnCpIwfIpChanTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 2), )
if mibBuilder.loadTexts: pdnCpIwfIpChanTable.setStatus('current')
pdnCpIwfIpChanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 2, 1), ).setIndexNames((0, "PDN-CP-IWF-MIB", "pdnCpIwfIndex"), (0, "PDN-CPIWF-IP-MIB", "pdnCpIwfIpChanType"))
if mibBuilder.loadTexts: pdnCpIwfIpChanEntry.setStatus('current')
pdnCpIwfIpChanType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 2, 1, 1), VoiceChannelType())
if mibBuilder.loadTexts: pdnCpIwfIpChanType.setStatus('current')
pdnCpIwfIpChandot1dBasePort = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnCpIwfIpChandot1dBasePort.setStatus('current')
pdnCpIwfIpChanTosDSCP = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpChanTosDSCP.setStatus('current')
pdnCpIwfIpRtpTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 1), )
if mibBuilder.loadTexts: pdnCpIwfIpRtpTable.setStatus('current')
pdnCpIwfIpRtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 1, 1), )
pdnCpIwfEntry.registerAugmentions(("PDN-CPIWF-IP-MIB", "pdnCpIwfIpRtpEntry"))
pdnCpIwfIpRtpEntry.setIndexNames(*pdnCpIwfEntry.getIndexNames())
if mibBuilder.loadTexts: pdnCpIwfIpRtpEntry.setStatus('current')
pdnCpIwfIpRtpLocalPortBase = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpRtpLocalPortBase.setStatus('current')
pdnCpIwfIpMgcpTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2), )
if mibBuilder.loadTexts: pdnCpIwfIpMgcpTable.setStatus('current')
pdnCpIwfIpMgcpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1), )
pdnCpIwfEntry.registerAugmentions(("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpEntry"))
pdnCpIwfIpMgcpEntry.setIndexNames(*pdnCpIwfEntry.getIndexNames())
if mibBuilder.loadTexts: pdnCpIwfIpMgcpEntry.setStatus('current')
pdnCpIwfIpMgcpPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpPortNumber.setStatus('current')
pdnCpIwfIpMgcpPriAgentName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpPriAgentName.setStatus('current')
pdnCpIwfIpMgcpPriAgentIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpPriAgentIpAddr.setStatus('current')
pdnCpIwfIpMgcpPriAgentPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpPriAgentPortNum.setStatus('current')
pdnCpIwfIpMgcpPriAgentDNSIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpPriAgentDNSIpAddr.setStatus('current')
pdnCpIwfIpMgcpSecAgentName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpSecAgentName.setStatus('current')
pdnCpIwfIpMgcpSecAgentIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpSecAgentIpAddr.setStatus('current')
pdnCpIwfIpMgcpSecAgentPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpSecAgentPortNum.setStatus('current')
pdnCpIwfIpMgcpSecAgentDNSIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpSecAgentDNSIpAddr.setStatus('current')
pdnCpIwfIpMgcpRFC2833LoopSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 10), SwitchState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpRFC2833LoopSignal.setStatus('current')
pdnCpIwfIpMgcpIADomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpIADomainName.setStatus('current')
pdnCpIwfIpMgcpEndPtFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ipaddr", 1), ("bracketandipaddr", 2), ("domainname", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpEndPtFormat.setStatus('current')
pdnCpIwfIpMgcpRSIPKeepAlive = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpRSIPKeepAlive.setStatus('current')
pdnCpIwfIpActiveSoftSwitchChanged = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 0, 1))
if mibBuilder.loadTexts: pdnCpIwfIpActiveSoftSwitchChanged.setStatus('current')
pdnCpIwfIpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 1))
pdnCpIwfIpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 2))
pdnCpIwfIpNtfyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 3))
pdnCpIwfIpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 1, 1)).setObjects(("PDN-CPIWF-IP-MIB", "pdnCpIwfIpConfigGroup"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpApplConfigGroup"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpNtfyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnCpIwfIpMIBCompliance = pdnCpIwfIpMIBCompliance.setStatus('current')
pdnCpIwfIpConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 2, 1)).setObjects(("PDN-CPIWF-IP-MIB", "pdnCpIwfIpChandot1dBasePort"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpChanTosDSCP"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpAddress"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpNetMask"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpDefGateway"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpActiveSoftswitch"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnCpIwfIpConfigGroup = pdnCpIwfIpConfigGroup.setStatus('current')
pdnCpIwfIpApplConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 2, 2)).setObjects(("PDN-CPIWF-IP-MIB", "pdnCpIwfIpRtpLocalPortBase"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpPortNumber"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpPriAgentName"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpPriAgentIpAddr"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpPriAgentPortNum"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpPriAgentDNSIpAddr"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpSecAgentName"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpSecAgentIpAddr"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpSecAgentPortNum"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpSecAgentDNSIpAddr"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpRFC2833LoopSignal"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpIADomainName"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpEndPtFormat"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpRSIPKeepAlive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnCpIwfIpApplConfigGroup = pdnCpIwfIpApplConfigGroup.setStatus('current')
pdnCpIwfIpNtfyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 3, 1)).setObjects(("PDN-CPIWF-IP-MIB", "pdnCpIwfIpActiveSoftSwitchChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnCpIwfIpNtfyGroup = pdnCpIwfIpNtfyGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-CPIWF-IP-MIB", pdnCpIwfIpChanTosDSCP=pdnCpIwfIpChanTosDSCP, pdnCpIwfIpConfigGroup=pdnCpIwfIpConfigGroup, pdnCpIwfIpMgcpSecAgentName=pdnCpIwfIpMgcpSecAgentName, pdnCpIwfIpAddress=pdnCpIwfIpAddress, pdnCpIwfIpStatsObjects=pdnCpIwfIpStatsObjects, pdnCpIwfIpMIBObjects=pdnCpIwfIpMIBObjects, VoiceChannelType=VoiceChannelType, pdnCpIwfIpMgcpEntry=pdnCpIwfIpMgcpEntry, pdnCpIwfIpNotifications=pdnCpIwfIpNotifications, pdnCpIwfIpMgcpPriAgentIpAddr=pdnCpIwfIpMgcpPriAgentIpAddr, pdnCpIwfIpMgcpTable=pdnCpIwfIpMgcpTable, pdnCpIwfIpMgcpPortNumber=pdnCpIwfIpMgcpPortNumber, pdnCpIwfIpMgcpRSIPKeepAlive=pdnCpIwfIpMgcpRSIPKeepAlive, pdnCpIwfIpMIB=pdnCpIwfIpMIB, pdnCpIwfIpNetMask=pdnCpIwfIpNetMask, pdnCpIwfIpChanEntry=pdnCpIwfIpChanEntry, pdnCpIwfIpApplConfigGroup=pdnCpIwfIpApplConfigGroup, pdnCpIwfIpNtfyGroup=pdnCpIwfIpNtfyGroup, pdnCpIwfIpActiveSoftswitch=pdnCpIwfIpActiveSoftswitch, pdnCpIwfIpMgcpSecAgentIpAddr=pdnCpIwfIpMgcpSecAgentIpAddr, pdnCpIwfIpMgcpPriAgentName=pdnCpIwfIpMgcpPriAgentName, pdnCpIwfIpMgcpEndPtFormat=pdnCpIwfIpMgcpEndPtFormat, pdnCpIwfIpDefGateway=pdnCpIwfIpDefGateway, PYSNMP_MODULE_ID=pdnCpIwfIpMIB, pdnCpIwfIpRtpEntry=pdnCpIwfIpRtpEntry, pdnCpIwfIpApplObjects=pdnCpIwfIpApplObjects, pdnCpIwfIpChanTable=pdnCpIwfIpChanTable, pdnCpIwfIpMIBCompliances=pdnCpIwfIpMIBCompliances, pdnCpIwfIpMIBCompliance=pdnCpIwfIpMIBCompliance, pdnCpIwfIpMIBConformance=pdnCpIwfIpMIBConformance, pdnCpIwfIpRtpLocalPortBase=pdnCpIwfIpRtpLocalPortBase, pdnCpIwfIpMIBGroups=pdnCpIwfIpMIBGroups, pdnCpIwfIpConfigObjects=pdnCpIwfIpConfigObjects, pdnCpIwfIpTestObjects=pdnCpIwfIpTestObjects, pdnCpIwfIpChandot1dBasePort=pdnCpIwfIpChandot1dBasePort, pdnCpIwfIpMgcpSecAgentPortNum=pdnCpIwfIpMgcpSecAgentPortNum, pdnCpIwfIpActiveSoftSwitchChanged=pdnCpIwfIpActiveSoftSwitchChanged, pdnCpIwfIpTable=pdnCpIwfIpTable, pdnCpIwfIpEntry=pdnCpIwfIpEntry, pdnCpIwfIpRtpTable=pdnCpIwfIpRtpTable, pdnCpIwfIpChanType=pdnCpIwfIpChanType, pdnCpIwfIpMgcpRFC2833LoopSignal=pdnCpIwfIpMgcpRFC2833LoopSignal, pdnCpIwfIpMgcpSecAgentDNSIpAddr=pdnCpIwfIpMgcpSecAgentDNSIpAddr, pdnCpIwfIpMgcpIADomainName=pdnCpIwfIpMgcpIADomainName, pdnCpIwfIpMgcpPriAgentPortNum=pdnCpIwfIpMgcpPriAgentPortNum, pdnCpIwfIpNtfyGroups=pdnCpIwfIpNtfyGroups, pdnCpIwfIpMgcpPriAgentDNSIpAddr=pdnCpIwfIpMgcpPriAgentDNSIpAddr)