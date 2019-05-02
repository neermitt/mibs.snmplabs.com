#
# PySNMP MIB module SN-ELSTP40-PRIV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SN-ELSTP40-PRIV-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:07:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, Counter32, internet, IpAddress, ModuleIdentity, Unsigned32, MibIdentifier, enterprises, ObjectIdentity, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "Counter32", "internet", "IpAddress", "ModuleIdentity", "Unsigned32", "MibIdentifier", "enterprises", "ObjectIdentity", "NotificationType", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ad = MibIdentifier((1, 3, 6, 1, 4, 1, 4196))
adProductMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 4196, 1))
simaticNet = MibIdentifier((1, 3, 6, 1, 4, 1, 4196, 1, 1))
iHub = MibIdentifier((1, 3, 6, 1, 4, 1, 4196, 1, 1, 1))
iSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4196, 1, 1, 2))
iLeanSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3))
elsTP40M = MibIdentifier((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1))
elsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 1))
elsStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2))
elsMail = MibIdentifier((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 3))
elsTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 4))
elsEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 5))
elsIPInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 6))
version = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 62)).clone('V1.0.0.0')).setMaxAccess("readonly")
if mibBuilder.loadTexts: version.setStatus('mandatory')
if mibBuilder.loadTexts: version.setDescription('Firmware Revision')
hardware = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 62)).clone('01')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardware.setStatus('mandatory')
if mibBuilder.loadTexts: hardware.setDescription('Hardware Revision')
ownIP = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 6, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ownIP.setStatus('mandatory')
if mibBuilder.loadTexts: ownIP.setDescription('ip address')
netMask = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 6, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netMask.setStatus('mandatory')
if mibBuilder.loadTexts: netMask.setDescription('network mask')
gateway = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 6, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gateway.setStatus('mandatory')
if mibBuilder.loadTexts: gateway.setDescription('gateway address')
fromDHCP = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 6, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fromDHCP.setStatus('mandatory')
if mibBuilder.loadTexts: fromDHCP.setDescription('shows if address is from DHCP')
emailFrom = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 62)).clone('owner@anywhere.com')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: emailFrom.setStatus('mandatory')
if mibBuilder.loadTexts: emailFrom.setDescription('Mail receiver')
emailTo = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 3, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 62)).clone('test@els.com')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: emailTo.setStatus('mandatory')
if mibBuilder.loadTexts: emailTo.setDescription('Mail subject')
emailSubject = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 3, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 62)).clone('test@els.com')).setMaxAccess("readonly")
if mibBuilder.loadTexts: emailSubject.setStatus('mandatory')
if mibBuilder.loadTexts: emailSubject.setDescription('Mail Sender')
smtpdIP = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 3, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smtpdIP.setStatus('mandatory')
if mibBuilder.loadTexts: smtpdIP.setDescription('ip address of smtp Daemon')
trapIP1 = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 4, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapIP1.setStatus('mandatory')
if mibBuilder.loadTexts: trapIP1.setDescription("1. trap receiver's ip address")
trapIP2 = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 4, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapIP2.setStatus('mandatory')
if mibBuilder.loadTexts: trapIP2.setDescription("2. trap receiver's ip address")
emailMask = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 5, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: emailMask.setStatus('mandatory')
if mibBuilder.loadTexts: emailMask.setDescription('used to mask off Switch-Events to be reported by mail ')
trapMask = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 5, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapMask.setStatus('mandatory')
if mibBuilder.loadTexts: trapMask.setDescription('used to mask off Switch-events to be reported by Trap')
otherMask = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 5, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: otherMask.setStatus('mandatory')
if mibBuilder.loadTexts: otherMask.setDescription('used to mask off PST-Request or Power-On events to be reported by Trap or Email')
receiveError1 = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: receiveError1.setStatus('mandatory')
if mibBuilder.loadTexts: receiveError1.setDescription('number of receive errors of port 1')
receiveError2 = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: receiveError2.setStatus('mandatory')
if mibBuilder.loadTexts: receiveError2.setDescription('number of receive errors of port 2')
receiveError3 = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: receiveError3.setStatus('mandatory')
if mibBuilder.loadTexts: receiveError3.setDescription('number of receive errors of port 3')
receiveError4 = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: receiveError4.setStatus('mandatory')
if mibBuilder.loadTexts: receiveError4.setDescription('number of receive errors of port 4')
collisionCount1 = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: collisionCount1.setStatus('mandatory')
if mibBuilder.loadTexts: collisionCount1.setDescription('number of collisions of port 1')
collisionCount2 = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: collisionCount2.setStatus('mandatory')
if mibBuilder.loadTexts: collisionCount2.setDescription('number of collisions of port 2')
collisionCount3 = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: collisionCount3.setStatus('mandatory')
if mibBuilder.loadTexts: collisionCount3.setDescription('number of collisions of port 3')
collisionCount4 = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: collisionCount4.setStatus('mandatory')
if mibBuilder.loadTexts: collisionCount4.setDescription('number of collisions of port 4')
ledStatus = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ledStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ledStatus.setDescription('reflects LEDs of switch')
startBank = MibScalar((1, 3, 6, 1, 4, 1, 4196, 1, 1, 3, 1, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: startBank.setStatus('mandatory')
if mibBuilder.loadTexts: startBank.setDescription('shows startBank ')
mibBuilder.exportSymbols("SN-ELSTP40-PRIV-MIB", emailFrom=emailFrom, startBank=startBank, elsTrap=elsTrap, hardware=hardware, receiveError3=receiveError3, elsEvents=elsEvents, elsIPInfo=elsIPInfo, ad=ad, ledStatus=ledStatus, smtpdIP=smtpdIP, ownIP=ownIP, receiveError1=receiveError1, collisionCount2=collisionCount2, trapMask=trapMask, elsInfo=elsInfo, adProductMibs=adProductMibs, elsTP40M=elsTP40M, version=version, elsStatus=elsStatus, fromDHCP=fromDHCP, emailTo=emailTo, collisionCount1=collisionCount1, otherMask=otherMask, emailSubject=emailSubject, receiveError4=receiveError4, trapIP1=trapIP1, collisionCount4=collisionCount4, simaticNet=simaticNet, receiveError2=receiveError2, netMask=netMask, collisionCount3=collisionCount3, trapIP2=trapIP2, iLeanSwitch=iLeanSwitch, gateway=gateway, emailMask=emailMask, elsMail=elsMail, iHub=iHub, iSwitch=iSwitch)