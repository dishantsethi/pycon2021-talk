from OpenSSL import crypto
from socket import gethostname

def generate_self_signed_key():
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 2048)
    cert = crypto.X509()
   # cert.get_subject().C = "IND"
   # cert.get_subject().ST = "DEL"
    cert.get_subject().O = "intern"
    #cert.get_subject().OU = ""
    cert.get_subject().CN = "dishant" #gethostname()
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(365*24*60*60)  # 1 years expiry date
    cert.set_issuer(cert.get_subject())  # self-sign this certificate
    cert.set_pubkey(k)

    cert.add_extensions([
        crypto.X509Extension(b"basicConstraints", True,
                             b"CA:TRUE, pathlen:0"),
        crypto.X509Extension(b"keyUsage", True,
                             b"keyCertSign, cRLSign"),
        crypto.X509Extension(b"subjectKeyIdentifier", False, b"hash",
                             subject=cert),
    ])

    cert.add_extensions([
        crypto.X509Extension(b"authorityKeyIdentifier", False, b"keyid:always", issuer=cert)
    ])
    cert.sign(k, 'sha256')


    open("selfsign.crt", 'wb').write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
    open("private.key", 'wb').write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
generate_self_signed_key()
