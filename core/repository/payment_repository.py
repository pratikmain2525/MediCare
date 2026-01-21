from core.configs.database import get_db_connection
from core.model.payment_model import Payment
from sqlalchemy.exc import SQLAlchemyError

async def create_payment(data: dict):
    async for db in get_db_connection():
        try:
            payment = Payment(**data)
            db.add(payment)
            await db.commit()
            await db.refresh(payment)
            return payment
        except SQLAlchemyError as e:
            await db.rollback()
            raise e
