#
# PySNMP MIB module IBMNETU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IBMNETU-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:40:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, IpAddress, TimeTicks, Gauge32, Counter32, ObjectIdentity, enterprises, NotificationType, Counter64, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "IpAddress", "TimeTicks", "Gauge32", "Counter32", "ObjectIdentity", "enterprises", "NotificationType", "Counter64", "MibIdentifier", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
ibmnetu = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 150))
ibmnetuadmin = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 150, 1))
ibmnetusystem = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 150, 2))
ibmnetuhardware = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 150, 3))
ibmneturouting = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 150, 4))
ibmnetuswitching = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 150, 5))
ibmnetuadminproducts = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 150, 1, 1))
ibmnetumod400 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 150, 1, 1, 1))
ibmnetuadminOID = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 150, 1, 2))
ibmnetuadminDebug = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 150, 1, 3))
ibmnetusystemInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 150, 2, 1))
ibmnetucfgInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 150, 2, 2))
ibmnetuhardwareGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1))
ibmnetuhardware400Specific = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 2))
ibmnetuEnetChipSet = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 150, 1, 2, 1))
enetChipSetToshiba = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 150, 1, 2, 1, 1))
enetChipSetAMD = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 150, 1, 2, 1, 2))
ibmnetuPCIAdapTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 1), )
if mibBuilder.loadTexts: ibmnetuPCIAdapTable.setStatus('mandatory')
ibmnetuPCIAdapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 1, 1), ).setIndexNames((0, "IBMNETU-MIB", "ibmnetuPCIAdapSlotNum"))
if mibBuilder.loadTexts: ibmnetuPCIAdapEntry.setStatus('mandatory')
ibmnetuPCIAdapSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmnetuPCIAdapSlotNum.setStatus('mandatory')
ibmnetuPCIAdapType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))).clone(namedValues=NamedValues(("unknown", 1), ("not-present", 2), ("atm-mmf-lic294", 3), ("reserved1", 4), ("atm-smf-lic295", 5), ("reserved2", 6), ("token-ring-lic280", 7), ("escon-lic287", 8), ("reserved3", 9), ("reserved4", 10), ("serial-rs232-lic282", 11), ("serial-v35-lic290", 12), ("serial-x21-lic291", 13), ("ethernet-lic281", 14), ("ethernet-fast-lic288", 15), ("serial-hssi-lic289", 16), ("fddi-lic286", 17), ("reserved5", 18), ("reserved6", 19), ("parallel-channel-lic299", 20)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmnetuPCIAdapType.setStatus('mandatory')
ibmnetuPCIAdapOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("unknown", 1), ("not-configured", 2), ("not-present", 3), ("does-not-apply", 4), ("enable-pending", 5), ("enabled", 6), ("disable-pending", 7), ("disabled", 8), ("not-initialized", 9), ("unknown-device", 10), ("hardware-error", 11), ("not-powered", 12), ("diagnostics", 13), ("wrs-available", 14), ("mis-configured", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmnetuPCIAdapOperStatus.setStatus('mandatory')
ibmnetuGraphicTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 2), )
if mibBuilder.loadTexts: ibmnetuGraphicTable.setStatus('mandatory')
ibmnetuGraphicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 2, 1), ).setIndexNames((0, "IBMNETU-MIB", "ibmnetuGraphicSlotNum"), (0, "IBMNETU-MIB", "ibmnetuGraphicPortNum"))
if mibBuilder.loadTexts: ibmnetuGraphicEntry.setStatus('mandatory')
ibmnetuGraphicSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmnetuGraphicSlotNum.setStatus('mandatory')
ibmnetuGraphicPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmnetuGraphicPortNum.setStatus('mandatory')
ibmnetuGraphicifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmnetuGraphicifIndex.setStatus('mandatory')
mibBuilder.exportSymbols("IBMNETU-MIB", ibmnetuPCIAdapTable=ibmnetuPCIAdapTable, ibmnetuhardware400Specific=ibmnetuhardware400Specific, ibmnetuadminproducts=ibmnetuadminproducts, ibmneturouting=ibmneturouting, ibmnetuadminOID=ibmnetuadminOID, ibmnetuGraphicEntry=ibmnetuGraphicEntry, enetChipSetToshiba=enetChipSetToshiba, ibmProd=ibmProd, ibmnetucfgInfo=ibmnetucfgInfo, ibmnetusystem=ibmnetusystem, ibmnetu=ibmnetu, ibmnetuGraphicifIndex=ibmnetuGraphicifIndex, ibmnetuPCIAdapOperStatus=ibmnetuPCIAdapOperStatus, ibm=ibm, ibmnetuPCIAdapEntry=ibmnetuPCIAdapEntry, ibmnetuhardware=ibmnetuhardware, ibmnetuPCIAdapType=ibmnetuPCIAdapType, ibmnetuPCIAdapSlotNum=ibmnetuPCIAdapSlotNum, enetChipSetAMD=enetChipSetAMD, ibmnetuhardwareGeneral=ibmnetuhardwareGeneral, ibmnetusystemInfo=ibmnetusystemInfo, ibmnetuadmin=ibmnetuadmin, ibmnetuGraphicTable=ibmnetuGraphicTable, ibmnetuGraphicSlotNum=ibmnetuGraphicSlotNum, ibmnetuGraphicPortNum=ibmnetuGraphicPortNum, ibmnetuEnetChipSet=ibmnetuEnetChipSet, ibmnetumod400=ibmnetumod400, ibmnetuswitching=ibmnetuswitching, ibmnetuadminDebug=ibmnetuadminDebug)