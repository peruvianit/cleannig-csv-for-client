

class Summary:
    def __init__(self):
        self._execute_data = None
        self._name_file = None
        self._rows_worked = None
        self._number_invoices = None
        self._total_amount = None

    @property
    def execute_data(self):
        return self._execute_data

    @execute_data.setter
    def execute_data(self, value):
        self._execute_data = value

    @property
    def name_file(self):
        return self._name_file

    @name_file.setter
    def name_file(self, value):
        self._name_file = value

    @property
    def rows_worked(self):
        return self._rows_worked

    @rows_worked.setter
    def rows_worked(self, value):
        self._rows_worked = value

    @property
    def number_invoices(self):
        return self._number_invoices

    @number_invoices.setter
    def number_invoices(self, value):
        self._number_invoices = value

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value