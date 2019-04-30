#
# PySNMP MIB module TIARA-NETWORKS-ENVIRONMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARA-NETWORKS-ENVIRONMENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:09:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Integer32, NotificationType, Gauge32, NotificationType, Counter64, Bits, TimeTicks, Unsigned32, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Integer32", "NotificationType", "Gauge32", "NotificationType", "Counter64", "Bits", "TimeTicks", "Unsigned32", "ObjectIdentity", "Counter32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
tiaraMgmt, = mibBuilder.importSymbols("TIARA-NETWORKS-SMI", "tiaraMgmt")
tiaraEnvironmentMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174, 2, 3))
tiaraEnvironmentMib.setRevisions(('1900-08-18 00:00',))
if mibBuilder.loadTexts: tiaraEnvironmentMib.setLastUpdated('0008180000Z')
if mibBuilder.loadTexts: tiaraEnvironmentMib.setOrganization('Tiara Networks, Inc.')
class EnvState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("normal", 1), ("warning", 2), ("critical", 3), ("fail", 4), ("turned-off", 5))

class EnvInstalled(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("not-installed", 1), ("installed", 2))

class EnvStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class EnvType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unknown", 1), ("minus48VDC", 2))

envObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1))
envNotificationEnables = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 3, 2))
envNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 3, 3))
envTempSensorTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 1), )
if mibBuilder.loadTexts: envTempSensorTable.setStatus('current')
envTempSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 1, 1), ).setIndexNames((0, "TIARA-NETWORKS-ENVIRONMENT-MIB", "envTempSensorUnitIndex"))
if mibBuilder.loadTexts: envTempSensorEntry.setStatus('current')
envTempSensorUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)))
if mibBuilder.loadTexts: envTempSensorUnitIndex.setStatus('current')
envTempSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envTempSensorValue.setStatus('current')
envTempSensorState = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 1, 1, 3), EnvState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envTempSensorState.setStatus('current')
envFanTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 2), )
if mibBuilder.loadTexts: envFanTable.setStatus('current')
envFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 2, 1), ).setIndexNames((0, "TIARA-NETWORKS-ENVIRONMENT-MIB", "envFanUnitIndex"))
if mibBuilder.loadTexts: envFanEntry.setStatus('current')
envFanUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)))
if mibBuilder.loadTexts: envFanUnitIndex.setStatus('current')
envFanState = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 2, 1, 2), EnvState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envFanState.setStatus('current')
envPwrsupPowerFailCount = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envPwrsupPowerFailCount.setStatus('current')
envPwrsupTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 4), )
if mibBuilder.loadTexts: envPwrsupTable.setStatus('current')
envPwrsupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 4, 1), ).setIndexNames((0, "TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupIndex"))
if mibBuilder.loadTexts: envPwrsupEntry.setStatus('current')
envPwrsupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: envPwrsupIndex.setStatus('current')
envPwrsupInstalled = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 4, 1, 2), EnvInstalled()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envPwrsupInstalled.setStatus('current')
envPwrsupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 4, 1, 3), EnvStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envPwrsupStatus.setStatus('current')
envPwrsupType = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 4, 1, 4), EnvType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envPwrsupType.setStatus('current')
envPwrsupUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envPwrsupUptime.setStatus('current')
envPwrsupDowntime = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envPwrsupDowntime.setStatus('current')
envEnableTemperatureNotification = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 3, 2, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: envEnableTemperatureNotification.setStatus('current')
envEnableFanNotification = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 3, 2, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: envEnableFanNotification.setStatus('current')
envEnablePowerNotification = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 3, 2, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: envEnablePowerNotification.setStatus('current')
envTemperatureNotification = NotificationType((1, 3, 6, 1, 4, 1, 3174, 2, 3, 3) + (0,1)).setObjects(("TIARA-NETWORKS-ENVIRONMENT-MIB", "envTempSensorUnitIndex"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envTempSensorValue"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envTempSensorState"))
envFanNotification = NotificationType((1, 3, 6, 1, 4, 1, 3174, 2, 3, 3) + (0,2)).setObjects(("TIARA-NETWORKS-ENVIRONMENT-MIB", "envFanUnitIndex"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envFanState"))
envPowerSupply1DownNotification = NotificationType((1, 3, 6, 1, 4, 1, 3174, 2, 3, 3) + (0,3)).setObjects(("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupPowerFailCount"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupIndex"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupInstalled"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupStatus"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupType"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupUptime"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupDowntime"))
envPowerSupply1UpNotification = NotificationType((1, 3, 6, 1, 4, 1, 3174, 2, 3, 3) + (0,4)).setObjects(("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupPowerFailCount"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupIndex"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupInstalled"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupStatus"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupType"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupUptime"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupDowntime"))
envPowerSupply2DownNotification = NotificationType((1, 3, 6, 1, 4, 1, 3174, 2, 3, 3) + (0,5)).setObjects(("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupPowerFailCount"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupIndex"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupInstalled"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupStatus"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupType"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupUptime"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupDowntime"))
envPowerSupply2UpNotification = NotificationType((1, 3, 6, 1, 4, 1, 3174, 2, 3, 3) + (0,6)).setObjects(("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupPowerFailCount"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupIndex"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupInstalled"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupStatus"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupType"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupUptime"), ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupDowntime"))
mibBuilder.exportSymbols("TIARA-NETWORKS-ENVIRONMENT-MIB", envFanEntry=envFanEntry, EnvState=EnvState, envPwrsupPowerFailCount=envPwrsupPowerFailCount, envPwrsupIndex=envPwrsupIndex, envTempSensorTable=envTempSensorTable, envObjects=envObjects, tiaraEnvironmentMib=tiaraEnvironmentMib, envPwrsupInstalled=envPwrsupInstalled, envPowerSupply1DownNotification=envPowerSupply1DownNotification, envPwrsupStatus=envPwrsupStatus, envEnablePowerNotification=envEnablePowerNotification, envFanUnitIndex=envFanUnitIndex, envPwrsupEntry=envPwrsupEntry, envTemperatureNotification=envTemperatureNotification, envPowerSupply2UpNotification=envPowerSupply2UpNotification, EnvInstalled=EnvInstalled, envPwrsupType=envPwrsupType, envPowerSupply1UpNotification=envPowerSupply1UpNotification, envTempSensorValue=envTempSensorValue, envFanState=envFanState, envEnableTemperatureNotification=envEnableTemperatureNotification, envEnableFanNotification=envEnableFanNotification, envPwrsupDowntime=envPwrsupDowntime, envNotifications=envNotifications, EnvType=EnvType, envPowerSupply2DownNotification=envPowerSupply2DownNotification, envFanTable=envFanTable, envTempSensorUnitIndex=envTempSensorUnitIndex, envTempSensorEntry=envTempSensorEntry, envNotificationEnables=envNotificationEnables, PYSNMP_MODULE_ID=tiaraEnvironmentMib, envFanNotification=envFanNotification, envTempSensorState=envTempSensorState, envPwrsupTable=envPwrsupTable, EnvStatus=EnvStatus, envPwrsupUptime=envPwrsupUptime)