#
# PySNMP MIB module HP-ICF-MAD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-MAD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:34:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, ObjectIdentity, Counter32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, Unsigned32, NotificationType, ModuleIdentity, Gauge32, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "Counter32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "Unsigned32", "NotificationType", "ModuleIdentity", "Gauge32", "MibIdentifier", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfMadMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95))
hpicfMadMIB.setRevisions(('2012-12-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfMadMIB.setRevisionsDescriptions(('Initial version for this MIB module',))
if mibBuilder.loadTexts: hpicfMadMIB.setLastUpdated('201212120000Z')
if mibBuilder.loadTexts: hpicfMadMIB.setOrganization(' HP Networking')
if mibBuilder.loadTexts: hpicfMadMIB.setContactInfo('Hewlett-Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfMadMIB.setDescription('The MIB module is for Multi Active Detection Technology (MAD).')
hpicfMadNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 0))
hpicfMadObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1))
hpicfMadConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 2))
hpicfMadLacpAggObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1))
hpicfMadLacpAggTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 1), )
if mibBuilder.loadTexts: hpicfMadLacpAggTable.setStatus('current')
if mibBuilder.loadTexts: hpicfMadLacpAggTable.setDescription('Information describing the MAD configuration on LACP trunks.')
hpicfMadLacpAggEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 1, 1), ).setIndexNames((0, "HP-ICF-MAD-MIB", "hpicfMadLacpAggTrunkId"))
if mibBuilder.loadTexts: hpicfMadLacpAggEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfMadLacpAggEntry.setDescription('Information describing the MAD configuration on LACP trunks.')
hpicfMadLacpAggTrunkId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpicfMadLacpAggTrunkId.setStatus('current')
if mibBuilder.loadTexts: hpicfMadLacpAggTrunkId.setDescription('A LACP trunk ID to uniquely identify each entry in the table.')
hpicfMadPassthroughLacpAggAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMadPassthroughLacpAggAdminStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfMadPassthroughLacpAggAdminStatus.setDescription('The desired administrative state of MAD passthrough on LACP trunk interface.By default lacp mad passthrough will be enabled on all LACP trunks.')
hpicfMadLacpAggPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 2), )
if mibBuilder.loadTexts: hpicfMadLacpAggPortStatsTable.setStatus('current')
if mibBuilder.loadTexts: hpicfMadLacpAggPortStatsTable.setDescription('A table that contains MAD( Multi Active Detection) information of every port that is associated with LACP trunk. A row appears in this table for each physical port of LACP trunk.')
hpicfMadLacpAggPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 2, 1), ).setIndexNames((0, "HP-ICF-MAD-MIB", "hpicfMadLacpAggPortIndex"))
if mibBuilder.loadTexts: hpicfMadLacpAggPortStatsEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfMadLacpAggPortStatsEntry.setDescription('A list of Link Aggregation Control Protocol statistics for each port on this device.')
hpicfMadLacpAggPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hpicfMadLacpAggPortIndex.setStatus('current')
if mibBuilder.loadTexts: hpicfMadLacpAggPortIndex.setDescription('Physical port to uniquely identify an entry.')
hpicfMadPassthroughLacpAggPDUsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfMadPassthroughLacpAggPDUsRx.setStatus('current')
if mibBuilder.loadTexts: hpicfMadPassthroughLacpAggPDUsRx.setDescription('The number of valid LACP PDUs with MAD TLV received on this aggregation port. This value is read-only.')
hpicfMadPassthroughLacpAggPDUsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfMadPassthroughLacpAggPDUsTx.setStatus('current')
if mibBuilder.loadTexts: hpicfMadPassthroughLacpAggPDUsTx.setDescription('The number of LACP PDUs with MAD TLV transmitted on this aggregation port. This value is read-only.')
hpicfMadPassthroughLacpAggPDUsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfMadPassthroughLacpAggPDUsDropped.setStatus('current')
if mibBuilder.loadTexts: hpicfMadPassthroughLacpAggPDUsDropped.setDescription('The number of LACPDUs with MAD TLV dropped on this aggregation port. This value is read-only.')
hpicfMadLacpAggGoups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 2, 1))
hpicfMadLacpAggCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 2, 2))
hpicfMadLacpAggCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 2, 2, 1)).setObjects(("HP-ICF-MAD-MIB", "hpicfMadLacpAggConfigGroup"), ("HP-ICF-MAD-MIB", "hpicfMadLacpAggStatisticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMadLacpAggCompliance1 = hpicfMadLacpAggCompliance1.setStatus('current')
if mibBuilder.loadTexts: hpicfMadLacpAggCompliance1.setDescription('The compliance statement')
hpicfMadLacpAggConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 2, 1, 1)).setObjects(("HP-ICF-MAD-MIB", "hpicfMadPassthroughLacpAggAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMadLacpAggConfigGroup = hpicfMadLacpAggConfigGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfMadLacpAggConfigGroup.setDescription('These objects are used for managing LACP MAD configuration parameters.')
hpicfMadLacpAggStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 2, 1, 2)).setObjects(("HP-ICF-MAD-MIB", "hpicfMadPassthroughLacpAggPDUsRx"), ("HP-ICF-MAD-MIB", "hpicfMadPassthroughLacpAggPDUsTx"), ("HP-ICF-MAD-MIB", "hpicfMadPassthroughLacpAggPDUsDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMadLacpAggStatisticsGroup = hpicfMadLacpAggStatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfMadLacpAggStatisticsGroup.setDescription('These objects are used for providing information about each port.')
mibBuilder.exportSymbols("HP-ICF-MAD-MIB", hpicfMadConformance=hpicfMadConformance, hpicfMadLacpAggConfigGroup=hpicfMadLacpAggConfigGroup, hpicfMadObjects=hpicfMadObjects, hpicfMadLacpAggTrunkId=hpicfMadLacpAggTrunkId, hpicfMadPassthroughLacpAggPDUsRx=hpicfMadPassthroughLacpAggPDUsRx, hpicfMadMIB=hpicfMadMIB, hpicfMadNotifications=hpicfMadNotifications, hpicfMadLacpAggPortStatsEntry=hpicfMadLacpAggPortStatsEntry, hpicfMadLacpAggPortIndex=hpicfMadLacpAggPortIndex, hpicfMadLacpAggGoups=hpicfMadLacpAggGoups, hpicfMadPassthroughLacpAggAdminStatus=hpicfMadPassthroughLacpAggAdminStatus, hpicfMadPassthroughLacpAggPDUsDropped=hpicfMadPassthroughLacpAggPDUsDropped, hpicfMadLacpAggCompliance1=hpicfMadLacpAggCompliance1, hpicfMadPassthroughLacpAggPDUsTx=hpicfMadPassthroughLacpAggPDUsTx, hpicfMadLacpAggEntry=hpicfMadLacpAggEntry, hpicfMadLacpAggStatisticsGroup=hpicfMadLacpAggStatisticsGroup, hpicfMadLacpAggPortStatsTable=hpicfMadLacpAggPortStatsTable, hpicfMadLacpAggCompliances=hpicfMadLacpAggCompliances, hpicfMadLacpAggObjects=hpicfMadLacpAggObjects, PYSNMP_MODULE_ID=hpicfMadMIB, hpicfMadLacpAggTable=hpicfMadLacpAggTable)