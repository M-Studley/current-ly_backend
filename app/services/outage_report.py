from typing import Sequence, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.outage_report import OutageReport
from schemas.outage_report import OutageReportCreate, OutageReportUpdate


class OutageReportService:
    @staticmethod
    async def create_report(session: AsyncSession, report_data: OutageReportCreate) -> OutageReport:
        """Create a new outage report."""
        new_report = OutageReport(**report_data.model_dump())
        session.add(new_report)
        await session.commit()
        await session.refresh(new_report)
        return new_report

    @staticmethod
    async def get_all_reports(session: AsyncSession) -> Sequence[OutageReport]:
        """Retrieve all outage reports."""
        result = await session.execute(select(OutageReport))
        return result.scalars().all()

    @staticmethod
    async def get_report_by_id(session: AsyncSession, report_id: int) -> Optional[OutageReport]:
        """Retrieve an outage report by its ID."""
        result = await session.execute(select(OutageReport).where(OutageReport.id == report_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_reports_by_user(session: AsyncSession, user_id: int) -> Sequence[OutageReport]:
        """Retrieve all reports submitted by a specific user."""
        result = await session.execute(select(OutageReport).where(OutageReport.user_id == user_id))
        return result.scalars().all()

    @staticmethod
    async def get_reports_for_outage(session: AsyncSession, outage_id: int) -> Sequence[OutageReport]:
        """Retrieve all reports for a specific outage."""
        result = await session.execute(select(OutageReport).where(OutageReport.outage_id == outage_id))
        return result.scalars().all()

    @staticmethod
    async def update_report(session: AsyncSession, report_id: int, report_data: OutageReportUpdate) -> Optional[
        OutageReport]:
        """Update an existing outage report."""
        report = await OutageReportService.get_report_by_id(session, report_id)
        if not report:
            return None

        for key, value in report_data.dict(exclude_unset=True).items():
            setattr(report, key, value)

        await session.commit()
        await session.refresh(report)
        return report

    @staticmethod
    async def delete_report(session: AsyncSession, report_id: int) -> bool:
        """Delete an outage report by its ID."""
        report = await OutageReportService.get_report_by_id(session, report_id)
        if not report:
            return False

        await session.delete(report)
        await session.commit()
        return True
