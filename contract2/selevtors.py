from contract2.models import Contract


def get_contract(contract_id):
    return Contract.objects.get(pk=contract_id)