

from model.unico import Unico

import datetime

class MapperObject:
    def client_to_unico(self, count_item, client, file_csv):
        date_now =f"{datetime.datetime.now():%d/%m/%Y}"
        unico = Unico(  str(file_csv).upper().replace('.CSV', ''),
                        count_item,
                        int(client['bimestre_fatturazione'][2:]),
                        None,
                        client['codice_fiscale'],
                        client['partita_iva'],
                        client['intestatario'],
                        date_now,
                        None,
                        client['totale_fattura'],
                        None,
                        client['fattura'],
                        client['data_emissione_fattura'],
                        file_csv,
                        client['impianto'],
                        client['localita_impianto'],
                        client['indirizzo_impianti'],
                        None,
                        None,
                        client['bimestre_fatturazione'],
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None)

        return unico