#
# PySNMP MIB module HARMONIC-INC-NSG9000-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HARMONIC-INC-NSG9000-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:24:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter64, Counter32, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, MibIdentifier, IpAddress, enterprises, ObjectIdentity, iso, TimeTicks, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "Counter32", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "MibIdentifier", "IpAddress", "enterprises", "ObjectIdentity", "iso", "TimeTicks", "Gauge32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
harmonicInc = MibIdentifier((1, 3, 6, 1, 4, 1, 1563))
hOids = MibIdentifier((1, 3, 6, 1, 4, 1, 1563, 1))
hObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1563, 2))
hTrapFields = MibIdentifier((1, 3, 6, 1, 4, 1, 1563, 3))
hModuleOids = MibIdentifier((1, 3, 6, 1, 4, 1, 1563, 1, 1))
hSystemOid = MibIdentifier((1, 3, 6, 1, 4, 1, 1563, 1, 1, 1))
hPlatformOid = MibIdentifier((1, 3, 6, 1, 4, 1, 1563, 1, 1, 2))
hGbePortOid = MibIdentifier((1, 3, 6, 1, 4, 1, 1563, 1, 1, 3))
hSlotOid = MibIdentifier((1, 3, 6, 1, 4, 1, 1563, 1, 1, 4))
hRfModuleOid = MibIdentifier((1, 3, 6, 1, 4, 1, 1563, 1, 1, 5))
hRfPortOid = MibIdentifier((1, 3, 6, 1, 4, 1, 1563, 1, 1, 6))
hQamChannelOid = MibIdentifier((1, 3, 6, 1, 4, 1, 1563, 1, 1, 7))
hSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 1563, 2, 1))
hTrapTimeLastGenerated = MibScalar((1, 3, 6, 1, 4, 1, 1563, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hTrapTimeLastGenerated.setStatus('mandatory')
if mibBuilder.loadTexts: hTrapTimeLastGenerated.setDescription('The value of sysUpTime at the time the last trap was generated. This object can be used by the management station to determine whether traps were generated since the last poll.')
hTrapForwardTable = MibTable((1, 3, 6, 1, 4, 1, 1563, 2, 1, 4), )
if mibBuilder.loadTexts: hTrapForwardTable.setStatus('mandatory')
if mibBuilder.loadTexts: hTrapForwardTable.setDescription('This table contains one row per event (trap) forwarding discriminator.')
hTrapForwardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1563, 2, 1, 4, 1), ).setIndexNames((0, "HARMONIC-INC-NSG9000-MIB", "hTrapDestAddr"))
if mibBuilder.loadTexts: hTrapForwardEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hTrapForwardEntry.setDescription('An entry in the Trap Forwarding Table contains information about a particular event forwarding discrminator (EFD). Each EFD specifies exactly one destination. Its discriminator construct always evaluates to TRUE value, i.e. all event reports pass a particualar EFD. This is the reason why discriminator construct are omitted.')
hTrapDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1563, 2, 1, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hTrapDestAddr.setStatus('mandatory')
if mibBuilder.loadTexts: hTrapDestAddr.setDescription('The IP address of the network management entity to which traps (of the type specified in this table entry) should be sent. The value of this object uniquely identifies the trap destination.')
hTrapDestAddrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1563, 2, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4, 6))).clone(namedValues=NamedValues(("active", 1), ("createAndGo", 4), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hTrapDestAddrStatus.setStatus('mandatory')
if mibBuilder.loadTexts: hTrapDestAddrStatus.setDescription('The status of the table entry denotes both action and current states. Set-requests can carry the action values createAndGo(4) and destroy(6). Get-request always yields the current value active(1). In order for a management application to create an entry the Set-request with hlpTrapDestAddrStatus(createAndGo) variable binding must be sent to the agent. The instance ID part of the status variable will indicate the desired ip-address. In order for a management application to delete an entry the Set-request with hlpTrapDestAddrStatus(destroy) variable binding must be sent to the agent. Upon creation, the entry moves into active(1) state and stays in this state until deletion.')
hAlarmStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 1563, 3, 1))
hAlarmSeverity = MibIdentifier((1, 3, 6, 1, 4, 1, 1563, 3, 2))
hAlarmDesc = MibIdentifier((1, 3, 6, 1, 4, 1, 1563, 3, 3))
hTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1563, 1, 2))
hPlatformTempFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,1)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hPlatformTempFailTrap.setDescription('Temp Failure')
hPlatformVoltageFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,2)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hPlatformVoltageFailTrap.setDescription('Voltage Failure')
hPlatformFan1FailTrap = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,3)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hPlatformFan1FailTrap.setDescription('Fan 1 Failure')
hPlatformFan2FailTrap = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,4)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hPlatformFan2FailTrap.setDescription('Fan 2 Failure')
hPlatformFan3FailTrap = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,5)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hPlatformFan3FailTrap.setDescription('Fan 3 Failure')
hPlatformFan4FailTrap = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,6)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hPlatformFan4FailTrap.setDescription('Fan 4 Failure')
hPlatformPS1VoltageFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,7)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hPlatformPS1VoltageFailTrap.setDescription('Power supply 1 Failure')
hPlatformPS2VoltageFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,8)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hPlatformPS2VoltageFailTrap.setDescription('Power supply 2 Failure')
hPlatformR6ConnLossTrap = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,9)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hPlatformR6ConnLossTrap.setDescription('R6 connection lost')
hPlatformD6ConnLossTrap = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,10)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hPlatformD6ConnLossTrap.setDescription('D6 connection lost')
hGbePortLinkDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,11)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hGbePortLinkDownTrap.setDescription('Gbe port link down')
hRfModuleHwFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,12)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hRfModuleHwFailTrap.setDescription('Rf module hw failure')
hRfModuleTempFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,13)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hRfModuleTempFailTrap.setDescription('Rf module temperature failure')
hRfPortHwFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,14)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hRfPortHwFailTrap.setDescription('Rf port hw failure')
hRfPortTempFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,15)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hRfPortTempFailTrap.setDescription('Rf port temperature failure')
hQamChanneOverflowTrap = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,16)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hQamChanneOverflowTrap.setDescription('Qam channel overflow')
hServicePatMissing = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,17)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hServicePatMissing.setDescription('Service pat missing')
hServicePmtMissing = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,18)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hServicePmtMissing.setDescription('Service pmt missing')
hSwitchToAlternateSource = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,19)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hSwitchToAlternateSource.setDescription('SDV service switch to alternate source')
hPassThroughSourceFailure = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,20)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hPassThroughSourceFailure.setDescription('Source Failure')
hPidRemuxSourceFailure = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,21)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hPidRemuxSourceFailure.setDescription('Source Failure')
hDtiCardMissing = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,22)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hDtiCardMissing.setDescription('DTI Card Missing')
hMcECMMissing = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,23)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hMcECMMissing.setDescription('ECM Missing')
hMcECMNearingExpiration = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,24)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hMcECMNearingExpiration.setDescription('ECM Nearing Expiration')
hMcECMExpired = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,25)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hMcECMExpired.setDescription('ECM Expired')
hDtiClientLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,26)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hDtiClientLinkDown.setDescription('DTI Client Link Down')
hDtiClientNotLocked = NotificationType((1, 3, 6, 1, 4, 1, 1563, 1, 2) + (0,27)).setObjects(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"), ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"), ("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hDtiClientNotLocked.setDescription('DTI Client Not Locked')
mibBuilder.exportSymbols("HARMONIC-INC-NSG9000-MIB", hTrapFields=hTrapFields, hQamChanneOverflowTrap=hQamChanneOverflowTrap, hPassThroughSourceFailure=hPassThroughSourceFailure, hPlatformR6ConnLossTrap=hPlatformR6ConnLossTrap, hTrapDestAddrStatus=hTrapDestAddrStatus, hGbePortOid=hGbePortOid, hPlatformFan4FailTrap=hPlatformFan4FailTrap, hRfPortHwFailTrap=hRfPortHwFailTrap, hServicePmtMissing=hServicePmtMissing, hRfModuleOid=hRfModuleOid, hOids=hOids, hMcECMNearingExpiration=hMcECMNearingExpiration, hPlatformFan3FailTrap=hPlatformFan3FailTrap, hPidRemuxSourceFailure=hPidRemuxSourceFailure, hPlatformPS1VoltageFailTrap=hPlatformPS1VoltageFailTrap, hRfPortOid=hRfPortOid, hTrapTimeLastGenerated=hTrapTimeLastGenerated, hTrapForwardTable=hTrapForwardTable, hPlatformVoltageFailTrap=hPlatformVoltageFailTrap, hGbePortLinkDownTrap=hGbePortLinkDownTrap, hAlarmStatus=hAlarmStatus, hPlatformPS2VoltageFailTrap=hPlatformPS2VoltageFailTrap, hObjects=hObjects, hPlatformFan1FailTrap=hPlatformFan1FailTrap, hDtiClientLinkDown=hDtiClientLinkDown, hPlatformFan2FailTrap=hPlatformFan2FailTrap, hSwitchToAlternateSource=hSwitchToAlternateSource, harmonicInc=harmonicInc, hModuleOids=hModuleOids, hRfModuleHwFailTrap=hRfModuleHwFailTrap, hSlotOid=hSlotOid, hPlatformTempFailTrap=hPlatformTempFailTrap, hTrapForwardEntry=hTrapForwardEntry, hTrapDestAddr=hTrapDestAddr, hAlarmSeverity=hAlarmSeverity, hPlatformD6ConnLossTrap=hPlatformD6ConnLossTrap, hRfPortTempFailTrap=hRfPortTempFailTrap, hSystemOid=hSystemOid, hTraps=hTraps, hPlatformOid=hPlatformOid, hDtiClientNotLocked=hDtiClientNotLocked, hQamChannelOid=hQamChannelOid, hRfModuleTempFailTrap=hRfModuleTempFailTrap, hMcECMMissing=hMcECMMissing, hServicePatMissing=hServicePatMissing, hDtiCardMissing=hDtiCardMissing, hMcECMExpired=hMcECMExpired, hSystem=hSystem, hAlarmDesc=hAlarmDesc)
