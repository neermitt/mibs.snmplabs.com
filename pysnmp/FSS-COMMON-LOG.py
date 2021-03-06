#
# PySNMP MIB module FSS-COMMON-LOG (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FSS-COMMON-LOG
# Produced by pysmi-0.3.4 at Mon Apr 29 19:02:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
fssCommon, = mibBuilder.importSymbols("FSS-COMMON-SMI", "fssCommon")
FCCondEffect, FCCondType, FCTrapType, FCStdTypeIndex, FCStdObjectIndex, FCObjectName, FCTcCondType, FCSeverity, FCServEffect, FCTrapHistIndex, FCDirection, FCTimePeriod, FCTcaCondType, FCLocation = mibBuilder.importSymbols("FSS-COMMON-TC", "FCCondEffect", "FCCondType", "FCTrapType", "FCStdTypeIndex", "FCStdObjectIndex", "FCObjectName", "FCTcCondType", "FCSeverity", "FCServEffect", "FCTrapHistIndex", "FCDirection", "FCTimePeriod", "FCTcaCondType", "FCLocation")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, TimeTicks, Counter64, Bits, Integer32, ObjectIdentity, iso, Counter32, Unsigned32, NotificationType, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Counter64", "Bits", "Integer32", "ObjectIdentity", "iso", "Counter32", "Unsigned32", "NotificationType", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, DateAndTime, RowPointer, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "RowPointer", "TextualConvention")
fssLog = ModuleIdentity((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000))
if mibBuilder.loadTexts: fssLog.setLastUpdated('201601200000Z')
if mibBuilder.loadTexts: fssLog.setOrganization('Fujitsu Network Communications, Inc.')
fssBase = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 500))
fssAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200))
fssAlarmCurrent = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1))
fssAlarmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 100))
fssAlarmPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 100, 0))
fssTca = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300))
fssTcaTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 100))
fssTcaPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 100, 0))
fssTc = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 400))
fssTcTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 400, 100))
fssTcPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 400, 100, 0))
fssCondTrap = NotificationType((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 100, 0, 1)).setObjects(("FSS-COMMON-LOG", "fssTrapObjectName"), ("FSS-COMMON-LOG", "fssAlarmType"), ("FSS-COMMON-LOG", "fssAlarmCondEffect"), ("FSS-COMMON-LOG", "fssAlarmTypeQual"), ("FSS-COMMON-LOG", "fssTrapTimeStamp"), ("FSS-COMMON-LOG", "fssAlarmSeverity"), ("FSS-COMMON-LOG", "fssTrapDescription"), ("FSS-COMMON-LOG", "fssAlarmServiceEffect"))
if mibBuilder.loadTexts: fssCondTrap.setStatus('current')
fssCondQual = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 100, 100), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fssCondQual.setStatus('current')
fssTcaTrap = NotificationType((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 100, 0, 1)).setObjects(("FSS-COMMON-LOG", "fssTrapObjectName"), ("FSS-COMMON-LOG", "fssTcaType"), ("FSS-COMMON-LOG", "fssTcaTypeQual"), ("FSS-COMMON-LOG", "fssTrapTimeStamp"), ("FSS-COMMON-LOG", "fssTrapDescription"), ("FSS-COMMON-LOG", "fssTcaMonVal"), ("FSS-COMMON-LOG", "fssTcaThLev"))
if mibBuilder.loadTexts: fssTcaTrap.setStatus('current')
fssTcaCondQual = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 100, 100), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fssTcaCondQual.setStatus('current')
fssTcTrap = NotificationType((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 400, 100, 0, 1)).setObjects(("FSS-COMMON-LOG", "fssTrapObjectName"), ("FSS-COMMON-LOG", "fssTcType"), ("FSS-COMMON-LOG", "fssTcTypeQual"), ("FSS-COMMON-LOG", "fssTrapTimeStamp"), ("FSS-COMMON-LOG", "fssTrapDescription"))
if mibBuilder.loadTexts: fssTcTrap.setStatus('current')
fssTcCondQual = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 400, 100, 100), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fssTcCondQual.setStatus('current')
fssStandingAlarmXTable = MibTable((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1), )
if mibBuilder.loadTexts: fssStandingAlarmXTable.setStatus('current')
fssStandingAlarmXEntry = MibTableRow((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1, 1), ).setIndexNames((0, "FSS-COMMON-LOG", "fssStdAlarmObjectIndex"), (0, "FSS-COMMON-LOG", "fssStdAlarmTypeIndex"))
if mibBuilder.loadTexts: fssStandingAlarmXEntry.setStatus('current')
fssStdAlarmObjectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1, 1, 1), FCStdObjectIndex())
if mibBuilder.loadTexts: fssStdAlarmObjectIndex.setStatus('current')
fssStdAlarmTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1, 1, 2), FCStdTypeIndex())
if mibBuilder.loadTexts: fssStdAlarmTypeIndex.setStatus('current')
fssStdAlarmObjectName = MibTableColumn((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1, 1, 3), FCObjectName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssStdAlarmObjectName.setStatus('current')
fssStdAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1, 1, 4), FCCondType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssStdAlarmType.setStatus('current')
fssStdAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1, 1, 5), FCSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssStdAlarmSeverity.setStatus('current')
fssStdAlarmServEffect = MibTableColumn((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1, 1, 6), FCServEffect()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssStdAlarmServEffect.setStatus('current')
fssStdAlarmLocn = MibTableColumn((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1, 1, 7), FCLocation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssStdAlarmLocn.setStatus('current')
fssStdAlarmDir = MibTableColumn((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1, 1, 8), FCDirection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssStdAlarmDir.setStatus('current')
fssTrapObjectName = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 500, 1), FCObjectName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssTrapObjectName.setStatus('current')
fssTrapDescription = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 500, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssTrapDescription.setStatus('current')
fssTrapType = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 500, 3), FCTrapType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssTrapType.setStatus('current')
fssTrapTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 500, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssTrapTimeStamp.setStatus('current')
fssAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 3), FCCondType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssAlarmType.setStatus('current')
fssAlarmCondEffect = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 4), FCCondEffect()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssAlarmCondEffect.setStatus('current')
fssAlarmTypeQual = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssAlarmTypeQual.setStatus('current')
fssAlarmLocn = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 6), FCLocation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssAlarmLocn.setStatus('current')
fssAlarmDir = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 7), FCDirection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssAlarmDir.setStatus('current')
fssAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 8), FCSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssAlarmSeverity.setStatus('current')
fssAlarmServiceEffect = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 9), FCServEffect()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssAlarmServiceEffect.setStatus('current')
fssTcaType = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 1), FCTcaCondType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssTcaType.setStatus('current')
fssTcaTypeQual = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssTcaTypeQual.setStatus('current')
fssTcaCondEffect = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 3), FCCondEffect()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssTcaCondEffect.setStatus('current')
fssTcaLocn = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 4), FCLocation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssTcaLocn.setStatus('current')
fssTcaDir = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 5), FCDirection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssTcaDir.setStatus('current')
fssTcaMonVal = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssTcaMonVal.setStatus('current')
fssTcaThLev = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssTcaThLev.setStatus('current')
fssTcaTimePeriod = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 8), FCTimePeriod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssTcaTimePeriod.setStatus('current')
fssTcType = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 400, 1), FCTcCondType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssTcType.setStatus('current')
fssTcTypeQual = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 400, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fssTcTypeQual.setStatus('current')
fssLogConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100))
fssLogGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 1))
fssLogCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 2))
fssLogTrapCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 2, 1)).setObjects(("FSS-COMMON-LOG", "fssLogTrapGroup"), ("FSS-COMMON-LOG", "fssLogNotificationGroup"), ("FSS-COMMON-LOG", "fssLogTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fssLogTrapCompliance = fssLogTrapCompliance.setStatus('current')
fssLogTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 1, 1)).setObjects(("FSS-COMMON-LOG", "fssCondQual"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fssLogTrapGroup = fssLogTrapGroup.setStatus('current')
fssTcaLogTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 1, 2)).setObjects(("FSS-COMMON-LOG", "fssTcaCondQual"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fssTcaLogTrapGroup = fssTcaLogTrapGroup.setStatus('current')
fssLogNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 1, 100)).setObjects(("FSS-COMMON-LOG", "fssCondTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fssLogNotificationGroup = fssLogNotificationGroup.setStatus('current')
fssTcaLogNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 1, 101)).setObjects(("FSS-COMMON-LOG", "fssTcaTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fssTcaLogNotificationGroup = fssTcaLogNotificationGroup.setStatus('current')
fssTcLogNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 1, 102)).setObjects(("FSS-COMMON-LOG", "fssTcTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fssTcLogNotificationGroup = fssTcLogNotificationGroup.setStatus('current')
fssLogStandingCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 2, 3)).setObjects(("FSS-COMMON-LOG", "fssLogAlarmStandingGroup"), ("FSS-COMMON-LOG", "fssLogAlarmStandingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fssLogStandingCompliance = fssLogStandingCompliance.setStatus('current')
fssLogAlarmStandingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 1, 7)).setObjects(("FSS-COMMON-LOG", "fssStdAlarmType"), ("FSS-COMMON-LOG", "fssStdAlarmSeverity"), ("FSS-COMMON-LOG", "fssStdAlarmServEffect"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fssLogAlarmStandingGroup = fssLogAlarmStandingGroup.setStatus('current')
mibBuilder.exportSymbols("FSS-COMMON-LOG", fssTc=fssTc, fssTcType=fssTcType, fssCondTrap=fssCondTrap, fssTcLogNotificationGroup=fssTcLogNotificationGroup, fssAlarmType=fssAlarmType, fssAlarmCondEffect=fssAlarmCondEffect, fssAlarm=fssAlarm, PYSNMP_MODULE_ID=fssLog, fssLogNotificationGroup=fssLogNotificationGroup, fssAlarmPrefix=fssAlarmPrefix, fssAlarmTraps=fssAlarmTraps, fssTcaTraps=fssTcaTraps, fssTca=fssTca, fssTcPrefix=fssTcPrefix, fssStdAlarmTypeIndex=fssStdAlarmTypeIndex, fssLogConformance=fssLogConformance, fssAlarmSeverity=fssAlarmSeverity, fssStandingAlarmXTable=fssStandingAlarmXTable, fssTcCondQual=fssTcCondQual, fssAlarmLocn=fssAlarmLocn, fssStdAlarmLocn=fssStdAlarmLocn, fssTcaPrefix=fssTcaPrefix, fssTcaCondQual=fssTcaCondQual, fssTcaDir=fssTcaDir, fssStdAlarmType=fssStdAlarmType, fssTcTrap=fssTcTrap, fssTrapType=fssTrapType, fssLogTrapCompliance=fssLogTrapCompliance, fssTcaThLev=fssTcaThLev, fssTcaTimePeriod=fssTcaTimePeriod, fssCondQual=fssCondQual, fssStdAlarmObjectName=fssStdAlarmObjectName, fssLogCompliances=fssLogCompliances, fssStandingAlarmXEntry=fssStandingAlarmXEntry, fssTrapObjectName=fssTrapObjectName, fssLogStandingCompliance=fssLogStandingCompliance, fssLogTrapGroup=fssLogTrapGroup, fssTcTraps=fssTcTraps, fssLogAlarmStandingGroup=fssLogAlarmStandingGroup, fssTrapTimeStamp=fssTrapTimeStamp, fssStdAlarmSeverity=fssStdAlarmSeverity, fssAlarmDir=fssAlarmDir, fssTcaLogNotificationGroup=fssTcaLogNotificationGroup, fssTcaLogTrapGroup=fssTcaLogTrapGroup, fssBase=fssBase, fssStdAlarmObjectIndex=fssStdAlarmObjectIndex, fssStdAlarmServEffect=fssStdAlarmServEffect, fssLogGroups=fssLogGroups, fssTcaType=fssTcaType, fssTrapDescription=fssTrapDescription, fssTcaTypeQual=fssTcaTypeQual, fssTcaMonVal=fssTcaMonVal, fssAlarmTypeQual=fssAlarmTypeQual, fssTcaCondEffect=fssTcaCondEffect, fssAlarmCurrent=fssAlarmCurrent, fssStdAlarmDir=fssStdAlarmDir, fssAlarmServiceEffect=fssAlarmServiceEffect, fssTcaLocn=fssTcaLocn, fssTcTypeQual=fssTcTypeQual, fssLog=fssLog, fssTcaTrap=fssTcaTrap)
