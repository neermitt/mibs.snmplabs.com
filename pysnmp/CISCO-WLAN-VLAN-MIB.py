#
# PySNMP MIB module CISCO-WLAN-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WLAN-VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:43:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
CDot11IfMicAlgorithm, CDot11IfWepKeyPermuteAlgorithm, WepKeyType128 = mibBuilder.importSymbols("CISCO-DOT11-IF-MIB", "CDot11IfMicAlgorithm", "CDot11IfWepKeyPermuteAlgorithm", "WepKeyType128")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, ModuleIdentity, TimeTicks, Integer32, Counter32, IpAddress, iso, Counter64, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "ModuleIdentity", "TimeTicks", "Integer32", "Counter32", "IpAddress", "iso", "Counter64", "ObjectIdentity", "MibIdentifier")
DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
ciscoWlanVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 268))
ciscoWlanVlanMIB.setRevisions(('2002-06-12 00:00', '2002-04-04 00:00', '2002-03-07 00:00',))
if mibBuilder.loadTexts: ciscoWlanVlanMIB.setLastUpdated('200206120000Z')
if mibBuilder.loadTexts: ciscoWlanVlanMIB.setOrganization('Cisco System Inc.')
ciscoWlanVlanMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 268, 1))
cwvlRoamDomainConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 1))
cwvlDot11VlanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2))
class CwvlVlanIdOrZero(TextualConvention, Unsigned32):
    reference = 'RFC 2674, Bridge MIB Extensions, August 1999.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4095)

cwvlWlanDot1qEncapEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwvlWlanDot1qEncapEnabled.setStatus('current')
cwvlBridgingNativeVlanId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 1, 2), CwvlVlanIdOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwvlBridgingNativeVlanId.setStatus('current')
cwvlVoIPVlanEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 1, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwvlVoIPVlanEnabled.setStatus('current')
cwvlVoIPVlanId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 1, 4), CwvlVlanIdOrZero().clone(4095)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwvlVoIPVlanId.setStatus('current')
cwvlPublicVlanId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 1, 5), CwvlVlanIdOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwvlPublicVlanId.setStatus('current')
cwvlWlanVlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1), )
if mibBuilder.loadTexts: cwvlWlanVlanTable.setStatus('current')
cwvlWlanVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-WLAN-VLAN-MIB", "cwvlWlanVlanId"))
if mibBuilder.loadTexts: cwvlWlanVlanEntry.setStatus('current')
cwvlWlanVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 1), CwvlVlanIdOrZero())
if mibBuilder.loadTexts: cwvlWlanVlanId.setStatus('current')
cwvlWlanEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwvlWlanEnabled.setStatus('current')
cwvlWlanNUcastKeyRotateInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000000))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwvlWlanNUcastKeyRotateInterval.setStatus('current')
cwvlWlanEncryptionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("wep", 2), ("aes", 3))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwvlWlanEncryptionMode.setStatus('current')
cwvlWlanEncryptionMandatory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 5), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwvlWlanEncryptionMandatory.setStatus('current')
cwvlWlanMicAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 6), CDot11IfMicAlgorithm().clone('micNone')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwvlWlanMicAlgorithm.setStatus('current')
cwvlWlanWepKeyPermuteAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 7), CDot11IfWepKeyPermuteAlgorithm().clone('wepPermuteNone')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwvlWlanWepKeyPermuteAlgorithm.setStatus('current')
cwvlWlanWepKeyHashing = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwvlWlanWepKeyHashing.setStatus('current')
cwvlWlanEncryptionAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standard", 1), ("cisco", 2))).clone('cisco')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwvlWlanEncryptionAlgorithm.setStatus('current')
cwvlWlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwvlWlanRowStatus.setStatus('current')
cwvlWlanNUcastKeyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 2), )
if mibBuilder.loadTexts: cwvlWlanNUcastKeyTable.setStatus('current')
cwvlWlanNUcastKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-WLAN-VLAN-MIB", "cwvlWlanVlanId"), (0, "CISCO-WLAN-VLAN-MIB", "cwvlWlanNUcastKeyIndex"))
if mibBuilder.loadTexts: cwvlWlanNUcastKeyEntry.setStatus('current')
cwvlWlanNUcastKeyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: cwvlWlanNUcastKeyIndex.setStatus('current')
cwvlWlanNUcastKeyLen = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 13))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwvlWlanNUcastKeyLen.setStatus('current')
cwvlWlanNUcastKeyValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 2, 1, 3), WepKeyType128()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwvlWlanNUcastKeyValue.setStatus('current')
cwvlWlanWepChangeNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwvlWlanWepChangeNotifEnabled.setStatus('current')
ciscoWlanVlanMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 268, 0))
ciscoWlanVlanWepChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 268, 0, 1)).setObjects(("CISCO-WLAN-VLAN-MIB", "cwvlWlanNUcastKeyValue"))
if mibBuilder.loadTexts: ciscoWlanVlanWepChangeNotif.setStatus('current')
ciscoWlanVlanMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 268, 2))
ciscoWlanVlanMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 268, 2, 1))
ciscoWlanVlanMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 268, 2, 2))
ciscoWlanVlanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 268, 2, 1, 1)).setObjects(("CISCO-WLAN-VLAN-MIB", "ciscoWlanRoamDomainGroup"), ("CISCO-WLAN-VLAN-MIB", "ciscoWlanVlanNotificationGroup"), ("CISCO-WLAN-VLAN-MIB", "ciscoWlanDot11VlanConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWlanVlanMIBCompliance = ciscoWlanVlanMIBCompliance.setStatus('current')
ciscoWlanRoamDomainGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 268, 2, 2, 1)).setObjects(("CISCO-WLAN-VLAN-MIB", "cwvlWlanDot1qEncapEnabled"), ("CISCO-WLAN-VLAN-MIB", "cwvlBridgingNativeVlanId"), ("CISCO-WLAN-VLAN-MIB", "cwvlVoIPVlanEnabled"), ("CISCO-WLAN-VLAN-MIB", "cwvlVoIPVlanId"), ("CISCO-WLAN-VLAN-MIB", "cwvlPublicVlanId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWlanRoamDomainGroup = ciscoWlanRoamDomainGroup.setStatus('current')
ciscoWlanDot11VlanConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 268, 2, 2, 2)).setObjects(("CISCO-WLAN-VLAN-MIB", "cwvlWlanEnabled"), ("CISCO-WLAN-VLAN-MIB", "cwvlWlanNUcastKeyRotateInterval"), ("CISCO-WLAN-VLAN-MIB", "cwvlWlanEncryptionMode"), ("CISCO-WLAN-VLAN-MIB", "cwvlWlanEncryptionMandatory"), ("CISCO-WLAN-VLAN-MIB", "cwvlWlanMicAlgorithm"), ("CISCO-WLAN-VLAN-MIB", "cwvlWlanWepKeyPermuteAlgorithm"), ("CISCO-WLAN-VLAN-MIB", "cwvlWlanWepKeyHashing"), ("CISCO-WLAN-VLAN-MIB", "cwvlWlanEncryptionAlgorithm"), ("CISCO-WLAN-VLAN-MIB", "cwvlWlanRowStatus"), ("CISCO-WLAN-VLAN-MIB", "cwvlWlanNUcastKeyLen"), ("CISCO-WLAN-VLAN-MIB", "cwvlWlanNUcastKeyValue"), ("CISCO-WLAN-VLAN-MIB", "cwvlWlanWepChangeNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWlanDot11VlanConfigGroup = ciscoWlanDot11VlanConfigGroup.setStatus('current')
ciscoWlanVlanNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 268, 2, 2, 3)).setObjects(("CISCO-WLAN-VLAN-MIB", "ciscoWlanVlanWepChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWlanVlanNotificationGroup = ciscoWlanVlanNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WLAN-VLAN-MIB", ciscoWlanVlanNotificationGroup=ciscoWlanVlanNotificationGroup, cwvlWlanNUcastKeyTable=cwvlWlanNUcastKeyTable, cwvlWlanVlanTable=cwvlWlanVlanTable, cwvlWlanEncryptionMandatory=cwvlWlanEncryptionMandatory, cwvlWlanEncryptionAlgorithm=cwvlWlanEncryptionAlgorithm, cwvlWlanNUcastKeyIndex=cwvlWlanNUcastKeyIndex, cwvlVoIPVlanId=cwvlVoIPVlanId, cwvlWlanEncryptionMode=cwvlWlanEncryptionMode, cwvlWlanNUcastKeyLen=cwvlWlanNUcastKeyLen, ciscoWlanVlanMIBCompliance=ciscoWlanVlanMIBCompliance, cwvlVoIPVlanEnabled=cwvlVoIPVlanEnabled, CwvlVlanIdOrZero=CwvlVlanIdOrZero, cwvlPublicVlanId=cwvlPublicVlanId, cwvlWlanEnabled=cwvlWlanEnabled, ciscoWlanVlanMIBNotifications=ciscoWlanVlanMIBNotifications, ciscoWlanVlanMIBGroups=ciscoWlanVlanMIBGroups, cwvlWlanNUcastKeyRotateInterval=cwvlWlanNUcastKeyRotateInterval, cwvlWlanWepChangeNotifEnabled=cwvlWlanWepChangeNotifEnabled, ciscoWlanVlanMIBObjects=ciscoWlanVlanMIBObjects, ciscoWlanVlanWepChangeNotif=ciscoWlanVlanWepChangeNotif, ciscoWlanRoamDomainGroup=ciscoWlanRoamDomainGroup, cwvlRoamDomainConfig=cwvlRoamDomainConfig, ciscoWlanVlanMIBCompliances=ciscoWlanVlanMIBCompliances, cwvlWlanWepKeyHashing=cwvlWlanWepKeyHashing, ciscoWlanVlanMIBConformance=ciscoWlanVlanMIBConformance, cwvlWlanDot1qEncapEnabled=cwvlWlanDot1qEncapEnabled, PYSNMP_MODULE_ID=ciscoWlanVlanMIB, ciscoWlanDot11VlanConfigGroup=ciscoWlanDot11VlanConfigGroup, ciscoWlanVlanMIB=ciscoWlanVlanMIB, cwvlDot11VlanConfig=cwvlDot11VlanConfig, cwvlWlanVlanId=cwvlWlanVlanId, cwvlBridgingNativeVlanId=cwvlBridgingNativeVlanId, cwvlWlanVlanEntry=cwvlWlanVlanEntry, cwvlWlanWepKeyPermuteAlgorithm=cwvlWlanWepKeyPermuteAlgorithm, cwvlWlanNUcastKeyValue=cwvlWlanNUcastKeyValue, cwvlWlanNUcastKeyEntry=cwvlWlanNUcastKeyEntry, cwvlWlanMicAlgorithm=cwvlWlanMicAlgorithm, cwvlWlanRowStatus=cwvlWlanRowStatus)