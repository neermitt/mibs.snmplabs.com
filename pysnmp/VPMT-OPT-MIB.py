#
# PySNMP MIB module VPMT-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VPMT-OPT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:28:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, MibIdentifier, Bits, TimeTicks, NotificationType, IpAddress, Integer32, Unsigned32, Gauge32, Counter32, ObjectIdentity, Counter64, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "MibIdentifier", "Bits", "TimeTicks", "NotificationType", "IpAddress", "Integer32", "Unsigned32", "Gauge32", "Counter32", "ObjectIdentity", "Counter64", "iso", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2))
cdx6500CfgGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2))
class DisplayString(OctetString):
    pass

cdx6500VPMTCfgTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26), )
if mibBuilder.loadTexts: cdx6500VPMTCfgTable.setStatus('mandatory')
cdx6500VPMTCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1), ).setIndexNames((0, "VPMT-OPT-MIB", "cdx6500VPMTCfgEntryNum"))
if mibBuilder.loadTexts: cdx6500VPMTCfgEntry.setStatus('mandatory')
cdx6500VPMTCfgEntryNum = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgEntryNum.setStatus('mandatory')
cdx6500VPMTCfgvpType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("vpmt-ptype-null", 1), ("vpmt-ptype-voice", 2), ("vpmt-ptype-pri-voice", 3), ("vpmt-ptype-bypass-voice", 4), ("vpmt-ptype-tdm-data", 5), ("vpmt-ptype-pri-data", 6), ("vpmt-ptype-bypass-data", 7), ("vpmt-ptype-trans-ccs-voice", 8), ("vpmt-ptype-ccs-bypass", 9), ("vpmt-ptype-bri-voice", 10), ("vpmt-ptype-aam", 11), ("vpmt-ptype-num", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgvpType.setStatus('mandatory')
cdx6500VPMTCfgvpNum = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgvpNum.setStatus('mandatory')
cdx6500VPMTCfgdslNum = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgdslNum.setStatus('mandatory')
cdx6500VPMTCfgds0Rate = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("vpmt-rate-56k", 1), ("vpmt-rate-64k", 2), ("vpmt-rate-num", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgds0Rate.setStatus('mandatory')
cdx6500VPMTCfgsrcTimeSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgsrcTimeSlot.setStatus('mandatory')
cdx6500VPMTCfgdestTimeSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgdestTimeSlot.setStatus('mandatory')
cdx6500VPMTCfglocalDialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfglocalDialNum.setStatus('mandatory')
cdx6500VPMTCfgsubAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgsubAddress.setStatus('mandatory')
cdx6500VPMTCfgcallPermission = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("out", 1), ("inc", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgcallPermission.setStatus('mandatory')
cdx6500VPMTCfgnum_ccs_bypass_connections = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 11), Integer32()).setLabel("cdx6500VPMTCfgnum-ccs-bypass-connections").setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgnum_ccs_bypass_connections.setStatus('mandatory')
cdx6500VPMTCfgPhysical_Port = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 12), Integer32()).setLabel("cdx6500VPMTCfgPhysical-Port").setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgPhysical_Port.setStatus('mandatory')
mibBuilder.exportSymbols("VPMT-OPT-MIB", cdx6500VPMTCfgdslNum=cdx6500VPMTCfgdslNum, codex=codex, cdx6500VPMTCfgsrcTimeSlot=cdx6500VPMTCfgsrcTimeSlot, cdx6500VPMTCfgsubAddress=cdx6500VPMTCfgsubAddress, cdx6500VPMTCfgds0Rate=cdx6500VPMTCfgds0Rate, cdx6500CfgGeneralGroup=cdx6500CfgGeneralGroup, cdx6500VPMTCfgEntryNum=cdx6500VPMTCfgEntryNum, cdx6500VPMTCfgcallPermission=cdx6500VPMTCfgcallPermission, cdx6500VPMTCfgTable=cdx6500VPMTCfgTable, cdxProductSpecific=cdxProductSpecific, cdx6500VPMTCfglocalDialNum=cdx6500VPMTCfglocalDialNum, cdx6500VPMTCfgvpNum=cdx6500VPMTCfgvpNum, cdx6500VPMTCfgdestTimeSlot=cdx6500VPMTCfgdestTimeSlot, cdx6500VPMTCfgnum_ccs_bypass_connections=cdx6500VPMTCfgnum_ccs_bypass_connections, cdx6500Configuration=cdx6500Configuration, cdx6500VPMTCfgvpType=cdx6500VPMTCfgvpType, cdx6500VPMTCfgPhysical_Port=cdx6500VPMTCfgPhysical_Port, cdx6500=cdx6500, cdx6500VPMTCfgEntry=cdx6500VPMTCfgEntry, DisplayString=DisplayString)