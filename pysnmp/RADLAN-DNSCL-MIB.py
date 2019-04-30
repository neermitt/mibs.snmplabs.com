#
# PySNMP MIB module RADLAN-DNSCL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-DNSCL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:38:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
dnsResConfigSbeltEntry, = mibBuilder.importSymbols("DNS-RESOLVER-MIB", "dnsResConfigSbeltEntry")
DnsName, = mibBuilder.importSymbols("DNS-SERVER-MIB", "DnsName")
rlDnsCl, = mibBuilder.importSymbols("RADLAN-MIB", "rlDnsCl")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, Bits, Gauge32, iso, TimeTicks, NotificationType, ModuleIdentity, Counter64, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "Bits", "Gauge32", "iso", "TimeTicks", "NotificationType", "ModuleIdentity", "Counter64", "MibIdentifier", "IpAddress")
RowStatus, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TruthValue", "TextualConvention")
DisplayString, = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString")
rlDnsClMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 93, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDnsClMibVersion.setStatus('current')
rlDnsClEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 93, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClEnable.setStatus('current')
rlDnsClDomainNameTable = MibTable((1, 3, 6, 1, 4, 1, 89, 93, 3), )
if mibBuilder.loadTexts: rlDnsClDomainNameTable.setStatus('current')
rlDnsClDomainNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 93, 3, 1), ).setIndexNames((0, "RADLAN-DNSCL-MIB", "rlDnsClDomainNameName"))
if mibBuilder.loadTexts: rlDnsClDomainNameEntry.setStatus('current')
rlDnsClDomainNameName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 3, 1, 1), DnsName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClDomainNameName.setStatus('current')
rlDnsClDomainNameOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dhcp", 2))).clone('static')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClDomainNameOwner.setStatus('current')
rlDnsClDomainNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 3, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClDomainNameRowStatus.setStatus('current')
rlDnsClMaxNumOfRetransmissions = MibScalar((1, 3, 6, 1, 4, 1, 89, 93, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClMaxNumOfRetransmissions.setStatus('current')
rlDnsClMinRetransmissionInterval = MibScalar((1, 3, 6, 1, 4, 1, 89, 93, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClMinRetransmissionInterval.setStatus('current')
rlDnsClNamesTable = MibTable((1, 3, 6, 1, 4, 1, 89, 93, 6), )
if mibBuilder.loadTexts: rlDnsClNamesTable.setStatus('current')
rlDnsClNamesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 93, 6, 1), ).setIndexNames((0, "RADLAN-DNSCL-MIB", "rlDnsClNamesName"), (0, "RADLAN-DNSCL-MIB", "rlDnsClNamesOwner"), (0, "RADLAN-DNSCL-MIB", "rlDnsClNamesIndex"))
if mibBuilder.loadTexts: rlDnsClNamesEntry.setStatus('current')
rlDnsClNamesName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 1), DnsName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDnsClNamesName.setStatus('current')
rlDnsClNamesOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dhcp", 2))).clone('static')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClNamesOwner.setStatus('current')
rlDnsClNamesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 3), Integer32())
if mibBuilder.loadTexts: rlDnsClNamesIndex.setStatus('current')
rlDnsClNamesAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClNamesAddr.setStatus('current')
rlDnsClNamesRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClNamesRowStatus.setStatus('current')
dnsResConfigSbeltExtTable = MibTable((1, 3, 6, 1, 4, 1, 89, 93, 7), )
if mibBuilder.loadTexts: dnsResConfigSbeltExtTable.setStatus('current')
dnsResConfigSbeltExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 93, 7, 1), )
dnsResConfigSbeltEntry.registerAugmentions(("RADLAN-DNSCL-MIB", "dnsResConfigSbeltExtEntry"))
dnsResConfigSbeltExtEntry.setIndexNames(*dnsResConfigSbeltEntry.getIndexNames())
if mibBuilder.loadTexts: dnsResConfigSbeltExtEntry.setStatus('current')
dnsResConfigSbeltOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dhcp", 2))).clone('static')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsResConfigSbeltOwner.setStatus('current')
mibBuilder.exportSymbols("RADLAN-DNSCL-MIB", rlDnsClDomainNameRowStatus=rlDnsClDomainNameRowStatus, rlDnsClNamesIndex=rlDnsClNamesIndex, rlDnsClNamesEntry=rlDnsClNamesEntry, rlDnsClEnable=rlDnsClEnable, rlDnsClMaxNumOfRetransmissions=rlDnsClMaxNumOfRetransmissions, rlDnsClNamesTable=rlDnsClNamesTable, rlDnsClNamesRowStatus=rlDnsClNamesRowStatus, rlDnsClDomainNameEntry=rlDnsClDomainNameEntry, rlDnsClNamesName=rlDnsClNamesName, rlDnsClMibVersion=rlDnsClMibVersion, dnsResConfigSbeltExtTable=dnsResConfigSbeltExtTable, dnsResConfigSbeltExtEntry=dnsResConfigSbeltExtEntry, dnsResConfigSbeltOwner=dnsResConfigSbeltOwner, rlDnsClDomainNameOwner=rlDnsClDomainNameOwner, rlDnsClNamesOwner=rlDnsClNamesOwner, rlDnsClNamesAddr=rlDnsClNamesAddr, rlDnsClDomainNameTable=rlDnsClDomainNameTable, rlDnsClDomainNameName=rlDnsClDomainNameName, rlDnsClMinRetransmissionInterval=rlDnsClMinRetransmissionInterval)