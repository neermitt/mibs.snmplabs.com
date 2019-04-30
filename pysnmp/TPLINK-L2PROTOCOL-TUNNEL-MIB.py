#
# PySNMP MIB module TPLINK-L2PROTOCOL-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-L2PROTOCOL-TUNNEL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:17:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, MibIdentifier, iso, Counter32, ModuleIdentity, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, Gauge32, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "MibIdentifier", "iso", "Counter32", "ModuleIdentity", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "Gauge32", "IpAddress", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkL2protocolTunnelMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 81))
tplinkL2protocolTunnelMIB.setRevisions(('2009-08-27 00:00',))
if mibBuilder.loadTexts: tplinkL2protocolTunnelMIB.setLastUpdated('200908270000Z')
if mibBuilder.loadTexts: tplinkL2protocolTunnelMIB.setOrganization('TPLINK')
tplinkL2protocolTunnelMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 81, 1))
tplinkL2protocolTunnelNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 81, 2))
tpL2ptGlobalCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 1))
tpL2ptEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpL2ptEnable.setStatus('current')
tpL2ptPortCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 2))
tpL2ptPortTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 2, 1), )
if mibBuilder.loadTexts: tpL2ptPortTable.setStatus('current')
tpL2ptPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpL2ptPortEntry.setStatus('current')
tpL2ptPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpL2ptPort.setStatus('current')
tpL2ptType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("uni", 1), ("nni", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpL2ptType.setStatus('current')
tpL2ptProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpL2ptProtocol.setStatus('current')
tpL2ptThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpL2ptThreshold.setStatus('current')
tpL2ptLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 2, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpL2ptLag.setStatus('current')
mibBuilder.exportSymbols("TPLINK-L2PROTOCOL-TUNNEL-MIB", tpL2ptGlobalCfg=tpL2ptGlobalCfg, tpL2ptProtocol=tpL2ptProtocol, tpL2ptThreshold=tpL2ptThreshold, tpL2ptLag=tpL2ptLag, tpL2ptEnable=tpL2ptEnable, tpL2ptPortEntry=tpL2ptPortEntry, PYSNMP_MODULE_ID=tplinkL2protocolTunnelMIB, tplinkL2protocolTunnelNotifications=tplinkL2protocolTunnelNotifications, tplinkL2protocolTunnelMIBObjects=tplinkL2protocolTunnelMIBObjects, tpL2ptPort=tpL2ptPort, tplinkL2protocolTunnelMIB=tplinkL2protocolTunnelMIB, tpL2ptPortTable=tpL2ptPortTable, tpL2ptType=tpL2ptType, tpL2ptPortCfg=tpL2ptPortCfg)