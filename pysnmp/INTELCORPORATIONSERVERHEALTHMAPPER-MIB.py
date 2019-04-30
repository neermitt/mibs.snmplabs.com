#
# PySNMP MIB module INTELCORPORATIONSERVERHEALTHMAPPER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTELCORPORATIONSERVERHEALTHMAPPER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:44:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, IpAddress, Unsigned32, iso, MibIdentifier, Counter64, enterprises, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Integer32, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "Unsigned32", "iso", "MibIdentifier", "Counter64", "enterprises", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Integer32", "NotificationType", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DmiInteger(Integer32):
    pass

class DmiDisplaystring(DisplayString):
    pass

class DmiDateX(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(28, 28)
    fixedLength = 28

class DmiComponentIndex(Integer32):
    pass

intel = MibIdentifier((1, 3, 6, 1, 4, 1, 343))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2))
server_management = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 10)).setLabel("server-management")
dmtfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 10, 7))
tServerHealthContributionTable = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 12), )
if mibBuilder.loadTexts: tServerHealthContributionTable.setStatus('mandatory')
eServerHealthContributionTable = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 12, 1), ).setIndexNames((0, "INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "DmiComponentIndex"), (0, "INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a2ContributionTableIndex"))
if mibBuilder.loadTexts: eServerHealthContributionTable.setStatus('mandatory')
a2ContributionTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 12, 1, 1), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2ContributionTableIndex.setStatus('mandatory')
a2Component = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 12, 1, 2), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Component.setStatus('mandatory')
a2Group = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 12, 1, 3), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Group.setStatus('mandatory')
a2StatusStore = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("vLocal", 0), ("vOperationalState", 1), ("vErrorControl", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2StatusStore.setStatus('mandatory')
a2LocalIndexAttributeIdToStoreGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 12, 1, 5), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2LocalIndexAttributeIdToStoreGroup.setStatus('mandatory')
a2HealthAttributeId = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 12, 1, 6), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2HealthAttributeId.setStatus('mandatory')
a2Contribution = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 12, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("vFalse", 0), ("vTrue", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a2Contribution.setStatus('mandatory')
a2UpdateThroughPolling = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 12, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("vFalse", 0), ("vTrue", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a2UpdateThroughPolling.setStatus('mandatory')
tServerHealthFilterTable = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 13), )
if mibBuilder.loadTexts: tServerHealthFilterTable.setStatus('mandatory')
eServerHealthFilterTable = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 13, 1), ).setIndexNames((0, "INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "DmiComponentIndex"), (0, "INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a3FilterTableIndex"))
if mibBuilder.loadTexts: eServerHealthFilterTable.setStatus('mandatory')
a3FilterTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 13, 1, 1), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3FilterTableIndex.setStatus('mandatory')
a3Component = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 13, 1, 2), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3Component.setStatus('mandatory')
a3Group = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 13, 1, 3), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3Group.setStatus('mandatory')
tServerHealthStatus = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 14), )
if mibBuilder.loadTexts: tServerHealthStatus.setStatus('mandatory')
eServerHealthStatus = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 14, 1), ).setIndexNames((0, "INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "DmiComponentIndex"))
if mibBuilder.loadTexts: eServerHealthStatus.setStatus('mandatory')
a4Status = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 14, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("vOk", 4), ("vNon-critical", 8), ("vCritical", 16), ("vNon-recoverable", 32)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Status.setStatus('mandatory')
a4StatusInInteger = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 14, 1, 2), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4StatusInInteger.setStatus('mandatory')
a4PollInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 14, 1, 3), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a4PollInterval.setStatus('mandatory')
tEventGenerationForServerHealthStatus = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 100), )
if mibBuilder.loadTexts: tEventGenerationForServerHealthStatus.setStatus('mandatory')
eEventGenerationForServerHealthStatus = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 100, 1), ).setIndexNames((0, "INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "DmiComponentIndex"), (0, "INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5AssociatedGroup"))
if mibBuilder.loadTexts: eEventGenerationForServerHealthStatus.setStatus('mandatory')
a5EventType = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 100, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 8, 16, 32, 48, 64))).clone(namedValues=NamedValues(("vServerOk", 4), ("vServerNon-critical", 8), ("vServerCritical", 16), ("vServerNon-recoverable", 32), ("vServerHealthDetailChanged", 48), ("vServerHealthDetailRefresh", 64)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a5EventType.setStatus('mandatory')
a5EventSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 100, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32))).clone(namedValues=NamedValues(("vMonitor", 1), ("vInformation", 2), ("vOk", 4), ("vNon-critical", 8), ("vCritical", 16), ("vNon-recoverable", 32)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a5EventSeverity.setStatus('mandatory')
a5IsEventState_based = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 100, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("vFalse", 0), ("vTrue", 1)))).setLabel("a5IsEventState-based").setMaxAccess("readonly")
if mibBuilder.loadTexts: a5IsEventState_based.setStatus('mandatory')
a5EventStateKey = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 100, 1, 4), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a5EventStateKey.setStatus('mandatory')
a5AssociatedGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 100, 1, 5), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a5AssociatedGroup.setStatus('mandatory')
a5EventSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 100, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("vOther", 0), ("vUnknown", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a5EventSystem.setStatus('mandatory')
a5EventSubsystem = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 100, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("vOther", 0), ("vUnknown", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a5EventSubsystem.setStatus('mandatory')
a5IsInstanceDataPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 100, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("vFalse", 0), ("vTrue", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a5IsInstanceDataPresent.setStatus('mandatory')
a5EventMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 100, 1, 10), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a5EventMessage.setStatus('mandatory')
tServerHealthDetail = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 15), )
if mibBuilder.loadTexts: tServerHealthDetail.setStatus('mandatory')
eServerHealthDetail = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 15, 1), ).setIndexNames((0, "INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "DmiComponentIndex"), (0, "INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a6HealthInstanceIndex"))
if mibBuilder.loadTexts: eServerHealthDetail.setStatus('mandatory')
a6HealthInstanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 15, 1, 1), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a6HealthInstanceIndex.setStatus('mandatory')
a6Component = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 15, 1, 2), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a6Component.setStatus('mandatory')
a6Group = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 15, 1, 3), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a6Group.setStatus('mandatory')
a6InstancePath = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 15, 1, 4), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a6InstancePath.setStatus('mandatory')
a6LastEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 15, 1, 5), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a6LastEventType.setStatus('mandatory')
a6Status = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 15, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("vOk", 4), ("vNon-critical", 8), ("vCritical", 16), ("vNon-recoverable", 32)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a6Status.setStatus('mandatory')
tServerHealthStatusTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 14, 0))
notification1ForServerHealthStatus = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 14, 0, 4)).setObjects(("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventType"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventSeverity"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5IsEventState_based"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventStateKey"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5AssociatedGroup"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventSystem"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventSubsystem"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5IsInstanceDataPresent"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventMessage"))
if mibBuilder.loadTexts: notification1ForServerHealthStatus.setStatus('current')
notification2ForServerHealthStatus = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 14, 0, 8)).setObjects(("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventType"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventSeverity"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5IsEventState_based"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventStateKey"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5AssociatedGroup"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventSystem"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventSubsystem"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5IsInstanceDataPresent"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventMessage"))
if mibBuilder.loadTexts: notification2ForServerHealthStatus.setStatus('current')
notification3ForServerHealthStatus = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 14, 0, 16)).setObjects(("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventType"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventSeverity"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5IsEventState_based"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventStateKey"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5AssociatedGroup"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventSystem"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventSubsystem"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5IsInstanceDataPresent"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventMessage"))
if mibBuilder.loadTexts: notification3ForServerHealthStatus.setStatus('current')
notification4ForServerHealthStatus = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 14, 0, 32)).setObjects(("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventType"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventSeverity"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5IsEventState_based"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventStateKey"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5AssociatedGroup"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventSystem"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventSubsystem"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5IsInstanceDataPresent"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventMessage"))
if mibBuilder.loadTexts: notification4ForServerHealthStatus.setStatus('current')
notification5ForServerHealthStatus = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 14, 0, 48)).setObjects(("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventType"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventSeverity"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5IsEventState_based"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventStateKey"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5AssociatedGroup"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventSystem"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventSubsystem"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5IsInstanceDataPresent"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventMessage"))
if mibBuilder.loadTexts: notification5ForServerHealthStatus.setStatus('current')
notification6ForServerHealthStatus = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 10, 7, 14, 0, 64)).setObjects(("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventType"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventSeverity"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5IsEventState_based"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventStateKey"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5AssociatedGroup"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventSystem"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventSubsystem"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5IsInstanceDataPresent"), ("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", "a5EventMessage"))
if mibBuilder.loadTexts: notification6ForServerHealthStatus.setStatus('current')
mibBuilder.exportSymbols("INTELCORPORATIONSERVERHEALTHMAPPER-MIB", tEventGenerationForServerHealthStatus=tEventGenerationForServerHealthStatus, a5EventSeverity=a5EventSeverity, dmtfGroups=dmtfGroups, a5EventSystem=a5EventSystem, notification2ForServerHealthStatus=notification2ForServerHealthStatus, tServerHealthStatusTraps=tServerHealthStatusTraps, a2LocalIndexAttributeIdToStoreGroup=a2LocalIndexAttributeIdToStoreGroup, notification6ForServerHealthStatus=notification6ForServerHealthStatus, intel=intel, a2UpdateThroughPolling=a2UpdateThroughPolling, a6InstancePath=a6InstancePath, notification4ForServerHealthStatus=notification4ForServerHealthStatus, a2Component=a2Component, a2StatusStore=a2StatusStore, notification5ForServerHealthStatus=notification5ForServerHealthStatus, a4Status=a4Status, notification3ForServerHealthStatus=notification3ForServerHealthStatus, a6Group=a6Group, a2Group=a2Group, a5EventStateKey=a5EventStateKey, a2ContributionTableIndex=a2ContributionTableIndex, products=products, a4StatusInInteger=a4StatusInInteger, a5EventMessage=a5EventMessage, a6LastEventType=a6LastEventType, DmiInteger=DmiInteger, a5IsEventState_based=a5IsEventState_based, DmiDisplaystring=DmiDisplaystring, a6HealthInstanceIndex=a6HealthInstanceIndex, a2Contribution=a2Contribution, a3FilterTableIndex=a3FilterTableIndex, a3Group=a3Group, tServerHealthStatus=tServerHealthStatus, a5EventType=a5EventType, tServerHealthFilterTable=tServerHealthFilterTable, eEventGenerationForServerHealthStatus=eEventGenerationForServerHealthStatus, a4PollInterval=a4PollInterval, a6Component=a6Component, a6Status=a6Status, a2HealthAttributeId=a2HealthAttributeId, eServerHealthContributionTable=eServerHealthContributionTable, a5AssociatedGroup=a5AssociatedGroup, a5EventSubsystem=a5EventSubsystem, a3Component=a3Component, DmiComponentIndex=DmiComponentIndex, server_management=server_management, notification1ForServerHealthStatus=notification1ForServerHealthStatus, tServerHealthDetail=tServerHealthDetail, eServerHealthStatus=eServerHealthStatus, eServerHealthDetail=eServerHealthDetail, a5IsInstanceDataPresent=a5IsInstanceDataPresent, eServerHealthFilterTable=eServerHealthFilterTable, tServerHealthContributionTable=tServerHealthContributionTable, DmiDateX=DmiDateX)