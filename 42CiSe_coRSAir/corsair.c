/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   corsair.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: maperez- <maperez-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/14 14:25:11 by maperez-          #+#    #+#             */
/*   Updated: 2022/07/21 12:42:34 by maperez-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "corsair.h"

void	corsair(const char	*cert_filestr)
{
	EVP_PKEY	*pkey;
	BIO			*certbio;
	BIO			*outbio;
	X509		*cert;
	int			ret;

	pkey = NULL;
	certbio = NULL;
	outbio = NULL;
	cert = NULL;
	/* ---------------------------------------------------------- *
   * These function calls initialize openssl for correct work.  *
   * ---------------------------------------------------------- */
	OpenSSL_add_all_algorithms();
	ERR_load_BIO_strings();
	ERR_load_crypto_strings();
	/* ---------------------------------------------------------- *
   * Create the Input/Output BIO's.                             *
   * ---------------------------------------------------------- */
	certbio = BIO_new(BIO_s_file());
	outbio = BIO_new_fp(stdout, BIO_NOCLOSE);
	/* ---------------------------------------------------------- *
   * Load the certificate from file (PEM).                      *
   * ---------------------------------------------------------- */
	ret = BIO_read_filename(certbio, cert_filestr);
	if (!(cert = PEM_read_bio_X509(certbio, NULL, 0, NULL)))
	{
		BIO_printf(outbio, "Error loading cert into memory.\n");
		exit(-1);
	}
	/* ---------------------------------------------------------- *
   * Extract the certificate's public key data.                 *
   * ---------------------------------------------------------- */
	if ((pkey = X509_get_pubkey(cert)) == NULL)
		BIO_printf(outbio, "Error getting public key from certificate.");
	/* ---------------------------------------------------------- *
   * Print the public key information and the key in PEM format *
   * ---------------------------------------------------------- */
	/* display the key type and size here */
	if (!PEM_write_bio_PUBKEY(outbio, pkey))
		BIO_printf(outbio, "Error writing public key data in PEM format.");
	/* ---------------------------------------------------------- *
   * Print the public key information and the key in PEM format *
   * ---------------------------------------------------------- */
	RSA  *rsa = EVP_PKEY_get1_RSA(pkey);

  const BIGNUM* n = RSA_get0_n(rsa);
  const BIGNUM* e = RSA_get0_e(rsa);

	printf("\nMódulo hexadecimal: ");
	BN_print_fp(stdout, n);
	printf("\n\nExponente hexadecimal: ");
	BN_print_fp(stdout, e);
	printf("\n\nMódulo: %s \n", BN_bn2dec(n));
	printf("\nExponente: %s \n", BN_bn2dec(e));
	EVP_PKEY_free(pkey);
	X509_free(cert);
	BIO_free_all(certbio);
	BIO_free_all(outbio);
}

void	ft_create_privkey(char	*prim1, char	*prim2)
{
	BN_CTX	*ctx = BN_CTX_new(); // Valor temporal.
	RSA		*rsa = RSA_new(); // Estructura.
	BIGNUM	*p = BN_new();	// Primo1.
	BIGNUM	*q = BN_new();	// Primo2.
	BIGNUM	*e = BN_new();
	BIGNUM	*uno = BN_new();
	BIGNUM	*n;
	BIGNUM	*m; // Para calcular
	BIGNUM	*a;	// correctamente
	BIGNUM	*b;	// el módulo inverso.
	BIGNUM	*d; // Módulo inverso (exponente privado)
	BIGNUM	*dmp1; // Valores para
	BIGNUM	*dmq1; // desencriptar la clave.
	BIGNUM	*iqmp;
	BIGNUM	*temp_p;
	BIGNUM	*temp_q;
	BIO		*outbio;
	int		ret;

	BN_dec2bn(&e, "65537");
	BN_dec2bn(&uno, "1");
	BN_dec2bn(&p, prim1);
	BN_dec2bn(&q, prim2);
	BN_CTX_start(ctx);
	n = BN_CTX_get(ctx);
	BN_mul(n, p, q, ctx);
	m = BN_CTX_get(ctx);
	a = BN_CTX_get(ctx);
	b = BN_CTX_get(ctx);
	BN_add(a, p, q);
	BN_sub(b, a, uno);
	BN_sub(m, n, b);
	d = BN_CTX_get(ctx);
	BN_mod_inverse(d, e, m, ctx);
	temp_p = BN_CTX_get(ctx);
	BN_sub(temp_p, p, uno);
	temp_q = BN_CTX_get(ctx);
	BN_sub(temp_q, q, uno);
	dmp1 = BN_CTX_get(ctx);
	BN_mod(dmp1, d, temp_p, ctx);
	dmq1 = BN_CTX_get(ctx);
	BN_mod(dmq1, d, temp_q, ctx);
	iqmp = BN_CTX_get(ctx);
	BN_mod_inverse(iqmp, q, p, ctx);

	RSA_set0_key(rsa, n, e, d);
	RSA_set0_factors(rsa, p, q);
	RSA_set0_crt_params(rsa, dmp1, dmq1, iqmp);
	/* --------------------------------------------------------- *
	* Imprimir clave pública y privada.							 *
	* ---------------------------------------------------------- */
	outbio = BIO_new_fp(stdout, BIO_NOCLOSE);
	// Detalles de la clave privada.
	RSA_print(outbio, rsa, 0);
	printf("\n");
    ret = PEM_write_bio_RSAPublicKey(outbio, rsa);
    if(ret != 1)
    {
        BIO_printf(outbio, "Error writing public key data in PEM format");
        return;
    }
    printf("\n\n");
    ret = PEM_write_bio_RSAPrivateKey(outbio, rsa, NULL, NULL, 0, NULL, NULL);
    if(ret != 1)
    {
        BIO_printf(outbio, "Error writing private key data in PEM format");
        return;
    }
	BN_CTX_end(ctx);
    RSA_free(rsa);
    BIO_free_all(outbio);
}

int	main(void)
{
	const char	cert_filestr[] = "./cert.pem";

	printf("\n");
	corsair(cert_filestr);
	printf("\n");
	ft_create_privkey("131071", "524287");
	printf("\n");
	//system("leaks a.out");
	return (0);
}
