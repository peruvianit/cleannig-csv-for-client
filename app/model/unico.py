

import csv


class Unico:
    def __init__(self,
                 id,
                 anno,
                 numero,
                 codice_fiscale,
                 partita_iva,
                 intestatario,
                 data_registrazione,
                 stato,
                 importo,
                 tipo_documento,
                 num_doc,
                 data_doc,
                 file,
                 utenza_telecom,
                 localita_impianto,
                 indirizzo_impianto,
                 utenza_file_debito_telecom,
                 utenza_telefonica,
                 bimestre_fatturazione,
                 liquidabile,
                 avallo_17_ventidue,
                 documenti_di_riferimento,
                 importo_contestabile_IVA_esclusa,
                 importo_contestabile_FCI,
                 contenzioso_A_FCI,
                 motivazione_a,
                 contenzioso_B_FCI,
                 motivazione_B,
                 contenzioso_1importi_IVA_eslcusa,
                 motivazione_1,
                 contenzioso_2_importi_IVA_eslcusa,
                 motivazione_2,
                 contenzioso_3_importi_IVA_eslcusa,
                 motivazione_3,
                 note_margine
                 ):
        self.id = int(id)
        self.anno = int(anno)
        if str(numero).isdigit():
            self.numero = int(numero)
        self.codice_fiscale = codice_fiscale
        if str(partita_iva).isdigit():
            self.partita_iva = int(partita_iva)

        self.intestatario = intestatario
        self.data_registrazione = data_registrazione
        self.stato = stato
        self.importo = importo
        self.tipo_documento = tipo_documento
        self.num_doc = num_doc
        self.data_doc = data_doc
        self.file = file
        self.utenza_telecom = utenza_telecom
        self.localita_impianto = localita_impianto
        self.indirizzo_impianto = indirizzo_impianto
        self.utenza_file_debito_telecom = utenza_file_debito_telecom
        self.utenza_telefonica = utenza_telefonica
        self.bimestre_fatturazione = bimestre_fatturazione
        self.liquidabile = liquidabile
        self.avallo_17_ventidue = avallo_17_ventidue
        self.documenti_di_riferimento = documenti_di_riferimento
        self.importo_contestabile_IVA_esclusa = importo_contestabile_IVA_esclusa
        self.importo_contestabile_FCI = importo_contestabile_FCI
        self.contenzioso_A_FCI = contenzioso_A_FCI
        self.motivazione_a = motivazione_a
        self.contenzioso_B_FCI = contenzioso_B_FCI
        self.motivazione_B = motivazione_B
        self.contenzioso_1importi_IVA_eslcusa = contenzioso_1importi_IVA_eslcusa
        self.motivazione_1 = motivazione_1
        self.contenzioso_2_importi_IVA_eslcusa = contenzioso_2_importi_IVA_eslcusa
        self.motivazione_2 = motivazione_2
        self.contenzioso_3_importi_IVA_eslcusa = contenzioso_3_importi_IVA_eslcusa
        self.motivazione_3 = motivazione_3
        self.note_margine = note_margine


    @staticmethod
    def header_names():
        return ['id',
                'anno',
                'numero',
                'codice_fiscale',
                'partita_iva',
                'intestatario',
                'data_registrazione',
                'stato',
                'importo',
                'tipo_documento',
                'num_doc',
                'data_doc',
                'file',
                'utenza_telecom',
                'localita_impianto',
                'indirizzo_impianto',
                'utenza_file_debito_telecom',
                'utenza_telefonica',
                'bimestre_fatturazione',
                'liquidabile',
                'avallo_17_ventidue',
                'documenti_di_riferimento',
                'importo_contestabile_IVA_esclusa',
                'importo_contestabile_FCI',
                'contenzioso_A_FCI',
                'motivazione_a',
                'contenzioso_B_FCI',
                'motivazione_B',
                'contenzioso_1importi_IVA_eslcusa',
                'motivazione_1',
                'contenzioso_2_importi_IVA_eslcusa',
                'motivazione_2',
                'contenzioso_3_importi_IVA_eslcusa',
                'motivazione_3',
                'note_margine']