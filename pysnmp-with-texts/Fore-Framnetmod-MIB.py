#
# PySNMP MIB module Fore-Framnetmod-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-Framnetmod-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:17:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
frCircuitDlci, = mibBuilder.importSymbols("FRAME-RELAY-DTE-MIB", "frCircuitDlci")
frameInternetworking, atmSwitch = mibBuilder.importSymbols("Fore-Common-MIB", "frameInternetworking", "atmSwitch")
funiConnFuniVci, funiConnFuniVpi = mibBuilder.importSymbols("Fore-Funi-MIB", "funiConnFuniVci", "funiConnFuniVpi")
ifConvertToIfIndexChannelId, ifConvertToIfIndexPortId = mibBuilder.importSymbols("Fore-Ifcreate-MIB", "ifConvertToIfIndexChannelId", "ifConvertToIfIndexPortId")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, Counter64, iso, NotificationType, ObjectIdentity, TimeTicks, IpAddress, Unsigned32, Bits, MibIdentifier, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "Counter64", "iso", "NotificationType", "ObjectIdentity", "TimeTicks", "IpAddress", "Unsigned32", "Bits", "MibIdentifier", "ModuleIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fram = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 1, 16, 3))
if mibBuilder.loadTexts: fram.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: fram.setOrganization('FORE')
if mibBuilder.loadTexts: fram.setContactInfo(' Postal: FORE Systems Inc. 1000 FORE Drive Warrendale, PA 15086-7502 Tel: +1 724 742 6900 Email: nm_mibs@fore.com Web: http://www.fore.com')
if mibBuilder.loadTexts: fram.setDescription(' This is the FRAM netmod proprietory MIB. Currently, this mib defines one table: nmFramNetmodConfTable This table contains configuration information for FRAM netmod.')
nmFramNetmodConfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1), )
if mibBuilder.loadTexts: nmFramNetmodConfTable.setStatus('current')
if mibBuilder.loadTexts: nmFramNetmodConfTable.setDescription('This table has the objects for configuration of a FRAM netmod. Creation of an entry for this table is triggered by setting moduleState to inService. moduleState is one of the objects of moduleTable defined in fore-switch.mib')
nmFramNetmodConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1), ).setIndexNames((0, "Fore-Framnetmod-MIB", "nmFramBoard"), (0, "Fore-Framnetmod-MIB", "nmFramModule"))
if mibBuilder.loadTexts: nmFramNetmodConfEntry.setStatus('current')
if mibBuilder.loadTexts: nmFramNetmodConfEntry.setDescription('A table entry containing FRAM netmod specific config information')
nmFramBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmFramBoard.setStatus('current')
if mibBuilder.loadTexts: nmFramBoard.setDescription(' the index of this board within the ATM switch, equivalent to moduleBoard of moduleTable defined in fore-switch.mib')
nmFramModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmFramModule.setStatus('current')
if mibBuilder.loadTexts: nmFramModule.setDescription(' the number of this network module within the ATM switch board, equivalent to moduleNumber of moduleTable defined in fore-switch.mib')
nmFramEpdPpdBufferProportion = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("highzero", 1), ("high1quarter", 2), ("high2quarter", 3), ("high3quarter", 4))).clone('high2quarter')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmFramEpdPpdBufferProportion.setStatus('current')
if mibBuilder.loadTexts: nmFramEpdPpdBufferProportion.setDescription('Configuration of the buffer size configuration for the high and low priority cell. The sum of high and low priority buffers capacity is fixed, i.e., highzero selection means low priority buffer size being the maximum which is 32768 cells capacity. 4 possible way of partitioning the buffer: ________________________________ | High Priority | Low Priority | |_______________________________| | 0 cells | 32768 cells | |_______________________________| | 8192 cells | 24576 cells | |_______________________________| | 16384 cells | 16384 cells | |_______________________________| | 24576 cells | 8192 cells | |_______________________________| ')
nmFramEpdclp1HighPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(25, 25), ValueRangeConstraint(37, 37), ValueRangeConstraint(50, 50), ValueRangeConstraint(62, 62), )).clone(25)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmFramEpdclp1HighPrio.setStatus('current')
if mibBuilder.loadTexts: nmFramEpdclp1HighPrio.setDescription('The threshold for the high priority buffer for EPD and CLP=1 in percentage of the available size')
nmFramEpdclp0HighPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(50, 50), ValueRangeConstraint(62, 62), ValueRangeConstraint(75, 75), ValueRangeConstraint(87, 87), )).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmFramEpdclp0HighPrio.setStatus('current')
if mibBuilder.loadTexts: nmFramEpdclp0HighPrio.setDescription('The threshold for the high priority buffer for EPD and CLP=0 in percentage of the available size')
nmFramPpdclp1HighPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(50, 50), ValueRangeConstraint(62, 62), ValueRangeConstraint(75, 75), ValueRangeConstraint(87, 87), )).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmFramPpdclp1HighPrio.setStatus('current')
if mibBuilder.loadTexts: nmFramPpdclp1HighPrio.setDescription('The threshold for the high priority buffer for PPD and CLP=1, in percentage of the available size')
nmFramEpdclp1LowPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(25, 25), ValueRangeConstraint(37, 37), ValueRangeConstraint(50, 50), ValueRangeConstraint(62, 62), )).clone(25)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmFramEpdclp1LowPrio.setStatus('current')
if mibBuilder.loadTexts: nmFramEpdclp1LowPrio.setDescription('The threshold for the Low priority buffer for EPD and CLP=1 in percentage of the available size')
nmFramEpdclp0LowPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(50, 50), ValueRangeConstraint(62, 62), ValueRangeConstraint(75, 75), ValueRangeConstraint(87, 87), )).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmFramEpdclp0LowPrio.setStatus('current')
if mibBuilder.loadTexts: nmFramEpdclp0LowPrio.setDescription('The threshold for the Low priority buffer for EPD and CLP=0 in percentage of the available size')
nmFramPpdclp1LowPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(50, 50), ValueRangeConstraint(62, 62), ValueRangeConstraint(75, 75), ValueRangeConstraint(87, 87), )).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmFramPpdclp1LowPrio.setStatus('current')
if mibBuilder.loadTexts: nmFramPpdclp1LowPrio.setDescription('The threshold for the Low priority buffer for ppd and CLP=1 in percentage of the available size')
nmFramOamF5Supervision = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmFramOamF5Supervision.setStatus('current')
if mibBuilder.loadTexts: nmFramOamF5Supervision.setDescription(' enable/disable the FR/ATM interworking OAM F5 function on FRAM netmod')
nmFramOamF5AISRxPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmFramOamF5AISRxPeriod.setStatus('current')
if mibBuilder.loadTexts: nmFramOamF5AISRxPeriod.setDescription('Time interval at which an AIS OAM cells is to be received, value is a measurement in seconds')
nmFramOamF5AISTxPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmFramOamF5AISTxPeriod.setStatus('current')
if mibBuilder.loadTexts: nmFramOamF5AISTxPeriod.setDescription('Time interval at which an AIS OAM cells is to be transmitted, value is a measurement in seconds')
nmFramOamF5RDIRxPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmFramOamF5RDIRxPeriod.setStatus('current')
if mibBuilder.loadTexts: nmFramOamF5RDIRxPeriod.setDescription('Time interval at which an RDI OAM cells is to be received, value is a measurement in seconds')
nmFramOamF5RDITxPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmFramOamF5RDITxPeriod.setStatus('current')
if mibBuilder.loadTexts: nmFramOamF5RDITxPeriod.setDescription('Time interval at which an RDI OAM cells is to be transmitted, value is a measurement in seconds')
nmFramOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("justinserted", 1), ("releasedreset", 2), ("waitmsgstartup", 3), ("waittestend", 4), ("waitapplstartup", 5), ("selftest", 6), ("startupfailed", 7), ("pulledout", 8), ("bootconsole", 9), ("appluprunning", 10), ("down", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmFramOperState.setStatus('deprecated')
if mibBuilder.loadTexts: nmFramOperState.setDescription('This is the operational state corresponding to the FRAM netmod startup state machine.')
nmFramApplSwRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmFramApplSwRelease.setStatus('deprecated')
if mibBuilder.loadTexts: nmFramApplSwRelease.setDescription('The Embedded Software Version number running on this netmod')
nmFramBootSwRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmFramBootSwRelease.setStatus('deprecated')
if mibBuilder.loadTexts: nmFramBootSwRelease.setDescription('The Boot Software Version number running on this netmod')
nmFramApplKey = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 18), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmFramApplKey.setStatus('deprecated')
if mibBuilder.loadTexts: nmFramApplKey.setDescription("This object is for the purpose of setting up the Application type for the FRAM netmod. The application key should be specified when the application type is `unconfigured' or whenever the user want to reconfigure the netmod to run a different type of application. Changing the application type will cause the netmod to be reset and old configuration lost. Note this object is write-only and reading it will result in implementation-specific results.")
nmFramApplication = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("frAtmServiceAppl", 1), ("frAtmNetworkAppl", 2), ("framFuniAppl", 3))).clone('frAtmServiceAppl')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmFramApplication.setStatus('current')
if mibBuilder.loadTexts: nmFramApplication.setDescription('This object is for the purpose of setting up the Application type for the FRAM netmod. Changing the application type will cause the netmod to be reset and old configuration lost.')
nmFramOosLED = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3))).clone(namedValues=NamedValues(("off", 1), ("red", 3))).clone('off')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmFramOosLED.setStatus('deprecated')
if mibBuilder.loadTexts: nmFramOosLED.setDescription('Indicates the netmod service status. This LED is normally dark. When it becomes red, the netmod is Out Of Service (OOS) and can be removed. FRAM netmod can be set to OOS by user which means the netmod will stop passing data when the user set this LED to red(3). See the definition of moduleState object of moduleTable in fore-switch.mib')
nmFramMaxSigPathsPerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmFramMaxSigPathsPerPort.setStatus('current')
if mibBuilder.loadTexts: nmFramMaxSigPathsPerPort.setDescription('This object specifies the max number of UNI instances per port which can be created for FUNI SVC Signaling Support. In other words, this object defines the max number of FUNI services per port which can have SVC Signaling enabled.')
nmFramStatsMonitor = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmFramStatsMonitor.setStatus('current')
if mibBuilder.loadTexts: nmFramStatsMonitor.setDescription('This object specifies whether statistics are to be counted by the netmod system. The object controls from an overall perspective whether netmod, service and connection level statistics are to be counted. The object state will override the service level StatsMonitor objects, such that if the nmFramStatsMonitor is disabled then no statistics will be counted irrespective of whether the service level StatsMonitor is enabled. When the state changes from enabled to disabled all the related statistics will be frozen at their current value. When the state changes from disabled to enabled then all related statistics will be reset (zeroised).')
nmFramStatsEnabledTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 23), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmFramStatsEnabledTimeStamp.setStatus('current')
if mibBuilder.loadTexts: nmFramStatsEnabledTimeStamp.setDescription('nmFramStatsEnabledTimeStamp reflects the time, with reference to sysUpTime, when nmFramStatsMonitor is set to enabled. This will, therefore, provide a starting timestamp for the current statistics that are being counted.')
nmFramMsgType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmFramMsgType.setStatus('current')
if mibBuilder.loadTexts: nmFramMsgType.setDescription('This object is the identifier number of the messages that are sent from The SCP to the FRAM netmods.')
nmFramNakCause = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 3, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmFramNakCause.setStatus('current')
if mibBuilder.loadTexts: nmFramNakCause.setDescription('This object is the error code that indicates why a message sent from the SCP to the FRAM netmod did not succeed.')
framNakMsg = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2003)).setObjects(("Fore-Framnetmod-MIB", "nmFramMsgType"), ("Fore-Framnetmod-MIB", "nmFramNakCause"), ("Fore-Framnetmod-MIB", "nmFramBoard"), ("Fore-Framnetmod-MIB", "nmFramModule"), ("Fore-Ifcreate-MIB", "ifConvertToIfIndexPortId"), ("Fore-Ifcreate-MIB", "ifConvertToIfIndexChannelId"), ("FRAME-RELAY-DTE-MIB", "frCircuitDlci"), ("Fore-Funi-MIB", "funiConnFuniVpi"), ("Fore-Funi-MIB", "funiConnFuniVci"))
if mibBuilder.loadTexts: framNakMsg.setStatus('current')
if mibBuilder.loadTexts: framNakMsg.setDescription('This trap is sent when a message from the SCP to the FRAM netmod does not succeed.')
mibBuilder.exportSymbols("Fore-Framnetmod-MIB", nmFramOamF5Supervision=nmFramOamF5Supervision, nmFramMaxSigPathsPerPort=nmFramMaxSigPathsPerPort, nmFramApplication=nmFramApplication, nmFramEpdPpdBufferProportion=nmFramEpdPpdBufferProportion, nmFramStatsMonitor=nmFramStatsMonitor, nmFramOamF5RDITxPeriod=nmFramOamF5RDITxPeriod, nmFramModule=nmFramModule, nmFramEpdclp1LowPrio=nmFramEpdclp1LowPrio, PYSNMP_MODULE_ID=fram, nmFramOperState=nmFramOperState, nmFramStatsEnabledTimeStamp=nmFramStatsEnabledTimeStamp, nmFramEpdclp1HighPrio=nmFramEpdclp1HighPrio, nmFramApplSwRelease=nmFramApplSwRelease, nmFramMsgType=nmFramMsgType, nmFramOamF5RDIRxPeriod=nmFramOamF5RDIRxPeriod, nmFramNetmodConfEntry=nmFramNetmodConfEntry, nmFramBoard=nmFramBoard, nmFramOosLED=nmFramOosLED, nmFramNakCause=nmFramNakCause, nmFramNetmodConfTable=nmFramNetmodConfTable, nmFramEpdclp0LowPrio=nmFramEpdclp0LowPrio, fram=fram, framNakMsg=framNakMsg, nmFramOamF5AISTxPeriod=nmFramOamF5AISTxPeriod, nmFramPpdclp1LowPrio=nmFramPpdclp1LowPrio, nmFramOamF5AISRxPeriod=nmFramOamF5AISRxPeriod, nmFramApplKey=nmFramApplKey, nmFramBootSwRelease=nmFramBootSwRelease, nmFramEpdclp0HighPrio=nmFramEpdclp0HighPrio, nmFramPpdclp1HighPrio=nmFramPpdclp1HighPrio)