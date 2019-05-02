#
# PySNMP MIB module DLINK-MCB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-MCB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:49:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, Counter32, Bits, enterprises, Integer32, TimeTicks, NotificationType, Unsigned32, Gauge32, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "Counter32", "Bits", "enterprises", "Integer32", "TimeTicks", "NotificationType", "Unsigned32", "Gauge32", "IpAddress", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
company = MibIdentifier((1, 3, 6, 1, 4, 1, 171))
mcbMediaConverterFamily = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 41))
mcbMediaConverterChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 41, 1))
mcbSNMPMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 41, 1, 1))
mcbAdministrator = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 41, 1, 2))
mcbMCFrame = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 41, 1, 3))
mcbMCSlots = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 41, 1, 4))
mcbMCRedundantGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 41, 1, 5))
mcbSNMPTrapPowerFail = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbSNMPTrapPowerFail.setStatus('mandatory')
if mibBuilder.loadTexts: mcbSNMPTrapPowerFail.setDescription('Power Fail Trap')
mcbSNMPTrapFanFail = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbSNMPTrapFanFail.setStatus('mandatory')
if mibBuilder.loadTexts: mcbSNMPTrapFanFail.setDescription('Fan Fail Trap')
mcbSNMPTrapMCPlugin = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbSNMPTrapMCPlugin.setStatus('mandatory')
if mibBuilder.loadTexts: mcbSNMPTrapMCPlugin.setDescription('Media Converter Plugin Trap')
mcbSNMPTrapMCPullout = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbSNMPTrapMCPullout.setStatus('mandatory')
if mibBuilder.loadTexts: mcbSNMPTrapMCPullout.setDescription('Media Converter Pullout Trap')
mcbSNMPTrapMCLinkDown = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbSNMPTrapMCLinkDown.setStatus('mandatory')
if mibBuilder.loadTexts: mcbSNMPTrapMCLinkDown.setDescription('Media Converter Link Down Trap')
mcbSNMPTrapMCLinkUp = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbSNMPTrapMCLinkUp.setStatus('mandatory')
if mibBuilder.loadTexts: mcbSNMPTrapMCLinkUp.setDescription('Media Converter Link Up Trap')
mcbSNMPTrapMCLinkBroken = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbSNMPTrapMCLinkBroken.setStatus('mandatory')
if mibBuilder.loadTexts: mcbSNMPTrapMCLinkBroken.setDescription('Media Converter Link Broken Trap')
mcbSNMPTrapMCActiveSlotChange = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbSNMPTrapMCActiveSlotChange.setStatus('mandatory')
if mibBuilder.loadTexts: mcbSNMPTrapMCActiveSlotChange.setDescription('A active slot change Trap')
mcbSNMPTrapMCActiveSlotLose = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbSNMPTrapMCActiveSlotLose.setStatus('mandatory')
if mibBuilder.loadTexts: mcbSNMPTrapMCActiveSlotLose.setDescription('A active slot Lose Trap')
mcbAdministratorHardwareRev = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbAdministratorHardwareRev.setStatus('mandatory')
if mibBuilder.loadTexts: mcbAdministratorHardwareRev.setDescription('Hardware Revision')
mcbAdministratorSoftwareRev = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 2, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbAdministratorSoftwareRev.setStatus('mandatory')
if mibBuilder.loadTexts: mcbAdministratorSoftwareRev.setDescription('Software Revision')
mcbAdministratorBiosRev = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbAdministratorBiosRev.setStatus('mandatory')
if mibBuilder.loadTexts: mcbAdministratorBiosRev.setDescription('Bios Revision')
mcbAdministratorFactoryReset = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("action", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbAdministratorFactoryReset.setStatus('mandatory')
if mibBuilder.loadTexts: mcbAdministratorFactoryReset.setDescription('Administratoristrator Factory Reset The Whole Chassis')
mcbAdministratorFactoryResetCPU = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("action", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbAdministratorFactoryResetCPU.setStatus('mandatory')
if mibBuilder.loadTexts: mcbAdministratorFactoryResetCPU.setDescription('Administratoristrator Factory Reset Only CPU')
mcbAdministratorSoftwareReboot = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("action", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbAdministratorSoftwareReboot.setStatus('mandatory')
if mibBuilder.loadTexts: mcbAdministratorSoftwareReboot.setDescription('System Software Reboot')
mcbFramePowerOneOnStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbFramePowerOneOnStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mcbFramePowerOneOnStatus.setDescription('Main Power On Status')
mcbFramePowerTwoOnStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbFramePowerTwoOnStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mcbFramePowerTwoOnStatus.setDescription('Redundent Power On Status')
mcbFramePowerOneFailStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbFramePowerOneFailStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mcbFramePowerOneFailStatus.setDescription('Main Power Fail Status')
mcbFramePowerTwoFailStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbFramePowerTwoFailStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mcbFramePowerTwoFailStatus.setDescription('Redundent Power Fail Status')
mcbFrameFanOneFailStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbFrameFanOneFailStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mcbFrameFanOneFailStatus.setDescription('Main Fan Fail Status')
mcbFrameFanTwoFailStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbFrameFanTwoFailStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mcbFrameFanTwoFailStatus.setDescription('Redundent Fan Fail Status')
mcbMCSlotCount = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCSlotCount.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCSlotCount.setDescription('The Number Of Media Converters. ')
mcbMCSlotTable = MibTable((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2), )
if mibBuilder.loadTexts: mcbMCSlotTable.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCSlotTable.setDescription('Each Media Converter Device Relative Table')
mcbMCSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1), ).setIndexNames((0, "DLINK-MCB-MIB", "mcbMCSlotNo"))
if mibBuilder.loadTexts: mcbMCSlotEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCSlotEntry.setDescription('Each Media Converter Device Relative Entry')
mcbMCSlotNo = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCSlotNo.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCSlotNo.setDescription('Each Media Converter Device Relative Number On One Base')
mcbMCSlotExist = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("exist", 1), ("nonexist", 2), ("unsupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCSlotExist.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCSlotExist.setDescription('Each Device of Slot Is Exist Or Not')
mcbMCModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCModelName.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCModelName.setDescription('Each Media Converter Device Relative Model Name')
mcbMCMediaOneType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tp", 1), ("fiber", 2), ("unsupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCMediaOneType.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCMediaOneType.setDescription('Media Type Is TP Or Fiber')
mcbMCMediaTwoType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tp", 1), ("fiber", 2), ("unsupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCMediaTwoType.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCMediaTwoType.setDescription('Media Type Is TP Or Fiber')
mcbMCMediaOneLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("online", 1), ("offline", 2), ("unsupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCMediaOneLinkStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCMediaOneLinkStatus.setDescription('Media One Link Status')
mcbMCMediaTwoLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("online", 1), ("offline", 2), ("unsupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCMediaTwoLinkStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCMediaTwoLinkStatus.setDescription('Media Two Link Status')
mcbMCMediaOneDupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("half", 1), ("full", 2), ("unsupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCMediaOneDupStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCMediaOneDupStatus.setDescription('Media One Duplex Status')
mcbMCMediaTwoDupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("half", 1), ("full", 2), ("unsupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCMediaTwoDupStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCMediaTwoDupStatus.setDescription('Media Two Duplex Status')
mcbMCMediaOneSpeedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("speed10M", 1), ("speed100M", 2), ("speed1000M", 3), ("unsupported", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCMediaOneSpeedStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCMediaOneSpeedStatus.setDescription('Media One Speed Status')
mcbMCMediaTwoSpeedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("speed10M", 1), ("speed100M", 2), ("speed1000M", 3), ("unsupported", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCMediaTwoSpeedStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCMediaTwoSpeedStatus.setDescription('Media Two Speed Status')
mcbMCSlotName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbMCSlotName.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCSlotName.setDescription('Each Media Converter Chassis Slot Name')
mcbMCEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("unsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbMCEnable.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCEnable.setDescription('Enable or Disable the smart Media Converter')
mcbMCSetLLCF = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("unsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbMCSetLLCF.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCSetLLCF.setDescription('Enable or Disable the LLCF of the smart Media Converter')
mcbMCEnableMediaOne = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("unsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbMCEnableMediaOne.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCEnableMediaOne.setDescription('Enable the media one of the smart Media Converter')
mcbMCEnableMediaTwo = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("unsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbMCEnableMediaTwo.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCEnableMediaTwo.setDescription('Enable the media two of the smart Media Converter')
mcbMCSetMediaOneAutoNegotiate = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto-negotiate", 1), ("force", 2), ("unsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbMCSetMediaOneAutoNegotiate.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCSetMediaOneAutoNegotiate.setDescription('Set the Auto Negotiation mode or the Force mode of the media one of the smart Media Converter')
mcbMCSetMediaTwoAutoNegotiate = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto-negotiate", 1), ("force", 2), ("unsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbMCSetMediaTwoAutoNegotiate.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCSetMediaTwoAutoNegotiate.setDescription('Set the Auto Negotiation mode or the Force mode of the media two of the smart Media Converter')
mcbMCSetMediaOneSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("speed10M", 1), ("speed100M", 2), ("speed1000M", 3), ("unsupported", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbMCSetMediaOneSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCSetMediaOneSpeed.setDescription('Set the speed in Force mode of the media one of the smart Media Converter')
mcbMCSetMediaTwoSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("speed10M", 1), ("speed100M", 2), ("speed1000M", 3), ("unsupported", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbMCSetMediaTwoSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCSetMediaTwoSpeed.setDescription('Set the speed in Force mode of the media two of the smart Media Converter')
mcbMCSetMediaOneDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("half", 1), ("full", 2), ("unsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbMCSetMediaOneDuplex.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCSetMediaOneDuplex.setDescription('Set the duplex in Force mode of the media one of the smart Media Converter')
mcbMCSetMediaTwoDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("half", 1), ("full", 2), ("unsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbMCSetMediaTwoDuplex.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCSetMediaTwoDuplex.setDescription('Set the duplex in Force mode of the media two of the smart Media Converter')
mcbMCSetMediaOneFlowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("unsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbMCSetMediaOneFlowControl.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCSetMediaOneFlowControl.setDescription('Set the flow control in Force mode of the media one of the smart Media Converter')
mcbMCSetMediaTwoFlowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("unsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbMCSetMediaTwoFlowControl.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCSetMediaTwoFlowControl.setDescription('Set the flow control in Force mode of the media two of the smart Media Converter')
mcbMCSetMediaOneLLR = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("unsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbMCSetMediaOneLLR.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCSetMediaOneLLR.setDescription('Set the LLR of the media one of the smart Media Converter')
mcbMCSetMediaTwoLLR = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("unsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbMCSetMediaTwoLLR.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCSetMediaTwoLLR.setDescription('Set the LLR of the media two of the smart Media Converter')
mcbMCMediaOneBrokenStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unbroken", 1), ("broken", 2), ("unsupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCMediaOneBrokenStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCMediaOneBrokenStatus.setDescription('Media One Broken Status of the smart Media Converter')
mcbMCMediaTwoBrokenStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unbroken", 1), ("broken", 2), ("unsupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCMediaTwoBrokenStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCMediaTwoBrokenStatus.setDescription('Media Two Broken Status of the smart Media Converter')
mcbMCMediaOneTxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCMediaOneTxPacketCount.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCMediaOneTxPacketCount.setDescription('Media One transmitting packet count of the smart Media Converter')
mcbMCMediaOneRxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCMediaOneRxPacketCount.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCMediaOneRxPacketCount.setDescription('Media One receiving packet count of the smart Media Converter')
mcbMCMediaTwoTxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCMediaTwoTxPacketCount.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCMediaTwoTxPacketCount.setDescription('Media Two transmitting packet count of the smart Media Converter')
mcbMCMediaTwoRxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCMediaTwoRxPacketCount.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCMediaTwoRxPacketCount.setDescription('Media Two receiving packet count of the smart Media Converter')
mcbMCRedundantGroupCount = MibScalar((1, 3, 6, 1, 4, 1, 171, 41, 1, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCRedundantGroupCount.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCRedundantGroupCount.setDescription('The Number Of Redundant Groups. ')
mcbMCRedundantGroupTable = MibTable((1, 3, 6, 1, 4, 1, 171, 41, 1, 5, 2), )
if mibBuilder.loadTexts: mcbMCRedundantGroupTable.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCRedundantGroupTable.setDescription('Each Redundant Group Relative Table')
mcbMCRedundantGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 41, 1, 5, 2, 1), ).setIndexNames((0, "DLINK-MCB-MIB", "mcbMCRedundantGroupNo"))
if mibBuilder.loadTexts: mcbMCRedundantGroupEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCRedundantGroupEntry.setDescription('Each Redundant Group Relative Entry')
mcbMCRedundantGroupNo = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 5, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCRedundantGroupNo.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCRedundantGroupNo.setDescription('Each Redundant Group Relative Number On One Base')
mcbMCRedundantGroupPrimarySlot = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 5, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCRedundantGroupPrimarySlot.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCRedundantGroupPrimarySlot.setDescription('The primary slot member of the Redundant Group')
mcbMCRedundantGroupSecondarySlot = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 5, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCRedundantGroupSecondarySlot.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCRedundantGroupSecondarySlot.setDescription('The secondary slot member of the Redundant Group')
mcbMCRedundantGroupEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbMCRedundantGroupEnable.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCRedundantGroupEnable.setDescription('Enable or Disable the Redundant Group')
mcbMCRedundantGroupActiveSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 5, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcbMCRedundantGroupActiveSlot.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCRedundantGroupActiveSlot.setDescription('The active link slot member of the Redundant Group')
mcbMCRedundantGroupRestart = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 41, 1, 5, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("action", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcbMCRedundantGroupRestart.setStatus('mandatory')
if mibBuilder.loadTexts: mcbMCRedundantGroupRestart.setDescription('Restart the Redundant Group')
mcbPowerOneFail = NotificationType((1, 3, 6, 1, 4, 1, 171, 41, 1) + (0,1))
if mibBuilder.loadTexts: mcbPowerOneFail.setDescription("A PowerFail trap signifies that the sending protocol entity recognizes a failure in one of the communication links represented in the agent's configuration")
mcbFanOneFail = NotificationType((1, 3, 6, 1, 4, 1, 171, 41, 1) + (0,2))
if mibBuilder.loadTexts: mcbFanOneFail.setDescription("A FanFail trap signifies that the sending protocol entity recognizes a failure in one of the communication links represented in the agent's configuration")
mcbPowerTwoFail = NotificationType((1, 3, 6, 1, 4, 1, 171, 41, 1) + (0,3))
if mibBuilder.loadTexts: mcbPowerTwoFail.setDescription("A PowerFail trap signifies that the sending protocol entity recognizes a failure in one of the communication links represented in the agent's configuration")
mcbFanTwoFail = NotificationType((1, 3, 6, 1, 4, 1, 171, 41, 1) + (0,4))
if mibBuilder.loadTexts: mcbFanTwoFail.setDescription("A FanFail trap signifies that the sending protocol entity recognizes a failure in one of the communication links represented in the agent's configuration")
mcbMediaConverterPlugin = NotificationType((1, 3, 6, 1, 4, 1, 171, 41, 1) + (0,5)).setObjects(("DLINK-MCB-MIB", "mcbMCSlotNo"))
if mibBuilder.loadTexts: mcbMediaConverterPlugin.setDescription('A Media Converter Plugin trap signifies that the sending protocol entity checks if the model is pluged in the slot')
mcbMediaConverterPullout = NotificationType((1, 3, 6, 1, 4, 1, 171, 41, 1) + (0,6)).setObjects(("DLINK-MCB-MIB", "mcbMCSlotNo"))
if mibBuilder.loadTexts: mcbMediaConverterPullout.setDescription('A Media Converter Pullout trap signifies that the sending protocol entity checks if the model is pull out from the slot')
mcbMCMediaOneLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 171, 41, 1) + (0,7)).setObjects(("DLINK-MCB-MIB", "mcbMCSlotNo"))
if mibBuilder.loadTexts: mcbMCMediaOneLinkDown.setDescription('A Media Converter Media One Link Down trap signifies that the sending protocol entity checks if the media one of the specified media converter in the slot links down')
mcbMCMediaTwoLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 171, 41, 1) + (0,8)).setObjects(("DLINK-MCB-MIB", "mcbMCSlotNo"))
if mibBuilder.loadTexts: mcbMCMediaTwoLinkDown.setDescription('A Media Converter Media Two Link Down trap signifies that the sending protocol entity checks if the media two of the specified media converter in the slot links down')
mcbMCMediaOneLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 171, 41, 1) + (0,9)).setObjects(("DLINK-MCB-MIB", "mcbMCSlotNo"))
if mibBuilder.loadTexts: mcbMCMediaOneLinkUp.setDescription('A Media Converter Media One Link Up trap signifies that the sending protocol entity checks if the media one of the specified media converter in the slot links up')
mcbMCMediaTwoLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 171, 41, 1) + (0,10)).setObjects(("DLINK-MCB-MIB", "mcbMCSlotNo"))
if mibBuilder.loadTexts: mcbMCMediaTwoLinkUp.setDescription('A Media Converter Media Two Link Up trap signifies that the sending protocol entity checks if the media two of the specified media converter in the slot links up')
mcbMCMediaOneBroken = NotificationType((1, 3, 6, 1, 4, 1, 171, 41, 1) + (0,11)).setObjects(("DLINK-MCB-MIB", "mcbMCSlotNo"))
if mibBuilder.loadTexts: mcbMCMediaOneBroken.setDescription('A Media Converter Media One Broken trap signifies that the sending protocol entity checks if the media one of the specified media converter in the slot was broken')
mcbMCMediaTwoBroken = NotificationType((1, 3, 6, 1, 4, 1, 171, 41, 1) + (0,12)).setObjects(("DLINK-MCB-MIB", "mcbMCSlotNo"))
if mibBuilder.loadTexts: mcbMCMediaTwoBroken.setDescription('A Media Converter Media Two Broken trap signifies that the sending protocol entity checks if the media two of the specified media converter in the slot was broken')
mcbMCActiveSlotChange = NotificationType((1, 3, 6, 1, 4, 1, 171, 41, 1) + (0,13)).setObjects(("DLINK-MCB-MIB", "mcbMCRedundantGroupNo"))
if mibBuilder.loadTexts: mcbMCActiveSlotChange.setDescription('A Active Slot Change trap signifies that the sending protocol entity checks if the active slot of the redundant group is changed')
mcbMCActiveSlotLose = NotificationType((1, 3, 6, 1, 4, 1, 171, 41, 1) + (0,14)).setObjects(("DLINK-MCB-MIB", "mcbMCRedundantGroupNo"))
if mibBuilder.loadTexts: mcbMCActiveSlotLose.setDescription('A Active Slot Lose trap signifies that the sending protocol entity checks if the active slot of the redundant group is lost')
mibBuilder.exportSymbols("DLINK-MCB-MIB", mcbMCMediaOneLinkUp=mcbMCMediaOneLinkUp, mcbMCMediaTwoLinkDown=mcbMCMediaTwoLinkDown, mcbSNMPTrapMCLinkBroken=mcbSNMPTrapMCLinkBroken, mcbMCMediaTwoRxPacketCount=mcbMCMediaTwoRxPacketCount, mcbMCMediaOneDupStatus=mcbMCMediaOneDupStatus, mcbMCMediaTwoType=mcbMCMediaTwoType, mcbMCSetLLCF=mcbMCSetLLCF, mcbMCSetMediaOneFlowControl=mcbMCSetMediaOneFlowControl, mcbAdministratorFactoryReset=mcbAdministratorFactoryReset, mcbMCActiveSlotLose=mcbMCActiveSlotLose, mcbMCMediaOneLinkStatus=mcbMCMediaOneLinkStatus, mcbMCRedundantGroupSecondarySlot=mcbMCRedundantGroupSecondarySlot, mcbMCSlotNo=mcbMCSlotNo, mcbMCRedundantGroupNo=mcbMCRedundantGroupNo, mcbMCEnableMediaOne=mcbMCEnableMediaOne, mcbFrameFanOneFailStatus=mcbFrameFanOneFailStatus, mcbSNMPTrapMCActiveSlotChange=mcbSNMPTrapMCActiveSlotChange, mcbMCMediaOneType=mcbMCMediaOneType, mcbMCMediaOneTxPacketCount=mcbMCMediaOneTxPacketCount, mcbMCMediaTwoBroken=mcbMCMediaTwoBroken, mcbMCMediaTwoLinkStatus=mcbMCMediaTwoLinkStatus, mcbMCFrame=mcbMCFrame, company=company, mcbSNMPTrapMCLinkUp=mcbSNMPTrapMCLinkUp, mcbSNMPTrapMCLinkDown=mcbSNMPTrapMCLinkDown, mcbMCModelName=mcbMCModelName, mcbMCRedundantGroupPrimarySlot=mcbMCRedundantGroupPrimarySlot, mcbMediaConverterChassis=mcbMediaConverterChassis, mcbMCMediaOneRxPacketCount=mcbMCMediaOneRxPacketCount, mcbFramePowerOneFailStatus=mcbFramePowerOneFailStatus, mcbMediaConverterPlugin=mcbMediaConverterPlugin, mcbSNMPTrapMCActiveSlotLose=mcbSNMPTrapMCActiveSlotLose, mcbAdministratorSoftwareRev=mcbAdministratorSoftwareRev, mcbMCRedundantGroupEntry=mcbMCRedundantGroupEntry, mcbSNMPTrapPowerFail=mcbSNMPTrapPowerFail, mcbFrameFanTwoFailStatus=mcbFrameFanTwoFailStatus, mcbMCRedundantGroupEnable=mcbMCRedundantGroupEnable, mcbMCRedundantGroupTable=mcbMCRedundantGroupTable, mcbMCSlotEntry=mcbMCSlotEntry, mcbMCActiveSlotChange=mcbMCActiveSlotChange, mcbMCSetMediaOneDuplex=mcbMCSetMediaOneDuplex, mcbMCSetMediaOneSpeed=mcbMCSetMediaOneSpeed, mcbMCMediaOneSpeedStatus=mcbMCMediaOneSpeedStatus, mcbSNMPMIB=mcbSNMPMIB, mcbMCSetMediaOneAutoNegotiate=mcbMCSetMediaOneAutoNegotiate, mcbFanTwoFail=mcbFanTwoFail, mcbMCMediaTwoDupStatus=mcbMCMediaTwoDupStatus, mcbAdministratorHardwareRev=mcbAdministratorHardwareRev, mcbSNMPTrapMCPlugin=mcbSNMPTrapMCPlugin, mcbAdministratorBiosRev=mcbAdministratorBiosRev, mcbMCSlotName=mcbMCSlotName, mcbMCSlots=mcbMCSlots, mcbPowerTwoFail=mcbPowerTwoFail, mcbMCSetMediaTwoFlowControl=mcbMCSetMediaTwoFlowControl, mcbFramePowerOneOnStatus=mcbFramePowerOneOnStatus, mcbMCSetMediaTwoLLR=mcbMCSetMediaTwoLLR, mcbFanOneFail=mcbFanOneFail, mcbAdministratorSoftwareReboot=mcbAdministratorSoftwareReboot, mcbMCMediaTwoBrokenStatus=mcbMCMediaTwoBrokenStatus, mcbMCMediaOneBrokenStatus=mcbMCMediaOneBrokenStatus, mcbMCSetMediaTwoAutoNegotiate=mcbMCSetMediaTwoAutoNegotiate, mcbMCSetMediaOneLLR=mcbMCSetMediaOneLLR, mcbMediaConverterFamily=mcbMediaConverterFamily, mcbMCMediaOneBroken=mcbMCMediaOneBroken, mcbMCSlotCount=mcbMCSlotCount, mcbMCRedundantGroupCount=mcbMCRedundantGroupCount, mcbMCRedundantGroups=mcbMCRedundantGroups, mcbMCMediaTwoTxPacketCount=mcbMCMediaTwoTxPacketCount, mcbAdministrator=mcbAdministrator, mcbMCMediaTwoSpeedStatus=mcbMCMediaTwoSpeedStatus, mcbFramePowerTwoOnStatus=mcbFramePowerTwoOnStatus, mcbMCSetMediaTwoSpeed=mcbMCSetMediaTwoSpeed, mcbFramePowerTwoFailStatus=mcbFramePowerTwoFailStatus, mcbMCMediaTwoLinkUp=mcbMCMediaTwoLinkUp, mcbPowerOneFail=mcbPowerOneFail, mcbSNMPTrapFanFail=mcbSNMPTrapFanFail, mcbMediaConverterPullout=mcbMediaConverterPullout, mcbMCEnable=mcbMCEnable, mcbMCRedundantGroupActiveSlot=mcbMCRedundantGroupActiveSlot, mcbMCEnableMediaTwo=mcbMCEnableMediaTwo, mcbMCMediaOneLinkDown=mcbMCMediaOneLinkDown, mcbAdministratorFactoryResetCPU=mcbAdministratorFactoryResetCPU, mcbMCSetMediaTwoDuplex=mcbMCSetMediaTwoDuplex, mcbMCSlotTable=mcbMCSlotTable, mcbMCSlotExist=mcbMCSlotExist, mcbMCRedundantGroupRestart=mcbMCRedundantGroupRestart, mcbSNMPTrapMCPullout=mcbSNMPTrapMCPullout)