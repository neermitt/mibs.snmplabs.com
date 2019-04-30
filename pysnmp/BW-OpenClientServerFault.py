#
# PySNMP MIB module BW-OpenClientServerFault (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BW-OpenClientServerFault
# Produced by pysmi-0.3.4 at Mon Apr 29 17:25:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
alarmName, problemText, identifier, recommendedActionsText, faultFields, component, timeStamp, severity, alarmState, common, systemName, subcomponent = mibBuilder.importSymbols("BroadworksFault", "alarmName", "problemText", "identifier", "recommendedActionsText", "faultFields", "component", "timeStamp", "severity", "alarmState", "common", "systemName", "subcomponent")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, MibIdentifier, Unsigned32, Counter64, TimeTicks, ObjectIdentity, Integer32, Gauge32, NotificationType, iso, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "MibIdentifier", "Unsigned32", "Counter64", "TimeTicks", "ObjectIdentity", "Integer32", "Gauge32", "NotificationType", "iso", "Counter32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
systemFaults = ModuleIdentity((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1))
systemFaults.setRevisions(('2000-09-19 14:31',))
if mibBuilder.loadTexts: systemFaults.setLastUpdated('200201220000Z')
if mibBuilder.loadTexts: systemFaults.setOrganization('Broadsoft, Inc')
bwPMOpenClientServerLaunched = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 501)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMOpenClientServerLaunched.setStatus('current')
bwPMOpenClientServerShutDown = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 502)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMOpenClientServerShutDown.setStatus('current')
bwPMOpenClientServerRestarted = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 503)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMOpenClientServerRestarted.setStatus('current')
bwPMOpenClientServerDeath = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 504)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMOpenClientServerDeath.setStatus('current')
bwPMOpenClientServerStartupFailed = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 505)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMOpenClientServerStartupFailed.setStatus('current')
bwOpenClientServerNSConnFailed = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 506)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwOpenClientServerNSConnFailed.setStatus('current')
bwOpenClientServerASConnFailed = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 507)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwOpenClientServerASConnFailed.setStatus('current')
bwOpenClientServerClientConnTerminated = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 508)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwOpenClientServerClientConnTerminated.setStatus('current')
bwOpenClientServerASConnTerminated = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 509)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwOpenClientServerASConnTerminated.setStatus('current')
bwOpenClientServerNSConnTerminated = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 510)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwOpenClientServerNSConnTerminated.setStatus('current')
bwOpenClientServerExtAuthConnFailedRaise = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 511)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwOpenClientServerExtAuthConnFailedRaise.setStatus('current')
bwOpenClientServerExtAuthConnFailedClear = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 512)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwOpenClientServerExtAuthConnFailedClear.setStatus('current')
bwOpenClientServerExtAuthProcessingFailedRaise = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 513)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwOpenClientServerExtAuthProcessingFailedRaise.setStatus('current')
bwOpenClientServerExtAuthProcessingFailedClear = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 514)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwOpenClientServerExtAuthProcessingFailedClear.setStatus('current')
bwOpenClientServerUserIdForceLoggedOut = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 515)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwOpenClientServerUserIdForceLoggedOut.setStatus('current')
mibBuilder.exportSymbols("BW-OpenClientServerFault", bwPMOpenClientServerStartupFailed=bwPMOpenClientServerStartupFailed, bwOpenClientServerUserIdForceLoggedOut=bwOpenClientServerUserIdForceLoggedOut, bwOpenClientServerExtAuthConnFailedClear=bwOpenClientServerExtAuthConnFailedClear, bwPMOpenClientServerShutDown=bwPMOpenClientServerShutDown, systemFaults=systemFaults, bwOpenClientServerNSConnFailed=bwOpenClientServerNSConnFailed, bwOpenClientServerExtAuthProcessingFailedRaise=bwOpenClientServerExtAuthProcessingFailedRaise, bwPMOpenClientServerDeath=bwPMOpenClientServerDeath, bwPMOpenClientServerRestarted=bwPMOpenClientServerRestarted, bwPMOpenClientServerLaunched=bwPMOpenClientServerLaunched, bwOpenClientServerASConnFailed=bwOpenClientServerASConnFailed, bwOpenClientServerASConnTerminated=bwOpenClientServerASConnTerminated, bwOpenClientServerNSConnTerminated=bwOpenClientServerNSConnTerminated, bwOpenClientServerExtAuthConnFailedRaise=bwOpenClientServerExtAuthConnFailedRaise, bwOpenClientServerExtAuthProcessingFailedClear=bwOpenClientServerExtAuthProcessingFailedClear, bwOpenClientServerClientConnTerminated=bwOpenClientServerClientConnTerminated, PYSNMP_MODULE_ID=systemFaults)