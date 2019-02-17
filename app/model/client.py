

import csv


class Client:
    def __init__(self,
                 codice_fiscale,
                 partita_iva,
                 cfa,
                 contratto,
                 fattura,
                 intestatario,
                 impianto,
                 localita_impianto,
                 indirizzo_impianti,
                 descrizione_addebiti_accrediti,
                 descrizione_offerta_servizio,
                 importo_addebiti_accrediti,
                 sconto_riduzione,
                 importo_riduzione,
                 costo,
                 riferimento_iva,
                 flag_reg_der,
                 quantita,
                 durata,
                 numero_carta,
                 data_inizio_rif,
                 data_fine_rif,
                 tipologia_fattura,
                 data_emissione_fattura,
                 data_scadenza_fattura,
                 totale_fattura,
                 bimestre_fatturazione,
                 tipo_importo_addebito):

        self.codice_fiscale = codice_fiscale
        self.partita_iva = partita_iva
        self.cfa = cfa
        self.contratto = contratto
        self.fattura = fattura
        self.intestatario = intestatario
        self.impianto = impianto
        self.localita_impianto = localita_impianto
        self.indirizzo_impianti = indirizzo_impianti
        self.descrizione_addebiti_accrediti = descrizione_addebiti_accrediti
        self.descrizione_offerta_servizio = descrizione_offerta_servizio
        self.importo_addebiti_accrediti = importo_addebiti_accrediti
        self.sconto_riduzione = sconto_riduzione
        self.importo_riduzione = importo_riduzione
        self.costo = costo
        self.riferimento_iva = riferimento_iva
        self.flag_reg_der = flag_reg_der
        self.quantita = quantita
        self.durata = durata
        self.numero_carta = numero_carta
        self.data_inizio_rif = data_inizio_rif
        self.data_fine_rif = data_fine_rif
        self.tipologia_fattura = tipologia_fattura
        self.data_emissione_fattura = data_emissione_fattura
        self.data_scadenza_fattura = data_scadenza_fattura
        self.totale_fattura = totale_fattura
        self.bimestre_fatturazione = bimestre_fatturazione
        self.tipo_importo_addebito = tipo_importo_addebito


    @staticmethod
    def header_names(self):
        return ['codice_fiscale',
                'partita',
                'iva',
                'cfa',
                'contratto',
                'fattura',
                'intestatario',
                'impianto',
                'localita_impianto',
                'indirizzo_impianti',
                'descrizione_addebiti_accrediti',
                'descrizione_offerta_servizio',
                'importo_addebiti_accrediti',
                'sconto_riduzione',
                'importo_riduzione',
                'costo',
                'riferimento_iva',
                'flag',
                'reg_der',
                'quantita',
                'durata',
                'numero_carta',
                'data_inizio_rif',
                'data_fine_rif',
                'tipologia_fattura',
                'data_emissione_fattura',
                'data_scadenza_fattura',
                'totale_fattura',
                'bimestre_fatturazione',
                'tipo_importo_addebito']


    @classmethod
    def load_from_csv(cls, path_csv, header = False):

        client_data = []
        with open(path_csv, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')

            row_number = 0
            for row in spamreader:
                row_number += 1

                if row_number == 1 and header:
                    continue
                # Load Model

                if row[0] == "#":
                    continue

                client_model = cls(row[0],
                                row[1],
                                row[2],
                                row[3],
                                row[4],
                                row[5],
                                row[6],
                                row[7],
                                row[8],
                                row[9],
                                row[10],
                                row[11],
                                row[12],
                                row[13],
                                row[14],
                                row[15],
                                row[16],
                                row[17],
                                row[18],
                                row[19],
                                row[20],
                                row[21],
                                row[22],
                                row[23],
                                row[24],
                                row[25],
                                row[26],
                                row[27])
                client_data.append(client_model)

            return [ele.__dict__ for ele in client_data]