#
# PySNMP MIB module COMPAQ-AGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COMPAQ-AGENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:10:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
compaq_common_mgmt, = mibBuilder.importSymbols("COMPAQ-ID-REC-MIB", "compaq-common-mgmt")
cpqRackCommonEnclosureRack, cpqRackAssetIndex, cpqRackNetConnectorIndex, cpqRackNetConnectorRack, cpqRackNetConnectorChassis, cpqRackCommonEnclosureIndex = mibBuilder.importSymbols("CPQRACK-MIB", "cpqRackCommonEnclosureRack", "cpqRackAssetIndex", "cpqRackNetConnectorIndex", "cpqRackNetConnectorRack", "cpqRackNetConnectorChassis", "cpqRackCommonEnclosureIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, Gauge32, ObjectIdentity, Unsigned32, TimeTicks, NotificationType, Integer32, Bits, iso, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Unsigned32", "TimeTicks", "NotificationType", "Integer32", "Bits", "iso", "Counter64", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
agentGeneralMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 161, 3, 1))
agentBasicInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1))
agentBasicConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2))
agentIpProtoConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 3))
agentIpTrapManager = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 4))
agentConsoleModeManager = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 5))
agentSlipModeManager = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 6))
agentSNTP = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7))
agentDST = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8))
agentSwitchCommonMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 161, 3, 3))
agentSwitchCube = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 1))
agentSwitchPowerSupply = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2))
agentSwitchFan = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 3))
agentSwitchTempSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 4))
agentMgmtProtocolCapability = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("snmp-ip", 2), ("snmp-ipx", 3), ("snmp-ip-ipx", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMgmtProtocolCapability.setStatus('mandatory')
agentMibCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 2), )
if mibBuilder.loadTexts: agentMibCapabilityTable.setStatus('mandatory')
agentMibCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 2, 1), ).setIndexNames((0, "COMPAQ-AGENT-MIB", "agentMibCapabilityIndex"))
if mibBuilder.loadTexts: agentMibCapabilityEntry.setStatus('mandatory')
agentMibCapabilityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityIndex.setStatus('mandatory')
agentMibCapabilityDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 35))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityDescr.setStatus('mandatory')
agentMibCapabilityVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityVersion.setStatus('mandatory')
agentMibCapabilityType = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("standard", 2), ("proprietary", 3), ("experiment", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityType.setStatus('mandatory')
agentStatusConsoleInUse = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("in-use", 2), ("not-in-use", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentStatusConsoleInUse.setStatus('mandatory')
agentStatusSaveCfg = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("proceeding", 2), ("completed", 3), ("changed-not-save", 4), ("failed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentStatusSaveCfg.setStatus('mandatory')
agentSwitchMfgDate = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchMfgDate.setStatus('mandatory')
agentSwitchFirmwareMfgDate = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchFirmwareMfgDate.setStatus('mandatory')
agentBscSwFileTable = MibTable((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1), )
if mibBuilder.loadTexts: agentBscSwFileTable.setStatus('mandatory')
agentBscSwFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1), ).setIndexNames((0, "COMPAQ-AGENT-MIB", "agentBscSwFileIndex"))
if mibBuilder.loadTexts: agentBscSwFileEntry.setStatus('mandatory')
agentBscSwFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentBscSwFileIndex.setStatus('mandatory')
agentBscSwFileDscr = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentBscSwFileDscr.setStatus('mandatory')
agentBscSwFileAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentBscSwFileAddr.setStatus('mandatory')
agentBscSwFileTransferType = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("network-load", 2), ("out-of-band-load", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentBscSwFileTransferType.setStatus('mandatory')
agentBscSwFile = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentBscSwFile.setStatus('mandatory')
agentBscSwFileLocateId = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentBscSwFileLocateId.setStatus('mandatory')
agentBscSwFileLoadType = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("upload", 2), ("download", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentBscSwFileLoadType.setStatus('mandatory')
agentBscSwFileCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("inactive", 2), ("start", 3), ("delete", 4), ("create-and-go", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentBscSwFileCtrl.setStatus('mandatory')
agentBscFileServerTftpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentBscFileServerTftpPort.setStatus('mandatory')
agentBscSwFileTime = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentBscSwFileTime.setStatus('mandatory')
agentBscSwFileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentBscSwFileStatus.setStatus('mandatory')
agentFileTransfer = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("start", 2), ("start-and-reset", 3), ("noaction", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentFileTransfer.setStatus('obsolete')
agentSystemReset = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("cold-start", 2), ("warm-start", 3), ("no-reset", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSystemReset.setStatus('mandatory')
agentRs232PortConfig = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("console", 2), ("out-of-band", 3), ("notAvail", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRs232PortConfig.setStatus('mandatory')
agentOutOfBandBaudRateConfig = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("baudRate-2400", 2), ("baudRate-9600", 3), ("baudRate-19200", 4), ("baudRate-38400", 5), ("baudRate-115200", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutOfBandBaudRateConfig.setStatus('obsolete')
agentSaveCfg = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("idle", 2), ("set", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSaveCfg.setStatus('mandatory')
agentIpNumOfIf = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpNumOfIf.setStatus('mandatory')
agentIpTftpServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 3, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpTftpServerAddr.setStatus('obsolete')
agentIpGetIpFrom = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("bootp", 3), ("dhcp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpGetIpFrom.setStatus('mandatory')
agentIpTrapManagerTable = MibTable((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 4, 1), )
if mibBuilder.loadTexts: agentIpTrapManagerTable.setStatus('mandatory')
agentIpTrapManagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 4, 1, 1), ).setIndexNames((0, "COMPAQ-AGENT-MIB", "agentIpTrapManagerIpAddr"))
if mibBuilder.loadTexts: agentIpTrapManagerEntry.setStatus('mandatory')
agentIpTrapManagerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 4, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpTrapManagerIpAddr.setStatus('mandatory')
agentIpTrapManagerComm = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 4, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpTrapManagerComm.setStatus('mandatory')
agentIpTrapManagerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpTrapManagerStatus.setStatus('mandatory')
agentConsoleModeManagerDataBits = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("bits-7", 2), ("bits-8", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentConsoleModeManagerDataBits.setStatus('mandatory')
agentConsoleModeManagerStopBits = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("stopbits-1", 2), ("stopbits-2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentConsoleModeManagerStopBits.setStatus('mandatory')
agentConsoleModeManagerParity = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 5, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("odd", 2), ("even", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentConsoleModeManagerParity.setStatus('mandatory')
agentConsoleModeManagerBaudRate = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 5, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("baudRate-2400", 2), ("baudRate-9600", 3), ("baudRate-19200", 4), ("baudRate-38400", 5), ("baudRate-57200", 6), ("baudRate-115200", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentConsoleModeManagerBaudRate.setStatus('mandatory')
agentSlipModeManagerLocalIP = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 6, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSlipModeManagerLocalIP.setStatus('mandatory')
agentSlipModeManagerRemoteIP = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 6, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSlipModeManagerRemoteIP.setStatus('mandatory')
agentSlipModeManagerMTU = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("mtu-1006", 2), ("mtu-1500", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSlipModeManagerMTU.setStatus('mandatory')
agentSlipModeManagerBaudRate = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 6, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("baudRate-2400", 2), ("baudRate-9600", 3), ("baudRate-19200", 4), ("baudRate-38400", 5), ("baudRate-57200", 6), ("baudRate-115200", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSlipModeManagerBaudRate.setStatus('mandatory')
agentSNTPState = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSNTPState.setStatus('mandatory')
agentSNTPTimeSource = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("system", 0), ("server1", 1), ("server2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSNTPTimeSource.setStatus('mandatory')
agentSNTPServer1IPAddr = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSNTPServer1IPAddr.setStatus('mandatory')
agentSNTPServer2IPAddr = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSNTPServer2IPAddr.setStatus('mandatory')
agentSNTPTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-779, 839))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSNTPTimeZone.setStatus('mandatory')
agentSNTPPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 99999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSNTPPollInterval.setStatus('mandatory')
agentSNTPCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSNTPCurrentTime.setStatus('mandatory')
agentSNTPUpTime = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSNTPUpTime.setStatus('mandatory')
agentSNTPBootTime = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSNTPBootTime.setStatus('mandatory')
agentDSTStatus = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("repeating", 2), ("annual", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTStatus.setStatus('mandatory')
agentDSTOffset = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTOffset.setStatus('mandatory')
agentDSTRepeatingStartMonth = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTRepeatingStartMonth.setStatus('mandatory')
agentDSTRepeatingStartWhichDay = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTRepeatingStartWhichDay.setStatus('mandatory')
agentDSTRepeatingStartDayOfWeek = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTRepeatingStartDayOfWeek.setStatus('mandatory')
agentDSTRepeatingStartHour = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTRepeatingStartHour.setStatus('mandatory')
agentDSTRepeatingStartMinute = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTRepeatingStartMinute.setStatus('mandatory')
agentDSTRepeatingEndMonth = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTRepeatingEndMonth.setStatus('mandatory')
agentDSTRepeatingEndWhichDay = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTRepeatingEndWhichDay.setStatus('mandatory')
agentDSTRepeatingEndDayOfWeek = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTRepeatingEndDayOfWeek.setStatus('mandatory')
agentDSTRepeatingEndHour = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTRepeatingEndHour.setStatus('mandatory')
agentDSTRepeatingEndMinute = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTRepeatingEndMinute.setStatus('mandatory')
agentDSTAnnualStartMonth = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTAnnualStartMonth.setStatus('mandatory')
agentDSTAnnualStartDayOfMonth = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTAnnualStartDayOfMonth.setStatus('mandatory')
agentDSTAnnualStartHour = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTAnnualStartHour.setStatus('mandatory')
agentDSTAnnualStartMinute = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTAnnualStartMinute.setStatus('mandatory')
agentDSTAnnualEndMonth = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTAnnualEndMonth.setStatus('mandatory')
agentDSTAnnualEndDayOfMonth = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTAnnualEndDayOfMonth.setStatus('mandatory')
agentDSTAnnualEndHour = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTAnnualEndHour.setStatus('mandatory')
agentDSTAnnualEndMinute = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDSTAnnualEndMinute.setStatus('mandatory')
agentSwitchCubeTable = MibTable((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 1, 1), )
if mibBuilder.loadTexts: agentSwitchCubeTable.setStatus('mandatory')
agentSwitchCubeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 1, 1, 1), ).setIndexNames((0, "CPQRACK-MIB", "cpqRackAssetIndex"), (0, "CPQRACK-MIB", "cpqRackCommonEnclosureRack"), (0, "CPQRACK-MIB", "cpqRackCommonEnclosureIndex"), (0, "CPQRACK-MIB", "cpqRackNetConnectorRack"), (0, "CPQRACK-MIB", "cpqRackNetConnectorChassis"), (0, "CPQRACK-MIB", "cpqRackNetConnectorIndex"), (0, "COMPAQ-AGENT-MIB", "agentSwitchCubeType"))
if mibBuilder.loadTexts: agentSwitchCubeEntry.setStatus('mandatory')
agentSwitchCubeType = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("dualTSX", 2), ("quadT", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchCubeType.setStatus('mandatory')
agentSwitchCubeSpareName = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchCubeSpareName.setStatus('mandatory')
agentSwitchCubeSparePartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchCubeSparePartNumber.setStatus('mandatory')
agentSwitchPowerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1), )
if mibBuilder.loadTexts: agentSwitchPowerSupplyTable.setStatus('mandatory')
agentSwitchPowerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1, 1), ).setIndexNames((0, "CPQRACK-MIB", "cpqRackAssetIndex"), (0, "CPQRACK-MIB", "cpqRackCommonEnclosureRack"), (0, "CPQRACK-MIB", "cpqRackCommonEnclosureIndex"), (0, "CPQRACK-MIB", "cpqRackNetConnectorRack"), (0, "CPQRACK-MIB", "cpqRackNetConnectorChassis"), (0, "CPQRACK-MIB", "cpqRackNetConnectorIndex"), (0, "COMPAQ-AGENT-MIB", "agentSwitchPowerSupplyIndex"))
if mibBuilder.loadTexts: agentSwitchPowerSupplyEntry.setStatus('mandatory')
agentSwitchPowerSupplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchPowerSupplyIndex.setStatus('mandatory')
agentSwitchPowerSupplyMaxPwrOutput = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchPowerSupplyMaxPwrOutput.setStatus('mandatory')
agentSwitchPowerSupplyCurPwrOutput = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchPowerSupplyCurPwrOutput.setStatus('mandatory')
agentSwitchPowerSupplyIntakeTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchPowerSupplyIntakeTemp.setStatus('mandatory')
agentSwitchPowerSupplyExhaustTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchPowerSupplyExhaustTemp.setStatus('mandatory')
agentSwitchPowerSupplyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("noError", 1), ("generalFailure", 2), ("bistFailure", 3), ("fanFailure", 4), ("tempFailure", 5), ("interlockOpen", 6), ("epromFailed", 7), ("vrefFailed", 8), ("dacFailed", 9), ("ramTestFailed", 10), ("voltageChannelFailed", 11), ("orringdiodeFailed", 12), ("brownOut", 13), ("giveupOnStartup", 14), ("nvramInvalid", 15), ("calibrationTableInvalid", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchPowerSupplyStatus.setStatus('mandatory')
agentSwitchPowerSupplyInputLineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noError", 1), ("lineOverVoltage", 2), ("lineUnderVoltage", 3), ("lineHit", 4), ("brownOut", 5), ("linePowerLoss", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchPowerSupplyInputLineStatus.setStatus('mandatory')
agentSwitchPowerSupplyCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("degraded", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchPowerSupplyCondition.setStatus('mandatory')
agentSwitchFanTable = MibTable((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 3, 1), )
if mibBuilder.loadTexts: agentSwitchFanTable.setStatus('mandatory')
agentSwitchFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 3, 1, 1), ).setIndexNames((0, "CPQRACK-MIB", "cpqRackAssetIndex"), (0, "CPQRACK-MIB", "cpqRackCommonEnclosureRack"), (0, "CPQRACK-MIB", "cpqRackCommonEnclosureIndex"), (0, "CPQRACK-MIB", "cpqRackNetConnectorRack"), (0, "CPQRACK-MIB", "cpqRackNetConnectorChassis"), (0, "CPQRACK-MIB", "cpqRackNetConnectorIndex"), (0, "COMPAQ-AGENT-MIB", "agentSwitchFanIndex"))
if mibBuilder.loadTexts: agentSwitchFanEntry.setStatus('mandatory')
agentSwitchFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchFanIndex.setStatus('mandatory')
agentSwitchFanCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("degraded", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchFanCondition.setStatus('mandatory')
agentSwitchTempSensorTable = MibTable((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 4, 1), )
if mibBuilder.loadTexts: agentSwitchTempSensorTable.setStatus('mandatory')
agentSwitchTempSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 4, 1, 1), ).setIndexNames((0, "CPQRACK-MIB", "cpqRackAssetIndex"), (0, "CPQRACK-MIB", "cpqRackCommonEnclosureRack"), (0, "CPQRACK-MIB", "cpqRackCommonEnclosureIndex"), (0, "CPQRACK-MIB", "cpqRackNetConnectorRack"), (0, "CPQRACK-MIB", "cpqRackNetConnectorChassis"), (0, "CPQRACK-MIB", "cpqRackNetConnectorIndex"), (0, "COMPAQ-AGENT-MIB", "agentSwitchTempSensorIndex"))
if mibBuilder.loadTexts: agentSwitchTempSensorEntry.setStatus('mandatory')
agentSwitchTempSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchTempSensorIndex.setStatus('mandatory')
agentSwitchTempSensorCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchTempSensorCurrent.setStatus('mandatory')
agentSwitchTempSensorThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchTempSensorThreshold.setStatus('mandatory')
agentSwitchTempSensorCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("degraded", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchTempSensorCondition.setStatus('mandatory')
agentSwitchTempSensorTempType = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 5, 9, 15))).clone(namedValues=NamedValues(("other", 1), ("blowout", 5), ("caution", 9), ("critical", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSwitchTempSensorTempType.setStatus('mandatory')
endOfMIB = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 9999), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: endOfMIB.setStatus('mandatory')
mibBuilder.exportSymbols("COMPAQ-AGENT-MIB", agentSwitchPowerSupplyTable=agentSwitchPowerSupplyTable, agentSwitchPowerSupplyIndex=agentSwitchPowerSupplyIndex, agentIpTrapManagerComm=agentIpTrapManagerComm, agentDSTRepeatingEndMonth=agentDSTRepeatingEndMonth, agentMibCapabilityTable=agentMibCapabilityTable, agentGeneralMgmt=agentGeneralMgmt, agentDSTAnnualEndMinute=agentDSTAnnualEndMinute, agentSlipModeManagerMTU=agentSlipModeManagerMTU, agentSNTPPollInterval=agentSNTPPollInterval, agentSwitchPowerSupplyStatus=agentSwitchPowerSupplyStatus, agentDSTStatus=agentDSTStatus, agentSwitchCommonMgmt=agentSwitchCommonMgmt, agentSNTPBootTime=agentSNTPBootTime, agentSwitchCubeEntry=agentSwitchCubeEntry, agentSNTP=agentSNTP, agentConsoleModeManagerBaudRate=agentConsoleModeManagerBaudRate, endOfMIB=endOfMIB, agentIpTrapManagerTable=agentIpTrapManagerTable, agentDSTAnnualEndHour=agentDSTAnnualEndHour, agentIpProtoConfig=agentIpProtoConfig, agentSlipModeManagerRemoteIP=agentSlipModeManagerRemoteIP, agentDSTRepeatingEndMinute=agentDSTRepeatingEndMinute, agentBscSwFileAddr=agentBscSwFileAddr, agentSwitchTempSensor=agentSwitchTempSensor, agentSNTPCurrentTime=agentSNTPCurrentTime, agentStatusSaveCfg=agentStatusSaveCfg, agentSwitchFan=agentSwitchFan, agentSwitchPowerSupplyIntakeTemp=agentSwitchPowerSupplyIntakeTemp, agentSwitchTempSensorThreshold=agentSwitchTempSensorThreshold, agentDSTAnnualStartHour=agentDSTAnnualStartHour, agentSwitchCubeTable=agentSwitchCubeTable, agentDSTRepeatingStartMonth=agentDSTRepeatingStartMonth, agentBscFileServerTftpPort=agentBscFileServerTftpPort, agentDSTRepeatingEndWhichDay=agentDSTRepeatingEndWhichDay, agentBscSwFileStatus=agentBscSwFileStatus, agentConsoleModeManagerParity=agentConsoleModeManagerParity, agentMibCapabilityType=agentMibCapabilityType, agentBscSwFileTime=agentBscSwFileTime, agentIpTrapManagerStatus=agentIpTrapManagerStatus, agentSNTPServer1IPAddr=agentSNTPServer1IPAddr, agentMibCapabilityIndex=agentMibCapabilityIndex, agentIpTrapManagerEntry=agentIpTrapManagerEntry, agentIpTrapManagerIpAddr=agentIpTrapManagerIpAddr, agentSwitchCubeSparePartNumber=agentSwitchCubeSparePartNumber, agentSwitchTempSensorCondition=agentSwitchTempSensorCondition, agentConsoleModeManagerDataBits=agentConsoleModeManagerDataBits, agentSwitchMfgDate=agentSwitchMfgDate, agentSwitchPowerSupplyMaxPwrOutput=agentSwitchPowerSupplyMaxPwrOutput, agentSwitchTempSensorIndex=agentSwitchTempSensorIndex, agentSNTPUpTime=agentSNTPUpTime, agentIpGetIpFrom=agentIpGetIpFrom, agentBscSwFileEntry=agentBscSwFileEntry, agentIpTftpServerAddr=agentIpTftpServerAddr, agentSlipModeManagerBaudRate=agentSlipModeManagerBaudRate, agentDSTAnnualStartDayOfMonth=agentDSTAnnualStartDayOfMonth, agentSwitchTempSensorTable=agentSwitchTempSensorTable, agentStatusConsoleInUse=agentStatusConsoleInUse, agentSwitchFanIndex=agentSwitchFanIndex, agentBasicConfig=agentBasicConfig, agentMibCapabilityVersion=agentMibCapabilityVersion, agentSwitchPowerSupplyEntry=agentSwitchPowerSupplyEntry, agentMibCapabilityDescr=agentMibCapabilityDescr, agentSwitchPowerSupplyInputLineStatus=agentSwitchPowerSupplyInputLineStatus, agentSwitchCube=agentSwitchCube, agentBscSwFileCtrl=agentBscSwFileCtrl, agentConsoleModeManagerStopBits=agentConsoleModeManagerStopBits, agentMibCapabilityEntry=agentMibCapabilityEntry, agentSwitchCubeSpareName=agentSwitchCubeSpareName, agentDSTRepeatingStartHour=agentDSTRepeatingStartHour, agentSwitchFanEntry=agentSwitchFanEntry, agentSystemReset=agentSystemReset, agentSwitchTempSensorTempType=agentSwitchTempSensorTempType, agentDSTRepeatingStartDayOfWeek=agentDSTRepeatingStartDayOfWeek, agentDSTAnnualEndMonth=agentDSTAnnualEndMonth, agentConsoleModeManager=agentConsoleModeManager, agentSNTPServer2IPAddr=agentSNTPServer2IPAddr, agentBscSwFileIndex=agentBscSwFileIndex, agentSwitchFanTable=agentSwitchFanTable, agentSwitchPowerSupplyCurPwrOutput=agentSwitchPowerSupplyCurPwrOutput, agentSwitchTempSensorCurrent=agentSwitchTempSensorCurrent, agentDSTAnnualStartMinute=agentDSTAnnualStartMinute, agentSwitchPowerSupplyCondition=agentSwitchPowerSupplyCondition, agentDST=agentDST, agentIpNumOfIf=agentIpNumOfIf, agentDSTRepeatingEndDayOfWeek=agentDSTRepeatingEndDayOfWeek, agentBscSwFileTable=agentBscSwFileTable, agentDSTRepeatingEndHour=agentDSTRepeatingEndHour, agentMgmtProtocolCapability=agentMgmtProtocolCapability, agentSNTPTimeSource=agentSNTPTimeSource, agentFileTransfer=agentFileTransfer, agentDSTRepeatingStartMinute=agentDSTRepeatingStartMinute, agentBscSwFileDscr=agentBscSwFileDscr, agentSwitchPowerSupplyExhaustTemp=agentSwitchPowerSupplyExhaustTemp, agentBscSwFile=agentBscSwFile, agentRs232PortConfig=agentRs232PortConfig, agentDSTAnnualStartMonth=agentDSTAnnualStartMonth, agentSlipModeManager=agentSlipModeManager, agentBscSwFileLoadType=agentBscSwFileLoadType, agentSwitchCubeType=agentSwitchCubeType, agentSlipModeManagerLocalIP=agentSlipModeManagerLocalIP, agentDSTRepeatingStartWhichDay=agentDSTRepeatingStartWhichDay, agentSwitchPowerSupply=agentSwitchPowerSupply, agentSNTPState=agentSNTPState, agentBscSwFileLocateId=agentBscSwFileLocateId, agentBasicInfo=agentBasicInfo, agentBscSwFileTransferType=agentBscSwFileTransferType, agentSwitchFirmwareMfgDate=agentSwitchFirmwareMfgDate, agentSNTPTimeZone=agentSNTPTimeZone, agentIpTrapManager=agentIpTrapManager, agentOutOfBandBaudRateConfig=agentOutOfBandBaudRateConfig, agentDSTOffset=agentDSTOffset, agentDSTAnnualEndDayOfMonth=agentDSTAnnualEndDayOfMonth, agentSwitchFanCondition=agentSwitchFanCondition, agentSaveCfg=agentSaveCfg, agentSwitchTempSensorEntry=agentSwitchTempSensorEntry)