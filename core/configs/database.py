from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from core.configs.settings import get_config
from core.model.BaseModel import EntityMeta

from core.model.doctor_model import Doctor
from core.model.patient_model import Patient
from core.model.consultation_model import Consultation
# from core.model.payment_model import Payment
from core.model.prescription_model import Prescription

env = get_config()

DATABASE_URL = (
    f"{env.DATABASE_DIALECT}+asyncpg://"
    f"{env.DATABASE_USERNAME}:{env.DATABASE_PASSWORD}"
    f"@{env.DATABASE_HOSTNAME}:{env.DATABASE_PORT}"
    f"/{env.DATABASE_NAME}"
)

engine = create_async_engine(DATABASE_URL, echo=env.DEBUG_MODE)

AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

async def get_db_connection():
    async with AsyncSessionLocal() as session:
        yield session


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(EntityMeta.metadata.create_all)

