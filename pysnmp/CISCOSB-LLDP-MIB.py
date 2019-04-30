#
# PySNMP MIB module CISCOSB-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-LLDP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:06:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
rndErrorDesc, rndErrorSeverity = mibBuilder.importSymbols("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc", "rndErrorSeverity")
rndNotifications, switch001 = mibBuilder.importSymbols("CISCOSB-MIB", "rndNotifications", "switch001")
Dscp, = mibBuilder.importSymbols("DIFFSERV-DSCP-TC", "Dscp")
AddressFamilyNumbers, = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
LldpXMedCapabilities, = mibBuilder.importSymbols("LLDP-EXT-MED-MIB", "LldpXMedCapabilities")
lldpRemLocalPortNum, lldpRemTimeMark, LldpManAddress, LldpPortList, LldpPortNumber, lldpRemIndex = mibBuilder.importSymbols("LLDP-MIB", "lldpRemLocalPortNum", "lldpRemTimeMark", "LldpManAddress", "LldpPortList", "LldpPortNumber", "lldpRemIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Counter64, Counter32, Bits, iso, TimeTicks, IpAddress, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Counter64", "Counter32", "Bits", "iso", "TimeTicks", "IpAddress", "Unsigned32", "MibIdentifier")
RowStatus, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TextualConvention")
rlLldp = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110))
rlLldp.setRevisions(('2005-06-20 00:00',))
if mibBuilder.loadTexts: rlLldp.setLastUpdated('200506200000Z')
if mibBuilder.loadTexts: rlLldp.setOrganization('Cisco Small Business')
rlLldpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1))
rlLldpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1))
rlLldpXMedConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2))
class PolicyNumber(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 32768)

class PolicyContainerAppType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 0), ("voice", 1), ("voiceSignaling", 2), ("guestVoice", 3), ("guestVoiceSignaling", 4), ("softPhoneVoice", 5), ("videoconferencing", 6), ("streamingVideo", 7), ("videoSignaling", 8))

class PolicyAppVoiceUpdateMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("manual", 0), ("auto", 1))

rlLldpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpEnabled.setStatus('current')
rlLldpClearRx = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 2), PortList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpClearRx.setStatus('current')
rlLldpDuMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("filtering", 1), ("flooding", 2))).clone('filtering')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpDuMode.setStatus('current')
rlLldpAutoAdvLocPortManAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 4), )
if mibBuilder.loadTexts: rlLldpAutoAdvLocPortManAddrTable.setStatus('current')
rlLldpAutoAdvLocPortManAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 4, 1), ).setIndexNames((0, "CISCOSB-LLDP-MIB", "rlLldpAutoAdvLocPortNum"))
if mibBuilder.loadTexts: rlLldpAutoAdvLocPortManAddrEntry.setStatus('current')
rlLldpAutoAdvLocPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 4, 1, 1), LldpPortNumber())
if mibBuilder.loadTexts: rlLldpAutoAdvLocPortNum.setStatus('current')
rlLldpAutoAdvManAddrOwnerIfId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 4, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpAutoAdvManAddrOwnerIfId.setStatus('current')
rlLldpAutoAdvManAddrNone = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 4, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpAutoAdvManAddrNone.setStatus('current')
rlLldpAutoAdvManAddrSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 4, 1, 4), AddressFamilyNumbers()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpAutoAdvManAddrSubtype.setStatus('current')
rlLldpAutoAdvManAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 4, 1, 5), LldpManAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpAutoAdvManAddr.setStatus('current')
rlLldpAutoAdvPortsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 4, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpAutoAdvPortsStatus.setStatus('current')
rlLldpXMedLocMediaPolicyContainerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1), )
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerTable.setStatus('current')
rlLldpXMedLocMediaPolicyContainerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1), ).setIndexNames((0, "CISCOSB-LLDP-MIB", "rlLldpXMedLocMediaPolicyContainerIndex"))
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerEntry.setStatus('current')
rlLldpXMedLocMediaPolicyContainerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1, 1), PolicyNumber())
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerIndex.setStatus('current')
rlLldpXMedLocMediaPolicyContainerAppType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1, 2), PolicyContainerAppType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerAppType.setStatus('current')
rlLldpXMedLocMediaPolicyContainerVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), ValueRangeConstraint(4095, 4095), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerVlanID.setStatus('current')
rlLldpXMedLocMediaPolicyContainerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerPriority.setStatus('current')
rlLldpXMedLocMediaPolicyContainerDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1, 5), Dscp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerDscp.setStatus('current')
rlLldpXMedLocMediaPolicyContainerUnknown = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerUnknown.setStatus('current')
rlLldpXMedLocMediaPolicyContainerTagged = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerTagged.setStatus('current')
rlLldpXMedLocMediaPolicyContainerPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1, 8), PortList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerPorts.setStatus('current')
rlLldpXMedLocMediaPolicyContainerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1, 9), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerRowStatus.setStatus('current')
rlLldpTLVsTxOverloadingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3), )
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingTable.setStatus('current')
rlLldpTLVsTxOverloadingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 1), ).setIndexNames((0, "CISCOSB-LLDP-MIB", "rlLldpTxOverloadingPortNum"), (0, "CISCOSB-LLDP-MIB", "rlLldpTxOverloadingIndex"))
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingEntry.setStatus('current')
rlLldpTxOverloadingPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 1, 1), LldpPortNumber())
if mibBuilder.loadTexts: rlLldpTxOverloadingPortNum.setStatus('current')
rlLldpTxOverloadingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: rlLldpTxOverloadingIndex.setStatus('current')
rlLldpTxOverloadingGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("mandatory", 1), ("optional", 2), ("medCap", 3), ("medLocation", 4), ("medNetPolicy", 5), ("medPoe", 6), ("medInventory", 7), ("xDot3", 8), ("xDot1", 9), ("dcbx", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpTxOverloadingGroupId.setStatus('current')
rlLldpTLVsTxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpTLVsTxSize.setStatus('current')
rlLldpTLVsTxGroupOverloading = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpTLVsTxGroupOverloading.setStatus('current')
rlLldpTLVsTxLeftSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpTLVsTxLeftSize.setStatus('current')
rlLldpTLVsTxOverloadingSizeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 4), )
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingSizeTable.setStatus('current')
rlLldpTLVsTxOverloadingSizeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 4, 1), ).setIndexNames((0, "CISCOSB-LLDP-MIB", "rlLldpTxOverloadingPortNum"))
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingSizeEntry.setStatus('current')
rlLldpTotalTLVsTxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpTotalTLVsTxSize.setStatus('current')
rlLldpTLVsTxOverloading = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 4, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpTLVsTxOverloading.setStatus('current')
rlLldpLeftTLVsTxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 4, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpLeftTLVsTxSize.setStatus('current')
rlLldpTLVsTxOverloadingPorts = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 5), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingPorts.setStatus('current')
rlLldpTLVsTxOverloadingStateEnterTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 209)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingStateEnterTrap.setStatus('current')
rlLldpTLVsTxOverloadingStateExitTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 210)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingStateExitTrap.setStatus('current')
rlLldpXMedNetPolVoiceUpdateMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 7), PolicyAppVoiceUpdateMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpXMedNetPolVoiceUpdateMode.setStatus('current')
rlLldpRemTtlTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 8), )
if mibBuilder.loadTexts: rlLldpRemTtlTable.setStatus('current')
rlLldpRemTtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 8, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"))
if mibBuilder.loadTexts: rlLldpRemTtlEntry.setStatus('current')
rlLldpRemTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 8, 1, 1), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpRemTtl.setStatus('current')
rlLldpChassisIdSubtype = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 7))).clone(namedValues=NamedValues(("macAddress", 4), ("local", 7))).clone('macAddress')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpChassisIdSubtype.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-LLDP-MIB", rlLldpEnabled=rlLldpEnabled, rlLldpAutoAdvManAddrSubtype=rlLldpAutoAdvManAddrSubtype, rlLldpClearRx=rlLldpClearRx, rlLldpAutoAdvLocPortManAddrTable=rlLldpAutoAdvLocPortManAddrTable, rlLldpAutoAdvLocPortManAddrEntry=rlLldpAutoAdvLocPortManAddrEntry, rlLldpTLVsTxGroupOverloading=rlLldpTLVsTxGroupOverloading, rlLldpTxOverloadingGroupId=rlLldpTxOverloadingGroupId, rlLldpTLVsTxSize=rlLldpTLVsTxSize, rlLldpTLVsTxLeftSize=rlLldpTLVsTxLeftSize, rlLldpXMedLocMediaPolicyContainerEntry=rlLldpXMedLocMediaPolicyContainerEntry, rlLldpXMedConfig=rlLldpXMedConfig, rlLldpXMedLocMediaPolicyContainerPorts=rlLldpXMedLocMediaPolicyContainerPorts, rlLldpXMedLocMediaPolicyContainerUnknown=rlLldpXMedLocMediaPolicyContainerUnknown, rlLldpTotalTLVsTxSize=rlLldpTotalTLVsTxSize, rlLldpTLVsTxOverloadingStateEnterTrap=rlLldpTLVsTxOverloadingStateEnterTrap, rlLldpAutoAdvManAddrOwnerIfId=rlLldpAutoAdvManAddrOwnerIfId, rlLldpAutoAdvLocPortNum=rlLldpAutoAdvLocPortNum, rlLldpAutoAdvManAddrNone=rlLldpAutoAdvManAddrNone, rlLldpChassisIdSubtype=rlLldpChassisIdSubtype, PolicyNumber=PolicyNumber, rlLldpXMedLocMediaPolicyContainerRowStatus=rlLldpXMedLocMediaPolicyContainerRowStatus, rlLldpXMedLocMediaPolicyContainerDscp=rlLldpXMedLocMediaPolicyContainerDscp, rlLldpTLVsTxOverloadingTable=rlLldpTLVsTxOverloadingTable, rlLldpAutoAdvPortsStatus=rlLldpAutoAdvPortsStatus, rlLldpAutoAdvManAddr=rlLldpAutoAdvManAddr, rlLldpTLVsTxOverloadingSizeTable=rlLldpTLVsTxOverloadingSizeTable, rlLldpXMedLocMediaPolicyContainerIndex=rlLldpXMedLocMediaPolicyContainerIndex, PolicyContainerAppType=PolicyContainerAppType, PYSNMP_MODULE_ID=rlLldp, rlLldpXMedLocMediaPolicyContainerAppType=rlLldpXMedLocMediaPolicyContainerAppType, rlLldpConfig=rlLldpConfig, rlLldp=rlLldp, rlLldpDuMode=rlLldpDuMode, rlLldpXMedLocMediaPolicyContainerTagged=rlLldpXMedLocMediaPolicyContainerTagged, rlLldpTLVsTxOverloadingSizeEntry=rlLldpTLVsTxOverloadingSizeEntry, rlLldpTLVsTxOverloadingPorts=rlLldpTLVsTxOverloadingPorts, rlLldpTLVsTxOverloadingEntry=rlLldpTLVsTxOverloadingEntry, rlLldpRemTtl=rlLldpRemTtl, rlLldpTLVsTxOverloading=rlLldpTLVsTxOverloading, rlLldpLeftTLVsTxSize=rlLldpLeftTLVsTxSize, rlLldpXMedLocMediaPolicyContainerPriority=rlLldpXMedLocMediaPolicyContainerPriority, rlLldpTxOverloadingPortNum=rlLldpTxOverloadingPortNum, rlLldpXMedNetPolVoiceUpdateMode=rlLldpXMedNetPolVoiceUpdateMode, rlLldpObjects=rlLldpObjects, rlLldpTLVsTxOverloadingStateExitTrap=rlLldpTLVsTxOverloadingStateExitTrap, rlLldpTxOverloadingIndex=rlLldpTxOverloadingIndex, rlLldpRemTtlEntry=rlLldpRemTtlEntry, PolicyAppVoiceUpdateMode=PolicyAppVoiceUpdateMode, rlLldpRemTtlTable=rlLldpRemTtlTable, rlLldpXMedLocMediaPolicyContainerVlanID=rlLldpXMedLocMediaPolicyContainerVlanID, rlLldpXMedLocMediaPolicyContainerTable=rlLldpXMedLocMediaPolicyContainerTable)