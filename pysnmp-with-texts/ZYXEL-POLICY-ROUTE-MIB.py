#
# PySNMP MIB module ZYXEL-POLICY-ROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-POLICY-ROUTE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:51:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, ObjectIdentity, TimeTicks, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, Bits, Counter32, iso, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "Bits", "Counter32", "iso", "Counter64", "IpAddress")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelPolicyRoute = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60))
if mibBuilder.loadTexts: zyxelPolicyRoute.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelPolicyRoute.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelPolicyRoute.setContactInfo('')
if mibBuilder.loadTexts: zyxelPolicyRoute.setDescription('The subtree for policy route')
zyxelPolicyRouteSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1))
zyPolicyRouteMaxNumberOfProfiles = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPolicyRouteMaxNumberOfProfiles.setStatus('current')
if mibBuilder.loadTexts: zyPolicyRouteMaxNumberOfProfiles.setDescription('The maximum number of policy route profile that can be created.')
zyxelPolicyRouteProfileTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 2), )
if mibBuilder.loadTexts: zyxelPolicyRouteProfileTable.setStatus('current')
if mibBuilder.loadTexts: zyxelPolicyRouteProfileTable.setDescription('The table contains policy route profile configuration.')
zyxelPolicyRouteProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 2, 1), ).setIndexNames((0, "ZYXEL-POLICY-ROUTE-MIB", "zyPolicyRouteProfileName"))
if mibBuilder.loadTexts: zyxelPolicyRouteProfileEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelPolicyRouteProfileEntry.setDescription('An entry contains policy route profile configuration.')
zyPolicyRouteProfileState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 2, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPolicyRouteProfileState.setStatus('current')
if mibBuilder.loadTexts: zyPolicyRouteProfileState.setDescription('Enable/Disable this policy routing profile and rule in the profile.')
zyPolicyRouteProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 2, 1, 2), DisplayString())
if mibBuilder.loadTexts: zyPolicyRouteProfileName.setStatus('current')
if mibBuilder.loadTexts: zyPolicyRouteProfileName.setDescription('A descriptive name for identification policy route profile.')
zyPolicyRouteProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyPolicyRouteProfileRowStatus.setStatus('current')
if mibBuilder.loadTexts: zyPolicyRouteProfileRowStatus.setDescription('This object allows entries to be created and deleted from the policy route profile table.')
zyPolicyRouteMaxNumberOfRules = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPolicyRouteMaxNumberOfRules.setStatus('current')
if mibBuilder.loadTexts: zyPolicyRouteMaxNumberOfRules.setDescription('The maximum number of policy route rule that can be created.')
zyxelPolicyRouteTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 4), )
if mibBuilder.loadTexts: zyxelPolicyRouteTable.setStatus('current')
if mibBuilder.loadTexts: zyxelPolicyRouteTable.setDescription('The table contains policy route rule configuration.')
zyxelPolicyRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 4, 1), ).setIndexNames((0, "ZYXEL-POLICY-ROUTE-MIB", "zyPolicyRouteProfile"), (0, "ZYXEL-POLICY-ROUTE-MIB", "zyPolicyRouteSequence"))
if mibBuilder.loadTexts: zyxelPolicyRouteEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelPolicyRouteEntry.setDescription('An entry contains policy route rule configuration. ')
zyPolicyRouteProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 4, 1, 1), DisplayString())
if mibBuilder.loadTexts: zyPolicyRouteProfile.setStatus('current')
if mibBuilder.loadTexts: zyPolicyRouteProfile.setDescription('The policy routing profile you configure.')
zyPolicyRouteSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 4, 1, 2), Integer32())
if mibBuilder.loadTexts: zyPolicyRouteSequence.setStatus('current')
if mibBuilder.loadTexts: zyPolicyRouteSequence.setDescription('The rule number from 1 to 64. The ordering of your rules is important as rules are applied in turn.')
zyPolicyRouteStatement = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("permit", 0), ("deny", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPolicyRouteStatement.setStatus('current')
if mibBuilder.loadTexts: zyPolicyRouteStatement.setDescription('Statement of policy route rule. Select Permit to forward traffic that matches this rule to the gateway specified in the rule. Select Deny to disable the rule action and forward traffic that matches this rule according to the routing table on the switch.')
zyPolicyRouteCalssifier = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 4, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPolicyRouteCalssifier.setStatus('current')
if mibBuilder.loadTexts: zyPolicyRouteCalssifier.setDescription('The available active classifiers you configure, which are not used by any policy rule or policy routing rule.')
zyPolicyRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 4, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPolicyRouteNextHop.setStatus('current')
if mibBuilder.loadTexts: zyPolicyRouteNextHop.setDescription('Next hop IP address if the incoming packets match the criteria. 0.0.0.0 means nothing be done.')
zyPolicyRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyPolicyRouteRowStatus.setStatus('current')
if mibBuilder.loadTexts: zyPolicyRouteRowStatus.setDescription('This object allows entries to be created and deleted from the policy route rule table.')
mibBuilder.exportSymbols("ZYXEL-POLICY-ROUTE-MIB", zyPolicyRouteMaxNumberOfProfiles=zyPolicyRouteMaxNumberOfProfiles, zyPolicyRouteProfileName=zyPolicyRouteProfileName, zyPolicyRouteProfileRowStatus=zyPolicyRouteProfileRowStatus, zyxelPolicyRouteProfileEntry=zyxelPolicyRouteProfileEntry, zyPolicyRouteStatement=zyPolicyRouteStatement, zyPolicyRouteRowStatus=zyPolicyRouteRowStatus, zyxelPolicyRouteProfileTable=zyxelPolicyRouteProfileTable, zyPolicyRouteMaxNumberOfRules=zyPolicyRouteMaxNumberOfRules, zyPolicyRouteProfileState=zyPolicyRouteProfileState, zyxelPolicyRouteEntry=zyxelPolicyRouteEntry, zyxelPolicyRoute=zyxelPolicyRoute, zyPolicyRouteSequence=zyPolicyRouteSequence, PYSNMP_MODULE_ID=zyxelPolicyRoute, zyPolicyRouteNextHop=zyPolicyRouteNextHop, zyxelPolicyRouteTable=zyxelPolicyRouteTable, zyPolicyRouteProfile=zyPolicyRouteProfile, zyxelPolicyRouteSetup=zyxelPolicyRouteSetup, zyPolicyRouteCalssifier=zyPolicyRouteCalssifier)