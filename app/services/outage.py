from typing import Sequence, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.outage import Outage
from schemas.outage import OutageCreate, OutageUpdate


class OutageService:
    @staticmethod
    async def create_outage(session: AsyncSession, outage_data: OutageCreate) -> Outage:
        """Create a new outage."""
        new_outage = Outage(**outage_data.model_dump())
        session.add(new_outage)
        await session.commit()
        await session.refresh(new_outage)
        return new_outage

    @staticmethod
    async def get_all_outages(session: AsyncSession) -> Sequence[Outage]:
        """Retrieve all outages."""
        result = await session.execute(select(Outage))
        return result.scalars().all()

    @staticmethod
    async def get_outage_by_id(session: AsyncSession, outage_id: int) -> Optional[Outage]:
        """Retrieve an outage by its ID."""
        result = await session.execute(select(Outage).where(Outage.id == outage_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_outages_by_location(session: AsyncSession, location_id: int) -> Sequence[Outage]:
        """Retrieve all outages for a specific location."""
        result = await session.execute(select(Outage).where(Outage.location_id == location_id))
        return result.scalars().all()

    @staticmethod
    async def update_outage(session: AsyncSession, outage_id: int, outage_data: OutageUpdate) -> Optional[Outage]:
        """Update an existing outage."""
        outage = await OutageService.get_outage_by_id(session, outage_id)
        if not outage:
            return None

        for key, value in outage_data.dict(exclude_unset=True).items():
            setattr(outage, key, value)

        await session.commit()
        await session.refresh(outage)
        return outage

    @staticmethod
    async def delete_outage(session: AsyncSession, outage_id: int) -> bool:
        """Delete an outage by its ID."""
        outage = await OutageService.get_outage_by_id(session, outage_id)
        if not outage:
            return False

        await session.delete(outage)
        await session.commit()
        return True
