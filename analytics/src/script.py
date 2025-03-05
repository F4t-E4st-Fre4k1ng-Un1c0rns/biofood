from typing import Optional
from uuid import UUID

from sqlalchemy import select, delete

from src.database.session import session_maker, session_maker_analyze
from src.database.orm import DishORM, OrderItemORM
from src.database.orm_analyze import AIData

from .analyze import analyze_sales


async def drop_analyze_table(filters: Optional[dict] = None):
    async with session_maker_analyze() as session:
        query = delete(AIData)
        if filters:
            query = query.filter_by(**filters)
        await session.execute(query)
        await session.commit()

async def add_records(data: list[dict], dish_id: UUID, dish_name: str):
    async with session_maker_analyze() as session:
        for record in data:
            db_record = AIData(dish_id=dish_id, dish_name=dish_name, **record)
            session.add(db_record)
        await session.commit()

async def script():

    await drop_analyze_table()

    async with session_maker() as session:
        dish_info = [(record.id, record.name) for record in (await session.execute(select(DishORM))).scalars()]
        for dish_id, dish_name in dish_info:
            dates_data = dict()
            query = (
                select(OrderItemORM)
                .where(OrderItemORM.dish_id == dish_id)
            )
            for record in list((await session.execute(query)).scalars()):
                record_date = record.order.takeout_time.date()
                dates_data[record_date] = dates_data.get(record_date, 0) + record.amount

            data_for_forecast = {"date": [], "sales": []}

            for date, sales in dates_data.items():
                data_for_forecast["date"].append(date)
                data_for_forecast["sales"].append(sales)
            try:
                forecast = analyze_sales(data_for_forecast)
                await add_records(forecast, dish_id, dish_name)
            except Exception as e:
                await drop_analyze_table({"dish_id": dish_id})
