from core.repository.payment_repository import create_payment
from core.configs.utils import generate_transaction_id

async def init_payment_service(patient_id: int):
    """
    Demo payment initialization
    """
    transaction_id = generate_transaction_id()

    payment_data = {
        "patient_id": patient_id,
        "transaction_id": transaction_id
    }

    payment = await create_payment(payment_data)

    return {
        "payment_id": payment.payment_id,
        "transaction_id": payment.transaction_id
    }
