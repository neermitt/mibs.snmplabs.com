#
# PySNMP MIB module TRAPEZE-NETWORKS-REGISTRATION-DEVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-REGISTRATION-DEVICES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:20:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, IpAddress, Counter64, Counter32, TimeTicks, NotificationType, ObjectIdentity, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "IpAddress", "Counter64", "Counter32", "TimeTicks", "NotificationType", "ObjectIdentity", "Unsigned32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
trpzRegistration, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzRegistration")
trpzRegistrationDevicesMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 3, 6))
trpzRegistrationDevicesMib.setRevisions(('2011-08-09 00:32', '2011-03-08 00:22', '2010-12-02 00:11', '2009-12-18 00:10', '2007-11-30 00:01', '2007-08-22 00:00',))
if mibBuilder.loadTexts: trpzRegistrationDevicesMib.setLastUpdated('201108090032Z')
if mibBuilder.loadTexts: trpzRegistrationDevicesMib.setOrganization('Trapeze Networks')
mobilityExchange = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 1))
mobilityExchange20 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 1, 1))
mobilityExchange8 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 1, 2))
mobilityExchange400 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 1, 3))
mobilityExchangeR2 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 1, 4))
mobilityExchange216 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 1, 6))
mobilityExchange200 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 1, 7))
mobilityExchange2800 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 1, 12))
mobilityExchange800 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 1, 13))
mobilityPoint = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 2))
mobilityPoint101 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 2, 1))
mobilityPoint122 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 2, 2))
mobilityPoint241 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 2, 3))
mobilityPoint252 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 2, 4))
wirelessLANController = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 3))
wirelessLANController880R = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 3, 1))
wirelessLANController8 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 3, 2))
wirelessLANController2 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 3, 3))
wirelessLANController800r = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 3, 4))
wirelessLANController2800 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 3, 5))
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-REGISTRATION-DEVICES-MIB", mobilityPoint101=mobilityPoint101, PYSNMP_MODULE_ID=trpzRegistrationDevicesMib, mobilityPoint122=mobilityPoint122, mobilityExchange2800=mobilityExchange2800, wirelessLANController8=wirelessLANController8, wirelessLANController2=wirelessLANController2, mobilityExchange200=mobilityExchange200, mobilityPoint252=mobilityPoint252, wirelessLANController=wirelessLANController, mobilityPoint241=mobilityPoint241, wirelessLANController800r=wirelessLANController800r, mobilityPoint=mobilityPoint, trpzRegistrationDevicesMib=trpzRegistrationDevicesMib, mobilityExchange216=mobilityExchange216, mobilityExchange8=mobilityExchange8, mobilityExchangeR2=mobilityExchangeR2, mobilityExchange400=mobilityExchange400, mobilityExchange20=mobilityExchange20, wirelessLANController880R=wirelessLANController880R, mobilityExchange800=mobilityExchange800, mobilityExchange=mobilityExchange, wirelessLANController2800=wirelessLANController2800)