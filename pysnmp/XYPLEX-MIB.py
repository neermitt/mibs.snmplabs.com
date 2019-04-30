#
# PySNMP MIB module XYPLEX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYPLEX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:40:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, enterprises, TimeTicks, Counter64, Counter32, Bits, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, Unsigned32, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "enterprises", "TimeTicks", "Counter64", "Counter32", "Bits", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "Unsigned32", "MibIdentifier", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xyplex = MibIdentifier((1, 3, 6, 1, 4, 1, 33))
system = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 1))
character = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 2))
xInternet = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 4))
sysIdent = MibScalar((1, 3, 6, 1, 4, 1, 33, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysIdent.setStatus('mandatory')
charPhysNumber = MibScalar((1, 3, 6, 1, 4, 1, 33, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPhysNumber.setStatus('mandatory')
charPhysTable = MibTable((1, 3, 6, 1, 4, 1, 33, 2, 2), )
if mibBuilder.loadTexts: charPhysTable.setStatus('mandatory')
charPhysEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 2, 2, 1), ).setIndexNames((0, "XYPLEX-MIB", "charPhysIndex"))
if mibBuilder.loadTexts: charPhysEntry.setStatus('mandatory')
charPhysIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPhysIndex.setStatus('mandatory')
charPhysPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPhysPortName.setStatus('mandatory')
charPhysAdminAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("dynamic", 2), ("local", 3), ("remote", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPhysAdminAccess.setStatus('mandatory')
charPhysOperAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("local", 3), ("remote", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPhysOperAccess.setStatus('mandatory')
charPhysBits = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(7, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPhysBits.setStatus('mandatory')
charPhysParity = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("even", 2), ("mark", 3), ("odd", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPhysParity.setStatus('mandatory')
charPhysSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPhysSpeed.setStatus('mandatory')
charPhysModemControl = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPhysModemControl.setStatus('mandatory')
charPhysSignalType = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("rs232", 1), ("centronics", 2), ("dataproducts", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPhysSignalType.setStatus('mandatory')
charPhysInSignalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPhysInSignalNumber.setStatus('mandatory')
charPhysOutSignalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPhysOutSignalNumber.setStatus('mandatory')
charPhysFlowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("cts", 2), ("dsr", 3), ("xon", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPhysFlowControl.setStatus('mandatory')
charPhysInFlow = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPhysInFlow.setStatus('mandatory')
charPhysOutFlow = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPhysOutFlow.setStatus('mandatory')
charPhysInFlowState = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("go", 1), ("stop", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPhysInFlowState.setStatus('mandatory')
charPhysOutFlowState = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("go", 1), ("stop", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPhysOutFlowState.setStatus('mandatory')
charPhysAutobaud = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPhysAutobaud.setStatus('mandatory')
charPhysInCharacters = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPhysInCharacters.setStatus('mandatory')
charPhysOutCharacters = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPhysOutCharacters.setStatus('mandatory')
charPhysFramingErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPhysFramingErrors.setStatus('mandatory')
charPhysParityErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPhysParityErrors.setStatus('mandatory')
charPhysOverrunErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPhysOverrunErrors.setStatus('mandatory')
charPhysLastInCharacter = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPhysLastInCharacter.setStatus('mandatory')
charPhysLastOutCharacter = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPhysLastOutCharacter.setStatus('mandatory')
charPhysNode = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 25), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPhysNode.setStatus('mandatory')
charPhysUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 26), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPhysUserName.setStatus('mandatory')
charPhysInSignalTable = MibTable((1, 3, 6, 1, 4, 1, 33, 2, 3), )
if mibBuilder.loadTexts: charPhysInSignalTable.setStatus('mandatory')
charPhysInSignalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 2, 3, 1), ).setIndexNames((0, "XYPLEX-MIB", "charInPhysIndex"), (0, "XYPLEX-MIB", "charInSignalName"))
if mibBuilder.loadTexts: charPhysInSignalEntry.setStatus('mandatory')
charInPhysIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charInPhysIndex.setStatus('mandatory')
charInSignalName = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charInSignalName.setStatus('mandatory')
charInSignalState = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charInSignalState.setStatus('mandatory')
charPhysOutSignalTable = MibTable((1, 3, 6, 1, 4, 1, 33, 2, 4), )
if mibBuilder.loadTexts: charPhysOutSignalTable.setStatus('mandatory')
charPhysOutSignalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 2, 4, 1), ).setIndexNames((0, "XYPLEX-MIB", "charOutPhysIndex"), (0, "XYPLEX-MIB", "charOutSignalName"))
if mibBuilder.loadTexts: charPhysOutSignalEntry.setStatus('mandatory')
charOutPhysIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charOutPhysIndex.setStatus('mandatory')
charOutSignalName = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charOutSignalName.setStatus('mandatory')
charOutSignalState = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charOutSignalState.setStatus('mandatory')
intDomainSuffix = MibScalar((1, 3, 6, 1, 4, 1, 33, 4, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 115))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: intDomainSuffix.setStatus('mandatory')
intDomainAddress1 = MibScalar((1, 3, 6, 1, 4, 1, 33, 4, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: intDomainAddress1.setStatus('mandatory')
intDomainAddress2 = MibScalar((1, 3, 6, 1, 4, 1, 33, 4, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: intDomainAddress2.setStatus('mandatory')
intGatewayAddress1 = MibScalar((1, 3, 6, 1, 4, 1, 33, 4, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: intGatewayAddress1.setStatus('mandatory')
intGatewayAddress2 = MibScalar((1, 3, 6, 1, 4, 1, 33, 4, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: intGatewayAddress2.setStatus('mandatory')
mibBuilder.exportSymbols("XYPLEX-MIB", charPhysTable=charPhysTable, intDomainAddress1=intDomainAddress1, xInternet=xInternet, intGatewayAddress1=intGatewayAddress1, charPhysBits=charPhysBits, charPhysOutCharacters=charPhysOutCharacters, charPhysModemControl=charPhysModemControl, charPhysInFlowState=charPhysInFlowState, charPhysOutFlow=charPhysOutFlow, sysIdent=sysIdent, charPhysLastInCharacter=charPhysLastInCharacter, charPhysNode=charPhysNode, charInSignalState=charInSignalState, charOutPhysIndex=charOutPhysIndex, charPhysInSignalEntry=charPhysInSignalEntry, charPhysInFlow=charPhysInFlow, charPhysParityErrors=charPhysParityErrors, charInPhysIndex=charInPhysIndex, charPhysInSignalTable=charPhysInSignalTable, character=character, charPhysNumber=charPhysNumber, charPhysPortName=charPhysPortName, charPhysUserName=charPhysUserName, system=system, charPhysSpeed=charPhysSpeed, charPhysLastOutCharacter=charPhysLastOutCharacter, charPhysParity=charPhysParity, charPhysAdminAccess=charPhysAdminAccess, charPhysInCharacters=charPhysInCharacters, charPhysOutSignalEntry=charPhysOutSignalEntry, charPhysFlowControl=charPhysFlowControl, charPhysEntry=charPhysEntry, charPhysOutSignalTable=charPhysOutSignalTable, charOutSignalName=charOutSignalName, intDomainSuffix=intDomainSuffix, charPhysSignalType=charPhysSignalType, charPhysFramingErrors=charPhysFramingErrors, charOutSignalState=charOutSignalState, charPhysInSignalNumber=charPhysInSignalNumber, xyplex=xyplex, intGatewayAddress2=intGatewayAddress2, charPhysOutSignalNumber=charPhysOutSignalNumber, charPhysOverrunErrors=charPhysOverrunErrors, charPhysOperAccess=charPhysOperAccess, charPhysOutFlowState=charPhysOutFlowState, charPhysAutobaud=charPhysAutobaud, charInSignalName=charInSignalName, charPhysIndex=charPhysIndex, intDomainAddress2=intDomainAddress2)