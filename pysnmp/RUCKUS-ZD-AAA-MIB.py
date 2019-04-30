#
# PySNMP MIB module RUCKUS-ZD-AAA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-ZD-AAA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:51:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ruckusZDWLANModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusZDWLANModule")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, ModuleIdentity, TimeTicks, Counter32, iso, Bits, Counter64, ObjectIdentity, MibIdentifier, NotificationType, Unsigned32, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "TimeTicks", "Counter32", "iso", "Bits", "Counter64", "ObjectIdentity", "MibIdentifier", "NotificationType", "Unsigned32", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ruckusZDAAAMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3))
if mibBuilder.loadTexts: ruckusZDAAAMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusZDAAAMIB.setOrganization('Ruckus Wireless, Inc.')
ruckusZDAAAObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1))
ruckusZDAAAConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1))
ruckusZDAAAConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 1), )
if mibBuilder.loadTexts: ruckusZDAAAConfigTable.setStatus('current')
ruckusZDAAAConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 1, 1), ).setIndexNames((0, "RUCKUS-ZD-AAA-MIB", "ruckusZDAAAConfigID"))
if mibBuilder.loadTexts: ruckusZDAAAConfigEntry.setStatus('current')
ruckusZDAAAConfigID = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 32)))
if mibBuilder.loadTexts: ruckusZDAAAConfigID.setStatus('current')
ruckusZDAAAConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAAAConfigName.setStatus('current')
ruckusZDAAAConfigServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("active-directory", 1), ("ldap-directory", 2), ("aaa-authentication", 3), ("aaa-accounting", 4))).clone('aaa-authentication')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAAAConfigServiceType.setStatus('current')
ruckusZDAAAConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ruckusZDAAAConfigRowStatus.setStatus('current')
ruckusZDAAASvrTable = MibTable((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2), )
if mibBuilder.loadTexts: ruckusZDAAASvrTable.setStatus('current')
ruckusZDAAASvrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1), ).setIndexNames((0, "RUCKUS-ZD-AAA-MIB", "ruckusZDAAAConfigID"))
if mibBuilder.loadTexts: ruckusZDAAASvrEntry.setStatus('current')
ruckusZDAAARadiusBackupControl = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAAARadiusBackupControl.setStatus('current')
ruckusZDAAARadiusPrimarySvrIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAAARadiusPrimarySvrIpAddress.setStatus('current')
ruckusZDAAARadiusPrimarySvrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAAARadiusPrimarySvrPort.setStatus('current')
ruckusZDAAARadiusPrimarySvrPasswd = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAAARadiusPrimarySvrPasswd.setStatus('current')
ruckusZDAAARadiusSecondarySvrIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAAARadiusSecondarySvrIpAddress.setStatus('current')
ruckusZDAAARadiusSecondarySvrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAAARadiusSecondarySvrPort.setStatus('current')
ruckusZDAAARadiusSecondarySvrPasswd = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAAARadiusSecondarySvrPasswd.setStatus('current')
ruckusZDAAARadiusFailoverTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 10)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAAARadiusFailoverTimeout.setStatus('current')
ruckusZDAAARadiusFailoverRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAAARadiusFailoverRetry.setStatus('current')
ruckusZDAAARadiusFailoverReconnectPrimary = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAAARadiusFailoverReconnectPrimary.setStatus('current')
mibBuilder.exportSymbols("RUCKUS-ZD-AAA-MIB", ruckusZDAAARadiusSecondarySvrPasswd=ruckusZDAAARadiusSecondarySvrPasswd, ruckusZDAAAConfigEntry=ruckusZDAAAConfigEntry, ruckusZDAAARadiusPrimarySvrPasswd=ruckusZDAAARadiusPrimarySvrPasswd, ruckusZDAAAConfigRowStatus=ruckusZDAAAConfigRowStatus, ruckusZDAAARadiusPrimarySvrPort=ruckusZDAAARadiusPrimarySvrPort, ruckusZDAAAConfig=ruckusZDAAAConfig, ruckusZDAAARadiusSecondarySvrPort=ruckusZDAAARadiusSecondarySvrPort, PYSNMP_MODULE_ID=ruckusZDAAAMIB, ruckusZDAAARadiusFailoverReconnectPrimary=ruckusZDAAARadiusFailoverReconnectPrimary, ruckusZDAAAObjects=ruckusZDAAAObjects, ruckusZDAAARadiusFailoverTimeout=ruckusZDAAARadiusFailoverTimeout, ruckusZDAAARadiusBackupControl=ruckusZDAAARadiusBackupControl, ruckusZDAAARadiusPrimarySvrIpAddress=ruckusZDAAARadiusPrimarySvrIpAddress, ruckusZDAAASvrTable=ruckusZDAAASvrTable, ruckusZDAAASvrEntry=ruckusZDAAASvrEntry, ruckusZDAAAConfigServiceType=ruckusZDAAAConfigServiceType, ruckusZDAAAMIB=ruckusZDAAAMIB, ruckusZDAAAConfigName=ruckusZDAAAConfigName, ruckusZDAAARadiusFailoverRetry=ruckusZDAAARadiusFailoverRetry, ruckusZDAAAConfigTable=ruckusZDAAAConfigTable, ruckusZDAAARadiusSecondarySvrIpAddress=ruckusZDAAARadiusSecondarySvrIpAddress, ruckusZDAAAConfigID=ruckusZDAAAConfigID)