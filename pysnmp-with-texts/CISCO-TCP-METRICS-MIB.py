#
# PySNMP MIB module CISCO-TCP-METRICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TCP-METRICS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:14:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
cfmFlowId, cfmFlowMetricsIntNumber, cfmFlowMonitorId = mibBuilder.importSymbols("CISCO-FLOW-MONITOR-MIB", "cfmFlowId", "cfmFlowMetricsIntNumber", "cfmFlowMonitorId")
FlowMetricValue, FlowMetricPrecision, FlowMetricScale = mibBuilder.importSymbols("CISCO-FLOW-MONITOR-TC-MIB", "FlowMetricValue", "FlowMetricPrecision", "FlowMetricScale")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Counter32, Counter64, IpAddress, Unsigned32, ModuleIdentity, Integer32, Gauge32, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Counter32", "Counter64", "IpAddress", "Unsigned32", "ModuleIdentity", "Integer32", "Gauge32", "MibIdentifier", "NotificationType")
DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TextualConvention")
ciscoTcpMetricsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 770))
ciscoTcpMetricsMIB.setRevisions(('2011-03-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTcpMetricsMIB.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTcpMetricsMIB.setLastUpdated('201103060000Z')
if mibBuilder.loadTexts: ciscoTcpMetricsMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTcpMetricsMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTcpMetricsMIB.setDescription('This MIB module defines objects that describe the quality metrics of TCP streams. GLOSSARY ============ Flow Monitor - a hardware or software entity that classifies traffic flows, collects flow data, and periodically computes flow metrics. Flow Metric - a measurement that reflects the quality of a traffic flow. Measurement Interval - the length of time over which a flow monitor collects data related to a traffic flow, after which the flow monitor computes flow metrics using the collected data. Traffic Flow - a unidirectional stream of packets conforming to a classifier. For example, packets having a particular source IP address, destination IP address, protocol type, source port number, and destination port number. Traffic Flow Stream - when the monitor identifies multiple individual traffic flows based on the flow classificiation, the monitor aggregates the flows and represents them as a single entry in the cfmFlowTable. The individual traffic flows contributing to the metrics are called as individual traffic flow stream. The metrics for the traffic flow with multiple streams contributing, are determined either by aggregating metrics of all individual streams, for example, cumulative bit rate is computed by cumulative bits of all streams divided by total duration, or by selecting the metric for one of the individual stream, for example, maximum bit rate of an individual stream.')
ciscoTcpMetricsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 770, 0))
ciscoTcpMetricsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 770, 1))
ciscoTcpMetricsMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 770, 2))
ciscoTcpMetricsMIBIds = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 770, 3))
ciscoTcpMetricsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 770, 2, 1))
cfmTcpMetrics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1))
cfmTcpMetricsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 1), )
if mibBuilder.loadTexts: cfmTcpMetricsTable.setStatus('current')
if mibBuilder.loadTexts: cfmTcpMetricsTable.setDescription("This table contains aggregate data maintained by a flow monitor for traffic flows for which it is computing TCP metrics. This table has an sparse dependent relationship on the cfmFlowMetricsTable (defined by the CISCO-FLOW-MONITOR-MIB), containing a row for each row in the cfmFlowMetricsTable having a corresponding instance of cfmFlowMetricsCollected with the 'tcp' bit set to one.")
cfmTcpMetricsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"), (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"))
if mibBuilder.loadTexts: cfmTcpMetricsEntry.setStatus('current')
if mibBuilder.loadTexts: cfmTcpMetricsEntry.setDescription('An entry describes cumulative and aggregate TCP metrics for a single traffic flow. The devices creates a row in the cfmTcpMetricsTable when a flow monitor starts monitoring a traffic flow and has been configured to compute TCP metrics for the same traffic flow. Likewise, the device destroys a row in the cfmTcpMetricsTable when the corresponding flow monitor has ceased monitoring the traffic flow (e.g., when a traffic flow has timed out).')
cfmTcpMetricsValid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 1, 1, 1), Bits().clone(namedValues=NamedValues(("roundTripTime", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmTcpMetricsValid.setStatus('current')
if mibBuilder.loadTexts: cfmTcpMetricsValid.setDescription("This object indicates which metrics are valid for the traffic flow: 'roundTripTime' If this bit is set to '1', then the corresponding instances of cfmTcpMetricsRoundTripTimeScale, cfmTcpMetricsRoundTripTimePrecision, and cfmTcpMetricsRoundTripTime are valid.")
cfmTcpMetricsRoundTripTimeScale = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 1, 1, 2), FlowMetricScale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmTcpMetricsRoundTripTimeScale.setStatus('current')
if mibBuilder.loadTexts: cfmTcpMetricsRoundTripTimeScale.setDescription('This object indicates the scaling factor for the corresponding instance of cfmTcpMetricsRoundTripTime.')
cfmTcpMetricsRoundTripTimePrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 1, 1, 3), FlowMetricPrecision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmTcpMetricsRoundTripTimePrecision.setStatus('current')
if mibBuilder.loadTexts: cfmTcpMetricsRoundTripTimePrecision.setDescription('This object indicates the precision for the corresponding instance of cfmFlowMetricsRoundTripTime.')
cfmTcpMetricsRoundTripTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 1, 1, 4), FlowMetricValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmTcpMetricsRoundTripTime.setStatus('current')
if mibBuilder.loadTexts: cfmTcpMetricsRoundTripTime.setDescription('This object indicates the round trip time for the packet observed by the flow monitor for the corresponding flow. The round trip time is defined as the length of time it takes for a TCP segment transmission and receipt of acknowledgement.')
cfmTcpMetricsTableChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmTcpMetricsTableChanged.setStatus('current')
if mibBuilder.loadTexts: cfmTcpMetricsTableChanged.setDescription('This object indicates the value of sysUpTime the last time the device created/destroyed a row in the cfmTcpMetricsTable.')
cfmTcpMetricsIntTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 3), )
if mibBuilder.loadTexts: cfmTcpMetricsIntTable.setStatus('current')
if mibBuilder.loadTexts: cfmTcpMetricsIntTable.setDescription("This table contains historic TCP metrics for the traffic flows monitored by each of the flow monitors supported by the device. This table has an sparse dependent relationship on the cfmFlowMetricsIntTable (defined by the CISCO-FLOW-MONITOR-MIB), containing a row for each row in the cfmFlowMetricsIntTable having a corresponding instance of cfmFlowMetricsCollected with the 'tcp' bit set to one.")
cfmTcpMetricsIntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"), (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"), (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntNumber"))
if mibBuilder.loadTexts: cfmTcpMetricsIntEntry.setStatus('current')
if mibBuilder.loadTexts: cfmTcpMetricsIntEntry.setDescription('An entry describes TCP metrics collected for a previous measurement interval for a corresponding traffic flow.')
cfmTcpMetricsIntValid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 3, 1, 1), Bits().clone(namedValues=NamedValues(("roundTripTime", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmTcpMetricsIntValid.setStatus('current')
if mibBuilder.loadTexts: cfmTcpMetricsIntValid.setDescription("This object indicates which metrics are valid for the measurement interval: 'roundTripTime' If this bit is set to '1', then the corresponding instances of cfmTcpMetricsIntRoundTripTimeScale, cfmTcpMetricsIntRoundTripTimePrecision, and cfmTcpMetricsIntRoundTripTime are valid.")
cfmTcpMetricsIntRoundTripTimeScale = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 3, 1, 2), FlowMetricScale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmTcpMetricsIntRoundTripTimeScale.setStatus('current')
if mibBuilder.loadTexts: cfmTcpMetricsIntRoundTripTimeScale.setDescription('This object indicates the scaling factor for the corresponding instance of cfmTcpMetricsIntRoundTripTime.')
cfmTcpMetricsIntRoundTripTimePrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 3, 1, 3), FlowMetricPrecision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmTcpMetricsIntRoundTripTimePrecision.setStatus('current')
if mibBuilder.loadTexts: cfmTcpMetricsIntRoundTripTimePrecision.setDescription('This object indicates the precision for the corresponding instance of cfmFlowMetricsIntRoundTripTime.')
cfmTcpMetricsIntRoundTripTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 3, 1, 4), FlowMetricValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmTcpMetricsIntRoundTripTime.setStatus('current')
if mibBuilder.loadTexts: cfmTcpMetricsIntRoundTripTime.setDescription('This object indicates the round trip time for traffic flow during the measurement interval.')
ciscoTcpMetricsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 770, 2, 2))
ciscoTcpMetricsMIBCompliance01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 770, 2, 1, 1)).setObjects(("CISCO-TCP-METRICS-MIB", "ciscoTcpMetricsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpMetricsMIBCompliance01 = ciscoTcpMetricsMIBCompliance01.setStatus('current')
if mibBuilder.loadTexts: ciscoTcpMetricsMIBCompliance01.setDescription('This compliance statement specifies the minimal requirements an implementation must meet in order to claim full compliance with the definition of the CISCO-TCP-METRICS-MIB.')
ciscoTcpMetricsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 770, 2, 2, 1)).setObjects(("CISCO-TCP-METRICS-MIB", "cfmTcpMetricsValid"), ("CISCO-TCP-METRICS-MIB", "cfmTcpMetricsRoundTripTimeScale"), ("CISCO-TCP-METRICS-MIB", "cfmTcpMetricsRoundTripTimePrecision"), ("CISCO-TCP-METRICS-MIB", "cfmTcpMetricsRoundTripTime"), ("CISCO-TCP-METRICS-MIB", "cfmTcpMetricsTableChanged"), ("CISCO-TCP-METRICS-MIB", "cfmTcpMetricsIntValid"), ("CISCO-TCP-METRICS-MIB", "cfmTcpMetricsIntRoundTripTimeScale"), ("CISCO-TCP-METRICS-MIB", "cfmTcpMetricsIntRoundTripTimePrecision"), ("CISCO-TCP-METRICS-MIB", "cfmTcpMetricsIntRoundTripTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpMetricsGroup = ciscoTcpMetricsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoTcpMetricsGroup.setDescription('This group contains objects that describe TCP metrics.')
mibBuilder.exportSymbols("CISCO-TCP-METRICS-MIB", ciscoTcpMetricsMIBIds=ciscoTcpMetricsMIBIds, ciscoTcpMetricsMIBCompliances=ciscoTcpMetricsMIBCompliances, cfmTcpMetricsIntTable=cfmTcpMetricsIntTable, cfmTcpMetricsIntRoundTripTimeScale=cfmTcpMetricsIntRoundTripTimeScale, cfmTcpMetricsIntValid=cfmTcpMetricsIntValid, ciscoTcpMetricsMIBGroups=ciscoTcpMetricsMIBGroups, cfmTcpMetricsIntEntry=cfmTcpMetricsIntEntry, cfmTcpMetricsIntRoundTripTime=cfmTcpMetricsIntRoundTripTime, cfmTcpMetricsTable=cfmTcpMetricsTable, cfmTcpMetrics=cfmTcpMetrics, cfmTcpMetricsRoundTripTimeScale=cfmTcpMetricsRoundTripTimeScale, ciscoTcpMetricsMIB=ciscoTcpMetricsMIB, ciscoTcpMetricsMIBCompliance01=ciscoTcpMetricsMIBCompliance01, ciscoTcpMetricsMIBConform=ciscoTcpMetricsMIBConform, cfmTcpMetricsTableChanged=cfmTcpMetricsTableChanged, cfmTcpMetricsRoundTripTime=cfmTcpMetricsRoundTripTime, ciscoTcpMetricsGroup=ciscoTcpMetricsGroup, ciscoTcpMetricsMIBNotifs=ciscoTcpMetricsMIBNotifs, cfmTcpMetricsIntRoundTripTimePrecision=cfmTcpMetricsIntRoundTripTimePrecision, ciscoTcpMetricsMIBObjects=ciscoTcpMetricsMIBObjects, cfmTcpMetricsEntry=cfmTcpMetricsEntry, cfmTcpMetricsRoundTripTimePrecision=cfmTcpMetricsRoundTripTimePrecision, PYSNMP_MODULE_ID=ciscoTcpMetricsMIB, cfmTcpMetricsValid=cfmTcpMetricsValid)