#
# PySNMP MIB module SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SSH-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:10:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, IpAddress, ModuleIdentity, Integer32, Bits, Counter64, iso, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "IpAddress", "ModuleIdentity", "Integer32", "Bits", "Counter64", "iso", "ObjectIdentity", "Unsigned32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
privateMgmt, = mibBuilder.importSymbols("SWPRIMGMT-MIB", "privateMgmt")
swSSHMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5))
if mibBuilder.loadTexts: swSSHMIB.setLastUpdated('9911220000Z')
if mibBuilder.loadTexts: swSSHMIB.setOrganization('Working Group')
if mibBuilder.loadTexts: swSSHMIB.setContactInfo(' ')
if mibBuilder.loadTexts: swSSHMIB.setDescription('The Secure Shell module MIB.')
swSSHMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 1))
swSSHAdmin = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHAdmin.setStatus('current')
if mibBuilder.loadTexts: swSSHAdmin.setDescription('This object indicates the Secure Shell is enable or disable.')
swSSHMaxConnections = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHMaxConnections.setStatus('current')
if mibBuilder.loadTexts: swSSHMaxConnections.setDescription('This object indicates the tolerance of connections at the same time.')
swSSHConnectionTimeout = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 120))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHConnectionTimeout.setStatus('current')
if mibBuilder.loadTexts: swSSHConnectionTimeout.setDescription('This object indicates the value of connection timeout. This value is in units of seconds.')
swSSHMaxAuthFailAttempts = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHMaxAuthFailAttempts.setStatus('current')
if mibBuilder.loadTexts: swSSHMaxAuthFailAttempts.setDescription('This object indicates the tolerance in times of Authentication failure.')
swSSHSessionKeyRekeying = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 10, 30, 60))).clone(namedValues=NamedValues(("never", 0), ("ten-min", 10), ("thirty-min", 30), ("sixty-min", 60)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHSessionKeyRekeying.setStatus('current')
if mibBuilder.loadTexts: swSSHSessionKeyRekeying.setDescription('This object indicates the time interval in minutes to negotiate new session key for client and server. ')
swSSHPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHPortNumber.setStatus('current')
if mibBuilder.loadTexts: swSSHPortNumber.setDescription('This object indicates the listened tcp port number.')
swSSHRegenerateHostKey = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("active", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHRegenerateHostKey.setStatus('current')
if mibBuilder.loadTexts: swSSHRegenerateHostKey.setDescription('As the object is set to active means to regenerate hostkey in SSH server. If set to normal, do nothing.')
swSSHCtrlAlgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2))
swSSHEncryptAlgCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1))
swSSHEncryptAlg3DESAdmin = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHEncryptAlg3DESAdmin.setStatus('current')
if mibBuilder.loadTexts: swSSHEncryptAlg3DESAdmin.setDescription('This object indicates the TDES encryption algorithm is enable or disable.')
swSSHEncryptAlgBlowfishAdmin = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHEncryptAlgBlowfishAdmin.setStatus('current')
if mibBuilder.loadTexts: swSSHEncryptAlgBlowfishAdmin.setDescription('This object indicates the Blowfish encryption algorithm is enable or disable.')
swSSHEncryptAlgAES128Admin = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHEncryptAlgAES128Admin.setStatus('current')
if mibBuilder.loadTexts: swSSHEncryptAlgAES128Admin.setDescription('This object indicates the AES128 encryption algorithm is enable or disable.')
swSSHEncryptAlgAES192Admin = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHEncryptAlgAES192Admin.setStatus('current')
if mibBuilder.loadTexts: swSSHEncryptAlgAES192Admin.setDescription('This object indicates the AES192 encryption algorithm is enable or disable.')
swSSHEncryptAlgAES256Admin = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHEncryptAlgAES256Admin.setStatus('current')
if mibBuilder.loadTexts: swSSHEncryptAlgAES256Admin.setDescription('This object indicates the AES256 encryption algorithm is enable or disable.')
swSSHEncryptAlgArcfourAdmin = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHEncryptAlgArcfourAdmin.setStatus('current')
if mibBuilder.loadTexts: swSSHEncryptAlgArcfourAdmin.setDescription('This object indicates the Arcfour encryption algorithm is enable or disable.')
swSSHEncryptAlgCAST128Admin = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHEncryptAlgCAST128Admin.setStatus('current')
if mibBuilder.loadTexts: swSSHEncryptAlgCAST128Admin.setDescription('This object indicates the CAST128 encryption algorithm is enable or disable.')
swSSHEncryptAlgTwofish128Admin = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHEncryptAlgTwofish128Admin.setStatus('current')
if mibBuilder.loadTexts: swSSHEncryptAlgTwofish128Admin.setDescription('This object indicates the Twofish128 encryption algorithm is enable or disable.')
swSSHEncryptAlgTwofish192Admin = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHEncryptAlgTwofish192Admin.setStatus('current')
if mibBuilder.loadTexts: swSSHEncryptAlgTwofish192Admin.setDescription('This object indicates the Twofish192 encryption algorithm is enable or disable.')
swSSHEncryptAlgTwofish256Admin = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHEncryptAlgTwofish256Admin.setStatus('current')
if mibBuilder.loadTexts: swSSHEncryptAlgTwofish256Admin.setDescription('This object indicates the Twofish256 encryption algorithm is enable or disable.')
swSSHAuthenMethodCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 2))
swSSHAuthenMethodPasswdAdmin = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHAuthenMethodPasswdAdmin.setStatus('current')
if mibBuilder.loadTexts: swSSHAuthenMethodPasswdAdmin.setDescription('This object indicates password authentication enable or disable.')
swSSHAuthenMethodPubKeyAdmin = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHAuthenMethodPubKeyAdmin.setStatus('current')
if mibBuilder.loadTexts: swSSHAuthenMethodPubKeyAdmin.setDescription('This object indicates Public Key authentication enable or disable.')
swSSHAuthenMethodHostBaseAdmin = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHAuthenMethodHostBaseAdmin.setStatus('current')
if mibBuilder.loadTexts: swSSHAuthenMethodHostBaseAdmin.setDescription('This object indicates Host Base authentication enable or disable.')
swSSHInteAlgCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 3))
swSSHInteAlgSHA1Admin = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHInteAlgSHA1Admin.setStatus('current')
if mibBuilder.loadTexts: swSSHInteAlgSHA1Admin.setDescription('This object indicates HMAC-SHA1 algorithm enable or disable .')
swSSHInteAlgMD5Admin = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHInteAlgMD5Admin.setStatus('current')
if mibBuilder.loadTexts: swSSHInteAlgMD5Admin.setDescription('This object indicates HMAC-MD5 algorithm enable or disable .')
swSSHPubKeyAlgCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 4))
swSSHPubKeyAlgDSAAdmin = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHPubKeyAlgDSAAdmin.setStatus('current')
if mibBuilder.loadTexts: swSSHPubKeyAlgDSAAdmin.setDescription('This object indicates DSA algorithm enable or disable .')
swSSHPubKeyAlgRSAAdmin = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 2, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHPubKeyAlgRSAAdmin.setStatus('current')
if mibBuilder.loadTexts: swSSHPubKeyAlgRSAAdmin.setDescription('This object indicates RSA algorithm enable or disable .')
swSSHUserCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 3), )
if mibBuilder.loadTexts: swSSHUserCtrlTable.setStatus('current')
if mibBuilder.loadTexts: swSSHUserCtrlTable.setDescription('A table that contains information about authentication method lists..')
swSSHUserCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 3, 1), ).setIndexNames((0, "SSH-MIB", "swSSHUserCtrlUserName"))
if mibBuilder.loadTexts: swSSHUserCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: swSSHUserCtrlEntry.setDescription('A list of the Authentication methods.')
swSSHUserCtrlUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSSHUserCtrlUserName.setStatus('current')
if mibBuilder.loadTexts: swSSHUserCtrlUserName.setDescription('This object indicates the user name.')
swSSHUserCtrlAuthMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("publickey", 2), ("password", 3), ("hostbased", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHUserCtrlAuthMode.setStatus('current')
if mibBuilder.loadTexts: swSSHUserCtrlAuthMode.setDescription('This object indicates user authentication method.')
swSSHUserCtrlHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHUserCtrlHostName.setStatus('current')
if mibBuilder.loadTexts: swSSHUserCtrlHostName.setDescription('This object indicates the host domain name. If the swSSHUserCtrlAuthMode is not hostbased(4), it must be NULL.')
swSSHUserCtrlHostIp = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 5, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSHUserCtrlHostIp.setStatus('current')
if mibBuilder.loadTexts: swSSHUserCtrlHostIp.setDescription('This object indicates the host IP address. If the swSSHUserCtrlAuthMode is not hostbased(4), it must be 0.0.0.0.')
mibBuilder.exportSymbols("SSH-MIB", PYSNMP_MODULE_ID=swSSHMIB, swSSHCtrlAlgGroup=swSSHCtrlAlgGroup, swSSHPubKeyAlgCtrl=swSSHPubKeyAlgCtrl, swSSHAuthenMethodCtrl=swSSHAuthenMethodCtrl, swSSHInteAlgCtrl=swSSHInteAlgCtrl, swSSHUserCtrlUserName=swSSHUserCtrlUserName, swSSHUserCtrlEntry=swSSHUserCtrlEntry, swSSHEncryptAlgArcfourAdmin=swSSHEncryptAlgArcfourAdmin, swSSHAdmin=swSSHAdmin, swSSHEncryptAlgAES192Admin=swSSHEncryptAlgAES192Admin, swSSHEncryptAlgTwofish192Admin=swSSHEncryptAlgTwofish192Admin, swSSHUserCtrlAuthMode=swSSHUserCtrlAuthMode, swSSHMaxAuthFailAttempts=swSSHMaxAuthFailAttempts, swSSHSessionKeyRekeying=swSSHSessionKeyRekeying, swSSHEncryptAlgCtrl=swSSHEncryptAlgCtrl, swSSHRegenerateHostKey=swSSHRegenerateHostKey, swSSHUserCtrlTable=swSSHUserCtrlTable, swSSHMaxConnections=swSSHMaxConnections, swSSHUserCtrlHostIp=swSSHUserCtrlHostIp, swSSHEncryptAlgTwofish256Admin=swSSHEncryptAlgTwofish256Admin, swSSHPubKeyAlgDSAAdmin=swSSHPubKeyAlgDSAAdmin, swSSHAuthenMethodPasswdAdmin=swSSHAuthenMethodPasswdAdmin, swSSHPortNumber=swSSHPortNumber, swSSHInteAlgSHA1Admin=swSSHInteAlgSHA1Admin, swSSHEncryptAlg3DESAdmin=swSSHEncryptAlg3DESAdmin, swSSHEncryptAlgBlowfishAdmin=swSSHEncryptAlgBlowfishAdmin, swSSHEncryptAlgAES128Admin=swSSHEncryptAlgAES128Admin, swSSHEncryptAlgCAST128Admin=swSSHEncryptAlgCAST128Admin, swSSHUserCtrlHostName=swSSHUserCtrlHostName, swSSHInteAlgMD5Admin=swSSHInteAlgMD5Admin, swSSHMIB=swSSHMIB, swSSHMgmt=swSSHMgmt, swSSHEncryptAlgAES256Admin=swSSHEncryptAlgAES256Admin, swSSHConnectionTimeout=swSSHConnectionTimeout, swSSHAuthenMethodPubKeyAdmin=swSSHAuthenMethodPubKeyAdmin, swSSHPubKeyAlgRSAAdmin=swSSHPubKeyAlgRSAAdmin, swSSHEncryptAlgTwofish128Admin=swSSHEncryptAlgTwofish128Admin, swSSHAuthenMethodHostBaseAdmin=swSSHAuthenMethodHostBaseAdmin)