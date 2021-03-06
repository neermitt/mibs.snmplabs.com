#
# PySNMP MIB module H3C-GRE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-GRE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:22:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Counter32, Integer32, TimeTicks, Unsigned32, Gauge32, iso, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Counter32", "Integer32", "TimeTicks", "Unsigned32", "Gauge32", "iso", "ModuleIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cGre = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 54))
h3cGre.setRevisions(('2005-06-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cGre.setRevisionsDescriptions(('The initial revision of this MIB module. ',))
if mibBuilder.loadTexts: h3cGre.setLastUpdated('200506040000Z')
if mibBuilder.loadTexts: h3cGre.setOrganization('Huawei 3Com Technologies Co., Ltd. ')
if mibBuilder.loadTexts: h3cGre.setContactInfo('Platform Team Huawei 3Com Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.huawei-3com.com Zip:100085 ')
if mibBuilder.loadTexts: h3cGre.setDescription('This MIB contains objects to Manage configuration and Monitor running state for GRE. ')
h3cGreObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 54, 1))
h3cGreTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 54, 1, 1), )
if mibBuilder.loadTexts: h3cGreTable.setStatus('current')
if mibBuilder.loadTexts: h3cGreTable.setDescription('A table of Generic Routing Encapsulation(GRE) configuration. It contains configuration of GRE Key, and enable flags of Key and Checksum. The detail of Key and Checksum is described in RFC2784 and RFC2890. ')
h3cGreEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 54, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cGreEntry.setStatus('current')
if mibBuilder.loadTexts: h3cGreEntry.setDescription('The entry of h3cGreTable ')
h3cGreKeyValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 54, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cGreKeyValue.setStatus('current')
if mibBuilder.loadTexts: h3cGreKeyValue.setDescription('The value of GRE key ')
h3cGreKey = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 54, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cGreKey.setStatus('current')
if mibBuilder.loadTexts: h3cGreKey.setDescription('The enable flag of GRE key ')
h3cGreChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 54, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cGreChecksum.setStatus('current')
if mibBuilder.loadTexts: h3cGreChecksum.setDescription('The enable flag of GRE Checksum ')
mibBuilder.exportSymbols("H3C-GRE-MIB", h3cGreKey=h3cGreKey, h3cGreObjects=h3cGreObjects, h3cGreEntry=h3cGreEntry, h3cGreTable=h3cGreTable, h3cGreChecksum=h3cGreChecksum, PYSNMP_MODULE_ID=h3cGre, h3cGre=h3cGre, h3cGreKeyValue=h3cGreKeyValue)
