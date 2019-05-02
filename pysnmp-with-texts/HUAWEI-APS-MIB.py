#
# PySNMP MIB module HUAWEI-APS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-APS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:42:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, ModuleIdentity, Integer32, ObjectIdentity, Counter64, IpAddress, Bits, NotificationType, iso, Counter32, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Integer32", "ObjectIdentity", "Counter64", "IpAddress", "Bits", "NotificationType", "iso", "Counter32", "TimeTicks", "Gauge32")
RowStatus, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TruthValue", "TextualConvention")
hwApsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161))
if mibBuilder.loadTexts: hwApsMIB.setLastUpdated('200712071432Z')
if mibBuilder.loadTexts: hwApsMIB.setOrganization('Huawei Technologies co.,Ltd.')
if mibBuilder.loadTexts: hwApsMIB.setContactInfo('VRP Team Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.huawei.com Zip:100085 ')
if mibBuilder.loadTexts: hwApsMIB.setDescription('The HUAWEI-APS-MIB contains objects to Manage configuration and Monitor running state for Class Based APS feature.')
hwApsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1))
hwApsProtectionTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1, 1), )
if mibBuilder.loadTexts: hwApsProtectionTable.setStatus('current')
if mibBuilder.loadTexts: hwApsProtectionTable.setDescription('APS protection configuration.')
hwApsProtectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1, 1, 1), ).setIndexNames((0, "HUAWEI-APS-MIB", "hwApsIfIndex"))
if mibBuilder.loadTexts: hwApsProtectionEntry.setStatus('current')
if mibBuilder.loadTexts: hwApsProtectionEntry.setDescription('APS protection configuration entry.')
hwApsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwApsIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwApsIfIndex.setDescription("The table's index that is a STM-1 or CSTM-1 interface.")
hwApsProtectionGroupNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwApsProtectionGroupNum.setStatus('current')
if mibBuilder.loadTexts: hwApsProtectionGroupNum.setDescription("The table's index that is APS protection group number from 1 to 8.")
hwApsIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("work", 1), ("protection", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwApsIfType.setStatus('current')
if mibBuilder.loadTexts: hwApsIfType.setDescription('The interface type .')
hwApsRestoreWaitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 12))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwApsRestoreWaitTime.setStatus('current')
if mibBuilder.loadTexts: hwApsRestoreWaitTime.setDescription('The latency time of restoration.')
hwApsProtectSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("lock", 1), ("force", 2), ("manual", 3), ("auto", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwApsProtectSwitch.setStatus('current')
if mibBuilder.loadTexts: hwApsProtectSwitch.setDescription('The switch of APS protection.')
hwApsWorkingIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwApsWorkingIfType.setStatus('current')
if mibBuilder.loadTexts: hwApsWorkingIfType.setDescription('State of the interface.')
hwApsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwApsRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwApsRowStatus.setDescription('Current operation status of the row.')
hwApsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 2))
hwApsProtectSwitchOver = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 2, 1)).setObjects(("HUAWEI-APS-MIB", "hwApsProtectionGroupNum"), ("HUAWEI-APS-MIB", "hwApsIfType"), ("HUAWEI-APS-MIB", "hwApsWorkingIfType"))
if mibBuilder.loadTexts: hwApsProtectSwitchOver.setStatus('current')
if mibBuilder.loadTexts: hwApsProtectSwitchOver.setDescription('APS protection switch successful.')
hwApsProtectSwitchBackOver = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 2, 2)).setObjects(("HUAWEI-APS-MIB", "hwApsProtectionGroupNum"), ("HUAWEI-APS-MIB", "hwApsIfType"), ("HUAWEI-APS-MIB", "hwApsWorkingIfType"))
if mibBuilder.loadTexts: hwApsProtectSwitchBackOver.setStatus('current')
if mibBuilder.loadTexts: hwApsProtectSwitchBackOver.setDescription('APS protection restore successful.')
hwApsProtectModeFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 2, 3)).setObjects(("HUAWEI-APS-MIB", "hwApsProtectionGroupNum"), ("HUAWEI-APS-MIB", "hwApsIfType"), ("HUAWEI-APS-MIB", "hwApsWorkingIfType"))
if mibBuilder.loadTexts: hwApsProtectModeFail.setStatus('current')
if mibBuilder.loadTexts: hwApsProtectModeFail.setDescription("The type of APS proctection doesn't match.")
hwApsProtectChnlFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 2, 4)).setObjects(("HUAWEI-APS-MIB", "hwApsProtectionGroupNum"), ("HUAWEI-APS-MIB", "hwApsIfType"), ("HUAWEI-APS-MIB", "hwApsWorkingIfType"))
if mibBuilder.loadTexts: hwApsProtectChnlFail.setStatus('current')
if mibBuilder.loadTexts: hwApsProtectChnlFail.setDescription("The tunnle of APS proctection doesn't match.")
hwApsProtectInvldK1K2Fail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 2, 5)).setObjects(("HUAWEI-APS-MIB", "hwApsProtectionGroupNum"), ("HUAWEI-APS-MIB", "hwApsIfType"), ("HUAWEI-APS-MIB", "hwApsWorkingIfType"))
if mibBuilder.loadTexts: hwApsProtectInvldK1K2Fail.setStatus('current')
if mibBuilder.loadTexts: hwApsProtectInvldK1K2Fail.setDescription('The number K byte is unusable. ')
hwApsProtectRemoteFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 2, 6)).setObjects(("HUAWEI-APS-MIB", "hwApsProtectionGroupNum"), ("HUAWEI-APS-MIB", "hwApsIfType"), ("HUAWEI-APS-MIB", "hwApsWorkingIfType"))
if mibBuilder.loadTexts: hwApsProtectRemoteFail.setStatus('current')
if mibBuilder.loadTexts: hwApsProtectRemoteFail.setDescription('The remote is inspected failure.')
hwApsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 3))
hwApsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 3, 1))
hwApsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 3, 1, 1)).setObjects(("HUAWEI-APS-MIB", "hwApsProtectionGroup"), ("HUAWEI-APS-MIB", "hwApsNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwApsCompliance = hwApsCompliance.setStatus('current')
if mibBuilder.loadTexts: hwApsCompliance.setDescription('The compliance statement for entities that implement extend APS on a router.')
hwApsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 3, 2))
hwApsProtectionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 3, 2, 1)).setObjects(("HUAWEI-APS-MIB", "hwApsProtectionGroupNum"), ("HUAWEI-APS-MIB", "hwApsIfType"), ("HUAWEI-APS-MIB", "hwApsRestoreWaitTime"), ("HUAWEI-APS-MIB", "hwApsProtectSwitch"), ("HUAWEI-APS-MIB", "hwApsWorkingIfType"), ("HUAWEI-APS-MIB", "hwApsRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwApsProtectionGroup = hwApsProtectionGroup.setStatus('current')
if mibBuilder.loadTexts: hwApsProtectionGroup.setDescription('This is a optional group of information.')
hwApsNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 3, 2, 2)).setObjects(("HUAWEI-APS-MIB", "hwApsProtectSwitchOver"), ("HUAWEI-APS-MIB", "hwApsProtectSwitchBackOver"), ("HUAWEI-APS-MIB", "hwApsProtectModeFail"), ("HUAWEI-APS-MIB", "hwApsProtectChnlFail"), ("HUAWEI-APS-MIB", "hwApsProtectInvldK1K2Fail"), ("HUAWEI-APS-MIB", "hwApsProtectRemoteFail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwApsNotificationsGroup = hwApsNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: hwApsNotificationsGroup.setDescription('This is a optional group of information.')
mibBuilder.exportSymbols("HUAWEI-APS-MIB", hwApsProtectSwitchOver=hwApsProtectSwitchOver, PYSNMP_MODULE_ID=hwApsMIB, hwApsGroups=hwApsGroups, hwApsProtectionTable=hwApsProtectionTable, hwApsCompliance=hwApsCompliance, hwApsNotificationsGroup=hwApsNotificationsGroup, hwApsWorkingIfType=hwApsWorkingIfType, hwApsProtectModeFail=hwApsProtectModeFail, hwApsRestoreWaitTime=hwApsRestoreWaitTime, hwApsProtectSwitch=hwApsProtectSwitch, hwApsProtectionGroupNum=hwApsProtectionGroupNum, hwApsCompliances=hwApsCompliances, hwApsMIB=hwApsMIB, hwApsProtectSwitchBackOver=hwApsProtectSwitchBackOver, hwApsProtectionGroup=hwApsProtectionGroup, hwApsProtectionEntry=hwApsProtectionEntry, hwApsProtectRemoteFail=hwApsProtectRemoteFail, hwApsObjects=hwApsObjects, hwApsRowStatus=hwApsRowStatus, hwApsIfIndex=hwApsIfIndex, hwApsProtectChnlFail=hwApsProtectChnlFail, hwApsConformance=hwApsConformance, hwApsIfType=hwApsIfType, hwApsProtectInvldK1K2Fail=hwApsProtectInvldK1K2Fail, hwApsNotifications=hwApsNotifications)