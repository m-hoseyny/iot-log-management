
from typing import TYPE_CHECKING
import uuid, datetime

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class DeviceCredential(Base):
    __tablename__ = 'device_credentials'
    # __table_args__ = (
    #     # this can be db.PrimaryKeyConstraint if you want it to be a primary key
    #     UniqueConstraint('provision_device_key'),
    #   )

    id = Column(UUID(as_uuid=True), primary_key=True)
    credentials_id = Column(String, nullable=False, index=True)
    credentials_type = Column(String, nullable=False)
    credentials_value = Column(String, nullable=False, index=True)
    device_id = Column(UUID(as_uuid=True), ForeignKey('devices.id'), default=uuid.uuid4, nullable=False, index=True)

    device = relationship("Device", back_populates="device_credential")

    created_at = Column(DateTime(), default=datetime.datetime.now)
    updated_at = Column(DateTime(), onupdate=datetime.datetime.now, default=datetime.datetime.now)

    def __repr__(self) -> str:
        return f'{self.id} [{self.credentials_type}] access_token={self.credentials_id}:{self.credentials_value}'


'''CREATE TABLE IF NOT EXISTS device_credentials (
    id uuid NOT NULL CONSTRAINT device_credentials_pkey PRIMARY KEY,
    created_time bigint NOT NULL,
    credentials_id varchar,
    credentials_type varchar(255),
    credentials_value varchar,
    device_id uuid,
    CONSTRAINT device_credentials_id_unq_key UNIQUE (credentials_id),
    CONSTRAINT device_credentials_device_id_unq_key UNIQUE (device_id)
);'''