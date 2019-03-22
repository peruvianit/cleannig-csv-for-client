

import csv


class UnicoDetail:
    def __init__(self,
                 block,
                 row,
                 anno,
                 codice_fiscale,
                 partita_iva,
                 num_doc,
                 data_doc,
                 impianto,
                 descrizione_addebiti_accrediti,
                 costo,
                 riferimento_iva,
                 flag_reg_der,
                 quantita,
                 durata,
                 bimestre_fatturazione,
                 tipo_importo_addebito
                 ):
        self.block = block
        self.row = int(row)
        self.anno = int(anno)
        self.codice_fiscale = codice_fiscale
        if str(partita_iva).isdigit():
            self.partita_iva = int(partita_iva)

        self.num_doc = num_doc
        self.data_doc = data_doc
        self.impianto = impianto
        self.descrizione_addebiti_accrediti = descrizione_addebiti_accrediti
        self.costo = costo
        self.riferimento_iva = riferimento_iva
        self.flag_reg_der = flag_reg_der
        self.quantita = quantita
        self.durata = durata
        self.bimestre_fatturazione = bimestre_fatturazione
        self.tipo_importo_addebito = tipo_importo_addebito


    @staticmethod
    def header_names():
        return ['block',
                'row',
                'anno',
                'codice_fiscale',
                'partita_iva',
                'num_doc',
                'data_doc',
                'impianto',
                'descrizione_addebiti_accrediti',
                'costo',
                'riferimento_iva',
                'flag_reg_der',
                'quantita',
                'durata',
                'bimestre_fatturazione',
                'tipo_importo_addebito']