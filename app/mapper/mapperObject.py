

from model.unico import Unico
from model.unicoDetail import UnicoDetail

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



    def client_to_unicoDetail(self, count_item, client, file_csv):
        date_now =f"{datetime.datetime.now():%d/%m/%Y}"
        unicoDetail = UnicoDetail( str(file_csv).upper().replace('.CSV', ''),
                                   count_item,
                                   int(client['bimestre_fatturazione'][2:]),
                                   client['codice_fiscale'],
                                   client['partita_iva'],
                                   client['fattura'],
                                   client['data_emissione_fattura'],
                                   client['impianto'],
                                   client['descrizione_addebiti_accrediti'],
                                   client['costo'],
                                   client['riferimento_iva'],
                                   client['flag_reg_der'],
                                   client['quantita'],
                                   client['durata'],
                                   client['bimestre_fatturazione'],
                                   client['tipo_importo_addebito']
                                )

        return unicoDetail