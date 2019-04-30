#
# PySNMP MIB module ERI-DNX-T3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ERI-DNX-T3-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:51:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
dnx, DecisionType, FunctionSwitch, devices, LinkCmdStatus, LinkPortAddress, PortStatus, trapSequence = mibBuilder.importSymbols("ERI-DNX-SMC-MIB", "dnx", "DecisionType", "FunctionSwitch", "devices", "LinkCmdStatus", "LinkPortAddress", "PortStatus", "trapSequence")
eriMibs, = mibBuilder.importSymbols("ERI-ROOT-SMI", "eriMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, Counter64, IpAddress, ModuleIdentity, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, iso, NotificationType, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Counter64", "IpAddress", "ModuleIdentity", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "iso", "NotificationType", "MibIdentifier", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eriDNXT3MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 644, 3, 3))
eriDNXT3MIB.setRevisions(('2002-08-19 00:00', '2002-04-11 00:00', '2001-04-01 00:00', '2000-09-15 00:00', '2000-07-26 00:00',))
if mibBuilder.loadTexts: eriDNXT3MIB.setLastUpdated('200208190000Z')
if mibBuilder.loadTexts: eriDNXT3MIB.setOrganization('Eastern Research, Inc.')
dnxT3 = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1))
t3Config = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1))
t3Diag = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 2))
t3PortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1), )
if mibBuilder.loadTexts: t3PortConfigTable.setStatus('current')
t3PortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1), ).setIndexNames((0, "ERI-DNX-T3-MIB", "t3CfgAddr"))
if mibBuilder.loadTexts: t3PortConfigEntry.setStatus('current')
t3CfgAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t3CfgAddr.setStatus('current')
t3CfgResource = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t3CfgResource.setStatus('current')
t3CfgCircuitName = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3CfgCircuitName.setStatus('current')
t3FacilityId = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 37))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3FacilityId.setStatus('current')
t3EquipmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3EquipmentId.setStatus('current')
t3Location = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3Location.setStatus('current')
t3FrameId = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3FrameId.setStatus('current')
t3UnitName = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3UnitName.setStatus('current')
t3PortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 37))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3PortNumber.setStatus('current')
t3Generator = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 37))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3Generator.setStatus('current')
t3M13OpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("c-bit", 0), ("bellcoreM13", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3M13OpMode.setStatus('current')
t3RcvLoopTiming = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 12), FunctionSwitch()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3RcvLoopTiming.setStatus('current')
t3ShortCable = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 13), DecisionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3ShortCable.setStatus('current')
t3M13RemLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("third-cbit-inverted", 0), ("second-cbit-inverted", 1), ("first-cbit-inverted", 2), ("third-cbit-stuffbit-inverted", 4), ("second-cbit-stuffbit-inverted", 5), ("first-cbit-stuffbit-inverted", 6), ("stuffbit-inverted", 7), ("stuffbit-is-zero", 8), ("stuffbit-is-one", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3M13RemLoop.setStatus('current')
t3RcvAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("framed1010-Cbit0-noXbit", 0), ("framed1010-Cbit0-Xbit1", 1), ("framed1010-noCbit-noXbit", 2), ("framed1111-noCbit-noXbit", 3), ("unframed1010", 4), ("unframed-allones", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3RcvAIS.setStatus('current')
t3XmtAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("ansi", 0), ("framed-allones-Cbit1", 1), ("unframed1010", 2), ("unframed-allones", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3XmtAIS.setStatus('current')
t3CmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 17), LinkCmdStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3CmdStatus.setStatus('current')
t3T1LinkConfigTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2), )
if mibBuilder.loadTexts: t3T1LinkConfigTable.setStatus('current')
t3T1LinkConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1), ).setIndexNames((0, "ERI-DNX-T3-MIB", "t3T1CfgLinkAddr"))
if mibBuilder.loadTexts: t3T1LinkConfigEntry.setStatus('current')
t3T1CfgLinkAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t3T1CfgLinkAddr.setStatus('current')
t3T1CfgResource = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t3T1CfgResource.setStatus('current')
t3T1CfgLinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1CfgLinkName.setStatus('current')
t3T1Status = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 4), PortStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1Status.setStatus('current')
t3T1Framing = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3))).clone(namedValues=NamedValues(("d4", 1), ("esf", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1Framing.setStatus('current')
t3T1Density = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("clear", 0), ("att-62411", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1Density.setStatus('current')
t3T1NetLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 7), FunctionSwitch()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1NetLoop.setStatus('current')
t3T1YelAlrm = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 8), DecisionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1YelAlrm.setStatus('current')
t3T1RecoverTime = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 10, 15))).clone(namedValues=NamedValues(("timeout-3-secs", 3), ("timeout-10-secs", 10), ("timeout-15-secs", 15)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1RecoverTime.setStatus('current')
t3T1EsfFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("att-54016", 0), ("ansi-t1-403", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1EsfFormat.setStatus('current')
t3T1IdleCode = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("busy", 0), ("idle", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1IdleCode.setStatus('current')
t3T1CfgCmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 12), LinkCmdStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1CfgCmdStatus.setStatus('current')
dnxT3Enterprise = ObjectIdentity((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 0))
if mibBuilder.loadTexts: dnxT3Enterprise.setStatus('current')
t3PortConfigTrap = NotificationType((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 0, 1)).setObjects(("ERI-DNX-SMC-MIB", "trapSequence"), ("ERI-DNX-T3-MIB", "t3CfgAddr"), ("ERI-DNX-T3-MIB", "t3CmdStatus"))
if mibBuilder.loadTexts: t3PortConfigTrap.setStatus('current')
t3T1ConfigTrap = NotificationType((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 0, 2)).setObjects(("ERI-DNX-SMC-MIB", "trapSequence"), ("ERI-DNX-T3-MIB", "t3T1CfgLinkAddr"), ("ERI-DNX-T3-MIB", "t3T1CfgCmdStatus"))
if mibBuilder.loadTexts: t3T1ConfigTrap.setStatus('current')
mibBuilder.exportSymbols("ERI-DNX-T3-MIB", t3PortNumber=t3PortNumber, t3Generator=t3Generator, t3UnitName=t3UnitName, t3T1ConfigTrap=t3T1ConfigTrap, t3CmdStatus=t3CmdStatus, t3T1YelAlrm=t3T1YelAlrm, t3T1NetLoop=t3T1NetLoop, t3Location=t3Location, t3CfgAddr=t3CfgAddr, t3FrameId=t3FrameId, t3M13RemLoop=t3M13RemLoop, t3RcvAIS=t3RcvAIS, t3T1LinkConfigTable=t3T1LinkConfigTable, t3Config=t3Config, eriDNXT3MIB=eriDNXT3MIB, t3FacilityId=t3FacilityId, t3ShortCable=t3ShortCable, t3M13OpMode=t3M13OpMode, t3T1Status=t3T1Status, t3T1Framing=t3T1Framing, t3T1LinkConfigEntry=t3T1LinkConfigEntry, t3CfgCircuitName=t3CfgCircuitName, dnxT3=dnxT3, t3T1CfgResource=t3T1CfgResource, t3T1RecoverTime=t3T1RecoverTime, t3PortConfigEntry=t3PortConfigEntry, t3RcvLoopTiming=t3RcvLoopTiming, t3T1EsfFormat=t3T1EsfFormat, t3T1Density=t3T1Density, t3T1CfgCmdStatus=t3T1CfgCmdStatus, t3XmtAIS=t3XmtAIS, t3T1CfgLinkName=t3T1CfgLinkName, PYSNMP_MODULE_ID=eriDNXT3MIB, t3T1CfgLinkAddr=t3T1CfgLinkAddr, dnxT3Enterprise=dnxT3Enterprise, t3PortConfigTable=t3PortConfigTable, t3T1IdleCode=t3T1IdleCode, t3CfgResource=t3CfgResource, t3PortConfigTrap=t3PortConfigTrap, t3EquipmentId=t3EquipmentId, t3Diag=t3Diag)