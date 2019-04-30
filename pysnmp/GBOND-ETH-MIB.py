#
# PySNMP MIB module GBOND-ETH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GBOND-ETH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:05:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
gBondMIB, = mibBuilder.importSymbols("GBOND-MIB", "gBondMIB")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, Counter64, NotificationType, Counter32, ModuleIdentity, ObjectIdentity, Integer32, IpAddress, iso, TimeTicks, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "Counter64", "NotificationType", "Counter32", "ModuleIdentity", "ObjectIdentity", "Integer32", "IpAddress", "iso", "TimeTicks", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gBondEthMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 211, 2))
gBondEthMIB.setRevisions(('2007-06-05 00:00',))
if mibBuilder.loadTexts: gBondEthMIB.setLastUpdated('200706050000Z')
if mibBuilder.loadTexts: gBondEthMIB.setOrganization('IETF ADSL MIB Working Group')
gBondEthObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 211, 2, 1))
gBondEthConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 211, 2, 2))
gBondEthPort = MibIdentifier((1, 3, 6, 1, 2, 1, 211, 2, 1, 1))
gBondEthBce = MibIdentifier((1, 3, 6, 1, 2, 1, 211, 2, 1, 2))
class GBondEthPtmTcType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("tc6465", 1), ("tcHDLC", 2))

gBondEthPortConfTable = MibTable((1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 1), )
if mibBuilder.loadTexts: gBondEthPortConfTable.setStatus('current')
gBondEthPortConfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: gBondEthPortConfEntry.setStatus('current')
gBondEthTcAdminType = MibTableColumn((1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 1, 1, 1), GBondEthPtmTcType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gBondEthTcAdminType.setStatus('current')
gBondEthPortCapabilityTable = MibTable((1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 2), )
if mibBuilder.loadTexts: gBondEthPortCapabilityTable.setStatus('current')
gBondEthPortCapabilityEntry = MibTableRow((1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: gBondEthPortCapabilityEntry.setStatus('current')
gBondEthTcTypesSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 2, 1, 1), Bits().clone(namedValues=NamedValues(("tc6465", 0), ("tcHDLC", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gBondEthTcTypesSupported.setStatus('current')
gBondEthPortStatusTable = MibTable((1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3), )
if mibBuilder.loadTexts: gBondEthPortStatusTable.setStatus('current')
gBondEthPortStatusEntry = MibTableRow((1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: gBondEthPortStatusEntry.setStatus('current')
gBondEthTcOperType = MibTableColumn((1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1, 1), GBondEthPtmTcType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gBondEthTcOperType.setStatus('current')
gBondEthInErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gBondEthInErrors.setStatus('current')
gBondEthInSmallFragments = MibTableColumn((1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gBondEthInSmallFragments.setStatus('current')
gBondEthInLargeFragments = MibTableColumn((1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gBondEthInLargeFragments.setStatus('current')
gBondEthInBadFragments = MibTableColumn((1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gBondEthInBadFragments.setStatus('current')
gBondEthInLostFragments = MibTableColumn((1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gBondEthInLostFragments.setStatus('current')
gBondEthInLostStarts = MibTableColumn((1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gBondEthInLostStarts.setStatus('current')
gBondEthInLostEnds = MibTableColumn((1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gBondEthInLostEnds.setStatus('current')
gBondEthInOverflows = MibTableColumn((1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gBondEthInOverflows.setStatus('current')
gBondEthBceStatusTable = MibTable((1, 3, 6, 1, 2, 1, 211, 2, 1, 2, 1), )
if mibBuilder.loadTexts: gBondEthBceStatusTable.setStatus('current')
gBondEthBceStatusEntry = MibTableRow((1, 3, 6, 1, 2, 1, 211, 2, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: gBondEthBceStatusEntry.setStatus('current')
gBondEthBceTcInCodingErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 211, 2, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gBondEthBceTcInCodingErrors.setStatus('current')
gBondEthBceTcInCrcErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 211, 2, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gBondEthBceTcInCrcErrors.setStatus('current')
gBondEthGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 211, 2, 2, 1))
gBondEthCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 211, 2, 2, 2))
gBondEthBasicGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 211, 2, 2, 1, 1)).setObjects(("GBOND-ETH-MIB", "gBondEthTcTypesSupported"), ("GBOND-ETH-MIB", "gBondEthTcAdminType"), ("GBOND-ETH-MIB", "gBondEthTcOperType"), ("GBOND-ETH-MIB", "gBondEthInErrors"), ("GBOND-ETH-MIB", "gBondEthInSmallFragments"), ("GBOND-ETH-MIB", "gBondEthInLargeFragments"), ("GBOND-ETH-MIB", "gBondEthInBadFragments"), ("GBOND-ETH-MIB", "gBondEthInLostFragments"), ("GBOND-ETH-MIB", "gBondEthInLostStarts"), ("GBOND-ETH-MIB", "gBondEthInLostEnds"), ("GBOND-ETH-MIB", "gBondEthInOverflows"), ("GBOND-ETH-MIB", "gBondEthBceTcInCodingErrors"), ("GBOND-ETH-MIB", "gBondEthBceTcInCrcErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gBondEthBasicGroup = gBondEthBasicGroup.setStatus('current')
gBondEthBceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 211, 2, 2, 1, 2)).setObjects(("GBOND-ETH-MIB", "gBondEthBceTcInCodingErrors"), ("GBOND-ETH-MIB", "gBondEthBceTcInCrcErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gBondEthBceGroup = gBondEthBceGroup.setStatus('current')
gBondEthCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 211, 2, 2, 2, 1)).setObjects(("GBOND-ETH-MIB", "gBondEthBasicGroup"), ("GBOND-ETH-MIB", "gBondEthBceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gBondEthCompliance = gBondEthCompliance.setStatus('current')
mibBuilder.exportSymbols("GBOND-ETH-MIB", gBondEthPort=gBondEthPort, gBondEthConformance=gBondEthConformance, gBondEthPortConfTable=gBondEthPortConfTable, gBondEthCompliance=gBondEthCompliance, PYSNMP_MODULE_ID=gBondEthMIB, gBondEthInLostFragments=gBondEthInLostFragments, gBondEthCompliances=gBondEthCompliances, gBondEthPortStatusEntry=gBondEthPortStatusEntry, gBondEthMIB=gBondEthMIB, gBondEthPortCapabilityTable=gBondEthPortCapabilityTable, gBondEthPortConfEntry=gBondEthPortConfEntry, gBondEthInLostStarts=gBondEthInLostStarts, gBondEthTcTypesSupported=gBondEthTcTypesSupported, gBondEthObjects=gBondEthObjects, gBondEthInOverflows=gBondEthInOverflows, gBondEthTcOperType=gBondEthTcOperType, gBondEthPortStatusTable=gBondEthPortStatusTable, gBondEthBceStatusEntry=gBondEthBceStatusEntry, gBondEthPortCapabilityEntry=gBondEthPortCapabilityEntry, gBondEthInErrors=gBondEthInErrors, gBondEthBceTcInCodingErrors=gBondEthBceTcInCodingErrors, gBondEthTcAdminType=gBondEthTcAdminType, gBondEthInLostEnds=gBondEthInLostEnds, gBondEthBceStatusTable=gBondEthBceStatusTable, gBondEthBceGroup=gBondEthBceGroup, gBondEthBasicGroup=gBondEthBasicGroup, gBondEthBce=gBondEthBce, gBondEthInBadFragments=gBondEthInBadFragments, gBondEthBceTcInCrcErrors=gBondEthBceTcInCrcErrors, gBondEthGroups=gBondEthGroups, gBondEthInSmallFragments=gBondEthInSmallFragments, GBondEthPtmTcType=GBondEthPtmTcType, gBondEthInLargeFragments=gBondEthInLargeFragments)