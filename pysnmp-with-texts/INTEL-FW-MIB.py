#
# PySNMP MIB module INTEL-FW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEL-FW-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:54:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
mib2ext, = mibBuilder.importSymbols("INTEL-GEN-MIB", "mib2ext")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, iso, Counter64, IpAddress, Gauge32, Integer32, ModuleIdentity, ObjectIdentity, MibIdentifier, Unsigned32, Bits, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Counter64", "IpAddress", "Gauge32", "Integer32", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Unsigned32", "Bits", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fw = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 9))
fwInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 9, 1))
fwModuleTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1), )
if mibBuilder.loadTexts: fwModuleTable.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleTable.setDescription('')
fwModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1), ).setIndexNames((0, "INTEL-FW-MIB", "fwModuleChassisIndex"), (0, "INTEL-FW-MIB", "fwModuleModuleIndex"), (0, "INTEL-FW-MIB", "fwModuleSWSectionIndex"), (0, "INTEL-FW-MIB", "fwModuleSWNumberIndex"))
if mibBuilder.loadTexts: fwModuleEntry.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleEntry.setDescription('')
fwModuleChassisIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwModuleChassisIndex.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleChassisIndex.setDescription('The chassis number')
fwModuleModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwModuleModuleIndex.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleModuleIndex.setDescription('Which module is currently to be used')
fwModuleSWSectionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("runningSW", 1), ("backUpSW", 2), ("upgradeSW", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwModuleSWSectionIndex.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleSWSectionIndex.setDescription('Section type: Running SW section: 1 Backup SW section : 2 Upgrade SW section: 3')
fwModuleSWNumberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwModuleSWNumberIndex.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleSWNumberIndex.setDescription('The index number of the file(s) in the section')
fwModuleDeletePlugIn = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwModuleDeletePlugIn.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleDeletePlugIn.setDescription('A write to this entry will delete the plugin pointed to by the index')
fwModuleDeleteBackup = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwModuleDeleteBackup.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleDeleteBackup.setDescription('A write to this entry will delete the backup section')
fwModuleFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwModuleFileName.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleFileName.setDescription('The filename of the file pointet to by the index')
fwModuleDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwModuleDescription.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleDescription.setDescription('A desctiption of the current file pointet to by the index')
fwModuleLoadTime = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwModuleLoadTime.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleLoadTime.setDescription('The load time for the current file')
fwModuleIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwModuleIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleIpAddress.setDescription('The IP address of the server that delivered the current file')
fwModuleMajorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwModuleMajorVersion.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleMajorVersion.setDescription('The major version of the current file')
fwModuleMinorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwModuleMinorVersion.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleMinorVersion.setDescription('The minor version of the current file')
fwModuleVersionTxt = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwModuleVersionTxt.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleVersionTxt.setDescription('The version text if any')
fwModuleSwStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("approved", 1), ("experimental", 2), ("invalid", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwModuleSwStatus.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleSwStatus.setDescription('The SW status: Approve running SW : Write (1)approved to this entry Undo running SW : Write (3)invalid to this entry Note: Writing (2)experimental is invalid')
fwModuleSwType = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("firmware", 1), ("plugin", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwModuleSwType.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleSwType.setDescription('SW file type: Firmware : (1) Plug-In : (2)')
fwModuleFileID = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwModuleFileID.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleFileID.setDescription('SW file ID: A unigue ID for the file. To be used as a link between pattern and fwinfo')
fwPatternTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2), )
if mibBuilder.loadTexts: fwPatternTable.setStatus('mandatory')
if mibBuilder.loadTexts: fwPatternTable.setDescription('')
fwPatternEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2, 1), ).setIndexNames((0, "INTEL-FW-MIB", "fwPatternChassisIndex"), (0, "INTEL-FW-MIB", "fwPatternModuleIndex"), (0, "INTEL-FW-MIB", "fwPatternFileIndex"))
if mibBuilder.loadTexts: fwPatternEntry.setStatus('mandatory')
if mibBuilder.loadTexts: fwPatternEntry.setDescription('')
fwPatternChassisIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwPatternChassisIndex.setStatus('mandatory')
if mibBuilder.loadTexts: fwPatternChassisIndex.setDescription('What chassis is the info received from?')
fwPatternModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwPatternModuleIndex.setStatus('mandatory')
if mibBuilder.loadTexts: fwPatternModuleIndex.setDescription('Which module is the info received from?')
fwPatternFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwPatternFileIndex.setStatus('mandatory')
if mibBuilder.loadTexts: fwPatternFileIndex.setDescription('The file pattern requested')
fwPatternFileFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(14, 14)).setFixedLength(14)).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwPatternFileFilter.setStatus('mandatory')
if mibBuilder.loadTexts: fwPatternFileFilter.setDescription('The filter is telling what files the firmware is capable of running')
fwPatternFileDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwPatternFileDesc.setStatus('mandatory')
if mibBuilder.loadTexts: fwPatternFileDesc.setDescription('Discription of the file')
fwPatternFileShortDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwPatternFileShortDesc.setStatus('mandatory')
if mibBuilder.loadTexts: fwPatternFileShortDesc.setDescription('Short description e.g. FIRMWARE or PLUGIN')
fwPatternDefaultEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwPatternDefaultEnable.setStatus('mandatory')
if mibBuilder.loadTexts: fwPatternDefaultEnable.setDescription("SW file status: Download by default(1), Don't download dy default(2)")
fwPatternFileID = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwPatternFileID.setStatus('mandatory')
if mibBuilder.loadTexts: fwPatternFileID.setDescription('SW file ID: This is udes to link the fwinfo and the pattern together')
fwInfoNoOfEntries = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwInfoNoOfEntries.setStatus('mandatory')
if mibBuilder.loadTexts: fwInfoNoOfEntries.setDescription('The total number of entries in the MIB')
fwInfoLastUpdateTime = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwInfoLastUpdateTime.setStatus('mandatory')
if mibBuilder.loadTexts: fwInfoLastUpdateTime.setDescription('sysTimeOfDay of the last time the MIB has been updated')
fwInfoGoUpgrade = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwInfoGoUpgrade.setStatus('mandatory')
if mibBuilder.loadTexts: fwInfoGoUpgrade.setDescription('Reboot unit to run on downloaded image This will perform a warm reset but before that it will be made sure that the product is able to boot the new image even if only a plug-in has been downloaded')
fwInfoLastTftpToStatusMsgTimeout = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwInfoLastTftpToStatusMsgTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: fwInfoLastTftpToStatusMsgTimeout.setDescription('The timeout in seconds between the last TFTP packet and the status message')
fwInfoResetToRebootTimeout = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwInfoResetToRebootTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: fwInfoResetToRebootTimeout.setDescription('The timeout in seconds between the GoUpgrade command and the following reboot')
mibBuilder.exportSymbols("INTEL-FW-MIB", fwModuleVersionTxt=fwModuleVersionTxt, fwModuleEntry=fwModuleEntry, fwInfoNoOfEntries=fwInfoNoOfEntries, fwPatternFileIndex=fwPatternFileIndex, fwInfoGoUpgrade=fwInfoGoUpgrade, fwModuleSwType=fwModuleSwType, fwModuleMajorVersion=fwModuleMajorVersion, fwModuleFileName=fwModuleFileName, fwPatternModuleIndex=fwPatternModuleIndex, fwModuleSWNumberIndex=fwModuleSWNumberIndex, fwModuleTable=fwModuleTable, fwModuleDeletePlugIn=fwModuleDeletePlugIn, fwModuleSWSectionIndex=fwModuleSWSectionIndex, fwModuleDescription=fwModuleDescription, fwPatternFileFilter=fwPatternFileFilter, fwPatternFileID=fwPatternFileID, fwModuleModuleIndex=fwModuleModuleIndex, fwInfoLastTftpToStatusMsgTimeout=fwInfoLastTftpToStatusMsgTimeout, fwPatternEntry=fwPatternEntry, fwInfoResetToRebootTimeout=fwInfoResetToRebootTimeout, fwPatternDefaultEnable=fwPatternDefaultEnable, fwModuleSwStatus=fwModuleSwStatus, fw=fw, fwModuleChassisIndex=fwModuleChassisIndex, fwPatternFileShortDesc=fwPatternFileShortDesc, fwPatternFileDesc=fwPatternFileDesc, fwPatternTable=fwPatternTable, fwModuleMinorVersion=fwModuleMinorVersion, fwModuleDeleteBackup=fwModuleDeleteBackup, fwPatternChassisIndex=fwPatternChassisIndex, fwModuleLoadTime=fwModuleLoadTime, fwInfoLastUpdateTime=fwInfoLastUpdateTime, fwModuleIpAddress=fwModuleIpAddress, fwInfo=fwInfo, fwModuleFileID=fwModuleFileID)