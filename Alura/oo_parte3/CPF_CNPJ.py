from validate_docbr import CPF, CNPJ


class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(str(documento)) == 11:
            return DocCpf(documento)
        elif len(str(documento)) == 14:
            return DocCnpj(documento)
        else:
            ValueError('Quantidade de Digitos Inválidos')


class DocCpf:

    def __init__(self, documento) -> None:
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF Inválido')

    def __str__(self):
        return self.format()

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)


class DocCnpj:

    def __init__(self, documento) -> None:
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ Inválido')

    def __str__(self):
        return self.format()

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)
