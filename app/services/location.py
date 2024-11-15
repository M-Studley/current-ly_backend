from typing import Sequence, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.location import Location
from schemas.location import LocationCreate, LocationUpdate


class LocationService:
    @staticmethod
    async def create_location(session: AsyncSession, location_data: LocationCreate) -> Location:
        """Create a new location."""
        new_location = Location(**location_data.model_dump())
        session.add(new_location)
        await session.commit()
        await session.refresh(new_location)
        return new_location

    @staticmethod
    async def get_all_locations(session: AsyncSession) -> Sequence[Location]:
        """Retrieve all locations."""
        result = await session.execute(select(Location))
        return result.scalars().all()

    @staticmethod
    async def get_location_by_id(session: AsyncSession, location_id: int) -> Optional[Location]:
        """Retrieve a location by its ID."""
        result = await session.execute(select(Location).where(Location.id == location_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def update_location(session: AsyncSession, location_id: int, location_data: LocationUpdate) -> Optional[
        Location]:
        """Update an existing location."""
        location = await LocationService.get_location_by_id(session, location_id)
        if not location:
            return None

        for key, value in location_data.dict(exclude_unset=True).items():
            setattr(location, key, value)

        await session.commit()
        await session.refresh(location)
        return location

    @staticmethod
    async def delete_location(session: AsyncSession, location_id: int) -> bool:
        """Delete a location by its ID."""
        location = await LocationService.get_location_by_id(session, location_id)
        if not location:
            return False

        await session.delete(location)
        await session.commit()
        return True
