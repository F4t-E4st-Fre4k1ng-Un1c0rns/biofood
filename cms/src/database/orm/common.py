from sqlalchemy import DateTime
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import FunctionElement


class utcnow(FunctionElement):
    """SQLAlchemy field with current UTC time"""

    type = DateTime(timezone=True)
    inherit_cache = True


@compiles(utcnow, "postgresql")
def pg_utcnow(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"
